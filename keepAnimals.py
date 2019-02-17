def keepAnimals(words):
    keepAnimals_dic = {}
    for word, count in words.items():
        if word in animal_list:
            keepAnimals_dic[word] = count
    return keepAnimals_dic
print (keepAnimals({"i": 1, "like": 2, "carrots": 1, "rabbit": 1}))
