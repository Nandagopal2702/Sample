""" . Write a function which will take a string argument and reverse the words in the string. For 
example - Input string -- “Hello World”. Output should be “olleH dlroW” """

def reverse_word(String):
    String2 = String.split(" ")
    res = [x[::-1] for x in String2]
    return " ".join(res)
    
        
print(reverse_word("Hello World"))

