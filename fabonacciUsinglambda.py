f=lambda x,y:x+y
n=int(input("enter"))
print("0 ,  1 , ",end="")
x,y=0,1
for i in range (n):
		print(f(x,y)," , ",end="")
		x,y=y,x+y
