import sys
import json
import re
import collections
import itertools

def count_hash_tags(tweet, tags_dict):
    tags = tweet["entities"]["hashtags"]
    for dt in tags:
        tag = dt['text']
        count = 1
        if  tag in tags_dict:
            count = tags_dict[tag] + 1
        tags_dict[tag] = count


def main():
    tweet_file = open(sys.argv[1])
    tags_dict = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in line:
            count_hash_tags(tweet, tags_dict)
    d = collections.OrderedDict(sorted(tags_dict.items(), key=lambda t: t[1], reverse=True))
    x = itertools.islice(d.items(), 0, 10)

    for key, value in x:
        print key, float(value)
    tweet_file.close()		

if __name__ == '__main__':
    main()
