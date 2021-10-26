test_list = ["50", "abc", "cde"] #create a list (actually, looks like array)
print(type(test_list)) #prove for this variable is list type
for i in range(len(test_list)): #looping from index 0 to length of test_list-1 (it means, from 0 to 2)
    print(test_list[i]) #print the test_list of i-th index
test_list = list(("50", "abc", "cde")) #Create a list same like before, but it used list built-in function (note : use 2 round-bracket)
print(test_llist) #print the proof of same declare list like before
test_list = list(("1", "2", "3", "4", "5", "6")) #re-declare test_list variable
print(test_list[1:len(test_list)]) #it works like using looping from index i-th to length of test_list-1
print(test_list[1:5]) #other example for using "var[index:index]" (works like looping from 1st index to 5-1 = 4th index)
print(test_list[:len(test_list)]) #it works like looping, but the start index is always from index 0 until length of test_list-1 (0 to 5)
print(test_list[:len(test_list)-1]) #other example for using "var[:index]" (works like looping from index 0 to length of test_list-1-1 (0 to 4)
print(test_list[-4:-1]) #another example for using "var[index:index]". it works like looping from -4 to -1 (decrement)

if "3" in test_list: #it works by finding "3" in list of test_list
    print("Yes, it is \"3\"") #print this, if statements true
#output : Yes, it is "3"

#test_list = ["1", "2", "3", "4", "5", "6"]
test_list[1:4] = ["2.1", "2.2", "2.3"] #it works by changing value of list test_list from index 1 to 3 to new value
print(test_list) #print test_list variable
#output : ['1', '2.1', '2.2', '2.3', '5', '6']

#test_list = ["1", "2.1", "2.2", "2.3", "5", "6"]
test_list[1:2] = ["2.11", "2.12", "2.13"] #also, we can replace 1 index (I take index 1st) value with 2 or 3 or even more new values.
print(test_list) #print test_list variable
#output : ['1', '2.11', '2.12', '2.13', '2.2', '2.3', '5', '6']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "2.3", "5", "6"]
test_list.insert(6, "3") #insert "3" to 6th index("5" is 6th index will be moved to 7th index and "6" is 7th index will be moved to 8th index and etc
print(test_list)
#output : ['1', '2.11', '2.12', '2.13', '2.2', '2.3', '3', '5', '6']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "2.3", "3", "5", "6"]
test_list.append("7") #insert "7" to the end of the list.
print(test_list)
#output : ['1', '2.11', '2.12', '2.13', '2.2', '2.3', '3', '5', '6', '7']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "2.3", "3", "5", "6"]
test_list2 = ["8", "9", "10"] #declare test_list2 variable as List and add "8", "9", "10" items
test_list.extend(test_list2) #Add value from test_list2 variable to test_list (it works like append(), by adding the value to the end of the list)
print(test_list)
#output : ['1', '2.11', '2.12', '2.13', '2.2', '2.3', '3', '5', '6', '7', '8', '9', '10']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "2.3", "3", "5", "6", "7", "8", "9", "10"]
test_list2 = ("11", "12") #declare var as tuple
test_list.extend(test_list2) #adding List value with extend(), we can add any iterable object like tuple and etc
#output : ['1', '2.11', '2.12', '2.13', '2.2', '2.3', '3', '5', '6', '7', '8', '9', '10', '11', '12']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "2.3", "3", "5", "6", "7", "8", "9", "10", "11", "12"]
test_list.remove("2.3") #remove List with "2.3" value
print(test_list)
#output : ['1', '2.11', '2.12', '2.13', '2.2', '3', '5', '6', '7', '8', '9', '10', '11', '12']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "3", "5", "6", "7", "8", "9", "10", "11", "12"]
test_list.pop(13) #Removing list value based on List index (in example pop 13th index
print(test_list)
#output : ['1', '2.11', '2.12', '2.13', '2.2', '3', '5', '6', '7', '8', '9', '10', '11']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "3", "5", "6", "7", "8", "9", "10", "11"]
test_list.pop() #Removing list value in the end of list
print(test_list)
#output : ['1', '2.11', '2.12', '2.13', '2.2', '3', '5', '6', '7', '8', '9', '10']

#test_list = ["1", "2.11", "2.12", "2.13", "2.2", "3", "5", "6", "7", "8", "9", "10"]
del test_list[3] #also, we can use "del" to delete/remove list value based on index
print(test_list)
#output : ['1', '2.11', '2.12', '2.2', '3', '5', '6', '7', '8', '9', '10']

del test_list #delete test_list variable
print(test_list)
#output : NameError: name 'test_list' is not defined
#output will cause an error because "test_list" variable has been deleted and it hasn't declared yet.

test_list = ["1", "2.11", "2.12", "2.2", "3", "5", "6", "7", "8", "9", "10"] #declare and init test_list
print(test_list) #make sure test_list has been declared and initiallized
test_list.clear() #clear list of test_list
print(test_list)
#output : []

test_list = ["1", "2.11", "2.12", "2.2", "3", "5", "6", "7", "8", "9", "10"]
for i in test_list: #looping all test_list value (can solve some cases if there are some index with non-value, so it would skip non-value from list looping)
    print(i) #print items in list of test_list
#output :
1
2.11
2.12
2.2
3
5
6
7
8
9
10

#test_list = ["1", "2.11", "2.12", "2.2", "3", "5", "6", "7", "8", "9", "10"]
#example for looping with "while"
i = 0
while i < len(test_list):
    print(test_list[i])
    i += 1
#output :
1
2.11
2.12
2.2
3
5
6
7
8
9
10

#using list comprehension
#test_list = ["1", "2.11", "2.12", "2.2", "3", "5", "6", "7", "8", "9", "10"]
[print(i) for i in test_list] #shortest code for looping values/items in List
#Output :
1
2.11
2.12
2.2
3
5
6
7
8
9
10
[None, None, None, None, None, None, None, None, None, None, None]
#test_list = ["1", "2.11", "2.12", "2.2", "3", "5", "6", "7", "8", "9", "10"]
make_new_list = [i for i in test_list if "2.11" in i] #take "2.11" value from test_list and save it to make_new_list variable
print(make_new_list)
#output : ['2.11']
#it is shorter than using :
'''
make_new_list = [] #first, declare it as List
for i in test_list:
    if "2.11" in i: #if test_list contains "2.11", add it to make_new_list
        make_new_list.append(i)
print(make_new_list)
#output : ['2.11']
'''

#another examples for using List Comprehension
#test_list = ["1", "2.11", "2.12", "2.2", "3", "5", "6", "7", "8", "9", "10"]
make_new_list = [i for i in test_list if not "1" in i] #save values of test_list
print(make_new_list)
#output : ['2.2', '3', '5', '6', '7', '8', '9']
#or we can copy list from one variable to another variable. example :
make_new_list = [i for i in test_list]
print(make_new_list)
#output : ['1', '2.11', '2.12', '2.2', '3', '5', '6', '7', '8', '9', '10']

test_list = ["abc", "cde", "fgh", "ijk"] #declare and init test_list
make_new_list = [i.upper() for i in test_list] #for every value in test_list will be converted to uppercase and saved in to make_new_list
print(test_list)
#output : ['ABC', 'CDE', 'FGH', 'IJK']

test_list = ["cde", "ijk", "abc", "fgh"] #declare and init test_list
test_list.sort() #sort list of test_list
print(test_list) #check to make sure if it's sorted
#output : ['abc', 'cde', 'fgh', 'ijk']

#descending sort for list
test_list = ["cde", "ijk", "abc", "fgh"] #declare and init test_list
test_list.sort(reverse=True) #sort list of test_list, but with reverse (means, sorting by descending)
print(test_list) #check to make sure if it's sorted
#output : ['ijk', 'fgh', 'cde', 'abc']

#sorting list with case sensitive
test_list = ["Cde", "ijk", "abc", "fgh"]
test_list.sort(reverse=True)
print(test_list)
#output : ['ijk', 'fgh', 'abc', 'Cde']

#sorting list with case insensitive by descending
test_list = ["Cde", "ijk", "abc", "fgh"]
test_list.sort(key=str.lower, reverse=True) #sort list of test_list without caring about uppercase or lowercase letter in list.
print(test_list) #check to make sure if it's sorted by descending and case insensitive
#output : ['ijk', 'fgh', 'Cde', 'abc']

#we are also able to reverse order of the list
#test_list =  ['ijk', 'fgh', 'Cde', 'abc']
test_list.reverse() #reverse the order of list
print(test_list)
#output : ['abc', 'Cde', 'fgh', 'ijk']

#there are few ways to join two lists or more
#method 1 :
test_list = ["cde", "ijk", "abc", "fgh"]
test_list2 = [1, 2, 3]
test_list3 = test_list + test_list2
print(test_list)
#output : ['cde', 'ijk', 'abc', 'fgh', 1, 2, 3]
#method 2 :
#test_list = ["cde", "ijk", "abc", "fgh"]
#test_list2 = [1, 2, 3]
for i in test_list2:
    test_list.append(i) #adding value of test_list2 into test_list
print(test_list)
#output : ['cde', 'ijk', 'abc', 'fgh', 1, 2, 3]
#method 3 :
test_list = ["cde", "ijk", "abc", "fgh"]
test_list2 = [1, 2, 3]
test_list.extend(test_list2) #test_list extend test_list2
#output : ['cde', 'ijk', 'abc', 'fgh', 1, 2, 3]
