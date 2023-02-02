#Given list x = [100,110,120,130,140,150], use list comprehension to create another list containing each number in the list multiplied by 5.  
# x = [100,110,120,130,140,150]
# y=[n*5 for n in x]
# print(y)

# Write a function named divisible_by_three that accepts a number n and prints all numbers from 1 to n that are divisible by 3. 
# def divisible_by_three(n):
#     for g in range(1,n):
#         if (g%3==0):
#          print(g)
# divisible_by_three(90)
# n=int(input("Enter your number :"))
# if (n%3==0):
#     print("{} is divisible by :".format(n))
# else:
#     print("{} is not divisible by :".format(n))

# Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]
# x = [[1,2],[3,4],[5,6]]
# f=x[0]+x[1]+x[2]
# print(f)

# Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. Example:
# smallest([3,6,8,2,4,1,5,7]) returns 1
# s=[5,3,7,9,1,3,8,2,4]
# g=min(s)
# print(g)

# Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates
# x = ['a','b','a','e','d','b','c','e','f','g','h']

# l = ['a','b','a','e','d','b','c','e','f','g','h']
# r=set(l)
# print(list(r))

# Write a function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.

# def divisible_by_seven():
#     f=[]
# for t in range(100,200):
#     if (t%7==0):
#         f.append(t)
# print(f)
# divisible_by_seven()

# Given this list of students containing age and name,  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.

# students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
# for name_age in students:
#         year=2022-name_age["age"]
#         name=name_age["name"]
#         print(f"Hello {name}, you were born in {year}")

# for x in students:
   

# std=list(set(students[0]))
# print(std)
# for x in students:
#     dob=2022-"age"
#     print(f"Hello my name is{dob} ")
# std=students[0],students[1],students[2],students[3]
# print(dict(std))
# for c in std:
#     if c in std=="age":
#         d=2022-f
#         print("Hello",values=0 )
    # print("Hello {}".format(students[1],[0]))


#1. Given a list L  and an index i, write code that will create a new
# list the same as L but with element N removed

# L=["a","e","i","o","u"]
# del L[2]
# j=[]
# for x in L:
#     j.append(x)
# print(j)

# 2. Given a list L and an index i, write code that will remove element
# N from L, in place (i.e., won’t create a new list)
# For example: L = [a, b, c, d, e, f, g, h],  N = 5  yields [a, b, c, d, e, g, h]


# 3. Given a list L, write code that will reverse the list.
# 4. Given a list L , write code that will reverse the list in place
# (i.e. won’t create a new list)
# For example: [1, 2, 3] -> [3, 2, 1]
# L=["My",]

#write a program to accept percentage from the user and display the grade according to the following criteria
#>90 A
#>80 and <=90 B
#>=60 and <= 80 C
#below 60 D
x = int(input("Enter percentage :"))
if x>90 and x<=100:
    print("Grade A")
elif x>80 and x<=90:
    print(" Grade B")
elif x >=60 and x<=80:
    print("Grade C")
elif x<60:
    print("Grade D")

# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
#Cost price (in Rs)    Tax
# >100000               15%
# >50000 and <=100000   10%
# <=50000               5%
tax = 0
# print(bool 0)