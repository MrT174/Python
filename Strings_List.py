'''
Assignment: String and List Practice
Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:

• .find()

• .replace()

• min()

• max()

• .sort()

• len()

Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
'''

words="It's thanksgiving day. It's my bithday, too!"
print words
print "Position of day is:  "
print words.find('day')

moreWords="It's that time of day"
print moreWords
print "Replace day with month-    " + moreWords.replace('day','month')

print "Print the maximum of x = [2,54,-2,7,12,98]"
x = [2,54,-2,7,12,98]
z=x
print max(z)


print "Print the minimum of x = [2,54,-2,7,12,98]"
x = [2,54,-2,7,12,98]
z=x
print min(z)



x = ["hello",2,54,-2,7,12,98,"world"]
z=x
z.sort()
print "first value:"
print min(z)
print "last value:"
print max(z)
print "Capturing only the last and first values below:"
last=max(z)
first=min(z)
list =[last, first]
for idx in list:
print idx

print "New List Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!"
x = [19,2,54,-2,7,12,98,32,10,-3,6]
numbers=x
numbers.sort()
numbers.split(",",x)
a,s,d,f,g,h,j,k,l,z,c =numbers
num1=[[a,s,d,f,g,h],j,k,l,z,c]
print num1
