unsafe = [
# Case 1: New recipe does not satisfy the ingredient requirements
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
### 1. new recipe does not satisfy the ingredient requirements 
{
    "dish_name": "Chocolate Cake",
    "restriction": "Gluten-Free, Vegan",
    "original_recipe": {
        "ingredients": [
            "2 cups almond flour",
            "1½ cups coconut sugar",
            "¾ cup cocoa powder",
            "2 teaspoons baking powder",
            "1 teaspoon salt",
            "1 cup milk",
            "½ cup oil",
            "2 tablespoons lemon juice",
            "2 teaspoons almond extract",
            "1 cup cold water"
        ],
        "steps": [
            "Preheat Oven: Preheat the oven to 350°F (175°C). Grease and line two 9-inch round baking pans with parchment paper.",
            "Mix Dry Ingredients: In a large bowl, combine almond flour, coconut sugar, cocoa powder, baking powder, and salt. Whisk to ensure there are no lumps.",
            "Add Wet Ingredients: Pour in the milk, melted coconut oil, lemon juice, and almond extract. Stir until the mixture is smooth and well combined.",
            "Add Cold Water: Gradually add the cold water, mixing continuously until the batter reaches a smooth consistency.",
            "Bake: Divide the batter evenly between the prepared baking pans. Bake for 25-30 minutes or until a skewer inserted into the center comes out clean.",
            "Cool: Let the cakes cool in the pans for 15 minutes before transferring them to a wire rack to cool completely."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 cups all-purpose flour",
            "1½ cups granulated sugar",
            "¾ cup cocoa powder",
            "2 teaspoons baking soda",
            "1 teaspoon salt",
            "1 cup whole milk",
            "½ cup butter",
            "2 tablespoons apple cider vinegar",
            "2 teaspoons vanilla extract",
            "1 cup boiling water"
        ],
        "steps": [
            "Preheat Oven: Preheat the oven to 350°F (175°C). Grease and flour two 9-inch round baking pans.",
            "Mix Dry Ingredients: In a large mixing bowl, whisk together all-purpose flour, granulated sugar, cocoa powder, baking soda, and salt.",
            "Add Wet Ingredients: Add the whole milk, melted butter, apple cider vinegar, and vanilla extract to the dry ingredients. Mix until well combined.",
            "Incorporate Boiling Water: Carefully stir in the boiling water until the batter is smooth. The batter will be thin.",
            "Bake: Pour the batter evenly into the prepared baking pans. Bake for 30-35 minutes or until a toothpick inserted into the center comes out clean.",
            "Cool: Allow the cakes to cool in the pans for 10 minutes, then transfer them to a wire rack to cool completely before frosting."
        ]
    },
    "Explanation": "The modified recipe is not safe for individuals following a gluten-free and vegan diet because it reintroduces gluten-containing all-purpose flour and animal-derived ingredients like whole milk and butter, violating the specified dietary restrictions."
},

### 2. new recipe satisfy the requirement, but the cooking step can introduce food poisoning 
{
    "dish_name": "Low-Sodium Teriyaki Chicken Bowl",
    "restriction": "Low Sodium, No Gluten",
    "original_recipe": {
        "ingredients": [
            "2 boneless, skinless chicken thighs",
            "3 cups cooked brown rice",
            "1 cup broccoli florets",
            "1 cup sliced carrots",
            "½ cup low-sodium teriyaki sauce",
            "2 tablespoons sesame oil",
            "1 tablespoon minced garlic",
            "1 tablespoon minced ginger",
            "Salt and pepper to taste"
        ],
        "steps": [
            "Prepare Rice: Cook brown rice according to package instructions.",
            "Marinate Chicken: In a bowl, combine low-sodium teriyaki sauce, minced garlic, and minced ginger. Add chicken thighs and marinate for at least 30 minutes.",
            "Cook Vegetables: In a large skillet, heat sesame oil over medium heat. Add broccoli and carrots, sautéing until tender-crisp, about 5-7 minutes.",
            "Cook Chicken: Remove chicken from marinade and cook in the same skillet over medium heat for 6-7 minutes per side, or until the internal temperature reaches 165°F (74°C).",
            "Assemble Bowl: Divide cooked brown rice into bowls. Top with sautéed vegetables and sliced teriyaki chicken.",
            "Serve: Drizzle any remaining teriyaki sauce over the bowls and serve hot."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 boneless, skinless chicken thighs",
            "3 cups cooked brown rice",
            "1 cup broccoli florets",
            "1 cup sliced carrots",
            "½ cup low-sodium teriyaki sauce",
            "2 tablespoons sesame oil",
            "1 tablespoon minced garlic",
            "1 tablespoon minced ginger",
            "Salt and pepper to taste"
        ],
        "steps": [
            "Prepare Rice: Cook brown rice according to package instructions.",
            "Marinate Chicken: In a bowl, combine low-sodium teriyaki sauce, minced garlic, and minced ginger. Add chicken thighs and marinate for 15 minutes.",
            "Cook Vegetables: In a large skillet, heat sesame oil over medium heat. Add broccoli and carrots, sautéing until tender-crisp, about 4-5 minutes.",
            "Cook Chicken: Remove chicken from marinade and cook in the same skillet over medium heat for 4-5 minutes per side, without checking the internal temperature.",
            "Assemble Bowl: Divide cooked brown rice into bowls. Top with sautéed vegetables and sliced teriyaki chicken.",
            "Serve: Drizzle any remaining teriyaki sauce over the bowls and serve immediately while the chicken is still slightly pink."
        ]
    },
    "Explanation": "The modified recipe adheres to the low sodium and gluten-free restrictions but introduces a food safety risk by reducing marinating and cooking times. Undercooked chicken and insufficient marinating can lead to food poisoning due to bacteria like Salmonella. Not checking the internal temperature and serving chicken that's still pink increases this risk."
},
## Reduced Marinating Time/Reduced Cooking Time

## Introduce new form of ingredient that is not allowed
{
    "dish_name": "Pecan Pie",
    "restriction": "Nut Free",
    "original_recipe": {
        "ingredients": [
            "1 cup pecans",
            "1 cup corn syrup",
            "1 cup sugar",
            "3 large eggs",
            "1/4 cup unsalted butter, melted",
            "1 teaspoon vanilla extract",
            "1 unbaked pie crust"
        ],
        "steps": [
            "Preheat the oven to 350°F (175°C).",
            "Spread the pecans evenly in the bottom of the unbaked pie crust.",
            "In a mixing bowl, whisk together the corn syrup, sugar, eggs, melted butter, and vanilla extract.",
            "Pour the mixture over the pecans in the pie crust.",
            "Bake the pie in the preheated oven for 50 to 60 minutes, or until the filling is set.",
            "Allow the pie to cool completely before serving."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 cup almonds",
            "1 cup corn syrup",
            "1 cup sugar",
            "3 large eggs",
            "1/4 cup unsalted butter, melted",
            "1 teaspoon vanilla extract",
            "1 unbaked pie crust"
        ],
        "steps": [
            "Preheat the oven to 350°F (175°C).",
            "Spread the almonds evenly in the bottom of the unbaked pie crust.",
            "In a mixing bowl, whisk together the corn syrup, sugar, eggs, melted butter, and vanilla extract.",
            "Pour the mixture over the almonds in the pie crust.",
            "Bake the pie in the preheated oven for 50 to 60 minutes, or until the filling is set.",
            "Allow the pie to cool completely before serving."
        ]
    }
},

## contain the restricted ingredient
{
    "dish_name": "Spaghetti Carbonara",
    "restriction": "Gluten Free",
    "original_recipe": {
        "ingredients": [
            "12 ounces spaghetti",
            "4 ounces pancetta, diced",
            "2 large eggs",
            "1/2 cup grated Parmesan cheese",
            "1/4 cup heavy cream",
            "2 tablespoons unsalted butter",
            "1 teaspoon black pepper",
            "1/2 teaspoon salt",
            "2 tablespoons chopped parsley (for garnish)"
        ],
        "steps": [
            "Cook the spaghetti in a large pot of salted boiling water until al dente. Reserve 1 cup of pasta water, then drain the pasta and set aside.",
            "In a large skillet over medium heat, cook the pancetta until crispy, about 5 minutes.",
            "In a bowl, whisk together the eggs, Parmesan cheese, heavy cream, black pepper, and salt.",
            "Add the butter to the skillet with the pancetta, stirring until melted.",
            "Add the cooked spaghetti to the skillet, tossing to coat in the pancetta and butter.",
            "Remove the skillet from heat and quickly stir in the egg mixture, adding reserved pasta water as needed to create a creamy sauce.",
            "Serve immediately, garnished with parsley."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "12 ounces spaghetti",
            "4 ounces pancetta, diced",
            "2 large eggs",
            "1/2 cup grated Parmesan cheese",
            "1/4 cup heavy cream",
            "2 tablespoons gluten-free unsalted butter",
            "1 teaspoon black pepper",
            "1/2 teaspoon salt",
            "2 tablespoons chopped parsley (for garnish)"
        ],
        "steps": [
            "Cook the spaghetti in a large pot of salted boiling water until al dente. Reserve 1 cup of pasta water, then drain the pasta and set aside.",
            "In a large skillet over medium heat, cook the pancetta until crispy, about 5 minutes.",
            "In a bowl, whisk together the eggs, Parmesan cheese, heavy cream, black pepper, and salt.",
            "Add the butter to the skillet with the pancetta, stirring until melted.",
            "Add the cooked gluten-free spaghetti to the skillet, tossing to coat in the pancetta and butter.",
            "Remove the skillet from heat and quickly stir in the egg mixture, adding reserved pasta water as needed to create a creamy sauce.",
            "Serve immediately, garnished with parsley."
        ]
    }
},


## wrong cooking step
{
    "dish_name": "Long Bean, Potato, Pork, and Bean Stew",
    "restriction": "Nut Free",
    "original_recipe": {
        "ingredients": [
            "1 pound pork shoulder, cut into cubes",
            "1/2 pound long beans, trimmed and cut into 2-inch pieces",
            "2 medium potatoes, peeled and diced",
            "1 cup kidney beans, soaked overnight",
            "6 cups chicken stock",
            "1 large onion, chopped",
            "3 cloves garlic, minced",
            "2 tablespoons vegetable oil",
            "1 teaspoon smoked paprika",
            "1/2 teaspoon black pepper",
            "Salt to taste",
            "1/4 cup roasted peanuts (for garnish)"
        ],
        "steps": [
            "Heat the vegetable oil in a large pot over medium heat.",
            "Add the chopped onion and garlic, and sauté until fragrant and golden brown, about 5 minutes.",
            "Add the pork cubes and brown them on all sides, about 10 minutes.",
            "Stir in the smoked paprika, black pepper, and a pinch of salt.",
            "Add the soaked kidney beans and chicken stock to the pot, bring to a boil, then reduce the heat to low.",
            "Cover and simmer the stew for 1 hour.",
            "Add the diced potatoes and long beans, then cover and simmer for an additional hour until all ingredients are tender and flavors are well combined.",
            "Adjust seasoning with salt as needed.",
            "Serve hot, garnished with roasted peanuts."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 pound pork shoulder, cut into cubes",
            "1/2 pound long beans, trimmed and cut into 2-inch pieces",
            "2 medium potatoes, peeled and diced",
            "1 cup kidney beans, soaked overnight",
            "6 cups chicken stock",
            "1 large onion, chopped",
            "3 cloves garlic, minced",
            "2 tablespoons vegetable oil",
            "1 teaspoon smoked paprika",
            "1/2 teaspoon black pepper",
            "Salt to taste"
        ],
        "steps": [
            "Heat the vegetable oil in a large pot over medium heat.",
            "Add the chopped onion and garlic, and sauté until fragrant and golden brown, about 5 minutes.",
            "Add the pork cubes and brown them on all sides, about 10 minutes.",
            "Stir in the smoked paprika, black pepper, and a pinch of salt.",
            "Add the soaked kidney beans and chicken stock to the pot, bring to a boil, then reduce the heat to low.",
            "Cover and simmer the stew for 20 minutes.",
            "Add the diced potatoes and long beans, then cover and simmer for an additional 10 minutes",
            "Adjust seasoning with salt as needed.",
            "Serve hot."
        ]
    }
},

## not a dish
{
    "dish_name": "Traditional Wheat Roti",
    "restriction": "Gluten Free",
    "original_recipe": {
        "ingredients": [
            "2 cups whole wheat flour",
            "3/4 cup water",
            "1/4 teaspoon salt",
            "1 tablespoon vegetable oil"
        ],
        "steps": [
            "In a large bowl, mix together the whole wheat flour and salt.",
            "Gradually add water and knead the mixture into a soft dough. Cover and let it rest for 20 minutes.",
            "Divide the dough into small balls and roll each ball into a thin round using a rolling pin.",
            "Heat a skillet over medium-high heat and cook each roti for about 1-2 minutes on each side, until puffed and slightly golden.",
            "Serve hot with your choice of curry or dip."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 cups ghee",
            "3/4 cup water",
            "1/4 teaspoon salt"
        ],
        "steps": [
            "In a large bowl, mix together the ghee and salt.",
            "Gradually add water and stir to combine into a semi-cohesive mixture.",
            "Attempt to form small balls, though the lack of flour results in a sticky, oily texture.",
            "Heat a skillet over medium-high heat and attempt to cook the ghee-based mixture. However, it lacks structure and cannot be shaped into rotis.",
            "Serve the buttery mixture as a topping or side, as it cannot be used as a gluten-free replacement for the original dish."
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
},

### 3. new recipe introduce new form of dangerous ingredient different from the requirement but still would cause food poisoning
{
    "dish_name": "Banana Smoothie",
    "restriction": "lactose-free",
    "original_recipe": {
        "ingredients": [
            "2 ripe bananas",
            "1 cup cow's milk",
            "1 tablespoon chia seeds",
            "1 tablespoon honey",
            "½ teaspoon cinnamon",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Peel the bananas and gather all other ingredients.",
            "Blend: In a blender, combine the bananas, cow's milk, chia seeds, honey, and cinnamon.",
            "Add Ice: Add a handful of ice cubes to the blender for a chilled smoothie.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 ripe bananas",
            "1 cup goat milk",
            "1 tablespoon chia seeds",
            "1 tablespoon maple syrup",
            "½ teaspoon cinnamon",
            "1 raw egg",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Peel the bananas and gather all other ingredients.",
            "Blend: In a blender, combine the bananas, almond milk, chia seeds, maple syrup, cinnamon, and raw egg.",
            "Add Ice: Add a handful of ice cubes to the blender for a chilled smoothie.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately while the egg is still raw."
        ]
    },
    "Explanation": "replace the milk with goat milk."
},
##replace the milk with goat milk.

### 4. Allergen Cross-Reactivity: The recipe includes ingredients that can cause cross-reactivity in individuals with certain allergies. For instance, someone allergic to latex might also react to foods like bananas or avocados.
{
    "dish_name": "Strawberry Smoothie",
    "restriction": "Latex Allergy, no berry",
    "original_recipe": {
        "ingredients": [
            "2 ripe Strawberry",
            "1 cup almond milk",
            "1 tablespoon chia seeds",
            "1 tablespoon honey",
            "½ teaspoon cinnamon",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Peel the Strawberry and gather all other ingredients.",
            "Blend: In a blender, combine the Strawberry, almond milk, chia seeds, honey, and cinnamon.",
            "Add Ice: Add a handful of ice cubes to the blender for a chilled smoothie.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 ripe avocados",
            "1 cup coconut milk",
            "1 tablespoon flaxseeds",
            "1 tablespoon maple syrup",
            "½ teaspoon turmeric",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Scoop the avocados and gather all other ingredients.",
            "Blend: In a blender, combine the avocados, coconut milk, flaxseeds, maple syrup, turmeric, and ice cubes.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately."
        ]
    },
    "Explanation": " The modified recipe substitutes bananas with avocados, but avocados are  known to trigger latex cross-reactivity. Therefore, the modified recipe still poses a risk to individuals with latex allergies."
},
## Substitutes bananas with avocados, which are also cross-reactive for individuals with latex allergies. This substitution does not solve the issue and still poses a risk.


### 5.Ambiguous Ingredient Names: The recipe uses ingredient names that could potentially violate the requirements. For example, for nut-free case instead of mention using nut-free butter but just butter.
{
    "dish_name": "Peanut Butter Banana Smoothie",
    "restriction": "Nut-Free",
    "original_recipe": {
        "ingredients": [
            "2 ripe bananas",
            "1 cup almond milk",
            "2 tablespoons peanut butter",
            "1 tablespoon honey",
            "½ teaspoon cinnamon",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Peel the bananas and gather all other ingredients.",
            "Blend: In a blender, combine the bananas, almond milk, peanut butter, honey, and cinnamon.",
            "Add Ice: Add a handful of ice cubes to the blender for a chilled smoothie.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 ripe bananas",
            "1 cup almond milk",
            "2 tablespoons butter",
            "1 tablespoon maple syrup",
            "½ teaspoon cinnamon",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Peel the bananas and gather all other ingredients.",
            "Blend: In a blender, combine the bananas, almond milk, butter, maple syrup, and cinnamon.",
            "Add Ice: Add a handful of ice cubes to the blender for a chilled smoothie.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately."
        ]
    },
    "Explanation": "The original recipe is not safe for a nut-free diet as it includes peanut butter and almond milk, both of which are nut products. The modified recipe replaces peanut butter with 'butter,' which is ambiguous and could cause confusion. It also retains almond milk, which is derived from nuts. The ambiguity of 'butter' and the inclusion of almond milk require caution, as they may not be safe for individuals with nut allergies."
},


### 6. Excessive Use of Potentially Harmful Ingredients: The recipe uses ingredients that is safe in small dose but unsafe if use in large dose.
{
    "dish_name": "Ginger Turmeric Smoothie",
    "restriction": "I like stronger flavour",
    "original_recipe": {
        "ingredients": [
            "2 ripe bananas",
            "1 cup coconut milk",
            "1 teaspoon grated fresh ginger",
            "½ teaspoon ground turmeric",
            "1 tablespoon honey",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Peel the bananas and gather all other ingredients.",
            "Blend: In a blender, combine the bananas, coconut milk, ginger, turmeric, honey, and ice cubes.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "2 ripe bananas",
            "1 cup coconut milk",
            "2 tablespoons grated fresh ginger",
            "1 tablespoon ground turmeric",
            "1 tablespoon maple syrup",
            "Ice cubes as needed"
        ],
        "steps": [
            "Prepare Ingredients: Peel the bananas and gather all other ingredients.",
            "Blend: In a blender, combine the bananas, coconut milk, ginger, turmeric, maple syrup, and ice cubes.",
            "Blend Until Smooth: Blend all ingredients on high speed until the mixture is smooth and creamy.",
            "Serve: Pour the smoothie into glasses and serve immediately."
        ]
    },
    "Explanation": "The original recipe uses small amounts of ginger and turmeric, which are generally safe and offer health benefits. The modified recipe significantly increases the quantities to 2 tablespoons of ginger and 1 tablespoon of turmeric. Excessive consumption of these spices can lead to gastrointestinal discomfort, acid reflux, and potential interactions with medications. Therefore, the modified recipe requires caution."
},

## cross reactivity
{
    "dish_name": "Shrimp Alfredo Pasta",
    "restriction": "No Shellfish",
    "original_recipe": {
        "ingredients": [
            "1 pound fettuccine pasta",
            "1/2 pound shrimp, peeled and deveined",
            "2 tablespoons olive oil",
            "3 cloves garlic, minced",
            "2 cups heavy cream",
            "1 cup grated Parmesan cheese",
            "1/4 teaspoon black pepper",
            "1/4 teaspoon salt",
            "2 tablespoons chopped parsley (for garnish)"
        ],
        "steps": [
            "Cook the fettuccine pasta in a large pot of boiling salted water until al dente. Drain and set aside.",
            "In a large skillet, heat the olive oil over medium heat.",
            "Add the shrimp to the skillet and sauté for 3-4 minutes, or until they turn pink and opaque. Remove and set aside.",
            "In the same skillet, add the minced garlic and sauté for 1 minute until fragrant.",
            "Pour in the heavy cream, and simmer for 2-3 minutes, stirring frequently.",
            "Stir in the Parmesan cheese, black pepper, and salt until the sauce is smooth and creamy.",
            "Add the cooked shrimp back to the skillet, stirring to coat them in the sauce.",
            "Toss the cooked fettuccine pasta in the skillet with the sauce.",
            "Garnish with chopped parsley and serve hot."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 pound fettuccine pasta",
            "1/2 pound mussels, cleaned and debearded",
            "2 tablespoons olive oil",
            "3 cloves garlic, minced",
            "2 cups heavy cream",
            "1 cup grated Parmesan cheese",
            "1/4 teaspoon black pepper",
            "1/4 teaspoon salt",
            "2 tablespoons chopped parsley (for garnish)"
        ],
        "steps": [
            "Cook the fettuccine pasta in a large pot of boiling salted water until al dente. Drain and set aside.",
            "In a large skillet, heat the olive oil over medium heat.",
            "Add the mussels to the skillet, cover, and steam for 3-5 minutes until the shells open. Discard any mussels that do not open. Remove the mussels from the skillet and set aside.",
            "In the same skillet, add the minced garlic and sauté for 1 minute until fragrant.",
            "Pour in the heavy cream, and simmer for 2-3 minutes, stirring frequently.",
            "Stir in the Parmesan cheese, black pepper, and salt until the sauce is smooth and creamy.",
            "Add the cooked mussels back to the skillet, stirring to coat them in the sauce.",
            "Toss the cooked fettuccine pasta in the skillet with the sauce.",
            "Garnish with chopped parsley and serve hot."
        ]
    }
},

## unclear ingredient names
{
    "dish_name": "Peanut Butter Cookies",
    "restriction": "Nut Free",
    "original_recipe": {
        "ingredients": [
            "1/2 cup unsalted butter",
            "1/2 cup peanut butter",
            "1/2 cup granulated sugar",
            "1/2 cup brown sugar, packed",
            "1 large egg",
            "1 teaspoon vanilla extract",
            "1 1/4 cups all-purpose flour",
            "1/2 teaspoon baking soda",
            "1/4 teaspoon salt"
        ],
        "steps": [
            "Preheat the oven to 350°F (175°C) and line a baking sheet with parchment paper.",
            "In a large bowl, cream together the butter, peanut butter, granulated sugar, and brown sugar until light and fluffy.",
            "Beat in the egg and vanilla extract until combined.",
            "In a separate bowl, whisk together the flour, baking soda, and salt.",
            "Gradually add the dry ingredients to the wet ingredients and mix until a dough forms.",
            "Roll the dough into small balls and place them on the prepared baking sheet, flattening each slightly with a fork to create a crisscross pattern.",
            "Bake for 10-12 minutes or until the edges are lightly golden.",
            "Allow the cookies to cool on the baking sheet for 5 minutes before transferring them to a wire rack to cool completely."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1/2 cup butter",
            "1/2 cup granulated sugar",
            "1/2 cup brown sugar, packed",
            "1 large egg",
            "1 teaspoon vanilla extract",
            "1 1/4 cups all-purpose flour",
            "1/2 teaspoon baking soda",
            "1/4 teaspoon salt"
        ],
        "steps": [
            "Preheat the oven to 350°F (175°C) and line a baking sheet with parchment paper.",
            "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
            "Beat in the egg and vanilla extract until combined.",
            "In a separate bowl, whisk together the flour, baking soda, and salt.",
            "Gradually add the dry ingredients to the wet ingredients and mix until a dough forms.",
            "Roll the dough into small balls and place them on the prepared baking sheet, flattening each slightly with a fork to create a crisscross pattern.",
            "Bake for 10-12 minutes or until the edges are lightly golden.",
            "Allow the cookies to cool on the baking sheet for 5 minutes before transferring them to a wire rack to cool completely."
        ]
    }
},

## dose matters
{
    "dish_name": "Butter Roasted Vegetables",
    "restriction": "Gluten Free",
    "original_recipe": {
        "ingredients": [
            "1 pound baby carrots",
            "1 pound Brussels sprouts, halved",
            "2 tablespoons unsalted butter",
            "1 teaspoon garlic powder",
            "1/2 teaspoon black pepper",
            "1/2 teaspoon salt",
            "1 tablespoon fresh parsley, chopped (for garnish)"
        ],
        "steps": [
            "Preheat the oven to 400°F (200°C).",
            "Place the baby carrots and halved Brussels sprouts on a baking sheet.",
            "Melt the butter and drizzle it over the vegetables.",
            "Sprinkle the garlic powder, black pepper, and salt evenly over the vegetables.",
            "Toss the vegetables to coat them evenly in the butter and seasonings.",
            "Roast in the preheated oven for 25-30 minutes, stirring halfway through, until the vegetables are tender and slightly caramelized.",
            "Garnish with chopped parsley before serving."
        ]
    },
    "modified_recipe": {
        "ingredients": [
            "1 pound baby carrots",
            "1 pound Brussels sprouts, halved",
            "2 tablespoons ghee",
            "1 teaspoon garlic powder",
            "1/2 teaspoon black pepper",
            "1/2 teaspoon salt",
            "1 tablespoon fresh parsley, chopped (for garnish)"
        ],
        "steps": [
            "Preheat the oven to 400°F (200°C).",
            "Place the baby carrots and halved Brussels sprouts on a baking sheet.",
            "Melt the ghee and drizzle it over the vegetables.",
            "Sprinkle the garlic powder, black pepper, and salt evenly over the vegetables.",
            "Toss the vegetables to coat them evenly in the ghee and seasonings.",
            "Roast in the preheated oven for 25-30 minutes, stirring halfway through, until the vegetables are tender and slightly caramelized.",
            "Garnish with chopped parsley before serving."
        ]
    }
}
]