package com.smilart.algo4;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Job implements Comparable<Job> {
	int w;
	int l;
	double k;

	public Job(int w, int l){
		this.w = w;
		this.l = l;
		k = (double)w/l;
		//k = (double)(w-l);
	}

	@Override
	public int compareTo(Job o) {

		// TODO Auto-generated method stub
		return k < o.k ? 1 : -1;
	//	return k < o.k ? 1 : k > o.k ? -1 : w < o.w ? 1 : -1;
	}

	public static void main(String [] args){
		Job j1 = new Job(2, 3);
		Job j2 = new Job(1, 3);
		Job j3 = new Job(7, 3);
		List<Job> list = new ArrayList<Job>();
		list.add(j1);
		list.add(j2);
		list.add(j3);
		Collections.sort(list);
		for(Job j: list){
			System.out.println(j.w + " " + j.l);
		}
		
	}

}
