list_fruit = ["Apple", "Banana", "Melon", "Kiwi", "Mango"]

print(list_fruit)

#Task 7(2nd Fruit)
print("Second Fruit of the Fruits list:", list_fruit[1])

#Task 8(type of variable)
print("List Type..: ",type(list_fruit))

#Task 10(5th fruit)
print("Last Fruit of the Fruits list:", list_fruit[4])

#Task 11(total size of the fruits)
print("Size of the fruit list:", len(list_fruit))

#Task 12(combining more then two lists)
list_fruit_second = ["Pineapple", "Rasberry", "Orange"]
all_fruits = list_fruit + list_fruit_second
print("Combined list of fruits:", all_fruits)

#Task 13 (loop)
for fruit in all_fruits:
    print(fruit)
