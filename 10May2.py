f=open("Screenshot.png" , 'rb')
str1=f.read()
f1=open("in.png",'wb')
f1.write(str1)
f.close()
f1.close()
