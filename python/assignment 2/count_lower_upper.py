""" In the given String -- 'MsYs TecHNOlogiEs iS a gREat place To woRk' 
find the count of lowercase and uppercase letters. """


s = "MsYs TecHNOlogiEs iS a gREat place To woRk"

low = 0
up = 0
sp = 0
for i in s:
    if i.islower():
        low += 1
    elif i.isupper():
        up += 1
    elif i.isspace():
        a= "".join(s)

print(low)
print(up)
