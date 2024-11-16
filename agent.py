from openai import OpenAI

# Initialize OpenAI client
# client = OpenAI(api_key='your_api_key_here')  # Replace with your API key

client = OpenAI(api_key='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')


def generator(dish_name, original_recipe, allergic_ingredients):
    # Create the prompt based on whether an original recipe was provided
    if original_recipe:
        prompt = (
            f"As an experienced chef and nutrition expert, you are tasked with modifying recipes to ensure they are safe, "
            f"nutritionally balanced, and inclusive for individuals with specific dietary restrictions. "
            f"Your goal is to provide high-quality substitutions that maintain the taste, texture, and cultural authenticity of the dish.\n\n"
            f"Dish Name: {dish_name}\n\n"
            f"Original Recipe:\n{original_recipe}\n\n"
            f"Allergic Ingredients:\n{allergic_ingredients}\n\n"
            f"Please provide a substituted recipe that avoids the specified allergic ingredients while preserving the dish's integrity, "
            f"ensuring it remains enjoyable and nutritionally balanced. Include clear ingredient substitutions and adjusted instructions if necessary."
        )
    else:
        prompt = (
            f"As an experienced chef and nutrition expert, you are tasked with creating a recipe that avoids specific ingredients "
            f"due to dietary restrictions. Your goal is to ensure the recipe is safe, nutritionally balanced, and inclusive, "
            f"while also being culturally appropriate and maintaining high standards of taste and texture.\n\n"
            f"Dish Name: {dish_name}\n\n"
            f"Allergic Ingredients to Avoid:\n{allergic_ingredients}\n\n"
            f"Please create a new recipe for {dish_name} that avoids the specified allergic ingredients. Ensure the recipe is clear, "
            f"nutritionally balanced, and culturally authentic. Provide detailed ingredients and step-by-step instructions."
        )

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
