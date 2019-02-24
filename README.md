# animal-stories

# detect if a word is an animal

animal_list = ["hare", "rabbit", "tortoise", "goat", "hound", "duck", "ducking", "fox", "lion", "boar", "ant", "grasshopper", 
                "cat", "monkey", "dog", "mouse", "crow", "eagle", "wolf", "peacock"]

def isAnimal(value):
    if value in animal_list:
        return True    
    else:
        return False
        
isAnimal("hare")
isAnimal("carrot") 
isAnimal("rabbit")


