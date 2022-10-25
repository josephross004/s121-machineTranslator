from numpy import double
import wordProcessing
import re

def generateBigrams(filename="data.txt"):
    d = {}
    s1 = ""
    s2 = ""
    key = ""
    with open (filename, "r", encoding="utf-8") as f:
        for line in f:
            l = wordProcessing.Sentence(line.lower(), "english")
            l.parseText()
            for i in l.parsedText:
                if s1 == "":
                    s1 = i
                    continue
                else:
                    if s2=="":
                        s2 = i
                    else:
                        s1 = s2
                        s2 = i
                    key = s1+", " +s2
                    if key in d.keys():
                        d[key]+=1
                    else:
                        d[key]=1
        return d

def generateUnigrams(filename="data.txt"):
    d = {}
    key = ""
    with open (filename, "r", encoding="utf-8") as f:
        for line in f:
            l = wordProcessing.Sentence(line.lower(), "english")
            l.parseText()
            for i in l.parsedText:
                key = i
                if i in d.keys():
                    d[key]+=1
                else:
                    d[key]=1
        return d

def bigramProbabilityFunction(text, textfile="data.txt"):
    t = wordProcessing.Sentence(text.lower(), "english")
    d = t.bigrams()
    pd = {}
    l = [k for k in d.keys()]
    bd = generateBigrams(textfile)
    ud = generateUnigrams(textfile)
    for bigram in d.keys():
        try:
            s = (((bd[bigram])/(ud[bigram[:bigram.find(",")]])))
            pd[bigram]=s
        except KeyError:
            pd[bigram]=0.01
    outputProb = 1
    for key in pd.keys():
        outputProb *= pd[key]
    return outputProb

def mostLikelySentence(text, textfile="data.txt"):
    t = wordProcessing.Sentence(text.lower(),"english")
    orders = t.orders()
    d = {}
    for txt in orders:
        tx = str(txt)
        tx = re.sub(",","",tx)
        tx = re.sub("\(","",tx)
        tx = re.sub("\)","",tx)
        tx = re.sub("\'","",tx)
        #print(tx + str(float(bigramProbabilityFunction(tx))))
        d[tx] = float(bigramProbabilityFunction(tx))
    max = ""
    mP = 0
    for key in d.keys():
        if d[key] > mP:
            mP = d[key]
            max = key
    return max
#print(generateBigrams())
#print(generateUnigrams())
#print(bigramProbabilityFunction("nothing to do"))
