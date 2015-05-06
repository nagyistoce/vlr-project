from __future__ import absolute_import, print_function

from tweepy import OAuthHandler
import json
import tweepy

consumer_key="uT183BEs2QfZFZxAbQ3bKrBO0"
consumer_secret="TQVqtAzkxNf9RtFbSKOngs9iUcOFTB8ebMWQnBRqJP3HP6UpOA"

access_token="31341259-bzwZny7Mo99JR28S4iSArDwZEpKRURaAvRXGm7I60"
access_token_secret="0NJOMzZU9bUvcoWY3hpCg811u5zZz4Z6HG7Yt4SiigwIx"

max_cnt = 100
max_pages = 15
terms = ["hockey","basketball","soccer","football","tennis","cricket","baseball"]

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    for term in terms:
        print("Fetching tweets for #" + term)
        f = open(term + '_12470504.txt', 'w')
        f.write("Tags\tImage\n\n")
        api = tweepy.API(auth)
        page_count = 0  
        for tweets in tweepy.Cursor(api.search, q="#" + term,lang="en", count=max_cnt,
                        result_type="recent", include_entities=True).pages():  
            page_count += 1  
            results = tweets
            for result in results:
                tag_str = []
                for tag in result.entities['hashtags']:
                    tag_str.append(tag['text'].encode('utf-8'))
                try: 
                    url_str = []
                    for m in result.entities['media']:
                        url_str.append(m['media_url'])
                    f.write(','.join(tag_str) + "\t")
                    f.write(','.join(url_str) + "\n");
                except KeyError:
                    pass
            if page_count > max_pages:
                    break
        f.close()