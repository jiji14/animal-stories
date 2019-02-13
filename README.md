# animal-stories

# detect if a word is an animal

animal_list = ["hare", "rabbit", "tortoise", "goat", "hound", "duck", "ducking", "fox", "lion", "boar", "ant", "grasshopper", 
                "cat", "monkey", "dog", "mouse", "crow", "eagle", "wolf", "peacock"]

def isAnimal(value):
    if value in animal_list:
        value = True    
    else:
        value = False
        
isAnimal("hare")
isAnimal("carrot") 
isAnimal("rabbit")


# count words

def countWords(text):
    word_list = text.split()
    dic = {}
    for word in word_list:
        dic[word] = dic.get(word, 0) + 1
    
countWords("i like carrots like rabbits")
