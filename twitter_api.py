# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:24:33 2018

@author: Juan Monsalve
"""

from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
import time
from tweepy import Stream
import csv
import json

consumer_key = "VnFkZkh3ur4qwU2jnSJpGbYaw"
consumer_secret = "UDF3ckidRp3O17t0QSvu4vfm7lguIHIEm7f1MCmFaKNH3yrEJo"
access_token = "1053099331606200320-7uygGUxljAZDYZGTjB2EtAI8ovEQ5U"
access_token_secret = "jhYd0mKsAzjpK4wfZSNROICrhN7pDTB0ThBdnC5pv4sS7"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)


class SListener(StreamListener):
    def __init__(self, api = None):
        self.output = open('tweets_%s.json' %
                           time.strftime('%Y%m%d-%H%M%S'), 'w')
        self.api = api or API()
  

########## Obtener una muestra   ##################
        
#listen = SListener(api)
#stream = Stream(auth, listen)
#stream.sample()


###################################################
        
        
        
        

########## Obtener datos con filtro ################
        
#track_words = ['#python']
#listen = SListener(api)
#
#stream = Stream(auth, listen)
#
#stream.filter(track = track_words)  

#####################################################
        



######## Obtener una muestra con el API Search #########
        
#todo
#Cerrar el archivo abierto
#
#results = api.search('#fracking', count=100)
#
#csvfile = open('my_scraped_tweets.csv','w')
#
#csvwriter = csv.writer(csvfile)
#
#for item in results:
#	# write out the user, the tweet and their follower count into a file
#	# the unicode bits are required to write non ASCII language bits into the file
#	csvwriter.writerow([(item.user.screen_name).encode("utf-8"),(item.text).encode("utf-8"),item.user.followers_count])
#	# time.sleep(1)

#######################################################
        
####### Tweepy status to JSON#################################

results = api.search('medellin', count=100)
json_strings = [json.dumps(json_obj._json) for json_obj in results]




###############################################################

            