f=open("m.txt",'r')
x=input("Enter the string : ")
str1=f.read()
if x in str1:
		print("result found")
else:  print("Sorry")
