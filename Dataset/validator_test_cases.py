unsafe = [
#     Case 1: New recipe does not satisfy the ingredient requirements
{
    "dish_name": "Peanut Butter Cookies",
    "restriction": "peanuts",
    "original_recipe": {
        "ingredients": [
            "2 cups peanut butter",
            "1 cup sugar",
            "1 egg"
        ],
        "steps": [
            "Preheat oven to 350°F.",
            "Mix peanut butter, sugar, and egg together.",
            "Roll into balls and flatten with a fork.",
            "Bake for 10 minutes."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 cups almond butter",
            "1 cup sugar",
            "1 egg"
        ],
        "steps": [
            "Preheat oven to 350°F.",
            "Mix almond butter, sugar, and egg together.",
            "Roll into balls and flatten with a fork.",
            "Bake for 10 minutes."
        ]
    }
},

# Case 2: New recipe satisfies the requirement, but the cooking step can introduce food poisoning
{
    "dish_name": "Grilled Chicken Salad",
    "restriction": "dairy",
    "original_recipe": {
        "ingredients": [
            "1 lb chicken breast",
            "1 cup lettuce",
            "1/2 cup cheese",
            "2 tbsp ranch dressing"
        ],
        "steps": [
            "Grill the chicken until fully cooked.",
            "Slice the chicken and mix with lettuce, cheese, and ranch dressing."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 lb chicken breast",
            "1 cup lettuce",
            "2 tbsp olive oil"
        ],
        "steps": [
            "Grill the chicken but remove it from heat before fully cooked.",
            "Slice the chicken and mix with lettuce and olive oil."
        ]
    }
},

# Case 3: New recipe introduces a new form of dangerous ingredient different from the restriction but still causes food poisoning
{
    "dish_name": "Seafood Paella",
    "restriction": "shrimp",
    "original_recipe": {
        "ingredients": [
            "1 cup rice",
            "1/2 lb shrimp",
            "1/2 lb clams",
            "1/2 lb mussels",
            "2 cups chicken broth",
            "1/2 tsp saffron"
        ],
        "steps": [
            "Cook rice with chicken broth and saffron.",
            "Add shrimp, clams, and mussels to the rice and cook until fully done."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 cup rice",
            "1/2 lb crab meat",
            "1/2 lb clams",
            "1/2 lb mussels",
            "2 cups chicken broth",
            "1/2 tsp saffron"
        ],
        "steps": [
            "Cook rice with chicken broth and saffron.",
            "Add crab meat, clams, and mussels to the rice and cook for only 5 minutes (undercooking the shellfish)."
        ]
    }
}
]

caution = [
# Case 1: Allergen Cross-Reactivity
{
    "dish_name": "Avocado Smoothie",
    "restriction": "latex",
    "original_recipe": {
        "ingredients": [
            "1 ripe avocado",
            "1 cup milk",
            "1 tbsp honey"
        ],
        "steps": [
            "Peel and pit the avocado.",
            "Blend the avocado, milk, and honey until smooth.",
            "Serve chilled."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 ripe banana",
            "1 cup milk",
            "1 tbsp honey"
        ],
        "steps": [
            "Peel the banana.",
            "Blend the banana, milk, and honey until smooth.",
            "Serve chilled."
        ]
    }
},

# Case 2: Ambiguous Ingredient Names
{
    "dish_name": "Nut-Free Cookies",
    "restriction": "nuts",
    "original_recipe": {
        "ingredients": [
            "1 cup all-purpose flour",
            "1/2 cup nut-free butter",
            "1/4 cup sugar",
            "1 egg"
        ],
        "steps": [
            "Preheat the oven to 350°F.",
            "Mix all ingredients together to form a dough.",
            "Shape the dough into cookies and bake for 10-12 minutes."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 cup all-purpose flour",
            "1/2 cup butter",
            "1/4 cup sugar",
            "1 egg"
        ],
        "steps": [
            "Preheat the oven to 350°F.",
            "Mix all ingredients together to form a dough.",
            "Shape the dough into cookies and bake for 10-12 minutes."
        ]
    }
},
# Case 3: Excessive Use of Potentially Harmful Ingredients
{
    "dish_name": "Spicy Chili",
    "restriction": "none",
    "original_recipe": {
        "ingredients": [
            "1 lb ground beef",
            "1 can diced tomatoes",
            "1/2 cup kidney beans",
            "1 tsp chili powder",
            "1/2 tsp cayenne pepper"
        ],
        "steps": [
            "Brown the ground beef in a pot.",
            "Add diced tomatoes, kidney beans, chili powder, and cayenne pepper.",
            "Simmer for 20 minutes and serve."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 lb ground beef",
            "1 can diced tomatoes",
            "1/2 cup kidney beans",
            "1 tbsp chili powder",
            "2 tsp cayenne pepper"
        ],
        "steps": [
            "Brown the ground beef in a pot.",
            "Add diced tomatoes, kidney beans, chili powder, and cayenne pepper.",
            "Simmer for 20 minutes and serve."
        ]
    }
}

]