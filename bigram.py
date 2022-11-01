import wordProcessing
import re
import unidecode 

def generateBigrams(filename="data-en.txt", lang="english"):
    d = {}
    s1 = ""
    s2 = ""
    key = ""
    with open (filename, "r", encoding="utf-8") as f:
        for line in f:
            l = wordProcessing.Sentence(unidecode.unidecode(line).lower(), lang)
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

def generateUnigrams(filename="data-en.txt", lang="english"):
    d = {}
    key = ""
    with open (filename, "r", encoding="utf-8") as f:
        for line in f:
            l = wordProcessing.Sentence(unidecode.unidecode(line).lower(), lang)
            l.parseText()
            for i in l.parsedText:
                key = i
                if i in d.keys():
                    d[key]+=1
                else:
                    d[key]=1
        return d

def bigramProbabilityFunction(text, textfile="data-en.txt", lang="english"):
    t = wordProcessing.Sentence(text.lower(), lang)
    d = t.bigrams()
    pd = {}
    l = [k for k in d.keys()]
    if lang == "english":
        pass
    elif lang == "spanish":
        textfile="data-es.txt"
    bd = generateBigrams(textfile)
    ud = generateUnigrams(textfile)
    for bigram in d.keys():
        try:
            #print(bd[bigram])
            s = (((bd[bigram])/(ud[bigram[:bigram.find(",")]])))
            pd[bigram]=s
        except KeyError:
            pd[bigram]=0.01
    outputProb = 1
    for key in pd.keys():
        outputProb *= pd[key]
    return outputProb

def mostLikelySentence(text, textfile="data-en.txt", lang="english"):
    t = unidecode.unidecode(text)
    t = wordProcessing.Sentence(t.lower(),lang)
    orders = t.orders()
    d = {}
    for txt in orders:
        tx = str(txt)
        tx = re.sub(",","",tx)
        tx = re.sub("\(","",tx)
        tx = re.sub("\)","",tx)
        tx = re.sub("\'","",tx)
        #print(tx + str(float(bigramProbabilityFunction(tx))))
        d[tx] = float(bigramProbabilityFunction(tx, "data-en.txt", lang))
    max = ""
    mP = 0
    for key in d.keys():
        if d[key] > mP:
            mP = d[key]
            max = key
    return max
#print(generateBigrams())
#print(generateUnigrams())
print(mostLikelySentence("el rojo tomate", "data-en.txt", "spanish"))
