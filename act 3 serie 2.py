def shuffle_symbol(word, c):
    result = ""
    for i in range(len(word)):
        if i > 0:
            result += c
        result += word[i]
    result += c
    return result

resultat = shuffle_symbol("abba", "c")
print(resultat) # affiche "acbcacbc"
