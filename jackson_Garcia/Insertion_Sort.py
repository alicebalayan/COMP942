#Function receiving an array
def insertion_sort(List):
  
  #for loop from 1 to length of list
  for i in range(1, len(List)):

    #Getting element from list.
    curNum = List[i]

    #starts at 0, then increments by -1,to end at -1 
    for j in range(i-1, -1,  -1 ):
      
      #If Comparing number is greater than The Current Number it takes The Current Number Location.
      if List[j] > curNum:
        List[j+1] = List[j]
      
      else:
      
      #Else increment J plus 1. and Break out of the for j loop.
        j +=1
        
        #break out of loop
        break
      #Current number takes J location.
      List[j] = curNum
      

#Creating an Array List
mylist = [8,4,2,12,11,9,10,3]

#PRINTING unsorted list
print(mylist)

#Using the insertion sort method
insertion_sort(mylist)

#print the sorted list.
print(mylist)
