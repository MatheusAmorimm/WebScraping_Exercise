import pandas as pd

df = pd.read_excel("data/books.csv")

general_avg_stars_df = df["Stars"].mean()

genre_avg_stars_df = df.groupby("Gender").agg(
    total_stars=("Stars", "sum"),
    book_count=("Stars", "count"),
    media_stars=("Stars", "mean")
).reset_index()

genre_above_avg_df = genre_avg_stars_df[genre_avg_stars_df["media_stars"] > general_avg_stars_df]

genre_avg_stars_df.to_excel("data/genre_avg.xlsx", index=False)
genre_above_avg_df.to_excel("data/genre_above.xlsx", index=False)
