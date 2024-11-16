import csv
from openai import OpenAI
import time
import gradio as gr

from agent import generator
from test_cases import test_cases


def get_user_input():
    # Gather the necessary information from the user
    dish_name = input("Enter the dish name (required): ").strip()
    while not dish_name:
        print("Dish name is required. Please enter a valid dish name.")
        dish_name = input("Enter the dish name (required): ").strip()

    original_recipe = input("Enter the original recipe (optional, leave blank if none): ").strip()

    allergic_ingredients = input("Enter the ingredients to substitute (required, separate by commas): ").strip()
    while not allergic_ingredients:
        print("Allergic ingredients are required. Please enter at least one ingredient to avoid.")
        allergic_ingredients = input("Enter the ingredients to substitute (required, separate by commas): ").strip()

    return dish_name, original_recipe, allergic_ingredients


def command_line_UI():
    # Get user inputs
    dish_name, original_recipe, allergic_ingredients = get_user_input()

    # Generate substituted recipe
    substituted_recipe = generator(dish_name, original_recipe, allergic_ingredients)

    # Display the result
    print("\nSubstituted Recipe:\n")
    print(substituted_recipe)


# Gradio interface
def gradio_interface(dish_name, original_recipe, allergic_ingredients):
    substituted_recipe = generator(dish_name, original_recipe, allergic_ingredients)
    return substituted_recipe


def web_UI():
    # Load your logo image file
    logo_path = "image/logo-removebg-preview.png"  # Replace with the actual path to your logo file

    # Create the Gradio app
    with gr.Blocks() as app:
        gr.Image(logo_path, elem_id="logo", label="SafePlates", height=150, width=150)  # Adjust the height as needed
        gr.Markdown("<h2 style='text-align: center;'>Allergic Ingredients Substitution</h2>")

        with gr.Row():
            with gr.Column():
                dish_name = gr.Textbox(label="Dish Name", placeholder="Enter the dish name")
                original_recipe = gr.Textbox(label="Original Recipe",
                                             placeholder="Enter the original recipe (optional)")
                allergic_ingredients = gr.Textbox(label="Allergic Ingredients",
                                                  placeholder="Enter ingredients to substitute (separate by commas)")

        submit_button = gr.Button("Generate Substituted Recipe")
        output = gr.Textbox(label="Substituted Recipe")

        # Define the action on button click
        submit_button.click(fn=gradio_interface, inputs=[dish_name, original_recipe, allergic_ingredients],
                            outputs=output)

    # Run the app
    app.launch()


def run_test_case(output_file="test_case_results.txt"):
    # Open the file with UTF-8 encoding
    with open(output_file, "w", encoding="utf-8") as file:
        for i, test_case in enumerate(test_cases):
            dish_name = test_case["dish_name"]
            original_recipe = test_case["original_recipe"]
            allergic_ingredients = test_case["allergic_ingredients"]

            # Print and write test case details to the file
            file.write(f"Test Case {i + 1}:\n")
            file.write(f"Dish Name: {dish_name}\n")
            print(f"Running Test Case {i + 1}...")
            print(f"Dish Name: {dish_name}")

            if original_recipe:
                file.write("Original Recipe Ingredients:\n")
                file.write(f"{original_recipe['ingredients']}\n")
                file.write("Original Recipe Instructions:\n")
                file.write(f"{original_recipe['instructions']}\n")
                print("Original Recipe Ingredients:")
                print(original_recipe["ingredients"])
                print("Original Recipe Instructions:")
                print(original_recipe["instructions"])
            else:
                file.write("Original Recipe: None provided\n")
                print("Original Recipe: None provided")

            file.write(f"Allergic Ingredients: {allergic_ingredients}\n")
            print(f"Allergic Ingredients: {allergic_ingredients}")

            # Generate the substituted recipe
            substituted_recipe = generator(dish_name, original_recipe, allergic_ingredients)

            # Print and write substituted recipe to the file
            file.write("\nSubstituted Recipe:\n")
            file.write(f"{substituted_recipe}\n")
            print("\nSubstituted Recipe:")
            print(substituted_recipe)
            print("-" * 50)
            file.write("-" * 50 + "\n")

    print(f"Test results have been saved to {output_file}")


if __name__ == "__main__":
    # uncomment this for interact within the command line interface
    # command_line_UI()

    # uncomment this for the website-based UI
    # web_UI()

    # uncomment this to run the provided test cases
    run_test_case()