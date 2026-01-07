import pandas as pd

df = pd.read_csv("dataset .csv")
df = df[['City', 'Aggregate rating']].dropna()
city_counts = df['City'].value_counts()
top_city_by_restaurants = city_counts.idxmax()
top_city_count = city_counts.max()

print(f"\nCity with Highest Number of Restaurants: {top_city_by_restaurants}")
print(f"Number of Restaurants: {top_city_count}")

city_avg_ratings = (
    df.groupby('City')['Aggregate rating']
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Rating by City:\n")
print(city_avg_ratings.head(10))
top_city_by_rating = city_avg_ratings.idxmax()
top_city_avg_rating = city_avg_ratings.max()
print(f"\nCity with Highest Average Rating: {top_city_by_rating}")
print(f"Average Rating: {top_city_avg_rating:.2f}")

city_counts_df = city_counts.reset_index()
city_counts_df.columns = ['City', 'Restaurant Count']
city_avg_ratings_df = city_avg_ratings.reset_index()
city_avg_ratings_df.columns = ['City', 'Average Rating']
city_counts_df.to_csv(
    "output/city_restaurant_counts.csv", index=False
)

city_avg_ratings_df.to_csv(
    "output/city_average_ratings.csv", index=False
)

summary_df = pd.DataFrame({
    'Metric': [
        'City with Highest Number of Restaurants',
        'City with Highest Average Rating'
    ],
    'Value': [
        f"{top_city_by_restaurants} ({top_city_count})",
        f"{top_city_by_rating} ({round(top_city_avg_rating, 2)})"
    ]
})

summary_df.to_csv(
    "output/city_analysis_summary.csv", index=False
)

print("\nResults saved in output/ folder")
