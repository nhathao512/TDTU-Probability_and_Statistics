import random

def lay_30():
    n = list(range(1, 65)) 
    random.shuffle(n)
    return n[:30]

tapS1 = lay_30() 
print(tapS1)

re_n = [i for i in range(1, 65) if i not in tapS1]
random.shuffle(re_n)
tapS2 = random.sample(re_n, 15)
print(tapS2)
