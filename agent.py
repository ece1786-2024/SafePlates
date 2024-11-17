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


def evaluator(dish_name, original_recipe, modified_recipe, restrictions):
    prompt = f"""
    I will provide you with:
        1.	A dish name.
        2.	A specific requirement (e.g., dietary restriction or allergy).
        3.	An original recipe corresponding to the dish name (including ingredients and cooking steps).
        4.	A modified recipe that attempts to adjust the original recipe based on the requirement.
    Your task is to determine if the modified recipe is valid. Follow these steps to evaluate the validity:
    •  Edibility and Nutritional Sense: Ensure the modified recipe produces a dish that is edible and nutritionally coherent. For example, replacing "butter chicken" with "butter cheese" is invalid if it results in a dish that is unbalanced or nonsensical.
    •  Ingredient Safety: Ensure that the substituted ingredients:
        •	Are safe to consume individually and in combination.
        •	Do not pose cross-contamination risks, especially in recipes tailored for allergies. For example, in a nut-free recipe, substitutions must explicitly be certified nut-free. If no explicit certification is provided, assume potential contamination and classify the recipe as invalid.
    •  Requirement Fulfillment: Confirm that the specific requirement is fully satisfied. Examples include:
        •	For allergies, substitutions must not only replace triggering ingredients but also prevent cross-reactivity or contamination risks. This must be explicitly verified (e.g., “certified nut-free”). If not explicitly stated, assume any potential risk as real risk.
        •	For dietary restrictions, ensure all ingredients comply with the stated guidelines.
    •  Cooking Steps: Evaluate whether the steps are logical and feasible with the modified ingredients.
    If the modified recipe passes all checks, the answer is simply “Yes” (valid modification). If any check fails, the answer starts with “No”, followed by an explanation of why it is not valid in a separate paragraph. Avoid any additional evaluation or commentary.
    
    ### Dish Name:
    {dish_name}

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
        return evaluation
    except Exception as e:
        return f"An error occurred during recipe evaluation: {str(e)}"


def agent_flow(dish_name, original_recipe, restrictions):
    new_recipe = generator(dish_name, original_recipe, restrictions)
    evaluation = evaluator(dish_name, original_recipe, new_recipe, restrictions)

    if evaluation.lower().startswith("yes"):
        return new_recipe
    else:
        return "No valid substitution available"