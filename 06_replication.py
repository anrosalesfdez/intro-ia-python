#replication
print()
print('replicaiton operator')
print('James' *3)
print(5 * "2")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#LAB
print()
print('#LAB')
# input a float value for variable a here
a = float(input('Insert value for a: '))
# input a float value for variable b here
b = float(input('Insert value for b: '))
# output the result of addition here
print(a+b)
# output the result of subtraction here
print(a-b)
# output the result of multiplication here
print(a*b)
# output the result of division here
print(a/b)
print("\nThat's all, folks!")

#LAB
print()
print('#LAB')
print('#LAB')
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# find a total of all minutes
total_minutes = hour*60+mins+dura
print('total_minutes: '+ str(total_minutes))

# find a number of hours 
new_hour =int( total_minutes / 60)
print('new_hour: '+ str(new_hour))

# find a number of minuts once taking the hours
new_minutes = total_minutes % 60
print('new_minutes: '+ str(new_minutes))

# correct hours to fall in the (0..23) range
while new_hour > 23:
    new_hour = new_hour - 24
print('new_hour corrected: '+ str(new_hour))

print(new_hour, ":", new_minutes, sep='')


