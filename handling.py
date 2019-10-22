'''#fo = open("foo.txt", "w")
#fo.write( "Python is a great language.\nYeah its great!!\n")
#f1=open("foo.txt","r")
# Close opend file
#fo.close()
#print(f1.read())
#f=open("xy.bin","rb")
#num=list(f.read())
#print(num)
#arr=bytearray(num)
#f.write(arr)
#f.close()
f =open("foo.txt","r+")
str=f.read(5)
position=f.tell()
print(position)
#position=f.seek(0,0)
result=f.read(4)
print(result)
f = open("demofile2.txt", "w+")
f.write("Now the file has too many more contents!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())'''
try:
   fh = open("testfile", "r")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print("Going to close the file")
      fh.close()
except IOError:
   print("Error: can\'t find file or read data")
