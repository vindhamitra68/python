num_list=[-5,10,30,-45,-3,33,-12,24]
print(num_list)
new_list=[x for x in num_list if x>0]
print("the positive numbers are: ",new_list)

n=int(input("enter the numbers of elements:"))
num_list=[]
for i in range(n):
  a=int(input("enter the numbers:"))
  num_list.append(a)
print("entered list:",num_list)
sqr_1st=[x**2 for x in num_list]
print("squared list:",sqr_1st)

word=input("enter a word:")
vowels=[x for x in word.lower() if x in['a','e','i','o','u']]
print("the vowels in the words are:",vowels)


w=input("enter a word:")
ord=[ord(x)for x in w]
print("the ordinal value is:",ord)