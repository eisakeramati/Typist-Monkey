
# coding: utf-8

# In[4]:


#calcScore returns a score that represents how much the 2 strings are alike

def calcScore(string, target):
    score = 0
    for i in range(len(target)):
        if (target[i] == string[i]):
            score = score + 1
        else:
            break
    return score


# The method through which we calculate the score of the given string is that if the right character is in the right index of the given string it gets a score, Also they order is imporatant we start from the most left character and if it doesn't match our goal strings first character we break out of the for loop and our given string gets zero score. for example if our goal string is "tastey apple":
# 
# 1) "tasyy orange" : 3
# 
# 2) "tsssssssssss" : 1
# 
# 3) "aaaakkkkk   " : 0

# In[5]:


#generate creates a random string from the given alphabet of the size given to it as input arguement

import random
def generate(lenS, alphabet):
    res=""
    for x in range(lenS):
        res = res + random.choice(alphabet)
    return res


# In[17]:


#the monkeyTypist function is basically a while loop that keeps generating Strings of characters and caculates their score
#(with the help of the above functions) it keeps the track of the best string found so it keeps giving smaller and smaller 
#input arguements to the generate function to create smaller strings to add to the best string. It also plots the progress
#of the function keeps track of the best scores and prints and plots them every 100 cycles

import matplotlib.pyplot as plt
def monkeyTypist():
    target = list("oh cant you see you belong to me")
    lenS = len(target)
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")
    epoch = 0
    bestStr = generate(lenS, alphabet)
    bestScore = calcScore(bestStr, target)
    it_list = [0]
    sc_list = [bestScore]
    while bestScore < len(target):
        temp = list(bestStr)
        for i in range(len(target) - bestScore):
            temp.pop()
        bestStr2="".join(temp)
        if bestScore==len(target):
            break
        newStr = generate(lenS - bestScore, alphabet)
        newStr = bestStr2 + newStr
        newScore = calcScore(newStr, target)
        if newScore > bestScore:
            bestScore = newScore
            bestStr = newStr
            sc_list.append((bestScore)*(100)/(len(bestStr)))
            it_list.append(epoch)
        if epoch%100 == 0 and epoch != 0:
            print("%s %d %d" % ("".join(bestStr), (bestScore)*(100)/(len(bestStr)), epoch))
        epoch = epoch+1
    print("%s %d %d" % ("".join(bestStr), (bestScore)*(100)/(len(bestStr)), epoch))
    plt.plot(it_list, sc_list, 'ro')
    plt.xlabel('Number of Iterations', fontsize=12)
    plt.ylabel('score of the best String', fontsize=12)
    plt.show()
monkeyTypist()

