 # length method(len)
name = "jamshaid"
print(len(name))
 #concept of endswith() method 
print(name.endswith("aid"))  #True   
print(name.endswith("main")) #False
 #concept of startswith() method
print(name.startswith("jam"))  #True
print(name.startswith("moon")) #False
print(name.capitalize()) #capitalize first letter of string
print(name.upper()) #convert string into upper case
print(name.lower()) #convert string into lower case
print(name.title()) #capitalize first letter of each word
print(name.count("a")) #count the number of occurences of a character in string
print(name.find("a")) #find the index of first occurence of a character in string
print(name.replace("j", "J")) #replace a character in string with another character
print(name.replace("j", "J").upper()) #replace a character in string with another character and convert string into upper case
print(name.replace("j", "J").lower()) #replace a character in string with another character and convert string into upper case and then lower case
