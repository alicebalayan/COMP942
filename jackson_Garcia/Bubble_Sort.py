def swap(s1, s2):
    return s2, s1

#Creating an Array
mylist = [5,6,8,9,7,3,2,1]  

#Getting the List of the Array
sizeoflist = len(mylist)

#Creating a Boolean for when a Swap was made
issort = False;

#while is sort Not True continue to do the loop of the array.
while( not issort):
  
  #Making the boolean Is sort True
  issort = True;
 
  for j in range (sizeoflist-1):
    print(mylist)
    if mylist[j] > mylist[j+1]:
      mylist[j] , mylist[j+1] = swap(mylist[j], mylist[j+1])
      issort=False;

print(issort)
