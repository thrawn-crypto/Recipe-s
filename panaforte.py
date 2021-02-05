# panaforte
# 3# dried fruit (mix of seasonal dried Fruit)
# 2.5#'s of nuts (no peanuts)
# 2 cups sugar
# 2 cups honey
# 1.5c A.P. Flour
# 2.66 T cocopowder
# 1.33 T cinnamon
# 2 t coriander
# 1 t nutmeg
# 2 T water
# .5 t salt

print("What times batch of Panaforte would you like to make?: ")

batch = int(input())

pan_amounts = [3, 2.5, 2, 2, 1.5, 2.66, 1.33, 2, 1, 2, .5]
pan_directions = ["#'s of Dried seasonal fruit", "#'s of nuts (no peanuts)", "Cup's of sugar",
                  "Cup's of honey", "Cup's of All Purpose Flour", "Tablespoon's of CoCo Powder"
                  "Tablespoon's Cinnamon", "teaspoon's coriander", "teaspoon's nutmeg"
                  "Tablespoon's Water", "teaspoon's Salt"]

pan_conversions = [num * batch for num in pan_amounts]
for pan_items in zip(pan_conversions, pan_directions):
    print(pan_items)
    
#directions
print("Directions:")
print("-------------------------------------------------------------------")
print("Preheat oven to 325 f")
print("You will need waxpaper 9in × 13in, plastic wrap, and pan spray, plastic gloves")
print("1: In a large bowl mix all ingredents untill incorperated")
print("2: Line a sheet tray with alluminum foil and spray with pan spray")
print("3: Spread mixture on foil, and cover with foil and sheet tray")
print("4: Bake for 10 minutes rotate and bake for another 10 minutes")
print("5: ")