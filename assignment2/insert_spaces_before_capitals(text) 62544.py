#insert_spaces_before_capitals(text)

def insert_spaces_before_capitals(text):
    result = ""                                                     #creates an empty string

    for i in range(len(text)):                                      # iterates through every characters
        if i > 0 and text[i].isupper() and text[i-1].islower():     # i > 0 ensures that we don't check the previous value for the first letter
                                                                    # text[i].isupper() checks whether the current character is uppercase
                                                                    # text[i-1].islower checks whether the previous character is lowercase
            result = result + " "                                   # adds the space if condition is true

        result = result + text[i]                                   # adding all the characters to the result from text
    return result

# implementation
text = "helloWorldPython"
answer = insert_spaces_before_capitals(text)
print(answer)
