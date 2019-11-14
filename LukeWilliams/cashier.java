package lazy;
import java.util.*; 
import java.io.*;
import java.math.*;
import java.text.DecimalFormat;

class algorithms 
{
	//stores the running total so each iteration of the coin operation
	//function can read it
	public double globalTotal;
	//function that recieves a coin value: penny, quarter, etc, total change value,
	//and returns number of coins to give that change amount
	public int coinOperation (double coinValue, double total)
	{
		
		double tally = total;
		int coinAmount = 0;
		/* The loop condition checks the current state of tally, which is a checker to make 
		 * sure we don't use too many coins. It subtracts any coin value from the tally
		 * and compares it to 0. If it is greater than or equal to 0, it 
		 * continues actually does the operation on tally. Tally tells us 
		 * if we should subtract more from the total ahead of time. 
		 * The loop then continues until
		 * we reach a subtraction of the coin value where tally is negative.
		 * When that happens it will stop the loop and hold the total where it was
		 * in the prior operation. Each time a valid operation is done
		 * on total we add 1 to the coin amount counter.
		 * 
		 */
		while (tally - coinValue >= 0) 
		{
			tally = tally - coinValue;
			if (tally >= 0)
			{
				total = total - coinValue;
				coinAmount = coinAmount + 1;
				System.out.println(total);
			}
		}
		globalTotal = total;
		return coinAmount;
	}
	
	public void cashier (double total)
	{
		
		int qNum = coinOperation(.25, total);
		int dNum = coinOperation(.1, globalTotal);
		int nNum = coinOperation(.05, globalTotal);
		int pNum = coinOperation(.01, globalTotal);
										
		//System.out.println("Total is now: " + total);
		System.out.println("Number of quarters used: " + qNum);			
		System.out.println("Number of dimes used: " + dNum);
		System.out.println("Number of nickels used: " + nNum);			
		System.out.println("Number of pennies used: " + pNum);
	}	
}



public class Main {
	
	public static void main(String[] args) throws IOException
	{	
		Scanner keyboard = new Scanner(System.in);
		algorithms demo = new algorithms();		
		System.out.print("Enter dollar amount\n");
		double input = keyboard.nextDouble();
		demo.cashier(input);		
		keyboard.close();		
						
	}

}

//lw
