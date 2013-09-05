package com.smilart.algo4;

import java.math.BigInteger;
import java.util.Arrays;

public class SPT {
	public static void main(String[] args) {
		In in = new In(args[0]);

		int N = Integer.parseInt(in.readLine());
		Job[] jobs = new Job[N];
		int i = 0;
		int [] line;
		while( (line = in.readIntsFromLine())!= null){

			jobs[i] = new Job(line[0], line[1] );
			i++;

		}
		Arrays.sort(jobs);

		// print out schedule
		BigInteger sum = BigInteger.valueOf(0);
		BigInteger totalLength = BigInteger.valueOf(0);
		for (int j = 0; j < N; j++){
			totalLength = totalLength.add(BigInteger.valueOf(jobs[j].l));
			
			sum = sum.add(totalLength.multiply(BigInteger.valueOf(jobs[j].w))); 
			
		}
		StdOut.println(sum);
	}
}
