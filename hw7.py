import hashlib
import os


fh= open('cryptoCatImage.jpg', 'rb')
catData=fh.read()
fh.close()

fh= open('cryptoDogImage.jpg', 'rb')
dogData=fh.read()
fh.close()

found=0
count=0

dogTable={}
catTable={}

while found==0:

    catapp=os.urandom(5)
    dogapp=os.urandom(5)

    catHash=hashlib.sha1(catData+catapp).hexdigest()[0:10]
    dogHash=hashlib.sha1(dogData+dogapp).hexdigest()[0:10]

    catTable[catHash]=catapp
    dogTable[dogHash]=dogapp

    if (catHash==dogHash):
        print("match found no check tables")
        newcatcontents=catData+catapp
        newdogcontents=dogData+dogapp
        fh=open("newcat.jpg", 'wb+')
        fh.write(newcatcontents)
        fh.close()
        fh=open("newdog.jpg", 'wb+')
        fh.write(newdogcontents)
        fh.close()

        found = 1
        break
    if catHash in dogTable:
        print("match found in dog!!!")
        newcatcontents=catData+catapp
        newdogcontents=dogData+dogTable[catHash]
        fh=open("newcat.jpg", 'wb+')
        fh.write(newcatcontents)
        fh.close()
        fh=open("newdog.jpg", 'wb+')
        fh.write(newdogcontents)
        fh.close()
        found=1
        break
    if dogHash in catTable:
        print("matchfound in cat")
        newcatcontents=catData+catTable[dogHash]
        newdogcontents=dogData+dogapp
        fh=open("newcat.jpg", 'wb+')
        fh.write(newcatcontents)
        fh.close()
        fh=open("newdog.jpg", 'wb+')
        fh.write(newdogcontents)
        fh.close()
        found=1
        break
    count=count+1
print("doneskis!!!")
print (count)
