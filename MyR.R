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

consumerSecret <- "l2mKh1xGOmvekBsyMsRBVjVbjNXhege8Dd01aW4sdRyT0qLbFK"
consumerKey <- "bJBT4eSkrSY1bZXEmo7oYSNIb"
accessToken <- "1178640755533008896-mqMaQBobGSBklCnVciUZRI1pluWiKj"
accessTokenSecret <- "s0OSjLXhAR6muJW3AL2y1WD9uzFt1YdSjoWBHaVW2BUhr"

setup_twitter_oauth(consumerKey,
 consumerSecret,
 accessToken,
 accessTokenSecret)

searchTwitter('word', since='2011-03-01', until='2011-03-02')
