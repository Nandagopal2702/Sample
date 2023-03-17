""" Write a method number_of_prime_numbers() which takes two input arguments num1 and 
    num2 and should return the total number of prime numbers in the range. The numbers num1 and 
    num2 are inclusive of the range. Also add all the numbers in an empty list and return the sum of the
    list. So finally your function will return two things, first will be the count of prime numbers and the 
    other will be the sum of all the prime numbers in the given range. """

def number_of_prime_number(num1,num2):
    list_1 = []
    for i in range(num1,num2+1):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                list_1.append(i)
    print(list_1)
    print(len(list_1))
    print(sum(list_1))

number_of_prime_number(num1=int(input()),num2=int(input()))









# def number_of_prime_numbers(num1,num2):
#     list_1 = []
#     for i in range(num1,num2):
#         if num1 <= 2 and num2 <= 2:
#             return "Enter the higher number"
#         else:
#             if num1 % i == 0:
#                 return "No prime number"
#             else:
#                 list_1.append(i)
#     return list_1
    
# prime = number_of_prime_numbers(20,60)
# print(prime)


