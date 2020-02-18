library(RColorBrewer)
library(wordcloud)
library(tm)
library(twitteR)
library(ROAuth)
library(plyr)
library(stringr)
library(base64enc)

download.file(url="http://curl.haxx.se/ca/cacert.pem",destfile="cacert.pem")

# Set constant requestURL
requestURL <- "https://api.twitter.com/oauth/request_token"
# Set constant accessURL
accessURL <- "https://api.twitter.com/oauth/access_token"
# Set constant authURL
authURL <- "https://api.twitter.com/oauth/authorize"

consumerSecret <- "consumerSecret"
consumerKey <- "consumerKey"
accessToken <- "accesToken"
accessTokenSecret <- "accessTokenSecret"

setup_twitter_oauth(consumerKey,
 consumerSecret,
 accessToken,
 accessTokenSecret)

searchTwitter("TweetsI'mLookingFor", since='2011-03-01', until='2011-03-02')
