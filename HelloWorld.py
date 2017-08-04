'''
fruits =['apples','banana','orange','strawberry']
vegetables=['lettuce','cucumber','carrots']
fruits_and_vegetables=fruits + vegetables
print fruits_and_vegetables
salad=3*vegetables
print salad


x=['Hello World!']
z =x*1
print z

def myfunc(list):
    hi=[list]
    z=hi*1
    return print z
print myfunc("list")
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
