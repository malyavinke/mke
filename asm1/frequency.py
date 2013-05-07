import sys
import json
import re

def coun_tweet_words(tweet, term_dict):
    total = 0
    words = re.split("[^A-Za-z,]", tweet['text'])
    for word in words:
        word = word.decode("utf-8")
        word.strip()
        if not word:
            break
        
#        word = word.lower()
        count = 1
        if  word in term_dict:
            count = term_dict[word] + 1
        term_dict[word] = count
        total = total + 1
    return total

def main():
    tweet_file = open(sys.argv[1])
    total = 0
    term_dict = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in line:
            total = total + coun_tweet_words(tweet, term_dict)
    for term in term_dict:
        print term, float(term_dict[term])/total

    tweet_file.close()		

if __name__ == '__main__':
    main()
