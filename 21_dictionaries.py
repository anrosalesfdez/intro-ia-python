#dictionary collection which is ordered** and changeable. No duplicate members
#set of key-value, each key must be unique 

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)


#get elements
print(dictionary["cat"])
print(dictionary.get("cat"))


# dictionaries are not lists - they don't preserve the order of their data
#The order in which a dictionary stores its data is completely out of your control, and your expectations.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


#loop for dictionaries: keys
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


#loop for dictionaries: items
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)


#change value for a particular key
dictionary['cat'] = 'minou'
print(dictionary)

#add element
dictionary['fish'] = 'poison'
dictionary.update({'bird': 'canard'})
print(dictionary)

#update element
dictionary['fish'] = 'poisonnnnn'
dictionary.update({'fish': 'poisonnnnneeeeeeeeeeee'})
print(dictionary)

#delete element
del dictionary['fish']
print(dictionary)


#To check if a given key exists in a dictionary, you can use the in
if "bird" in dictionary:
    print('Yes')
else:
    print('No')



#To copy a dictionary, use the copy()
copy_dictionary = dictionary.copy()
print(copy_dictionary)



# removes all the items
dictionary.clear()   
print(len(dictionary))    # outputs: 0

del dictionary    # removes the dictionary
