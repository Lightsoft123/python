test_list = ["50", "abc", "cde"] //create a list (actually, looks like array)
print(type(test_list)) //prove for this variable is list type
for i in range(len(test_list)): //looping from index 0 to length of test_list-1 (it means, from 0 to 2)
    print(test_list[i]) //print the test_list of i-th index
test_list = list(("50", "abc", "cde")) //Create a list same like before, but it used list built-in function (note : use 2 round-bracket)
print(test_llist) //print the proof of same declare list like before
test_list = list(("1", "2", "3", "4", "5", "6")) //re-declare test_list variable
print(test_list[1:len(test_list)]) //it works like using looping from index i-th to length of test_list-1
print(test_list[1:5]) //other example for using "var[index:index]" (works like looping from 1st index to 5-1 = 4th index)
print(test_list[:len(test_list)]) //it works like looping, but the start index is always from index 0 until length of test_list-1 (0 to 5)
print(test_list[:len(test_list)-1]) //other example for using "var[:index]" (works like looping from index 0 to length of test_list-1-1 (0 to 4)

