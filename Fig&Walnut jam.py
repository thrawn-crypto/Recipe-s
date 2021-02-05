#Fig & Walnut jam
# 4c chopped figs
# 1c honey
# 1c Walnuts
# 2T lemon juice
# 1T balsamic

print("What times batch of Fig & Walnut Jam would you like to make?: ")

batch = int(input())

fw_amounts = [4, 1, 1, 2, 1]
fw_directions = ["Cup's Quatered Figs", "Cup's Honey", "Cup's Walnuts"
                     "Tablespoon's Lemon Juice", " Tablespoon's Balsamic Vinegar"]

fw_conversions = [num * batch for num in fw_amounts]
for fw_items in zip(fw_conversions, fw_directions):
    print(fw_items)

#directions
print("Directions:")
print("-------------------------------------------------------------------")
