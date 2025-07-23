#set = unique values, no indexing

utensil = {"plate","cup","spoon","spoon"}
kitchen_stuff = {"fridge","stove", "plate"}
#print(utensil)

#utensil.add("jug")
#utensil.remove("plate")
#utensil.clear()

#utensil.update(kitchen_stuff)
#total_kitchen = utensil.union(kitchen_stuff)
#print(utensil)
#print(total_kitchen)
print(utensil.difference(kitchen_stuff))
print(utensil.intersection(kitchen_stuff))

#for x in utensil:
#    print(x)