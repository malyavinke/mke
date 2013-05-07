import sys
import json
import re
import collections
import itertools
#from sets import Set

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

def load_states():
    states = {}
    list = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    for abbr in list:
        states[abbr] = 0
    return states

def count_hash_tags(tweet, states, sent_dict):
    place = tweet["place"]
    if not place:
        return
    if place['country_code'] == 'US':
        abbr = place['full_name'].split(',')[1].strip()
        if abbr in states:
            states[abbr] = states[abbr] + tweet_sentiment(tweet, sent_dict)
    return

def main():

    sent_dict = load_sent_dict()
    tweet_file = open(sys.argv[2])
    states = load_states()
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in line:
            count_hash_tags(tweet, states, sent_dict)
    d = collections.OrderedDict(sorted(states.items(), key=lambda t: t[1], reverse=True))
    x = itertools.islice(d.items(), 0, 1)

    for key, value in x:
        print key
    tweet_file.close()		

if __name__ == '__main__':
    main()
