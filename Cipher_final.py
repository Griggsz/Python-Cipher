

while True: 
    try: # loop that checks input for any errors
        months_key = int(input("Please enter your birth month 1 - 12: ")) # gets user to enter their bith month
    except ValueError: # checks that an interger has been entered
        print("You have entered an incorrect character\n ")
        continue
    else:
        #if statment checks that the month is between 1 and 12
        if months_key <= 0 or months_key > 12 : 
            print("You have entered an incorrect number.\nPlease enter a number between 1 and 12\n ") 
        else:
            break

#loop for the user to enter the word they want to encypt
while True:
    word = str(input("Please enter the word you want to encrypt: ")) # user inputs word
    if not word.isalpha(): # checks to make sure the user enters only letters
        print("You have entered an incorrect word please try again") 
    else:
        break
word = word.upper() # converts the entered word to uppercase


# makes a new list that takes the word and converts it to a list of uni code numbers
word_uni = [ord(char) for char in word] 
new_word_uni = [] #empty list to store uni code with added cipher 
converted_num = [] # empty list to store uni code with added cipher and any changes if the number loops back round to A
# adds the month/key to each uni code number
for num in word_uni:
    new_word_uni = num + months_key
    # checks if the number goes above 90 "Z" resets it to 65 "A" and adds the remainder
    if new_word_uni > 90:
        remain = new_word_uni % 90
        new_word_uni = 65 + remain    
    converted_num.append(new_word_uni) # puts all the new convered numbers to a new list


cipher_word = [] # final place where the new convered word is stored
#converts each number in the list to its corresponding letter
for i in converted_num: 
    cipher_word.append(chr(i))
# finally takes the list and addes each letter together to create the word
cipher_word = "".join(cipher_word)

# prints final converted word
print ("Your converted word is: ", cipher_word)



#Main code written by Joel Griggs
#Last edited by Joel Griggs on 06/09/2023