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
},

#unsafe 1
{
"dish_name": "Seafood Stir-Fry",
"restriction": "Seafood-free",
"original_recipe": {
    "ingredients": [
        "1 pound (450g) shrimp, peeled and deveined",
        "2 tablespoons vegetable oil",
        "1 red bell pepper, sliced",
        "1 yellow bell pepper, sliced",
        "1 cup snap peas",
        "2 cloves garlic, minced",
        "1 tablespoon ginger, minced",
        "2 tablespoons soy sauce",
        "1 tablespoon oyster sauce",
        "1 teaspoon sesame oil",
        "1 teaspoon cornstarch mixed with 2 tablespoons water (optional, for thickening)",
        "Cooked rice for serving"
    ],
    "steps": [
        "Heat 1 tablespoon of vegetable oil in a large skillet or wok over medium-high heat.",
        "Add the shrimp and cook for 2-3 minutes until pink and opaque. Remove and set aside.",
        "Add the remaining tablespoon of oil to the skillet. Stir-fry the bell peppers and snap peas for 3-4 minutes until tender-crisp.",
        "Add the garlic and ginger, cooking for 1 minute until fragrant.",
        "Return the shrimp to the skillet and pour in the soy sauce, oyster sauce, and sesame oil.",
        "Mix well and simmer for 2 minutes. If a thicker sauce is desired, stir in the cornstarch slurry and cook until the sauce thickens.",
        "Serve hot over cooked rice."
    ]
},
"modified_recipe": {
    "ingredients": [
        "1 pound (450g) mollusks (scallops, oysters, clams and mussels)",
        "2 tablespoons vegetable oil",
        "1 red bell pepper, sliced",
        "1 yellow bell pepper, sliced",
        "1 cup snap peas",
        "2 cloves garlic, minced",
        "1 tablespoon ginger, minced",
        "2 tablespoons soy sauce",
        "1 tablespoon hoisin sauce (shellfish-free alternative to oyster sauce)",
        "1 teaspoon sesame oil",
        "1 teaspoon cornstarch mixed with 2 tablespoons water (optional, for thickening)",
        "Cooked rice for serving"
    ],
    "steps": [
        "Heat 1 tablespoon of vegetable oil in a large skillet or wok over medium-high heat.",
        "Add the diced mollusks and cook for 5-6 minutes until fully cooked and lightly browned. Remove and set aside.",
        "Add the remaining tablespoon of oil to the skillet. Stir-fry the bell peppers and snap peas for 3-4 minutes until tender-crisp.",
        "Add the garlic and ginger, cooking for 1 minute until fragrant.",
        "Return the mollusks to the skillet and pour in the soy sauce, hoisin sauce, and sesame oil.",
        "Mix well and simmer for 2 minutes. If a thicker sauce is desired, stir in the cornstarch slurry and cook until the sauce thickens.",
        "Serve hot over cooked rice."
    ]
}    
},

#unsafe 2
{
"dish_name": "Classic Sugar Cookies",
"restriction": "Sugar-free",
"original_recipe": {
    "ingredients": [
        "2 1/4 cups all-purpose flour",
        "1/2 tsp baking powder",
        "1/4 tsp salt",
        "3/4 cup unsalted butter, softened",
        "1 cup granulated sugar",
        "1 large egg",
        "1 tsp vanilla extract"
    ],
    "steps": [
        "Preheat the oven to 350°F (175°C). Line a baking sheet with parchment paper.",
        "In a medium bowl, whisk together the flour, baking powder, and salt.",
        "In a large bowl, beat the butter and sugar until light and fluffy.",
        "Add the egg and vanilla extract to the butter mixture, and beat until combined.",
        "Gradually mix in the dry ingredients until a dough forms.",
        "Roll the dough into 1-inch balls and place them on the prepared baking sheet.",
        "Flatten each ball slightly with the back of a spoon.",
        "Bake for 10–12 minutes or until the edges are golden.",
        "Let the cookies cool on the baking sheet for 5 minutes before transferring them to a wire rack."
    ]
},
"modified_recipe": {
    "ingredients": [
        "2 1/4 cups all-purpose flour",
        "1/2 tsp baking powder",
        "1/4 tsp salt",
        "3/4 cup unsalted butter, softened",
        "1 cup sugar substitute (like erythritol or stevia blend)",
        "1/4 cup unsweetened applesauce (as an egg replacement)",
        "1 tsp vanilla extract"
    ],
    "steps": [
        "Preheat the oven to 350°F (175°C). Line a baking sheet with parchment paper.",
        "In a medium bowl, whisk together the flour, baking powder, and salt.",
        "In a large bowl, beat the butter and sugar substitute until light and fluffy.",
        "Add the applesauce and vanilla extract to the butter mixture, and beat until combined.",
        "Gradually mix in the dry ingredients until a dough forms.",
        "Roll the dough into 1-inch balls and place them on the prepared baking sheet.",
        "Flatten each ball slightly with the back of a spoon.",
        "Bake for 10–12 minutes or until the edges are golden.",
        "Let the cookies cool on the baking sheet for 5 minutes before transferring them to a wire rack."
    ]
},
"Explanation": "Sugar substitute may not chemically stable at high temperature, unpleasent compound could be produce in baking process"
},

#unsafe 3
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
},

#caution 1
{
"dish_name": "Vanilla Pudding",
"restriction": "Fish-free",
"original_recipe": {
    "ingredients": [
        "2 cups whole milk",
        "1/2 cup sugar",
        "1 tsp vanilla extract",
        "2 tbsp gelatin (derived from fish)",
        "1/4 cup cold water"
    ],
    "steps": [
        "In a small bowl, sprinkle the gelatin over cold water and let it bloom for 5 minutes.",
        "In a saucepan, heat the milk and sugar over medium heat until the sugar dissolves, but do not let it boil.",
        "Stir the bloomed gelatin into the warm milk mixture until completely dissolved.",
        "Remove the saucepan from heat and stir in the vanilla extract.",
        "Pour the mixture into individual serving dishes and refrigerate for at least 4 hours or until set."
    ]
},
"modified_recipe": {
    "ingredients": [
        "2 cups whole milk",
        "1/2 cup sugar",
        "1 tsp vanilla extract",
        "2 tbsp gelatin (derived from fish)",
        "1/4 cup cold water"
    ],
    "steps": [
        "In a small bowl, sprinkle the gelatin over cold water and let it bloom for 5 minutes.",
        "In a saucepan, heat the milk and sugar over medium heat until the sugar dissolves, but do not let it boil.",
        "Stir the bloomed gelatin into the warm milk mixture until completely dissolved.",
        "Remove the saucepan from heat and stir in the vanilla extract.",
        "Pour the mixture into individual serving dishes and refrigerate for at least 4 hours or until set."
    ]
},
"Explanation": "Gelatin: Gelatin is often made from fish skin and bones"
},

#caution 2
{
"dish_name": "Pancakes",
"restriction": "Lactose-free",
"original_recipe": {
    "ingredients": [
        "1 cup (125g) all-purpose flour",
        "2 tablespoons sugar",
        "1 teaspoon baking powder",
        "1/2 teaspoon baking soda",
        "1/4 teaspoon salt",
        "1 large egg",
        "1 cup (240ml) milk",
        "2 tablespoons unsalted butter, melted",
        "1 teaspoon vanilla extract",
        "Optional: butter and syrup for serving"
    ],
    "steps": [
        "In a mixing bowl, whisk together the flour, sugar, baking powder, baking soda, and salt.",
        "In a separate bowl, whisk the egg, milk, melted butter, and vanilla extract until combined.",
        "Pour the wet ingredients into the dry ingredients and mix until just combined. Do not overmix.",
        "Heat a non-stick skillet over medium heat and grease lightly with butter or oil.",
        "Pour 1/4 cup of batter onto the skillet for each pancake.",
        "Cook until bubbles form on the surface, then flip and cook the other side until golden brown.",
        "Serve warm with butter and syrup if desired."
    ]
},
"modified_recipe": {
    "ingredients": [
        "1 cup (125g) all-purpose flour",
        "2 tablespoons sugar",
        "1 teaspoon baking powder",
        "1/2 teaspoon baking soda",
        "1/4 teaspoon salt",
        "1 large egg",
        "1 cup (240ml) milk",
        "2 tablespoons unsalted butter, melted",
        "1 teaspoon vanilla extract",
        "Optional: butter (lactose-free) and syrup for serving"
    ],
    "steps": [
        "In a mixing bowl, whisk together the flour, sugar, baking powder, baking soda, and salt.",
        "In a separate bowl, whisk the egg, milk, melted butter, and vanilla extract until combined.",
        "Pour the wet ingredients into the dry ingredients and mix until just combined. Do not overmix.",
        "Heat a non-stick skillet over medium heat and grease lightly with butter or oil.",
        "Pour 1/4 cup of batter onto the skillet for each pancake.",
        "Cook until bubbles form on the surface, then flip and cook the other side until golden brown.",
        "Serve warm with butter and syrup if desired."
    ]
}
},

#caution 3
{
"dish_name": "Classic Sugar Cookies",
"restriction": "Sugar-free",
"original_recipe": {
    "ingredients": [
        "2 1/4 cups all-purpose flour",
        "1/2 tsp baking powder",
        "1/4 tsp salt",
        "3/4 cup unsalted butter, softened",
        "1 cup granulated sugar",
        "1 large egg",
        "1 tsp vanilla extract"
    ],
    "steps": [
        "Preheat the oven to 350°F (175°C). Line a baking sheet with parchment paper.",
        "In a medium bowl, whisk together the flour, baking powder, and salt.",
        "In a large bowl, beat the butter and sugar until light and fluffy.",
        "Add the egg and vanilla extract to the butter mixture, and beat until combined.",
        "Gradually mix in the dry ingredients until a dough forms.",
        "Roll the dough into 1-inch balls and place them on the prepared baking sheet.",
        "Flatten each ball slightly with the back of a spoon.",
        "Bake for 10–12 minutes or until the edges are golden.",
        "Let the cookies cool on the baking sheet for 5 minutes before transferring them to a wire rack."
    ]
},
"modified_recipe": {
    "ingredients": [
        "2 1/4 cups all-purpose flour",
        "1/2 tsp baking powder",
        "1/4 tsp salt",
        "3/4 cup unsalted butter, softened",
        "1 cup sugar substitute (like erythritol or stevia blend)",
        "1/4 cup unsweetened applesauce (as an egg replacement)",
        "1 tsp vanilla extract"
    ],
    "steps": [
        "Preheat the oven to 350°F (175°C). Line a baking sheet with parchment paper.",
        "In a medium bowl, whisk together the flour, baking powder, and salt.",
        "In a large bowl, beat the butter and sugar substitute until light and fluffy.",
        "Add the applesauce and vanilla extract to the butter mixture, and beat until combined.",
        "Gradually mix in the dry ingredients until a dough forms.",
        "Roll the dough into 1-inch balls and place them on the prepared baking sheet.",
        "Flatten each ball slightly with the back of a spoon.",
        "Bake for 10–12 minutes or until the edges are golden.",
        "Let the cookies cool on the baking sheet for 5 minutes before transferring them to a wire rack."
    ]
},
"Explanation": "Sugar substitute usually much sweeter than table sugar, so use same amount could be unsafe if use in large dose. "
}
]