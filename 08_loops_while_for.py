#LOOPS
##LAB
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
def ask_for_number():
    return input('Enter a number: ')
    
guess_number = int(ask_for_number())
while guess_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess_number = int(ask_for_number())
print('Well done, muggle! You are free now.')

for i in range(10):
    print("The value of i is currently", i)

for j in range(2, 8):
    print("The value of j is currently", j)

x = range(3, 20, 2)

for n in x:
  print(n)

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

#LAB    
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

for i in range(1, 6):
    print(i,' Mississippi')
print('Ready or not, here I come!')

# break - example => exits the loop immediately, the program begins to execute the nearest instruction after the loop's body
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example => to skip the current iteration, and continue with the next iteration.
# range([start default 0], [stop], [step default 1])
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

#LAB
def ask_for_word():
    return input('Enter a word: ')

word = ask_for_word()
while word != 'chupacabra':
    word = ask_for_word()
print("You've successfully left the loop.")


# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input('Enter a word: ').upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter != 'A' and letter != 'E' and letter != 'I' and letter != 'O' and letter != 'U':
        print(letter)    

user_word = input('Enter a word: ').upper()
word_without_vowels = ''
for letter in user_word:
    # Complete the body of the for loop.
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    word_without_vowels = word_without_vowels + letter
# Print the word assigned to word_without_vowels
print(word_without_vowels)

word = "Python"
for letter in word:
    print(letter, end="*")

#LAB
blocks = int(input("Enter the number of blocks: "))
#
# Write your code here.
#
height = 1
while (blocks-height) > height:
    print(blocks)
    print(height)
    blocks -= height
    height += 1
print("The height of the pyramid:", height)


#LAB: COLLATZ'S HYPOTHESIS
def insert_number():
    return int(input('Insert non-negative, non-zero integer number: '))
c0 = insert_number()
if c0 <= 0:
    print('error in number')
else:
    while c0 != 1:
        if c0%2 == 0: #even = par
            c0 = c0/2
        else: #odd = impar
            c0 = 3*c0 + 1
        print(c0)
