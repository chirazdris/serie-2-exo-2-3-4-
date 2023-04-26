def shuffle(w1, w2):
    result = ""
    for i in range(max(len(w1), len(w2))):
        if i < len(w1):
            result += w1[i]
        if i < len(w2):
            result += w2[i]
    return result

resultat = shuffle("aaa", "bbb")
print(resultat) 
