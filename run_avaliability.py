import pandas as pd
import glob
from agent import agent_flow

dataset = "Dataset/availability_dataset__subset_1.csv"


def read_and_display_recipes(file_name):
    """
    Reads each recipe from the generated dataset and prints the details.
    
    Parameters:
        file_prefix (str): Prefix for the subset file names.
        num_subsets (int): Number of subsets to process.
    """

    # Read the subset file
    df = pd.read_csv(file_name)
    count = 0
    
    print(f"\n--- Recipes from {file_name} ---")
    for index, row in df.iterrows():
        result = agent_flow(
            f"Title: {row['title']}",
            str(f"Ingredients: {row['ingredients']}" + f"\nDirections: {row['directions']}"),
            str(row['requirment'])
            )
        if "It is not possible to generate a new recipe" in result:
            count += 1
    print(count)


read_and_display_recipes(dataset)
