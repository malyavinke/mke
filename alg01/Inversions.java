package com.smilart.algo;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;



public class Inversions {

    // merge and count
    private static double merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi) {
        double inversions = 0;

        // copy to aux[]
        for (int k = lo; k <= hi; k++) {
            aux[k] = a[k]; 
        }

        // merge back to a[]
        int i = lo, j = mid+1;
        for (int k = lo; k <= hi; k++) {
            if      (i > mid)                a[k] = aux[j++];
            else if (j > hi)                 a[k] = aux[i++];
            else if (less(aux[j], aux[i])) { a[k] = aux[j++]; inversions += (mid - i + 1); }
            else                             a[k] = aux[i++];
        }
        return inversions;
    }

    // return the number of inversions in the subarray b[lo..hi]
    // side effect b[lo..hi] is rearranged in ascending order
    private static double count(Comparable[] a, Comparable[] b, Comparable[] aux, int lo, int hi) {
    	double inversions = 0;
        if (hi <= lo) return 0;
        int mid = lo + (hi - lo) / 2;
        inversions += count(a, b, aux, lo, mid);  
        inversions += count(a, b, aux, mid+1, hi);
        inversions += merge(b, aux, lo, mid, hi);
        assert inversions == brute(a, lo, hi);
        return inversions;
    }


    // count number of inversions in the array a[] - do not overwrite a[]
    public static double count(Comparable[] a) {
        Comparable[] b   = new Comparable[a.length];
        Comparable[] aux = new Comparable[a.length];
        for (int i = 0; i < a.length; i++) b[i] = a[i];
        double inversions = count(a, b, aux, 0, a.length - 1);
        return inversions;
    }


    // is v < w ?
    private static boolean less(Comparable v, Comparable w) {
        return (v.compareTo(w) < 0);
    }

    // count number of inversions in a[lo..hi] via brute force (for debugging only)
    private static double brute(Comparable[] a, int lo, int hi) {
    	double inversions = 0;
        for (int i = lo; i <= hi; i++)
            for (int j = i + 1; j <= hi; j++)
                if (less(a[j], a[i])) inversions++;
        return inversions;
    }


    // count number of inversions via brute force
    public static double brute(Comparable[] a) {
        return brute(a, 0, a.length - 1);
    }




    // generate N real numbers between 0 and 1, and mergesort them
    public static void main(String[] args) throws FileNotFoundException {
    	Scanner sc = new Scanner (new FileInputStream(new File(args[0]))); 
     	List<Integer> list = new ArrayList<Integer>();
    	while(sc.hasNextInt()){
     		list.add(sc.nextInt());
     	}
    	Integer[] a = list.toArray(new Integer[list.size()]);
    	int N = a.length;
        Integer[] b = new Integer[N];
        for (int i = 0; i < N; i++)
            b[i] = a[i];
        DecimalFormat myFormatter = new DecimalFormat("00000000000000000");
        System.out.println(myFormatter.format(Inversions.count(b)));

      //  System.out.println(Inversions.brute(b));
    }
}
