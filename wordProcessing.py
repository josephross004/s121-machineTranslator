import re
import itertools

class Sentence:

    def __init__(self,text,language):
        self.language = language
        self.text = text
        self.parsedText = []
    
    def parseText(self, limiter="[^a-zA-Z'\d]"):
        textCopy = self.text
        parsed = re.split(limiter, textCopy)
        for i in reversed(range(len(parsed)-1)):
            if parsed[i] == '':
                parsed.pop(i)
        if parsed[len(parsed)-1]=='':
            parsed.pop(len(parsed)-1)
        self.parsedText = parsed
        return self.parsedText

    def bigrams(self):
        d = {}
        self.parseText()
        for i in range(len(self.parsedText)-1):
            key = self.parsedText[i]+", " +self.parsedText[i+1]
            if key in d.keys():
                d[key]+=1
            else:
                d[key]=1
        return d

    def orders(self):
        self.parseText()
        return(list(itertools.permutations(self.parsedText)))


class Word:

    def __init__(self, word, language):
        self.word = re.sub(r'(?:^[\s]+)|(?:[\s]+$)'.format(chars=re.escape("\s")), '', word)
        self.language=language
