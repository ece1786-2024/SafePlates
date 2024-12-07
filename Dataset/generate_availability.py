import pandas as pd
import random

def random_select_subsets_with_allergies(file_path, output_prefix, num_subsets, subset_size):
    """
    Randomly selects subsets from a CSV file, ensures subsets don't have overlapping elements,
    adds a random allergen-free label to each row, and saves each subset to a new file.
    
    Parameters:
        file_path (str): Path to the CSV file.
        output_prefix (str): Prefix for the output file names.
        num_subsets (int): Number of subsets to create. Default is 4.
        subset_size (int): Number of rows in each subset. Default is 10.
        
    Returns:
        dict: A dictionary where keys are subset names and values are DataFrames.
    """
    # List of common allergy-free labels
    allergy_free_list = [
        "Gluten-free",
        "Dairy-free",
        "Peanut-free",
        "Tree nut-free",
        "Soy-free",
        "Egg-free",
        "Fish-free",
        "Shellfish-free",
        "Wheat-free",
        "Sesame-free",
        "Mustard-free",
        "Sulfite-free",
        "Corn-free",
        "Lupin-free",
        "Celery-free"
    ]
    replace_meat_list = [
        "If pork exist, replace it with other meat",
        "If chicken exist in the recipe, replace it with other protein",
        "If the recipe has beef in it, repalce it with chicken",
        "If the recipe has lamb in it, replace it with seafood",
        "If exist, replace all the meat with beef",
        "If duck meat exist, replace it with other meat",
        "If fish exist, replace it with beef",
        "If all the darkmeat if exist, with white meat",
        "If seafood exist, replace it with other protein"

    ]
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Retain only required columns
    required_columns = ['title', 'ingredients', 'directions']
    df = df[required_columns]
    
    # Ensure there are enough rows in the CSV to create the subsets
    if len(df) < num_subsets * subset_size:
        raise ValueError("Not enough unique rows in the CSV file to create the subsets.")
    
    # Shuffle the data
    shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Create and save subsets
    subsets = {}
    for i in range(num_subsets):
        subset_name = f"_subset_{i+1}"
        subset_rows = shuffled_df.iloc[:subset_size]
        
        # Add a random allergen-free label to each row
        subset_rows['allergy_free'] = [
            random.choice(allergy_free_list) for _ in range(len(subset_rows))
        ]
        
        subsets[subset_name] = subset_rows
        
        # Save the subset to a new CSV file
        output_file = f"{output_prefix}_{subset_name}.csv"
        subset_rows.to_csv(output_file, index=False)
        print(f"Saved {subset_name} to {output_file}")
        
        # Remove selected rows to avoid duplicates
        shuffled_df = shuffled_df.iloc[subset_size:]
    
    return subsets

# Example usage
file_path = 'full_dataset.csv'
output_prefix = 'availability_dataset'
try:
    subsets = random_select_subsets_with_allergies(file_path, output_prefix, num_subsets=4, subset_size=200)
except ValueError as e:
    print(e)
