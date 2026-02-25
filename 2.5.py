#Write a program to read a file and display its contents. At the end it shall
#also display no. of words available in file.


file1=open("textfile.txt","r")
content=file1.read()
print(content)
words=content.split()
wordcount=len(words)
print("Word Count of file is ",wordcount)
file1.close()
