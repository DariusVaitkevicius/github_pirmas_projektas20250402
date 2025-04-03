shopping_list = ["pienas", "kiaušiniai", "duona", "sviestas", "tortas"]
print(shopping_list)
print(shopping_list[0])

shopping_list[shopping_list.index("duona")] = "bananas"
print(shopping_list)

shopping_list.insert(0, "obuolys")
print(shopping_list)

shopping_list.extend(["miltai", "cukrus"])
print(shopping_list)

print(shopping_list[2:4])