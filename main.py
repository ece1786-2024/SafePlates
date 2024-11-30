import csv
from openai import OpenAI
import time
import gradio as gr

from agent import generator, evaluator, agent_flow
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
    substituted_recipe = agent_flow(dish_name, original_recipe, allergic_ingredients)

    # Display the result
    print("\nSubstituted Recipe:\n")
    print(substituted_recipe)


# Gradio interface
def generate_in_gradio(dish_name, original_recipe, allergic_ingredients):
    substituted_recipe = agent_flow(dish_name, original_recipe, allergic_ingredients)
    return substituted_recipe


def web_UI():
    # Path to your logo image file
    logo_path = "image/logo-removebg-preview.png"  # Replace with the actual path to your logo file

    # Custom CSS for styling buttons and textboxes
    css = """
    .gradio-container {background-color: #DBE8B4}
    
    #logo {
        display: block;
        margin: 0 auto; /* Center the logo horizontally */
        max-width: 100%; /* Ensure the logo doesn't overflow */
        height: auto; /* Maintain aspect ratio */
    }
    
    #submit_button {
        background-color: #6EB05A; /* Blue background */
        color: white; /* White text */
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }

    #submit_button:hover {
        background-color: #468915; /* Darker blue on hover */
    }

    .gr-textbox {
        border: 5px solid #007bff; /* Blue border */
        border-radius: 5px;
    }

    .gr-textbox input {
        color: #333; /* Text color */
    }

    .gr-textbox input:focus {
        border-color: #0056b3; /* Darker blue on focus */
        box-shadow: 0 0 5px #0056b3; /* Glow effect on focus */
    }
    
    .gr-textbox label {
        font-size: 24px !important; /* Larger font size for Textbox labels */
        font-weight: bold; /* Optional: Make Textbox labels bold */
        color: #333; /* Label color */
    }
    
    .gr-checkbox label {
        font-size: 20px; /* Normal font size for Checkbox labels */
        font-weight: normal; /* Default weight for Checkbox labels */
        color: #333; /* Label color for Checkbox */
    }
    """

    # Create the Gradio app
    with gr.Blocks(css=css) as app:
        # Header Section
        with gr.Column(elem_id="header", elem_classes=["center"]):
            gr.Image(logo_path, elem_id="logo", height=200, width=200)  # Logo at the top
            gr.Markdown(
                "<h1 style='text-align: center; font-size: 36px;'>Allergic Ingredients Substitution</h1>"
            )

        # Input Section
        with gr.Row():
            with gr.Column():
                gr.Markdown(
                    "<h3 style='text-align: center; font-size: 24px;'>Input Details</h3>"
                )
                dish_name = gr.Textbox(label="Dish Name", placeholder="Enter the dish name", lines=1)

                # Checkbox and Original Recipe Section
                use_original_recipe = gr.Checkbox(label="Do you want to input an original recipe?")
                original_recipe = gr.Textbox(label="Original Recipe",
                                             placeholder="Enter the original recipe",
                                             lines=3, visible=False)

                def toggle_textbox(use_recipe):
                    if use_recipe:
                        return gr.update(visible=True), ""
                    return gr.update(visible=False), "If you want to input an original recipe, check the box above."

                use_original_recipe.change(
                    fn=toggle_textbox,
                    inputs=[use_original_recipe],
                    outputs=[original_recipe, gr.Text(label="", interactive=False)]
                )

                allergic_ingredients = gr.Textbox(
                    label="Special Requirements",
                    placeholder="Enter special requirements (e.g., seafood-free, gluten-free, vegetarian)",
                    lines=2
                )

        # Submit button
        with gr.Row():
            submit_button = gr.Button("Generate Substituted Recipe", elem_id="submit_button")

        # Output Section
        with gr.Column(elem_id="output_section", elem_classes=["center"]):
            gr.Markdown(
                "<h3 style='text-align: center; font-size: 24px;'>Substituted Recipe</h3>"
            )
            output = gr.Textbox(label="", interactive=False, lines=6)

        # Define button click action
        submit_button.click(fn=generate_in_gradio, inputs=[dish_name, original_recipe, allergic_ingredients],
                            outputs=output)

    # Launch the app
    app.launch()


def run_test_case(output_file="validated_test_case_results.txt"):
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

            # Generate the substituted recipe after evaluated by the validator
            validated_substituted_recipe = agent_flow(dish_name, original_recipe, allergic_ingredients)

            # Print and write substituted recipe to the file
            file.write("\nValidated Substituted Recipe:\n")
            file.write(f"{validated_substituted_recipe}\n")
            print("\nValidated Substituted Recipe:")
            print(validated_substituted_recipe)
            print("-" * 50)
            file.write("-" * 50 + "\n")

    print(f"Test results have been saved to {output_file}")


if __name__ == "__main__":
    # uncomment this for interact within the command line interface
    # command_line_UI()

    # uncomment this for the website-based UI
    web_UI()

    # uncomment this to run the provided test cases
    # run_test_case()