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
            messages=[
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
    system_prompt = f"""
    I will provide you with:
    1.	A dish name.
    2.	A specific requirement (e.g., dietary restriction or allergy).
    3.	An original recipe corresponding to the dish name (including ingredients and cooking steps).
    4.	A modified recipe that attempts to adjust the original recipe based on the requirement.
    Your task is to determine if the modified recipe is valid. Follow these steps to evaluate the validity:
    •  Edibility and Nutritional Sense: Ensure the modified recipe produces a dish that is edible and nutritionally coherent. For example, replacing "butter chicken" with "butter cheese" is invalid if it results in a dish that is unbalanced or nonsensical.
    •  Ingredient Safety: Ensure that the substituted ingredients:
    •	Are safe to consume individually and in combination.
    •	Do not pose cross-contamination risks, especially in recipes tailored for allergies. For example, in a nut-free recipe, substitutions must explicitly be certified nut-free. If no explicit certification is provided, assume the ingredient is potentially contaminated.
    •  Requirement Fulfillment: Confirm that the specific requirement is fully satisfied. Examples include:
    •	For allergies, not only ingredient safety needs to be assert, but also cross-reactivity risk and cross-contamination risk needs to be checked.
    •	For dietary restrictions, ensure all ingredients comply with the stated guidelines.
    •  Cooking Steps: Evaluate whether the steps are logical and feasible with the modified ingredients.
    If the modified recipe passes all checks, the answer is simply “Yes” (valid modification). Avoid any additional evaluation or commentary. If any check fails, depending on the reason it fails, if it violates the hard rule such as including forbidden ingredients, the answer should be “No” and follow with an explanation in separate paragraphs. If the check fails because of potential risk or ambiguity, the answer should be “Caution” and follow the points need to be watch out.
    """

    user_prompt = f"""
    ### Dish Name:
    {dish_name}

    ### Original Recipe:
    {original_recipe}

    ### Modified Recipe:
    {modified_recipe}

    ### User Restrictions:
    {restrictions}

    """
    client = OpenAI()

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": system_prompt

                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt
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

    # if evaluation.lower().startswith("yes"):
    #     return new_recipe
    # else:
    #     return "No valid substitution available"
    return new_recipe + "\n\n" + evaluation
