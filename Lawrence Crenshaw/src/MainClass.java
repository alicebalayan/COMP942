
public class MainClass {

    /* Main Class */
	 public static void main(String args[]) 
	    { 
	        int array[] = { 200, 15, 0, 77, 200,6 }; 
	  
	        Sort insert = new Sort(); 
	        insert.sort(array);   
	        print(array); 
	    } 
	 
	    /* Prints Out Order */
	    static void print(int array[]) 
	    {
	    	System.out.print("Result: " );
	        int n = array.length; 
	        for (int i = 0; i < n; ++i) 
	            System.out.print(+array[i] + " ,");   
	        System.out.println(); 
	    } 
	}
