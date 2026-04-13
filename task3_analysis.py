# import pandas as pd
# import numpy as np

# def main():

#     file_path = "data/trends_clean.csv"

#     # trying to load file
#     try:
#         df = pd.read_csv(file_path)
#     except Exception as e:
#         print("Couldn't load CSV file. Did you run Task 2?")
#         return

#     # basic info
#     print(f"\nLoaded data: {df.shape}")

#     print("\nFirst 5 rows:")
#     print(df.head())

#     # averages using pandas
#     avg_score = df["score"].mean()
#     avg_comments = df["num_comments"].mean()

#     print(f"\nAverage score   : {int(avg_score)}")
#     print(f"Average comments: {int(avg_comments)}")

#     # -----------------------------
#     # NUMPY BASED ANALYSIS
#     # -----------------------------
#     print("\n--- NumPy Stats ---")

#     scores = df["score"].values  # converting to numpy array

#     mean_score = np.mean(scores)
#     median_score = np.median(scores)
#     std_score = np.std(scores)

#     print(f"Mean score   : {int(mean_score)}")
#     print(f"Median score : {int(median_score)}")
#     print(f"Std deviation: {int(std_score)}")

#     print(f"Max score    : {int(np.max(scores))}")
#     print(f"Min score    : {int(np.min(scores))}")

#     # category with most stories
#     category_counts = df["category"].value_counts()
#     top_category = category_counts.idxmax()
#     top_count = category_counts.max()

#     print(f"\nMost stories in: {top_category} ({top_count} stories)")

#     # most commented story
#     max_comments_row = df.loc[df["num_comments"].idxmax()]
#     print(f'\nMost commented story: "{max_comments_row["title"]}" — {max_comments_row["num_comments"]} comments')

#     # -----------------------------
#     # ADDING NEW COLUMNS
#     # -----------------------------

#     # engagement = comments per upvote (rough idea)
#     df["engagement"] = df["num_comments"] / (df["score"] + 1)

#     # marking popular stories
#     df["is_popular"] = df["score"] > avg_score

#     # -----------------------------
#     # SAVE FILE
#     # -----------------------------
#     output_path = "data/trends_analysed.csv"
#     df.to_csv(output_path, index=False)

#     print(f"\nSaved to {output_path}")


# if __name__ == "__main__":
#     main()


# """
# ----------------------------------------
# MY UNDERSTANDING
# ----------------------------------------
# This part is mainly about analysing the cleaned data.

# Steps I followed:
# 1. Loaded the cleaned CSV from Task 2
# 2. Printed basic info like shape and first few rows
# 3. Calculated averages using pandas
# 4. Used NumPy for stats like mean, median, std deviation
# 5. Found:
#    - category with most stories
#    - most commented story
# 6. Added 2 new columns:
#    - engagement (comments per score)
#    - is_popular (above average score)
# 7. Saved updated file for next task

# ----------------------------------------
# HOW I TESTED THIS
# ----------------------------------------
# 1. Made sure Task 2 CSV exists
# 2. Ran:
#    python task3_analysis.py

# 3. Checked:
#    - output prints correctly
#    - no errors
#    - trends_analysed.csv created
#    - new columns exist in file

# ----------------------------------------
# NOTES
# ----------------------------------------
# - Used NumPy mainly for stats (as required)
# - Engagement formula is simple approximation
# - If file missing, script exits safely
# """