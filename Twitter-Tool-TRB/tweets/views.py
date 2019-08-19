# from django.shortcuts import render
# from django.http import http 
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import datetime
from datetime import timedelta
import pandas_highcharts
from pandas_highcharts.core import serialize
from django.contrib.auth.models import User
import datetime
import tweepy
import enchant
import string

d = enchant.Dict("en_US")

def tweets(request):

    ckey = 'RGcLF8pLxIRcA7rdmvKAEUErF'
    csecret = 'xcwAHvO5LmHYrFFtdrBKpbJA5jFY34DL8oMkCbfr7DHiQjGaRw'
    atoken = '1002463391557005312-EeaXyNEJpDH7lqlCznFsC97FkNNAfS'
    asecret = 'M9JD9zlOaXboGaobJORNMJr4jLzdkIVAbQNSMYfcz4UEm'

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)

    import datetime
    tweetsdata = {}
    if request.POST:
        username = request.POST.get('username')
        datestamp = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        tweetsdata = {}
        index = 0
        for x in tweepy.Cursor(api.user_timeline, id = username, tweet_mode='extended').items():
            if len(tweetsdata) == 5:
                break
            else:
                tweetsdata[index] = {}
                tweetsdata[index]['tweet_date'] = x._json['created_at']
                tweetsdata[index]['screen_name'] = x._json['user']['screen_name']
                tweetsdata[index]['id_str'] = x._json['user']['id_str']
                tweetsdata[index]['tweet'] = x._json['full_text']
                index = index + 1

        for i in tweetsdata:
            counter = 0 
            text = tweetsdata[i]['tweet'].split(' ')
            text = [''.join(c for c in s if c not in string.punctuation) for s in text]
            for e in text:
                if d.check(e) == True:
                    counter += 1
                else:
                    pass
            tweetsdata[i]['num_in_dict'] = counter

        df = pd.DataFrame(tweetsdata)

        tweetsdata = df.T.to_dict(orient='records')



    
    return render(request, 'tweets/tweets.html', {'tweets': tweetsdata})
