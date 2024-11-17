import openai
import os
from openai import OpenAI

def generator(dish_name, original_recipe="", restrictions=""):
    """
    Generates a safe recipe based on the original recipe and user restrictions.

    Parameters:
    - Dish name (str)
    - original_recipe (str): The original recipe text.
    - restrictions (str): User restrictions (allergies, dietary needs).

    Returns:
    - new_recipe (str): The modified recipe that adheres to the restrictions.
    """
    prompt = f"""
    Given the following information:

    **Dish Name:**
    {dish_name}

    **Original Recipe:**
    {original_recipe if original_recipe else "N/A"}

    **User Specifications:**
    {restrictions}

    Please provide a modified recipe that adheres to the user's specifications and restrictions, such as accommodate users' dietary restrictions or allergies. 
    Include a list of ingredients and detailed preparation steps. Ensure that the modified recipe is safe for the user and maintains the original flavor and characteristics of the dish as much as possible. 
    If no original recipe is provided, generate a new recipe based on the dish name and user specifications.
    """
    client = OpenAI()
    try:
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages= [
        {
          "role": "system",
          "content": [
            {
              "type": "text",
              "text": "You are a culinary expert that edit and generate recipes."
              
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt
            }
                    ]
        }
        ]
        )
        new_recipe = completion.choices[0].message.content
        return new_recipe
    
    except Exception as e:
        return f"An error occurred during recipe generation: {str(e)}"


def evaluator(original_recipe, modified_recipe, restrictions):
    prompt = f"""
    Evaluate the modified recipe below to ensure it adheres to the user's restrictions and makes sense. Provide feedback on its safety and reasonableness.
    Output 1 if the recipe is safe and acceptable;
    Output 0 if the recipe is not safe or not realistic or  taste totally different compared to the original recipe.

    ### Original Recipe:
    {original_recipe}

    ### Modified Recipe:
    {modified_recipe}

    ### User Restrictions:
    {restrictions}

    ### Evaluation:
    """
    client = OpenAI()

    try:
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages= [
        {
          "role": "system",
          "content": [
            {
              "type": "text",
              "text": "You are a food safety expert and culinary critic."
              
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt
            }
                    ]
        }
        ]
        )
        evaluation = completion.choices[0].message.content.strip()
        return int(evaluation)
    except Exception as e:
        return f"An error occurred during recipe evaluation: {str(e)}"