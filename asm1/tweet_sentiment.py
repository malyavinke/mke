import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def load_sent_dict():
    sent_file = open(sys.argv[1])
    sent_dict = {}
    for line in sent_file:
        name, score = line.split('\t')
        sent_dict[name] = int(score)
    sent_file.close
    return sent_dict

def tweet_sentiment(tweet, sent_dict):
    total = 0
    for word in re.findall(r"\b[a-zA-Z]+\b",tweet['text']):
        word = word.lower()
        if  word in sent_dict:
            total = total + sent_dict[word]
    return total

def main():
    sent_dict = load_sent_dict()
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in line:
            total = tweet_sentiment(tweet, sent_dict)
            print float(total)

    tweet_file.close()		

if __name__ == '__main__':
    main()
