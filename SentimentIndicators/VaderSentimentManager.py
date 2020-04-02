from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


class VaderSentimentManager(object):

    def __init__(self, a_txt='I am not a sentimental person but I believe in the utility of sentiment analysis'):
        analyser = SentimentIntensityAnalyzer()
        analyser.polarity_scores("This is a good course")
        analyser.polarity_scores("This is an awesome course") # degree modifier
        analyser.polarity_scores("The instructor is so cool")
        analyser.polarity_scores("The instructor is so cool!!") # exclaimataion changes score
        analyser.polarity_scores("The instructor is so COOL!!") # Capitalization changes score
        analyser.polarity_scores("Machine learning makes me :)") #emoticons
        analyser.polarity_scores("His antics had me ROFL")
        analyser.polarity_scores("The movie SUX") #Slangs
        TextBlob("His").sentiment()
        TextBlob("remarkable").sentiment()
        TextBlob("work").sentiment()
        TextBlob("ethic").sentiment()
        TextBlob("impressed").sentiment()
        TextBlob("me").sentiment()
        TextBlob("His remarkable work ethic impressed me").sentiment()
