
# Q-1 Triple all numbers given in the list
print("Question 1: Triple all numbers given in the list  ")
print("Answer :->")

result=map(lambda i:i*3,[2,4,6,7])
print(list(result))    
 
print("ANSWER 2 ")
print(":->")

#Q-2 Separate even odd number from given list
l =[]
n=int(input("Enter length: "))
for i in range(n):
    e=int(input("Enter Element: "))
    l.append(e)
print(l)
even = []
odd = []
for j in l:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("Even Element List:" , even)
print("Odd Element List:" , odd)

#Q-3 Print all string un lower case from given tuple
print (" Q-3: Print all string un lower case from given tuple")
print("ANSWER :->")

def output(s):
    return s.lower()
tuplee=['THIS','IS','MAP']
tup=map(output,tuplee)
print(tuple(tup))




#Q-4 Sqrt of given numbers using map

print ("Q-4 : Sqrt of given numbers using map")
print("ANSWER :->") 

def square(x):
    return x*x
numbers=[1,2,3,4,5,6]
squares = map(square,numbers)
print(list(squares))

#Q-5 duplicate string remove with map
print("Q-5 : duplicate string remove with map" )
print("Answer 5:->")

def duplicate(s):
    return str(s).upper()
chars ={'a','b','C','a','b','c'}
print(chars)
print("After removing duplicate characters")
result =map(duplicate,chars)
print(set(result))

#Q-6 Print table of any numbers
print("Q-6 - Print table of any numbers")
print("Answer 6: - DOUBT ")



#Q-7 Add two list
print("Q-7 Add two list")
print("Answer 7:->")
def add_two_num(x,y):
    return x+y
num1=[6,5]
num2=[4,2]
result=map(add_two_num,num1,num2)
print(list(result))


#Q-8 float to integer 
print("Answer 8 :- DON'T KNOW HOW TO DO")


#   Q=9 reverse a list using a built in function
print("Q=9 reverse a list using a built in function")
print("ANSWER 9 :->")

rev_list = [10, 11, 12, 13, 14, 15]
rev_list.reverse()
print("Using reverse() ", rev_list)

print("Using reversed() ", list(reversed(rev_list)))


#Q-10 Add @gmail.com to all the value and convert it to lower case
print("Q-10 Add @gmail.com to all the value and convert it to lower case")
print("Anser 10 :->")

def toUpper(str):
    return str.lower()
dict_item={"a" :"car","b":"train","c":"bike"}
a=map(lambda i:(i[0],i[1]+"@GMAIL:.com".lower()),dict_item.items())

print(dict(a))

