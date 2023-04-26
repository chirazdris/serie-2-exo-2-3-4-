def factors(word):
    factors_list = []
    for i in range(1, len(word)):
        if len(word) % i == 0:
            factors_list.append(word[:i])
    factors_list.append(word)  
    return factors_list

resultat = factors("aaabbbccc")
print(resultat)
