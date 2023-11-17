def stringMatch(string, element):
    L = len(string)
    L_element = len(element)
    for i in range(L - L_element + 1):
        if string[i:i+L_element] == element:
            return i
    return -1

string = "nobody_noticed_him"
print(stringMatch(string, 'not'))