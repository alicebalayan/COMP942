#include <iostream>
#include <algorithm>

using namespace std;

//function to check if the input is valid or not
int isValid(int val)
{
   return (val > 0);
}

//function to print an array
void getArray(int *arr, int size)
{
   int i; 
   for(i = 0; i < size; i++)
      cout<<arr[i]<<" ";
   cout<<"\n";
}

//function to calculate average from an array
int getAverage(int* arr, int size)
{
   int sum = 0;
   
   for(int i = 0 ; i < size; i++)
      sum += arr[i];

   return sum/size;
}

//driver function
int main()
{
   int size, i, val;  

   //asking from the user
   cout<<"How many test scores do you have? ";
   cin>>size;

   //declring dynamic array
   int *arrScore = new int[size];

   for(i = 0; i < size; i++)
   {
      cout<<"Test Score #"<<i+1<<": ";
      //getting value input from the user
      in:
      cin>>val;
      
      if(isValid(val))
         arrScore[i] = val;
      else
      {
         cout<<"Value must be one or greater: ";
         goto in;
      }  
   }
   
   //sorting array
   cout<<"The numbers in set are:"<<endl;
   sort(arrScore, arrScore+size);
   
   getArray(arrScore, size);
   
   //calling and displaying average score
   cout<<"Average Score: "<<getAverage(arrScore, size);

   return 0;
}