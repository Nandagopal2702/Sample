""" Given a list of first 10 natural numbers, write a program to find the square of all even numbers 
   and cube of all odd numbers and store them in another list """

list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = []
for i in list_1:
    if i%2 == 0:
        list_2.append(i**2)
    else:
        list_2.append(i**3)
print(list_2)