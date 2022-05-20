def name(x):
		c,l=0,len(x)
		new=x[0].title()
		for i in range (l):
				if(x[i]==' '):
						c=i
						new+=" "+x[i+1].title()
		new+=x[c+2: ]
		print(new)
a=input("enter : ")
name(a)
