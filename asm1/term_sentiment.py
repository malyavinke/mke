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

def tweet_sentiment(tweet, sent_dict, term_dict):
    total = 0
    new_words = {}
#    words = re.findall(r"\b[a-zA-Z]+\b",tweet['text'])
    ascii_str = tweet['text']
    try:
        ascii_str = ascii_str.decode('ascii')
    except:
        return 

    words = ascii_str.split()

    for word in words:
        low_word = word.lower()
        if  low_word in sent_dict:
            total = total + sent_dict[low_word]
        else:
            if word in new_words:
                new_words[word] = new_words[word] + 1
            else:
                new_words[word] = 1

    for term in new_words:
        entry = [0,0]
        if term in term_dict:
            entry = term_dict[term]

        if total >= 0:
            entry[0] = entry[0] + 1
        if total < 0:
            entry[1] = entry[1] + 1
        term_dict[term] = entry

def main():
    sent_dict = load_sent_dict()
    tweet_file = open(sys.argv[2])
    term_dict = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in line:
            tweet_sentiment(tweet, sent_dict, term_dict)

    for term in term_dict:
        sentiment = term_dict[term]
        if sentiment[1] > 1:
            print term, (float)(sentiment[0])/sentiment[1]
        else:
            print term, float(sentiment[0])

    tweet_file.close()		

if __name__ == '__main__':
    main()
