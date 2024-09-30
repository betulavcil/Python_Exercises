# Python Exercises


# TASK 1: Examine the types of data structures.

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4, "String", 3.2, False]
type(l)

d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}
type(d)


t = ("Machine Learning", "Data Science")
type(t)


s = {"Python", "Machine Learning", "Data Science", "Python"}
type(s)



# TASK 2: Convert all letters of the given string to uppercase.
# Use spaces instead of commas and periods, and separate words.


text = "The goal is to turn data into information, and information into insight."

text.upper().replace(",", " ").replace(".", " ").split()




# TASK 3: Do the following tasks for the given list.


lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Look at the number of elements of the given list.
len(lst)


# Step 2: Call the elements at zero and tenth index.
lst[0]
lst[10]
# idx = [0, 10]
# [lst[i] for i in idx]

# Step 3: Create list ["D","A","T","A"] from the given list.

data_list = lst[0:4]
data_list

# Step 4: Deleting the element at the eighth index.

lst.pop(8)
lst
# Bonus: .pop() gives the output of the element it deleted, we can save this.
# a = lst.pop(8)
# a
# lst



# Step 5: Add a new element.

lst.append(101)
lst

# BONUS
# Other methods
# lst.append(["a", "b", "c"])

# lst.extend(["a", "b", "c"])
# print(lst)


# Step 6: Re-add the element "N" at the eighth index.

lst.insert(8, "N")
lst




# TASK 4: Apply the following steps to the given dictionary structure.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}


# Step 1: Access the key values.

dict.keys()



# Step 2: Access the values.

dict.values()



# Step 3: Update the value of Daisy key 12 to 13.

dict.update({"Daisy": ["England", 13]})
dict


###########
# Other Methods
#1
dict["Daisy"] = ["England", 13]
dict


# 2
dict["Daisy"][1] = 13
dict



# Step 4: Add a new value with the key value Ahmet value [Turkey,24].
dict.update({"Ahmet": ["Turkey", 24]})
dict



# Step 5: Delete Antonio from the dictionary.

dict.pop("Antonio")
dict

# or
del dict["Antonio"]



# TASK 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns these lists.

l = [2, 13, 18, 93, 22]

def func(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list

even, odd = func(l)



# Solution with list comprehensions method
def func(lst):
    even_list = [i for i in lst if i % 2 == 0]
    odd_list = [i for i in lst if i % 2 != 0]
    return even_list, odd_list
even, odd = func(l)


def func(lst):
    even_list, odd_list = [i for i in lst if i % 2 == 0], [i for i in lst if i % 2 != 0]
    return even_list, odd_list
even, odd = func(l)


def func(lst):
    return [i for i in lst if i % 2 == 0], [i for i in lst if i % 2 != 0]
even, odd = func(l)








# TASK 6: The list below includes the names of students who have achieved success in the engineering and medical faculties.
# The first three students represent the success ranking of the engineering faculty, while the last three students belong to the medical faculty student ranking.
# Print the student rankings by faculty using enumarate.

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]


for ind, std in enumerate(students):
    print(f"Index: {ind}, Student name: {std}")


for ind, std in enumerate(students):
    if ind < 3:
        n_ind = ind + 1
        print("Engineering Faculty", n_ind, ". student:", std)
    else:
        n_ind = ind - 2
        print(f"Medical Faculty {n_ind}. student: {std}")


