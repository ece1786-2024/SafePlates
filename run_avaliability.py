import random

import pandas as pd
import glob
from agent import agent_flow

dataset1 = "Dataset/availability_dataset__subset_1.csv"
dataset2 = "Dataset/availability_dataset__subset_2.csv"
dataset3 = "Dataset/availability_dataset__subset_3.csv"
dataset4 = "Dataset/availability_dataset__subset_4.csv"

output1 = "Testing/availability_test_result_1.txt"
output2 = "Testing/availability_test_result_2.txt"
output3 = "Testing/availability_test_result_3.txt"
output4 = "Testing/availability_test_result_4.txt"

special_requirements = [
    "make it suitable for elders",
    "make it suitable for children",
    "make it suitable for baby",
    "make it suitable for pregnant women",
    "for any chicken I want to use dark meat",
    "for any chicken I want to use white meat",
    "replace all meat by pork",
    "replace all meat by shrimp",
    "make it sugar free",
    "I am trying to loss weight",
]


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
    print(f"\nCount of non-possible recipes: {count}")


# read_and_display_recipes(dataset1)


def read_and_save_recipes(file_name, output_file):
    """
    Reads each recipe from the generated dataset, processes it, and saves the inputs and results to a file.

    Parameters:
        file_name (str): Name of the input file containing recipes.
        output_file (str): Name of the output file to save results.
    """

    # Read the subset file
    df = pd.read_csv(file_name)
    count = 0

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"--- Recipes from {file_name} ---\n\n")

        for index, row in df.iterrows():
            print(f"Processing case {index}")
            # Prepare the inputs
            title = f"Title: {row['title']}"
            ingredients_and_directions = f"Ingredients: {row['ingredients']}\nDirections: {row['directions']}"
            # requirement = f"Requirement: {random.choice(special_requirements)}"
            requirement = f"Requirement: {row['requirment']}"

            # Process the inputs to get the result
            result = agent_flow(
                title,
                ingredients_and_directions,
                requirement,
                debug=True
            )

            # Save the inputs and result to the file
            file.write(f"Case {index}-{title}\n")
            file.write(f"{ingredients_and_directions}\n")
            file.write(f"{requirement}\n\n")
            file.write(f"Result:\n{result}\n")
            file.write("-" * 100 + "\n")

            if "It is not possible to generate a new recipe" in result:
                count += 1
                print(f"recipe at {index} is not possible")
                print(f"Result:{result}\n")

        # Write the summary to the file
        file.write(f"\nCount of non-possible recipes: {count}\n")

    print(f"\nCount of non-possible recipes: {count}")

    print(f"Inputs and results saved to {output_file}")


# Example usage
# read_and_save_recipes(dataset1, output1)
read_and_save_recipes(dataset2, output2)
# read_and_save_recipes(dataset3, output3)
# read_and_save_recipes(dataset4, output4)
