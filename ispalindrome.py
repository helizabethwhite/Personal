print("****This program will determine if a word is a palindrome.****")
print()
inp = input("Please enter a string or q to quit: ")

## EASY WAY
##while inp != "q":
##    for i in inp:
##        if i == " ":
##            print("Invalid entry.")
##            inp = input("Please enter a string: ")
##
##    print()
##    if inp[::-1] == inp:
##        print(inp[::-1] + " = " + inp)
##        print("is palindrome!")
##        print("-"*30)
##    else:
##        print(inp[::-1] + " != " + inp )
##        print("is not palindrome!")
##        print("-"*30)
##
##    inp = input("Please enter a string or q to quit: ")


## HARD WAY
##while inp!= "q":
##    result = ""
##    for i in range(len(inp)):
##        if i != 0:
##            result += inp[-i]
##    result += inp[0]
##
##    if result == inp:
##        print(result)
##        print("is a palindrome.")
##    else:
##        print(result)
##        print("is not a palindrome.")
##
##    inp = input("Please enter a string or q to quit: ")
