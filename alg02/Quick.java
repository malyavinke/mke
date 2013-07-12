package com.smilart.algo;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Quick {

	public double count = 0;

	// quicksort the array
	public  void sort(Comparable[] a) {
		sort1(a, 0, a.length - 1);
	}

	// quicksort the subarray from a[lo] to a[hi]
	private  void sort1(Comparable[] a, int lo, int hi) { 
		if (hi <= lo) return;
		int j = partition1(a, lo, hi);
		if (j > lo)
			sort1(a, lo, j-1);
		if (j < hi)
			sort1(a, j+1, hi);
		//        assert isSorted(a, lo, hi);
	}

	private  void sort2(Comparable[] a, int lo, int hi) { 
		if (hi <= lo) return;
		exch(a, lo, hi);
		int j = partition1(a, lo, hi);
		if (j > lo)
			sort2(a, lo, j-1);
		if (j < hi)
			sort2(a, j+1, hi);
		//        assert isSorted(a, lo, hi);
	}
	
	
	private  void sort3(Comparable[] a, int lo, int hi) { 
		if (hi <= lo) return;
		exch(a, lo, median(a, lo, hi) );
		int j = partition1(a, lo, hi);
		if (j > lo)
			sort3(a, lo, j-1);
		if (j < hi)
			sort3(a, j+1, hi);
		//        assert isSorted(a, lo, hi);
	}
	
	// partition the subarray a[lo .. hi] by returning an index j
	// so that a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
	private  int partition1(Comparable[] a, int lo, int hi) {
		int i = lo + 1;
		int j = i;
		for (; j <= hi; j++){
			if (less(a[j],  a[lo])){
				exch(a, j, i);
				i++;
			}
		}

		exch(a, lo, i -1 );
		count += hi-lo;
		return i -1;
	}


	// partition the subarray a[lo .. hi] by returning an index j
	// so that a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
	private  int partition(Comparable[] a, int lo, int hi) {
		int i = lo;
		int j = hi + 1;
		Comparable v = a[lo];
		while (true) { 

			// find item on lo to swap
			while (less(a[++i], v))
				if (i == hi) break;

			// find item on hi to swap
			while (less(v, a[--j]))
				if (j == lo) break;      // redundant since a[lo] acts as sentinel

			// check if pointers cross
			if (i >= j) break;

			exch(a, i, j);
		}

		// put v = a[j] into position
		exch(a, lo, j);

		// with a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
		return j;
	}

	/***********************************************************************
	 *  Helper sorting functions
	 ***********************************************************************/

	// is v < w ?
	private  boolean less(Comparable v, Comparable w) {
		return (v.compareTo(w) < 0);
	}

	// exchange a[i] and a[j]
	private static void exch(Object[] a, int i, int j) {
		Object swap = a[i];
		a[i] = a[j];
		a[j] = swap;
	}
	
	private int median(Comparable[] a, int lo, int hi){
		
		int med = (lo + hi) / 2;
		if ((less(a[lo], a[med]) && less(a[med], a[hi])) ||(less(a[hi], a[med]) && less(a[med], a[lo])))  return med;
		if ((less(a[lo], a[hi]) && less(a[hi], a[med])) ||(less(a[med], a[hi]) && less(a[hi], a[lo])))  return hi;
		return lo;
	}


	/***********************************************************************
	 *  Check if array is sorted - useful for debugging
	 ***********************************************************************/
	/*	private static boolean isSorted(Comparable[] a) {
		return isSorted(a, 0, a.length - 1);
	}

	private static boolean isSorted(Comparable[] a, int lo, int hi) {
		for (int i = lo + 1; i <= hi; i++)
			if (less(a[i], a[i-1])) return false;
		return true;
	}*/


	// print array to standard output
	private  void show(Comparable[] a) {
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i] + " ");
		}
		System.out.println();
	}
	// Read strings from standard input, sort them, and print.
	public static void main(String[] args) throws FileNotFoundException {
		Scanner sc = new Scanner (new FileInputStream(new File(args[0]))); 
		List<Integer> list = new ArrayList<Integer>();
		while(sc.hasNextInt()){
			list.add(sc.nextInt());
		}
		Integer[] a = list.toArray(new Integer[list.size()]);
		Quick quick = new Quick();
		int N = a.length;
        Integer[] b = new Integer[N];
        for (int i = 0; i < N; i++)
            b[i] = a[i];
		
		quick.sort1(b, 0, b.length - 1);
		System.out.println(quick.count);
		
		quick.count = 0;
		b = new Integer[N];
        for (int i = 0; i < N; i++)
            b[i] = a[i];
        quick.sort2(b, 0, b.length - 1);
        System.out.println(quick.count);
        
        quick.count = 0;
        b = new Integer[N];
        for (int i = 0; i < N; i++)
            b[i] = a[i];
        quick.sort3(b, 0, b.length - 1); 
		
		System.out.println(quick.count);
		//       show(a);


	}
}
