# get most talked about animals

def importantAnimals(keepAnimals_dic):
    if len(keepAnimals_dic) <= 2:
        animal_ls =list(keepAnimals_dic.keys())
        return animal_ls
    else:   
        animal_ls = list()
        for animals in range(2):
            maxdata = max(keepAnimals_dic, key=keepAnimals_dic.get)
            keepAnimals_dic.pop(maxdata)
            animal_ls.append(maxdata)
        return animal_ls

            
print (importantAnimals({"tortoise":2, "rabbit": 5, "goat": 7}))
print (importantAnimals({"tortoise":2}))
