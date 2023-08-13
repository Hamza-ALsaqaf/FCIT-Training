import random as r

gest_words=["ERP","Flwoer","Hamz"]

choiceWord=r.choice(gest_words)
Blankword=len(choiceWord)
blank=[]
temptry=3
win=0
for i in range(Blankword):
    blank.append("_")
print(choiceWord)
for i in range(Blankword):
    print(blank)
    print(temptry)
    enterLeter=input("Enter Leter...")
    if enterLeter in choiceWord:
        index=choiceWord.index(enterLeter)
        blank[index]=enterLeter
        win+=1
        if win==len(blank):
            print("win ..😎")
            break
    else:
        temptry-=1
        
        if temptry==0:
            print("lose 😪")
            break
    # if index ==i:
    #     blank[index]=enterLeter
    
    # print(index)
    # print(blank)
# print(blank
# print(blank) 

