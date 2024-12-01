from openai import OpenAI


# Initialize OpenAI client
client = OpenAI(api_key="")  # Replace with your API key

def generator(dish_name, original_recipe, allergic_ingredients, evaluator_comment=None):
    """
    Generates a safe recipe based on the original recipe and user restrictions.

    Parameters:
    - Dish name (str)
    - original_recipe (str): The original recipe text.
    - restrictions (str): User restrictions (allergies, dietary needs).

    Returns:
    - new_recipe (str): The modified recipe that adheres to the restrictions.
    """
    
    if evaluator_comment:
        prompt = prompt = f"""As an experienced chef and nutrition expert, your task is to modify recipes to ensure they are safe,
    nutritionally balanced, and inclusive for individuals with specific dietary restrictions. Your goal is to provide
    high-quality substitutions that maintain the taste, texture, and cultural authenticity of the dish.
    **suggestions and rules:** {evaluator_comment}
    Please also strongly follow the suggestions and rules above

    **Dish Name:** {dish_name}

    **Original Recipe:**
    {original_recipe}

    **Allergic Ingredients to Avoid:**
    {allergic_ingredients}

    Please provide a substituted recipe that omits the specified allergic ingredients while preserving the dish's integrity.
    Ensure it remains enjoyable and nutritionally balanced. Include clear ingredient substitutions and adjust the instructions
    if necessary. Pay special attention to ingredients that are commonly ambiguous or have mixed sources, such as oils, sauces,
    or additives. Specify the specific subtype or variant of these ingredients to ensure clarity and safety. 

    **Important:** Provide only the modified recipe with the ingredients list and step-by-step instructions. Do not include any
    additional commentary or introductions.
    """
    # Create the prompt based on whether an original recipe was provided
    elif original_recipe:
        prompt = f"""As an experienced chef and nutrition expert, your task is to modify recipes to ensure they are safe,
    nutritionally balanced, and inclusive for individuals with specific dietary restrictions. Your goal is to provide
    high-quality substitutions that maintain the taste, texture, and cultural authenticity of the dish.

    **Dish Name:** {dish_name}

    **Original Recipe:**
    {original_recipe}

    **Allergic Ingredients to Avoid:**
    {allergic_ingredients}

    Please provide a substituted recipe that omits the specified allergic ingredients while preserving the dish's integrity.
    Ensure it remains enjoyable and nutritionally balanced. Include clear ingredient substitutions and adjust the instructions
    if necessary. Pay special attention to ingredients that are commonly ambiguous or have mixed sources, such as oils, sauces,
    or additives. Specify the specific subtype or variant of these ingredients to ensure clarity and safety. 

    **Important:** Provide only the modified recipe with the ingredients list and step-by-step instructions. Do not include any
    additional commentary or introductions.
    """

    else:
        prompt = f"""As an experienced chef and nutrition expert, your task is to create a recipe that avoids specific ingredients
    due to dietary restrictions. Your goal is to ensure the recipe is safe, nutritionally balanced, and inclusive,
    while being culturally appropriate and maintaining high standards of taste and texture.

    **Dish Name:** {dish_name}

    **Allergic Ingredients to Avoid:**
    {allergic_ingredients}

    Please create a new recipe for **{dish_name}** that omits the specified allergic ingredients. Ensure the recipe is clear,
    nutritionally balanced, and culturally authentic. Provide detailed ingredients and step-by-step instructions.
    Pay special attention to ingredients that are commonly ambiguous or have mixed sources, such as oils, sauces, or additives.
    Specify the specific subtype or variant of these ingredients to ensure clarity and safety.

    **Important:** Provide only the recipe with the ingredients list and step-by-step instructions. Do not include any
    additional commentary or introductions."""

    try:
      # Generate the substituted recipe using GPT-4
      response = client.chat.completions.create(
          model="gpt-4o",
          messages=[
              {"role": "system", "content": "You are an experienced chef and nutrition expert specializing in allergen-free cooking and ingredient substitutions. You create recipes that are safe, nutritionally balanced, and culturally inclusive, while maintaining excellent taste and texture."},
              {"role": "user", "content": prompt}
          ]
      )

      # Extract the response content
      substituted_recipe = response.choices[0].message.content.strip()
      return substituted_recipe
    except Exception as e:
        return f"An error occurred during recipe generation: {str(e)}"

def evaluator(dish_name, original_recipe, modified_recipe, restrictions, testing=False):
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
    
    if testing:
        #TODO Do we need to return something different if testing?
        system_prompt = """
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
        If the modified recipe passes all checks, the answer is simply “Yes” (valid modification). Avoid any additional evaluation or commentary. If any check fails, depending on the reason it fails, if it violates the hard rule such as including forbidden ingredients, the answer should be “No” and follow with an explanation in separate paragraphs. If the check fails because of potential risk or ambiguity, the answer should be “Caution”.
        
        Note: Only responsed "Yes" or "No" or "Caution"
        ### Response: {"Yes" or "No" or "Caution"}
        
        """
    
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

    if 'no' in evaluation.lower() and len(evaluation) < 5:
        evaluation = evaluator(dish_name, original_recipe, new_recipe, restrictions)
        if 'no' in evaluation.lower() and len(evaluation) < 5:
            return f"It is not possible to generate a new recipe that satisfy your restrictions!"
            
    return f"The newly generated recipe based on your restrictions is:\n\n{new_recipe}\n\nEvaluation of the recipe:\n{evaluation}"

