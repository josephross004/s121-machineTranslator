import re

class Sentence:

    def __init__(self,text,language):
        self.language = language
        self.text = text
        self.parsedText = []
    
    def parseText(self, limiter="[^a-zA-Z\d]"):
        textCopy = self.text
        parsed = re.split(limiter, textCopy)
        for i in reversed(range(len(parsed)-1)):
            if parsed[i] == '':
                parsed.pop(i)
        if parsed[len(parsed)-1]=='':
            parsed.pop(len(parsed)-1)
        self.parsedText = parsed
        print(self.parsedText)

s = Sentence("english")
s.parseText()