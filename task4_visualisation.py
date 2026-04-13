# import pandas as pd
# import matplotlib.pyplot as plt
# import os

# def shorten_title(title, length=50):
#     # small helper to trim long titles so graph looks clean
#     if len(title) > length:
#         return title[:length] + "..."
#     return title

# def main():

#     file_path = "data/trends_analysed.csv"

#     # trying to load file
#     try:
#         df = pd.read_csv(file_path)
#     except:
#         print("Couldn't find analysed CSV. Run Task 3 first.")
#         return

#     # creating outputs folder if not exists
#     if not os.path.exists("outputs"):
#         os.makedirs("outputs")

#     # -----------------------------
#     # CHART 1: TOP 10 STORIES
#     # -----------------------------
#     top10 = df.sort_values(by="score", ascending=False).head(10)

#     titles = [shorten_title(t) for t in top10["title"]]
#     scores = top10["score"]

#     plt.figure()
#     plt.barh(titles, scores)
#     plt.xlabel("Score")
#     plt.ylabel("Story Title")
#     plt.title("Top 10 Stories by Score")
#     plt.gca().invert_yaxis()  # highest on top

#     plt.savefig("outputs/chart1_top_stories.png")

#     # -----------------------------
#     # CHART 2: STORIES PER CATEGORY
#     # -----------------------------
#     category_counts = df["category"].value_counts()

#     plt.figure()
#     plt.bar(category_counts.index, category_counts.values)
#     plt.xlabel("Category")
#     plt.ylabel("Number of Stories")
#     plt.title("Stories per Category")

#     plt.savefig("outputs/chart2_categories.png")

#     # -----------------------------
#     # CHART 3: SCATTER PLOT
#     # -----------------------------
#     plt.figure()

#     # separating popular vs non-popular
#     popular = df[df["is_popular"] == True]
#     not_popular = df[df["is_popular"] == False]

#     plt.scatter(popular["score"], popular["num_comments"], label="Popular")
#     plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

#     plt.xlabel("Score")
#     plt.ylabel("Number of Comments")
#     plt.title("Score vs Comments")
#     plt.legend()

#     plt.savefig("outputs/chart3_scatter.png")

#     # -----------------------------
#     # BONUS: DASHBOARD
#     # -----------------------------
#     fig, axes = plt.subplots(1, 3, figsize=(18, 5))

#     # chart 1 inside dashboard
#     axes[0].barh(titles, scores)
#     axes[0].set_title("Top Stories")
#     axes[0].invert_yaxis()

#     # chart 2 inside dashboard
#     axes[1].bar(category_counts.index, category_counts.values)
#     axes[1].set_title("Categories")

#     # chart 3 inside dashboard
#     axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
#     axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
#     axes[2].set_title("Score vs Comments")
#     axes[2].legend()

#     fig.suptitle("TrendPulse Dashboard")

#     plt.savefig("outputs/dashboard.png")

#     print("All charts saved in outputs/ folder")


# if __name__ == "__main__":
#     main()


# """
# ----------------------------------------
# MY UNDERSTANDING
# ----------------------------------------
# This part is about converting numbers into visuals.

# Steps I followed:
# 1. Loaded analysed CSV from Task 3
# 2. Created outputs folder to store images
# 3. Made 3 charts:
#    - Top 10 stories (horizontal bar)
#    - Stories per category (bar chart)
#    - Score vs comments (scatter plot)
# 4. Used is_popular column to separate points in scatter plot
# 5. Combined all charts into one dashboard
# 6. Saved all images as PNG files

# ----------------------------------------
# HOW I TESTED THIS
# ----------------------------------------
# 1. Made sure Task 3 file exists
# 2. Ran:
#    python task4_visualization.py

# 3. Checked:
#    - outputs folder created
#    - all 4 images saved
#    - charts look correct
#    - titles not too long

# ----------------------------------------
# NOTES
# ----------------------------------------
# - Titles trimmed manually to avoid messy graph
# - Colors are default matplotlib (kept simple)
# - Dashboard is basic but shows all insights together
# """