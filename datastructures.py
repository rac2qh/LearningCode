#!/Applications/.dce/python/python_3/bin/python3.9 

import argparse 

sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
print("Data Stuctures and Algorithms Examples")
print("--------------------------------------")



#forloop

print("For Loop")
def forloop():
    words = ["redwan", "chowdhury", "arman"]
    for i in words:
        print(i, len(i))

#if statement
def ifstatement():
    print("-------------")
    print("If Statement")
    a = 33; 
    b = 27; 
    c = 56; 

    if a + b > c: 
        print("A+B is greater than C")
    else: 
        print("C is greater than A + B")


#while loop
def whileloop():
    print("-------------")
    print("While loop")
    a = 1; 
    while a <= 5: 
        print(a)
        a+=1; 
        


#linkedlist
    print("-------------")
def linkedlist():
    print("Linked List")
    print("First we will go over a single linked list")
#arrays
#queues
#stack 
#hashmap 
#trees
#heaps
#graphs 

if __name__ == "__main__":
    forloop()
    ifstatement()
    whileloop()
    linkedlist()