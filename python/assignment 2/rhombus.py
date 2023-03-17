""" Print the below rohmbus pattern according to the given number for eg: given number is 4 then 
o/p will be :
   1
  212
 32123
4321234
 32123 
  212 
   1    """

num = int(input())
val = 0
for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print(val,end="")
    print()
    val+=1
    if val > 9:
        val = 0
for i in range(num-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(2*(num-i-1)-1):
        print(val,end="")
    print()
    val+=1
    if val > 9:
        val = 0


