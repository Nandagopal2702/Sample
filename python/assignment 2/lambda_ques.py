"""  Write a lambda function which takes two input arguments x and y. If x is greater than y then it 
should return square of y and if y is greater than x, then it should return square of x. """

x = int(input())
y = int(input())

result = lambda x,y : x**2 if (x > y) else y**2
print(result(x,y))