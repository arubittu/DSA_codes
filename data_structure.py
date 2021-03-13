import time
from sys import stdin, stdout 
import io,os

 

class fakeList: # my data structure
    def __init__(self):
        self.list=[]
    def append(self,element):
        self.list.append(element)
    def printI(self,index):
        print(self.list[index-1])
    def insert(self,index,element):
        self.list.insert(index-1, element)
    def delete(self,index):
        self.list.pop(index-1)
    def circular(self,dir):
        if dir==1:
            last=self.list.pop()
            self.list.insert(0,last)
        else:
            first=self.list.pop(0)
            self.list.append(first)
        


 

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.n=0 # number of items 
        self.string=''
       

    def append_data(self,data): #adding at the end/ tail
        
        new_node=Node(data,None,None)
        if self.head==None:  #if no nodes then do
            self.head=new_node
            self.tail=self.head
            
        else:   # when other nodes exists
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        self.n+=1
    
    def insert(self,index,data): # insert x at index
        NodeToInsert=self.head 
        NewNode=Node(data,None,None)#address of node to delete
        for i in range(index-1):
            NodeToInsert=NodeToInsert.next
        if NodeToInsert==self.head:
            NewNode.next=self.head
            self.head.prev=NewNode
            self.head=NewNode
        else:
            NewNode.prev=NodeToInsert.prev
            NewNode.next=NodeToInsert
            NodeToInsert.prev.next=NewNode
            NodeToInsert.prev=NewNode
        self.n+=1

    def __str__(self): #prints items
        arr=[]
        temp=self.head
        for i in range(self.n):
            arr.append(temp.data)
            temp=temp.next
        return " ".join(str(x) for x in arr) 

    def printI(self,index):
        NodeToPrint=self.head
        for i in range(index-1):
            NodeToPrint=NodeToPrint.next
        self.string= self.string + str(NodeToPrint.data)+'\n'
        #stdout.write(str(NodeToPrint.data)+'\n')#print(NodeToPrint.data)
    def printFinal(self):
        stdout.write(self.string)

    def circular(self,dir):#dir == 1 or -1
        if self.n==1:
            return
        else:
            if dir==1: 
                lastNode=self.tail.data
                self.DeleteNode(self.n)
                self.insert(1,lastNode)
            else:
                firsNode=self.head.data
                self.DeleteNode(1)
                self.append_data(firsNode)


    def DeleteNode(self,index):
        if self.head==None:
            raise ValueError('no element in list but deleteNode activated :(') 

        NodeToDelete=self.head

        if index==1:
            #self.head.data=None 
            self.head=NodeToDelete.next
            #NodeToDelete.next=None
            self.head.prev=None
        elif index==self.n:
            #self.tail.data=None
            self.tail=self.tail.prev 
            #NodeToDelete.prev=None
            self.tail.next=None
        else:
            for i in range(index-1):
                NodeToDelete=NodeToDelete.next
            NodeToDelete.prev.next=NodeToDelete.next 
            NodeToDelete.next.prev=NodeToDelete.prev
        self.n -=1
        return



if __name__=='__main__':
 
    first_input= stdin.readline()  #input()
     
    first_input=[int(s) for s in first_input.split()]
    n,q=first_input[0],first_input[1]
    
    array=stdin.readline()#input()
    array=[int(s) for s in array.split()]
    
    linkedList=fakeList()#doublyLinkedList()
    
    for i in range(n): #append data in linked list
        linkedList.append(array[i])
        #linkedList.append_data(array[i])
    #query=os.read(0,100000)
    #print(query)
    #query=stdin.readlines()
    #print(query)
    for j in range(q): # run q queries
        query=stdin.readline()#input()
        command=query[0]
        arguments=[int(s) for s in query[1:].split()]
        
        if command=='I':
            linkedList.insert(arguments[0],arguments[1])
        elif command=='D':
            linkedList.delete(arguments[0])
           # linkedList.DeleteNode(arguments[0])
        elif command=='R':
            linkedList.circular(arguments[0])
        else:
            linkedList.printI(arguments[0])
    #linkedList.printFinal()
  
    