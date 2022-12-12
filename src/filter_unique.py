import pandas as pd


amazon_food = pd.read_csv("amazon_food_nodes.csv")
amazon_food = amazon_food.drop_duplicates()

amazon_food.to_csv("amazon_food_nodes.csv", index=False)
