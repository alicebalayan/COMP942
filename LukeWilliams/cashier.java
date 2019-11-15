package lazy;
import java.util.*; 
import java.io.*;

class algorithms 
{
	//value passed between iterations of coin operation function
	public double globalTotal;
	
	/* 
	 *Tally is a test value for total. A coin value is subtracted from the tally
	 * and compares it to 0. If that operation causes tally to be >= 0, it 
	 * does the operation on total. The loop then continues until
	 * it reaches a subtraction of the coin value where tally is negative.
	 * When that happens it will stop the loop and hold the total where it was
	 * in the prior operation. Each time a valid operation is done
	 * on total we add 1 to the coin amount counter. 
	 */
	
	public int coinOperation (double coinValue, double total)
	{		
		double tally = total;
		int coinAmount = 0;
		
		while (tally - coinValue >= 0) 
		{
			tally = tally - coinValue;
			tally = Math.round(tally * 100.0)/100.0;
			if (tally >= 0)
			{
				total = tally;
				coinAmount = coinAmount + 1;
			}
		}
		globalTotal = total;
		return coinAmount;
	}
	
	public void cashier (double total)
	{		
		/* Calling coinOperation method for each denomination. This must be done in order
		 * from greatest to least
		*/
		int qNum = coinOperation(.25, total);
		int dNum = coinOperation(.1, globalTotal);
		int nNum = coinOperation(.05, globalTotal);
		int pNum = coinOperation(.01, globalTotal);

		System.out.println("Number of quarters used: " + qNum);			
		System.out.println("Number of dimes used: " + dNum);
		System.out.println("Number of nickels used: " + nNum);			
		System.out.println("Number of pennies used: " + pNum);
	}	
}

public class Main 
{	
	public static void main(String[] args) throws IOException
	{	
		Scanner keyboard = new Scanner(System.in);
		algorithms demo = new algorithms();		
		System.out.println("This is a demonstration of the Cashier Algorithm \nEnter a dollar/cents amount");
		System.out.print("$ ");
		double input = keyboard.nextDouble();
		demo.cashier(input);		
		keyboard.close();								
	}
}
