from nltk.corpus import brown

with open ("data.txt","w", encoding="utf-8") as f:
    f.write(" ".join(brown.words()))
    f.close()

