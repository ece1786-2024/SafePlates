# Test cases for the Allergic Ingredients Substitution
test_cases = [
    {
        "dish_name": "Lasagna",
        "original_recipe": {
            "ingredients": (
                "12 lasagna noodles, 1 lb ground beef, 1 jar marinara sauce, 16 oz ricotta cheese, "
                "3 cups shredded mozzarella cheese, 1/2 cup grated Parmesan cheese, 1 egg, "
                "2 cloves garlic (minced), 1 tbsp olive oil, 1 tsp dried oregano, 1 tsp salt, 1 tsp pepper"
            ),
            "instructions": (
                "1. Preheat oven to 375°F (190°C). Cook lasagna noodles according to package instructions. "
                "2. In a skillet, heat olive oil and sauté garlic until fragrant. Add ground beef and cook until browned. "
                "3. Stir in marinara sauce, oregano, salt, and pepper; simmer for 10 minutes. "
                "4. In a bowl, mix ricotta cheese, egg, Parmesan, and 1 cup of mozzarella. "
                "5. Layer the lasagna: spread sauce on the bottom of a baking dish, add noodles, spread ricotta mixture, "
                "add mozzarella, and repeat. Top with remaining mozzarella. "
                "6. Cover with foil and bake for 25 minutes, then uncover and bake for another 15 minutes until golden."
            )
        },
        "allergic_ingredients": "lasagna noodles, ricotta cheese, Parmesan cheese"
    },
    {
        "dish_name": "Chicken Alfredo",
        "original_recipe": {
            "ingredients": (
                "1 lb fettuccine pasta, 2 chicken breasts, 2 tbsp butter, 1 cup heavy cream, "
                "1/2 cup grated Parmesan cheese, 2 cloves garlic (minced), 1/4 tsp nutmeg, "
                "1 tbsp olive oil, 1 tsp salt, 1 tsp pepper, parsley (for garnish)"
            ),
            "instructions": (
                "1. Cook fettuccine according to package instructions. "
                "2. Season chicken breasts with salt and pepper. Heat olive oil in a skillet and cook chicken until golden "
                "and cooked through, about 6-8 minutes per side. Remove and slice. "
                "3. In the same skillet, melt butter and sauté garlic until fragrant. Add heavy cream and bring to a simmer. "
                "4. Stir in Parmesan cheese and nutmeg, stirring until smooth. "
                "5. Toss cooked pasta with Alfredo sauce and top with sliced chicken. Garnish with parsley."
            )
        },
        "allergic_ingredients": "fettuccine pasta, Parmesan cheese, heavy cream"
    },
    {
        "dish_name": "Vegetarian Pad Thai",
        "original_recipe": None,  # No original recipe provided
        "allergic_ingredients": "peanuts, soy sauce, eggs"
    },
    {
        "dish_name": "Beef Stroganoff",
        "original_recipe": None,  # No original recipe provided
        "allergic_ingredients": "sour cream, butter, wheat flour"
    }
]
