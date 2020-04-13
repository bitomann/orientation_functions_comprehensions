#Functions

# def greet():
#     print("Good Afternoon!!!")
    
# greet()

# def flex_greet(name, greeting):
#     return f"{greeting}, {name}"

# greeting_jp = flex_greet("Jean-Paul", "Bienvenue")
# greeting_jp = flex_greet("Jean-Paul")
# print(greeting_jp)

# Arbitrary Arguments(*args) and Keyword Arguments(**kwargs)


# args - takes any number of positional argument values and adds them to a list


# def list_fave_colors(name, *args):
#     print(name, type(name))
#     print(args, type(args))
    
#     for color in args:
#         print(f"My name is {name}, and one of my fave colors is {color}")


# Pass in any number of arguments after the name ("Fred" or "Tia", and the function works, thanks to *args)
# list_fave_colors("Fred", "red", "green", "blue", "orange")
# list_fave_colors("Tia", "puce", "goldenrod")

# kwargs -- takes any number of keyword arguments and adds them to a dictionary


# def make_family(name, **tacos):
#     print(name, type(name))
#     print(tacos, type(tacos))
    
#     family_str = f"We are the {name} family. "

#     family_stuff = tacos.items()
#     for title, person in family_stuff:
#         family_str += f"The {title} is {person}. "

#     return family_str


# Now we can make families of any size, and have flexibility to have those family members have whatever role we want
# family = make_family("Shepherd", mom="Anne", dad="Joe", dog="Murph")
# other_family = make_family("Parker", aunt="May", nephew="Peter")

# print(family)
# print(other_family)

# We can also use *args and **kwargs to call a function

# def mulitply(num1, num2, num3):
#     print("num1: ", num1)
#     print("num2: ", num2)
#     print("num3: ", num3)
#     return num1 * num2 * num3

#Calling the function with *args
# args = (2, 3, 4)
# product1 = mulitply(*args)

#Calling the function with **kwargs
# kwargs = {"num1": 8, "num2": 7, "num3": 6}
# product1 = mulitply(**kwargs)

# You can combine everything together!
def calculate_average(subject, *test_scores, **student_details):
    print("Type & value of subject: ", type(subject), subject)
    print("Type & value of test_scores: ", type(test_scores), test_scores)
    print("Type & value of the student_details: ", type(student_details), student_details)

    if subject == "English":
        average_score = 49
    else:
        average_score = sum(test_scores)/len(test_scores)
    
    print(f"{student_details['last_name']}, {student_details['first_name']} got an average score of {average_score} in {subject}.")


calculate_average("Math", 75, 64, 35, first_name="Andy", last_name="Collins")

# calculate_average("Math", 90, 90, 90, first_name="Andy", last_name="Collins")
