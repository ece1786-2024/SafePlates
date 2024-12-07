from ..Dataset.all_test_cases  import safe, unsafe, caution
from ..agent import evaluator


if __name__ == "__main__":
    categories = ["safe", "Not Safe", "Caution"]
    datasets = [safe, unsafe, caution]

    with open("validator_test_result.txt", "w") as file:
        count = 0
        correct = 0
        
        for category, dataset in zip(categories, datasets):
            file.write(f"\n<<----------------{category}------------------>>\n")   
            for data in dataset:
                dish_name = data['dish_name']
                restriction = data['restriction']
                original_recipe = data['original_recipe']
                modified_recipe = data['modified_recipe']
                
                result = evaluator(dish_name, original_recipe, modified_recipe, restriction)
                
                if "An error occurred during recipe generation:" in result:
                    print(result)

                else:  
                    split_result = result.split('\n')                    
                    validator_result = split_result[0]   
                    validator_result = validator_result.lower()

                    if category == "Safe":
                        if "yes" in validator_result:
                            correct += 1
                        else:
                            file.write(f"categories: {category}, evaluator result: {result}\n")
                            file.write(f"\n----------------------\n")
                            file.write(f"data: {data}\n")
                    
                    if category == "Not Safe":
                        if "no" in validator_result:
                            correct += 1
                        else:
                            file.write(f"categories: {category}, evaluator result: {result}\n")
                            file.write(f"\n----------------------\n")
                            file.write(f"data: {data}\n")
                    
                    if category == "Caution":
                        if "caution" in validator_result:
                            correct += 1
                        else:
                            file.write(f"categories: {category}, evaluator result: {result}\n")
                            file.write(f"\n----------------------\n")
                            file.write(f"data: {data}\n")
                            
                    count += 1
                file.write(f"\n<<Recipe #{count}---------------------------------->>\n")    
            file.write(f"\n----------------------\----------------------\----------------------\n")
            
        file.write(f"The validator is at {correct}/{count}% accuracy") 