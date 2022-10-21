import wordProcessing

def generateBigrams(filename="data.txt"):
    d = {}
    s1 = ""
    s2 = ""
    key = ""
    with open (filename, "r", encoding="utf-8") as f:
        for line in f:
            l = wordProcessing.Sentence(line, "english")
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
            l = wordProcessing.Sentence(line, "english")
            l.parseText()
            for i in l.parsedText:
                key = i
                if i in d.keys():
                    d[key]+=1
                else:
                    d[key]=1
        return d

def bigramProbabilityFunction(text, filename="bigrammodel.txt", textfile="data.txt"):
    t = wordProcessing.Sentence(text, "english")
    d = t.bigrams()
    pd = {}
    l = [k for k in d.keys()]
    bd = generateBigrams(textfile)
    ud = generateUnigrams(textfile)
    for bigram in d.keys():
        try:
            u = ud[bigram[:bigram.find(",")-1]]
            pd[bigram]=bd[bigram]/ud[bigram[:bigram.find(",")-1]]
        except KeyError:
            pd[bigram]=0

    return pd

print(generateBigrams())
print(generateUnigrams())
print(bigramProbabilityFunction("I have nothing to do"))
