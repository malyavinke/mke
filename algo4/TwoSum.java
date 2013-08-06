package com.smilart.algo4;

import java.util.Hashtable;

public class TwoSum {
	
    public static void main(String[] args) {
    	In in = new In(args[0]);
    	Hashtable<Long, Long> input = new Hashtable<Long, Long>();
    	Hashtable<Integer, Integer> result = new Hashtable<Integer, Integer>();
    	while(in.hasNextLine()){
    		Long value = Long.parseLong(in.readLine());
    		input.put(value, value);
    	}
//    	System.out.println(input.size());
    	for (int i = -10000; i < 10001; i++){
    		for (Long v : input.keySet()){
    			Long add = input.get(new Long(i-v));
    			if(add != null && add != v){
    				result.put(i, i);
    				break;
    			}
    		}
    	}
    	System.out.println(result.size());
    }

}
