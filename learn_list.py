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
