#this program mimics the split function in python strings

def split_string():
    string1 = input("Enter a string/sentence: ")

    list1 =[]
    word = ""

    for ch in string1:
        if ch != " ":
            word = word + ch
        else:
            if word != "":
                list1.append(word)
                word = ""
        
    
    if word != "":
        list1.append(word)
    
    return list1

print(split_string())
    