def index_of_caps(word):
    yy = []
    for i in word:
        if i.isupper():
            word.index.append(i)
    return yy

print(index_of_caps("eDaBiT"))
