import tweepy
from textblob import TextBlob
import nltk
nltk.download('punkt')

def tweetAnalysis(symbol,name):
    user_key="uLCKU6myhzi58R8X7GHlAk2VM"
    user_secret="tS9xKXmtWDNSCW2ri6cqTOtrifUZeqMKJu5jm06cxy24XF8vbG"


    access_token="106322211-dLt4z8tq9oVtx5etpIYANHJuC3I5ymT1W80wgh2b"
    access_token_secret="e9oPkfdyApMhyMyaD088C4cG9xi1nEhYriGfSWzrRCuq1"


    authentication=tweepy.OAuthHandler(user_key,user_secret)
    authentication.set_access_token(access_token,access_token_secret)

    myAPI=tweepy.API(authentication)

    symbolTweets=myAPI.search(symbol, count=100)

    positivity=0
    opinion=0
    finalfactor=0
    noOftweets=0
    key_words=0
    for st in symbolTweets:
        noOftweets+=1
        print(" ST Tweet is:",st.text)
        text=TextBlob(st.text)
        words=text.words
        factor = TextBlob(st.text).sentiment
        for w in words:
            if factor.polarity>0 and (w=="buy" or w=="invest"):
                key_words+=1

    opinion+=factor.subjectivity
    positivity+=factor.polarity
    if noOftweets!=0:
        if key_words!=0:
            finalfactor=(((opinion/8)/noOftweets)*(2*positivity/noOftweets))+(key_words/noOftweets)
        else:
            finalfactor = (opinion / noOftweets) * (positivity / noOftweets)
    print ("Final factor",finalfactor)
    positivity = 0
    opinion = 0
    finalfactor = 0
    noOftweets = 0
    key_words = 0
    for st in symbolTweets:
        noOftweets += 1
        print(" ST Tweet is:", st.text)
        text = TextBlob(st.text)
        words = text.words
        factor = TextBlob(st.text).sentiment
        for w in words:
            if factor.polarity > 0 and (w == "buy" or w == "invest"):
                key_words += 1

    opinion += factor.subjectivity
    positivity += factor.polarity
    if noOftweets != 0:
        if key_words != 0:
            finalfactor = (((opinion / 8) / noOftweets) * (2 * positivity / noOftweets)) + (key_words / noOftweets)
        else:
            finalfactor = (opinion / noOftweets) * (positivity / noOftweets)
    print("Final factor1", finalfactor)

    positivity = 0
    opinion = 0
    finalfactor1 = 0
    noOftweets = 0
    key_words = 0
    name=name.lower().replace("inc", "").replace("," ,"").replace(".","").strip()
    print("Name is",name)
    companyTweets=myAPI.search(name,count=100)
    for st in companyTweets:
        noOftweets += 1
        print(" ST Tweet is:", st.text)
        text = TextBlob(st.text)
        words = text.words
        factor = TextBlob(st.text).sentiment
        for w in words:
            if factor.polarity > 0 and (w == "buy" or w == "invest"):
                key_words += 1

    opinion += factor.subjectivity
    positivity += factor.polarity
    if noOftweets != 0:
        if key_words != 0:
            finalfactor1 = (((opinion / 8) / noOftweets) * (2 * positivity / noOftweets)) + (key_words / noOftweets)
        else:
            finalfactor1 = (opinion / noOftweets) * (positivity / noOftweets)
    print("Final factor2", finalfactor1)
    print ("FInally",((finalfactor+finalfactor1)/2))
    return ((finalfactor+finalfactor1)/2)

tweetAnalysis("GOOGL","GOOGLE inc")
