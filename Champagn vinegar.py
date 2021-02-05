#1 cup Champagne Vinegar 
#2 cups Blended Oil
#8 Tablespoons Dijon Mustard
#8 Tablespoons Lemon juice
#8 Tablespoons Honey
#8 dashes of Hot Sauce
#4ea Garlic
#4 teaspoons salt
#4 teaspoons pepper

print("What times batch of Champagne Vinegar would you like to make?: ")

batch = int(input())
champ_yield = 2
champ_amounts = [1, 2, 8, 8, 8, 8, 4, 4, 4]
champ_directions = ["Cup's Champagne Vinegar", "Cup's Blended Oil", "Tablespoons Dijon Mustard",
                    "Tablespoons Lemon Juice", "Tablespoons Honey", "Dashes Hot Sauce", "ea garlic", 
                    "teaspoons salt", "teaspoons pepper"]

champ_conversions = [num * batch for num in champ_amounts ]
for champ_items in zip(champ_conversions, champ_directions):
    print(champ_items)

#directions
print("Yield: " + str(champ_yield * batch) + "quarts")
print("Directions:")
print("-------------------------------------------------------------------")
print("1: Set up Blender or vitamix")
print("2: Add Garlic, Dijon, Hot-Sauce, and Vinegar and blend till smooth")
print("3: Once smooth add salt and pepper, lemon juice and blend")
print("4: While blending slowly add in blended oil until smooth")
print("5: Portion into Quarts, with a Label and Date.")