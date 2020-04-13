# Comprehensions
# A short-hand version of taking a collection (lists, dictionaries, sets), doing something to it and creating a new collection
# Format: new_collection = [expression_evaluated_for_each_item for taco in current_collection if conditional]
# OR *result*  = [*transform* for *item* in *iteration* if *filter*]
# The conditional is optional

# Here's a list. Let's capitalize every word in it and put those capitalized words in a new list.
stuff = ["name", "age", "address", "phone"]

# These three examples do the same thing: loop through the stuff list and make a new list that contains the capitalized words.

#1 Good old for loop:
# cap_stuff = []
# for foo in stuff:
#   cap_stuff.append(foo.capitalize())
# print(cap_stuff)

#2 Map using a lambda function:
# cap_stuff = list(map(lambda foo: foo.capitalize(), stuff))
# print(cap_stuff)

# def cap_string(foo):
#     return foo.capitalize()
  
# cap_stuff = list(map(cap_string, stuff))
# print(cap_stuff)

#3 Comprehension
# cap_stuff = [foo.capitalize() for foo in stuff]
# print(cap_stuff)

# Nested Comprehensions
# cap_stuff = [[item.capitalize() for item in foo] for foo in stuff]
# print(cap_stuff)

cap_stuff = []
# for foo in stuff:
#     inner_list = []
#     for item in foo:
#         inner_list.append(item.capitalize())
#     cap_stuff.append(inner_list)
# print(cap_stuff)

# Here's a dictionary example:
# profile = {
#   "name": "Fred",
#   "age": 34,
#   "address": "123 Sesame St"
# }

# For loop:
# profile_strings = []
# for key, value in profile.items():
#     profile_strings.append(f"The key is {key}. The value is {value}")

# Comprehension:
# profile_strings = [ f"The key is {key}. The value is {value}" for key, value in profile.items() if key == "name"]
# print(profile_strings)

# An example of generating a new dictionary from an existing one:
grades = {
  "math": .56,
  "english": .65,
  "history": .74,
  "spanish": .83
}

# In the new dictionary, the name of the subject (the key) is capitalized. The grade (the value) is multiplied by 100 and is now a string so we can have the % symbol.
formatted_grades = { key.capitalize():f"{int(value*100)}%" for (key,value) in grades.items()}

# formatted_grades = { key.capitalize():f"{int(grades[key]*100)}%" for key in grades}
print(formatted_grades)
