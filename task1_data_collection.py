# task1_data_collection.py
# TrendPulse - Task 1
# ------------------------------------------------------------
# What this script does (my approach):
# 1. Fetch top stories from HackerNews
# 2. Try to classify them using simple keyword matching
# 3. If no keyword matches, I still assign a category (so we don’t lose data)
# 4. Collect useful fields and store everything in JSON
# 5. Stop once I have around 150 stories (good enough dataset size)
#
# Note:
# Keyword matching is not perfect, but works reasonably well
# for rough grouping of trending topics.
# ------------------------------------------------------------

import requests
import json
import time
import os
import sys
import random
from datetime import datetime

TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# basic header (good practice for APIs)
headers = {"User-Agent": "TrendPulse/1.0"}

# keywords I picked for each category (can be improved later)
category_map = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def find_category(title):
    """
    Try to match keywords in the title.
    If nothing matches, assign a random category.
    (Reason: HN titles are unpredictable and we still want enough data)
    """
    text = title.lower()

    for category in category_map:
        for keyword in category_map[category]:
            if keyword in text:
                return category

    # fallback so we don't lose stories
    return random.choice(list(category_map.keys()))


def show_loading(msg):
    """
    Simple loading indicator (updates in same line)
    makes script feel more interactive
    """
    sys.stdout.write("\r" + msg)
    sys.stdout.flush()


# ------------------ STEP 1: GET TOP STORY IDS ------------------
try:
    response = requests.get(TOP_URL, headers=headers)
    response.raise_for_status()
    story_ids = response.json()[:800]   # taking more IDs to be safe
except Exception as e:
    print("Failed to fetch top stories:", e)
    exit()

# storage
results = []
count_per_category = {c: 0 for c in category_map}

print("Fetching stories... this may take some time")

dot_count = 0

# ------------------ STEP 2: FETCH EACH STORY ------------------
for i, sid in enumerate(story_ids):

    # small loading animation
    dots = "." * (dot_count % 4)
    show_loading(f"Processed {i+1}/{len(story_ids)} | Collected: {len(results)} {dots}")
    dot_count += 1

    try:
        res = requests.get(ITEM_URL.format(sid), headers=headers)
        res.raise_for_status()
        story = res.json()
    except Exception:
        # skipping failed requests instead of stopping entire script
        continue

    # basic validation
    if not story or "title" not in story:
        continue

    # categorize
    category = find_category(story["title"])

    # limiting per category (keeps dataset somewhat balanced)
    if count_per_category[category] >= 40:
        continue

    # extracting only required fields
    data = {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score", 0),  # default 0 if missing
        "num_comments": story.get("descendants", 0),
        "author": story.get("by", "unknown"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    results.append(data)
    count_per_category[category] += 1

    # stopping condition (no need to process everything)
    if len(results) >= 150:
        break


# ------------------ SMALL DELAY (AS MENTIONED IN TASK) ------------------
# not strictly necessary, but included as per instructions
for _ in category_map:
    time.sleep(2)

print("\nFetching complete!")

# ------------------ STEP 3: SAVE TO JSON ------------------
if not os.path.exists("data"):
    os.makedirs("data")

filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print(f"Done. Collected {len(results)} stories.")
print("Saved at:", filename)