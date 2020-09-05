import urllib.request
import re

class corpusReader:
    T = {",", ".", ":", "\n", "#", "(", ")", "!", "?", "\'", "\"", " "}
    letters = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, url):
        self.data = self.__readFile(url)
        self.N = self.__countCorpusSize()

    def __readFile(self, url):
        with urllib.request.urlopen(url) as response:
            text = response.read().decode('ascii', errors='ignore')
        data = str(text.lower())
        data = self.__cleanTxt(data)
        # no need to close urlib it's closing automaticly on the return command
        return data

    def __cleanTxt(self, data):
        new = ""
        for char in data:
            if char in self.T or char in self.letters:
                new += char
        return new

     # returns the corpus size without spaces
    def __countCorpusSize(self):
        lst = self.data.split()
        return len(lst)

    def __repr__(self):
        return self.data


class LanguageModel:

    def __init__(self, corpus):
        self.corpus = corpus #corpus type is corpusReader()
        self.N = corpus.N
        self.unigramMLE = self.__getUnigramMLE()
        self.bigramMLE = self.__getBigramMLE()
        self.unigramLaplace = self.__getUnigramLaplace()
        self.bigramLaplace = self.__getBigramLaplace()

    #generating a unigram that counts the appearances of each letter
    def __getUnigramCount(self):
        unigram = dict()
        T = self.corpus.T
        let = self.corpus.letters
        for letter in let:
            T.add(letter)
        for sign in T:
            unigram[sign] = 0
        for c in self.corpus.data: #going over the corpus
            if c != " ":
                unigram[c] = unigram[c] + 1

        return unigram

    #for each character in the corpus we add the probability
    def __getUnigramMLE(self):
        N = self.corpus.N
        if N == 0: #if corpus size is 0 then something is wrong
            print("invalid corpus size")
            return;
        unigCount = self.__getUnigramCount()
        unigProb = dict()
        for elem in unigCount:
            unigProb[elem] = ((unigCount[elem])/N)
        return unigProb

    #
    def __getUnigramLaplace(self):
        N = self.corpus.N
        if N == 0:  # if corpus size is 0 then something is wrong
            print("invalid corpus size")
            return;
        unigCount = self.__getUnigramCount()
        V = len(unigCount)
        unigProb = dict()
        for elem in unigCount:
            unigProb[elem] = ((unigCount[elem]) + 1 / N + V)

        return unigProb

    #generating a bigram that counts the appearances of pairs of letters
    def __getBigramCount(self):
        bigram = dict()
        corpus= self.corpus.data
        allcomb = self.__generateAllCombinations()
        for elem in allcomb:
            bigram[elem] = 0
        for i in range(1, len(corpus)-1):
            bigram[str(corpus[i-1])+str(corpus[i])] += 1

        return bigram

    def __getBigramMLE(self):
        N = self.corpus.N
        if N == 0:  # if corpus size is 0 then something is wrong
            print("invalid corpus size")
            return;
        bigCount = self.__getBigramCount()
        bigProb = dict()
        for elem in bigCount:
            bigProb[elem] = ((bigCount[elem]) / N)

        return bigProb

    def __generateAllCombinations(self):
        T=self.corpus.T
        let = self.corpus.letters
        for letter in let:
            T.add(letter)
        #T contains all signs
        T = list(T)
        n = len(T)
        #making all xy strings such as x,y in T
        allcomb=[]
        for i in range(n):
            for j in range(n):
                allcomb.append(str(T[i])+str(T[j]))

        return allcomb

    def __getBigramLaplace(self):
        N = self.corpus.N
        bigCount = self.__getBigramCount()
        V = len(bigCount)
        bigLaplace = dict()
        for c in bigCount:
            bigLaplace[c] = ((bigCount[c] + 1)/ (N + V))

        return bigLaplace
