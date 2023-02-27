def main():
    obj1=open("f.txt","w")
    obj1.write("hello how r u \n")
    obj1.write("welcome to the chapter file handling \n")
    obj1.write("Enjoy the session \n")
main()

def main1():
    obj1=open("f.txt","w")
    for i in range(1,20):
        i=str(i)
        obj1.write(i)
        obj1.write(" ")
main1()

def reads():
    f=open("f.txt","r")
    string=f.read()
    print(string)
reads()





 