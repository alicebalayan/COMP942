/*Bubble Sort Algorithm 

It is the most common sorting algorithm used in computer science. 
Useful when you need to sort values in specific order fast. 

Time complexity: O(n)

Date          Name              Version
11/1/2019     Alice Balayan     JS
*/

const arr = [87, 56, 99, 18, 20, 31]; //declare array with values OR ask for user input and pass the values to the function 
function bubbleSort (arr) {
  let swapVars; //use let instead of var to avoid undefined error in js
     do {
      swapVars = false; 
      for (var i = 0; i < arr.length; i++) { //iterate through an array
      if(arr[i] && arr[i + 1] && arr[i] > arr[i + 1]) {
        //swaps here a,b = b,a
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]; 
        swapVars = true;
  }
   }
     } while(swapVars);
return arr;
}
//display results
console.log("Before bubble sort:", arr.slice());
console.log("After bubble sort:", bubbleSort(arr.slice())); 
