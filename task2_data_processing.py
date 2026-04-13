import pandas as pd
import os
import json

def main():

    print("Looking for JSON file inside data folder...")

    # checking available files
    if not os.path.exists("data"):
        print("data folder not found. Run Task 1 first.")
        return

    files = os.listdir("data")

    # picking latest JSON file
    json_files = [f for f in files if f.endswith(".json")]

    if len(json_files) == 0:
        print("No JSON file found.")
        return

    json_files.sort()
    latest_file = json_files[-1]

    path = os.path.join("data", latest_file)

    # loading JSON
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("Error reading file:", e)
        return

    df = pd.DataFrame(data)

    print(f"\nLoaded {len(df)} stories from {path}")

    # -------------------------
    # STEP 1: REMOVE DUPLICATES
    # -------------------------
    before = len(df)
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")

    # -------------------------
    # STEP 2: HANDLE NULL VALUES
    # -------------------------
    # removing rows where important fields are missing
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")

    # -------------------------
    # STEP 3: FIX DATA TYPES
    # -------------------------
    # sometimes numbers come as float or string
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # -------------------------
    # STEP 4: REMOVE LOW QUALITY DATA
    # -------------------------
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # -------------------------
    # STEP 5: CLEAN TEXT
    # -------------------------
    # removing unwanted spaces in titles
    df["title"] = df["title"].str.strip()

    # -------------------------
    # SAVE CLEAN DATA
    # -------------------------
    output_path = "data/trends_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"\nSaved {len(df)} rows to {output_path}")

    # -------------------------
    # SUMMARY
    # -------------------------
    print("\nStories per category:")
    print(df["category"].value_counts())


if __name__ == "__main__":
    main()


"""
----------------------------------------
MY UNDERSTANDING (in simple words)
----------------------------------------
This script takes the raw JSON from Task 1 and cleans it.

What I did step by step:
1. Loaded JSON into a DataFrame
2. Removed duplicate stories using post_id
3. Dropped rows where important data is missing
4. Converted score and comments into integers
5. Removed low quality stories (score < 5)
6. Cleaned titles by removing extra spaces
7. Saved final clean data as CSV

----------------------------------------
HOW I TESTED THIS
----------------------------------------
1. First ran Task 1 to generate JSON
2. Then ran:
   python task2_data_processing.py

3. Checked:
   - Console shows counts at each step
   - trends_clean.csv is created
   - Opened CSV to verify data looks clean

----------------------------------------
NOTES
----------------------------------------
- If JSON file is missing, script stops safely
- Assumes Task 1 ran successfully
- Cleaning is basic but enough for analysis
"""