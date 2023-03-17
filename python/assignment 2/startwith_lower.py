""" Write a program to extract the words starting with lowercase letter present in the list.
    ['Nissan','maruti', 'hyundai', 'Volkswagen', 'audi'] """

list_1 = ['Nissan','maruti', 'hyundai', 'Volkswagen', 'audi']
list_2 = []
for i in list_1:
    if i[0].islower():
        list_2.append(i)

print(list_2)
