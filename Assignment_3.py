#Question_1
a=[1,2,3,4,5]
print(a)

#Question 2

a=['google’,’apple’,’facebook’,’microsoft’,’tesla']
a.append([1, 2, 3, 4, 5])
print(a)


#Question 3
a=["google","apple","tesla","google","microsoft","google"]
print(a.count("google"))


#Question 4

a=[2,4,5,3,6,1]
a.sort()
print(a)

#Question 5

a=[11,12,13,14,15,16,17,18,19,20]
b=[1,2,3,4,5,6,7,8,9,10]
c=a+b
c.sort()
print(c)


#Question 6
#STACK

a= ["Microsoft","Google","Microsoft"]
a.append("Twitter")
a.append("Facebook")
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)


#OPTIONAL QUESTION

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in a:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)



