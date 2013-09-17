package com.smilart.algo4;


import java.io.*;
import java.net.URL;
import java.net.URLConnection;
import java.util.*;

class Knapsack
{
   public static void main (String args[]) // entry point from OS
   {
      Scanner scanner = null; 
	   
	   try {
           // first try to read file from local file system
          
		   String s = args[0];
		   File file = new File(s);
           if (file.exists()) {
               scanner = new Scanner(file);
            //   scanner.useLocale(usLocale);
              
           }

       }
       catch (IOException ioe) {
           System.err.println("Could not open file");
       }
	   
	   new MyClass(scanner); 
		

	  // create dynamic entry point
   }
}

class MyClass {

   MyClass (Scanner s)
   {
      Scanner ls;
      int B[][];
      int numItems, maxWeight, w, k;
      int benefit[], weight[];
      int remainingWeight;
      int setNumber = 1;

    //***  Read in the initial numItems, maxWeight pair
      String [] line = s.nextLine().split(" ");
      numItems = Integer.valueOf(line[1]);
      maxWeight = Integer.valueOf(line[0]);
      
      System.out.println(numItems);
      System.out.println(maxWeight);
 
 //   while ( (numItems != 0) && (maxWeight != 0) )
 //   {
      // *** Read in all the data for the items
          benefit = new int [numItems+1];
          weight = new int [numItems+1];
//          ls = new Scanner(s.nextLine());
          
          
          for (k = 1; k <= numItems; k++)
              {  
        	  line = s.nextLine().split(" ");
        	  
        	  benefit [k] = Integer.valueOf(line[0]);
              weight [k] = Integer.valueOf(line[1]);
              }

      // *** initialize
          B = new int [numItems+1][maxWeight+1]; 
          for (w = 0; w <= maxWeight; w++) 
                    B[0][w] = 0; 

      // *** Now do the work!
          for (k = 1; k <= numItems; k++)
              {
                  for (w = maxWeight; w >= weight[k]; w--)
                      if (benefit[k] + B[k-1][w-weight[k]] > B[k-1][w])
                         B[k][w] = benefit[k] + B[k-1][w-weight[k]];
                      else
                         B[k][w] = B[k-1][w];
                  for (w = 0; w < weight[k]; w++)
                         B[k][w] = B[k-1][w];
              }

      // *** Print out the results.   
          System.out.println("Set #" + setNumber);
          System.out.println("Max benefit = " + B[numItems][maxWeight]);
          System.out.print("Items used:");
          for (k = numItems, remainingWeight=maxWeight; k > 0; k--)
              {
                if (remainingWeight >= weight[k])
                   if ( B[k][remainingWeight] == (benefit[k] + B[k-1][remainingWeight - weight[k]]) )
                    {
                       System.out.print("  " + k);
                       remainingWeight -= weight[k];
                    }
              }
              System.out.println();
              System.out.println();
              setNumber++;

 /*     // ***  Read in the next numItems, maxWeight pair
      ls = new Scanner(s.nextLine());
      numItems = ls.nextInt();
      maxWeight = ls.nextInt();
   }  */
 
 }

}  //**  end of the "MyClass" class