#list
fruits = ["apple", "banana","apple","cherry" ,"kiwi" ,"cherry"]

print("-----------list-----------------")
print(fruits)
print(fruits.pop(4))
print(fruits.index("cherry"))
print(fruits.count("apple"))
print(fruits.copy())
fruits.remove("apple")
print(fruits)



#dictionary
car = {
  "brand": "Tesla",
  "model": "3",
  "owner": "elon musk"
}

print("\n ----------dictionary-------------")
print(car)
print(car.values())
print(car.keys())
print(car.copy())
print(car.items())
print(car.popitem())


#set
shapes = {"circle" , "square" , "triangle"}
shapes2 = {"circle" ,"rectangle" ,"cone"}
print("\n---------------set---------------")
print(shapes)
shapes.add("cylindrical")
print(shapes.copy())
shapes.remove("square")
print(shapes)
shapes.add(4)
print(shapes)
shapes2.clear()
print(shapes2)


#tuple
foods = ("pizza" , "burger" , "pasta","pizza")

print("\n---------------tuple------------")
print(foods)
print(foods.count("pizza"))
print(foods.index("burger"))



#string
stringvar = "this is a random string text"
print("\n--------------string-------------")
print(stringvar.capitalize())
print(stringvar.count("is"))
print(stringvar.encode())
print(stringvar.find("random"))
print(stringvar.isupper())
