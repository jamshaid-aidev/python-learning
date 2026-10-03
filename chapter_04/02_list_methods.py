friends = ["Apple", "Orange", 5, 34.56, False, "Ali", "Ahmad"]
print(friends)

friends.append("Jamshaid") #append is a function that can add the new value in the end.
print(friends)


 #sort the list in ascending order
numbers = [2, 3 , 1, 5, 4]
numbers.sort()
print(numbers)

# reverse the list in descending order
numbers_2 = [1, 2, 3, 4, 5]
numbers_2.reverse()
print(numbers_2)

# insert a value at a specific index
numbers_3 = [1, 2, 3, 4, 5]
numbers_3.insert(2, 10) #insert the value 10 at index 2
print(numbers_3)  


# pop a value from the list
numbers_4 = [1, 2, 3, 4, 5]
popped_value = numbers_4.pop(2) # remove and return the element at index 2
print(popped_value)
print(numbers_4)


#remove a value from the list
numbers_5 = [1, 2, 3, 4, 5] 
numbers_5.remove(3) # remove the element with value 3
print(numbers_5)