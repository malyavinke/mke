import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sent_dict = {}
    for line in sent_file:
        name, score = line.split('\t')
	sent_dict[name] = int(score)
    print len(sent_dict)
    
    
    for line in tweet_file:
	tweet = json.loads(line)
	
        if 'text' in line:
    	    total = 0
            for word in re.findall(r"\b[a-zA-Z]+\b",tweet['text']):
                word = word.lower()
#                print word
                if  word in sent_dict:
#		    print 'asdsaadadaadadadadadadadad'
#            	    print sent_dict[word]
            	    total = total + sent_dict[word]
            	    
	    print total
    
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
