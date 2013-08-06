package com.smilart.algo4;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MedianOfStream {

	private int count;
	public int getCount() {
		return count;
	}


	private long sum;


	private PriorityQueue<Integer> highs, lows;

	public MedianOfStream(int size) {

		highs = new PriorityQueue<Integer>(size, new Comparator<Integer>() {
			@Override
			public int compare(Integer arg0, Integer arg1) {
				return arg0.compareTo(arg1);
			}
		});

		lows = new PriorityQueue<Integer>(size, new Comparator<Integer>() {
			@Override
			public int compare(Integer arg0, Integer arg1) {
				return arg1.compareTo(arg0);
			}
		});
	}

	private int getMedian() {
		/*if (count == 1)
			lows.peek();
		if (lows.size() == highs.size()) {
			return lows.peek();
		} else if (lows.size() < highs.size()) {
			return highs.peek();
		}*/
		return lows.peek();
	}

	private void swap(){
		int h = highs.poll();
		int l = lows.poll();
		highs.add(l);
		lows.add(h);
	}

	public int updateMedian(int n) {
		count++;

		if ((count % 2) > 0){
			lows.add(n);
		}else{
			highs.add(n);	
		}

		if (count > 1){	

			if(highs.peek()<lows.peek()) {
				swap(); // O(log n)
			}
		}
		int med = getMedian();
		sum = sum + med;
		return med; // O(1)
	}

	public long getSum() {
		return sum;
	}


	public static void main(String[] args) {
		In in = new In(args[0]);
		MedianOfStream mfs = new MedianOfStream(6000);
		while(in.hasNextLine()){
			int value = Integer.parseInt(in.readLine());
			int med = mfs.updateMedian(value);

		//	System.out.println(value + " " + med );
		}

		System.out.println(mfs.getSum() % 10000 );

	}
}

