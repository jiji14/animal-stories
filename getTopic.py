## getTopic

def getTopic(text):
    
    getTopic_1 = countWords(text)
    getTopic_2 = keepAnimals(getTopic_1)
    getTopic_3 = getImportantAnimals(getTopic_2)

    return getTopic_3

print (getTopic("""On a hot summer day, a fox comes upon an orchard and sees a bunch of ripened grapes. 
It thinks: “Just what I need to quench my thirst.” It moves back a few paces, runs, and jumps but falls short of reaching the grapes. 
It tries in different ways to reach the bunch of grapes, but in vain. It finally gives up, and says to himself “I am sure they are sour anyway."""))

print (getTopic("""This is another interesting animal story for kids that brings a valuable moral lesson to motivate them. Enjoy it now! 
One day, a strong and powerful hound was chasing a hare. After running for a long time, the tired hound gives up the hunt. 
A herd of goats watching this mocks the hound, saying that the little one is better than the beast. 
To this, the hound responds: “The rabbit was running for its life, I was only running for dinner. That is the difference between us"""))
