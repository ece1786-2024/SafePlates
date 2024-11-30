from ..Dataset.validator_dataset  import safe, non_safe, caution
from ..agent import evaluator


if __name__ == "__main__":
    categories = ["Safe", "Not Safe", "Caution"]
    datasets = [safe, non_safe, caution]
    
    for category, dataset in zip(categories, datasets):
        count = 0
        correct = 0
        for data in dataset:
            dish_name = data['dish_name']
            restriction = data['requirement']
            original_recipe = data['original_recipe']
            modified_recipe = data['new_recipe']
            
            result = evaluator(dish_name, original_recipe, modified_recipe, restriction, testing=True)
            
            print(f"Result #{count}: {result}")
            
            if "An error occurred during recipe generation:" in result:
                print(result)
                
            else:
                if categories == "Safe":
                    if "yes" in result.lower():
                        correct += 1
                        
                if categories == "Not Safe":
                    if "no" in result.lower():
                        correct += 1
                
                if categories == "Caution":
                    if "caution" in result.lower():
                        correct += 1
                        
                count += 1
                    
            print(f"The validator is at {correct}/{count}% accuracy")     