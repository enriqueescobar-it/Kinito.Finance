from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk


class NltkManager(object):

    def __init__(self, a_txt: str = 'I am not a sentimental person but I believe in the utility of sentiment analysis'):
        self.__tokenize(a_txt)
        self.__setLemma()
        self.__setStemming(a_txt)
        self.__setStopWords()

    def __tokenize(self, a_txt: str = ''):
        self.Tokens = word_tokenize(a_txt)
        print(self.Tokens)

    def __setLemma(self):
        lemmatizer = WordNetLemmatizer()
        self.Lemmas = [lemmatizer.lemmatize(word) for word in self.Tokens]
        print(self.Lemmas)

    def __setStemming(self, a_txt: str = ''):
        tokens_lc = word_tokenize(a_txt.lower())
        porterStemmer = PorterStemmer()
        self.TokensLowerCaseStem = [porterStemmer.stem(word) for word in tokens_lc]
        print(self.TokensLowerCaseStem)

    def __setStopWords(self):
        stopwords = nltk.corpus.stopwords.words('english')
        print(stopwords)
        self.TokensWithoutStopWords = [j for j in self.Tokens if j not in stopwords]
