# RedPepper jelly recipy
# 2 1/2cups redpepper(blended)
# 2t red pepper flakes
# 3T apple pectin
# 3 1/4 cups sugar
# 1 cup white wine vinegar
# 1 tablespoon butter
# 3/4 t salt
# seperate pectin and 1/4c sugar in a seperate bowl
# bring everything but pectin to a bowl
# whisk in pectin sugar mix
# 1-1 vin, but

print("How many cups of blended red pepper do you have?: ")

cups = int(input())
rpj_amounts = [1, .8, 1.2, 1.3, .4, .4, .3]
rpj_directions = ["Cup's Red peppers(blended)", "teaspoon's Red Pepper Flakes", "Tablespoon's Apple Pectin",
                  "Cup's Sugar", "Cup's White Wine Vinegar", "Tablespoon's Butter", "teaspoon's Salt"]

rpj_conversions = [num * cups for num in rpj_amounts]

for rpj_items in zip(rpj_conversions, rpj_directions):

    print(rpj_items)
#cooking directions:
    #directions
print("Directions:")
print("-------------------------------------------------------------------")
print("1: Seperate 1/8th the amount of sugar and combine with apple pectin.")
print("2: Add all ingredents but the apple pectin sugar mixture to a heavy bottom pot.")
print("3: bring to a boil.")
print("4: Whisk in pectin sugar mixture and reduce heat to a simmer.")
print("5: ")