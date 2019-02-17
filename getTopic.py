# getTopic

def getTopic(text):

    animal_list = ["hare", "rabbit", "tortoise", "goat", "hound", "duck", "ducking", "fox", "lion", "boar", "ant", "grasshopper", 
                "cat", "monkey", "dog", "mouse", "crow", "eagle", "wolf", "peacock"]
    
    word_list = text.split()
    text_dic = {}
    for word in word_list:
        text_dic[word] = text_dic.get(word, 0) + 1
    
    keepAnimals_dic = {}
    for word, count in text_dic.items():
        if word in animal_list:
            keepAnimals_dic[word] = count
            
    if len(keepAnimals_dic) <= 2:
        animal_list =list(keepAnimals_dic.keys())
        return animal_list
    else:   
        animal_list = list()
        for animals in range(2):
            maxdata = max(keepAnimals_dic, key=keepAnimals_dic.get)
            animal_list.append(maxdata)
        return animal_list
       
print (getTopic("On a hot summer day, a fox comes upon an orchard and sees a bunch of ripened grapes. It thinks: “Just what I need to quench my thirst.” It moves back a few paces, runs, and jumps but falls short of reaching the grapes. It tries in different ways to reach the bunch of grapes, but in vain. It finally gives up, and says to himself “I am sure they are sour anyway."))
