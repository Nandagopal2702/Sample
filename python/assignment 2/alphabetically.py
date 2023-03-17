""" Given a dictionary 
   {'Msys Technologies':'Sanjay Sehgal','Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan',
    'Wipro':'Thierry Delaporte'} 
   make a list of all the values associated with keys in alphabetically sorted order """

dict = {'Msys Technologies':'Sanjay Sehgal','Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan',
        'Wipro':'Thierry Delaporte'}

new_dict = sorted(dict.items())
new_list = []
for i in new_dict:
    new_list.append(list(i))

print(new_list)


