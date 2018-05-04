##skc1v12@soton.ac.uk 
## This code is to find out if there are any string of choice can be found within last N number of tweets

from twython import Twython
from twython import TwythonStreamer



CON_KEY ='***********************************' #Consumer Key (API Key)
CON_SEC ='***********************************' #Consumer secret (API Secret)
Access_Token = '*******-*********************'
Access_Token_Secret = '**********************'


# Primary Method

C = 0

class MyStreamer(TwythonStreamer):
   def on_success(self,data):
      global C
      if 'text' in data:
         C = C + 1
         
         if C>=N: #Amend N to any number
            print ("string is found") #Amend
            self.disconnect()

   def on_error(self, status_code, data):
         print(status_code)
         return()

stream = MyStreamer(CON_KEY,CON_SEC,Access_Token,Access_Token_Secret)
stream.statuses.filter(track ='string of choice') # Amend the string of choice to any text / phrase etc.

#Alternate Method

##client = Twython(CON_KEY,CON_SEC,Access_Token,Access_Token_Secret)
##
##try:
##   q = 'string of choice' # Amend the string of choice to any text / phrase etc.
##   RESULTS = client.search(q ='string of choice',count=N) #Amend N to any number
##   NUM_TWEET = 0
##
##   for tweet in RESULTS['statuses']:
##
##         NUM = (tweet['text'].count(q)) # Find 'keyword' in each instance of tweet
##
##         if NUM > 0: #if 'keyword' is found
##
##              NUM_TWEET = NUM_TWEET+1 #update counter by one (for each instance)
##
##   if NUM_TWEET >= 3: # Conditional statement - if total number of tweets found with 'keyword' is more than three, then execute following
##      print ('string of choice is found!') # Amend the string of choice to any text / phrase etc.
##      #print ('string of choice is found and the number of tweets are: ', NUM_TWEET) # Amend the string of choice to any text / phrase etc.
##   else:
##      print ('Could not find tweet related to string of choice') # Amend the string of choice to any text / phrase etc.
##
##except KeyboardInterrupt:
##   GPIO.cleanup()
