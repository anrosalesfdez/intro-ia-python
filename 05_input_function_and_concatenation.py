#input() funtion
print()
print('#input() funtion')
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

print('#cast numbers: int(), float()')
anything = input("Enter a number: ")
something = int(anything) ** 2.0
print(anything, "to the power of 2 is", something)

anything = float(input("Enter a number: "))
something = int(anything) ** 2.0
print(anything, "to the power of 2 is", something)

#concatenation of strings
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
