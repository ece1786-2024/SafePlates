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
            
            result = evaluator(dish_name, original_recipe, modified_recipe, restriction)
            
            print(f"Result #{count}: {result}")
            
            if "An error occurred during recipe generation:" in result:
                print(result)
                
            else:
                if categories == "Safe":
                    if categories.lower() in result.lower() and "no" not in result.lower():
                        correct += 1
                    #TODO do we need to consider something else?
                        
                if categories == "Not Safe":
                    if categories.lower() in result.lower():
                        correct += 1
                    #TODO do we need to consider something else?
                
                if categories == "Caution":
                    if categories.lower() in result.lower():
                        correct += 1
                    #TODO do we need to consider something else?
                        
                count += 1
                    
            print(f"The validator is at {correct}/{count}% accuracy")     