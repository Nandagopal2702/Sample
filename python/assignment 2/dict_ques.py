""" In the dictionary {'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'} 
    list out all the keys in a list named as 'list_keys' and 
    list out all the values in a list named as 'list_values'.Also find out the value of key 'Australia' 
    in the list and as it is not existing in the list print 'NA' as its value """

dict = {'India':'New Delhi', 'USA':'Washington D.C', 'Nepal':'Kathmandu'}
find = "Australia"

list_keys = list(dict.keys()) #listing the keys of dict
list_values = list(dict.values()) # listing the values of dict

key = dict.get(find,"NA") # finding the Australia in dict
value = dict.get(find.index,"''") # finding the value of Australia in the dict

print(list_keys)
print(list_values)
print(key)
print(value)


