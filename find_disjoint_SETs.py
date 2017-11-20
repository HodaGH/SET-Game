'''
## Author: Hoda Gholami
## Purpose: The goal is to read a collection of SET cards from standard input (stdin) and:
##          1. find and print the number of possible SETs of three cards in the input.
##         
2. find and print the largest disjoint collection of SETs in the input.
## Input: input will contain an
integer N, followed by a list of N distinct SET cards, one per line
## Output: 1. A single line containing the number of possible SETs of three cards in the input.
##         2. A single line containing the maximum number of disjoint SETs in the input.
##         3. The cards forming a largest collection of disjoint SETs, each card on its own line and each
SET preceded by a blank line.
## Assumptions:
##         1. Input is in valid format so we don't have to check the validitity of input data
'''

import time
import copy

def checkCol(c1, c2, c3):
    '''
    This function returns 1 if all the cards have same color or totally different colors.
    '''
    if (c1[0] == c2[0] == c3[0]) or ((c1[0] != c2[0] and c2[0] != c3[0] and c1[0] != c3[0])):
        return 1
    return 0

def checkSym(c1, c2, c3):
    '''
    This function returns 1 if all the cards have same symbol or totally different symbols.
    '''   
    if(c1[1] == c2[1] == c3[1]) or (c1[1] != c2[1] and c2[1] != c3[1] and c1[1] != c3[1]):
        return 1
    return 0

def checkShad(c1, c2, c3):
    '''
    This function returns 1 if all the cards have same shading or totally different shading.
    '''
    if(c1[2] == c2[2] == c3[2]) or (c1[2] != c2[2] and c2[2] != c3[2] and c1[2] != c3[2]):
        return 1
    return 0

def checkNum(c1, c2, c3):
    '''
    This function returns 1 if all the cards have same number or totally different numbers.
    '''
    if(c1[3] == c2[3] == c3[3]) or (c1[3] != c2[3] and c2[3] != c3[3] and c1[3] != c3[3]):
        return 1
    return 0

def checkSET(c1, c2, c3):
    '''
    This function returns 1 these three cards form a SET otherwise it return 0.
    '''
    return checkCol(c1, c2, c3) and checkSym(c1, c2, c3) and checkNum(c1, c2, c3) and checkShad(c1, c2, c3)

def possibleSets(cardlist):
    '''
    This function returns the list of all possible SETs.
    '''
    listOfSets = [(cardlist[i], cardlist[j], cardlist[k]) for i in range(0,N) for j in range(i+1, N) for k in range(j+1, N) if checkSET(cardlist[i], cardlist[j], cardlist[k])]
    return listOfSets

def maxDisSets(index, disCards, disSETs, count, listOfSets):
    '''
    This function iterates over each SET in listOfSets, and it checks the selected set if it is disjoint from all selected sets so far,
    if yes, it does add its index to the disSETs set of disjoints SETS
    if no, it adds its cards to set of all visited cards
    '''
    global maxCount
    global maxDisSETs #list of indexes of SETs that form the maximum disjoint sets
    
    if index > len(listOfSets) - 1:
        return maxCount
    if count >= maxCount:
        maxCount = count
        maxDisSETs = disSETs
        
    maxDisSets(copy.deepcopy(index + 1), copy.deepcopy(disCards), copy.deepcopy(disSETs), copy.deepcopy(count), listOfSets )
    if((listOfSets[index][0] not in disCards) and (listOfSets[index][1] not in disCards) and (listOfSets[index][2] not in disCards)):
        disCards.add(listOfSets[index][0])
        disCards.add(listOfSets[index][1])
        disCards.add(listOfSets[index][2])
        count = count + 1
        disSETs.add(index)
        
        if count >= maxCount:
            maxCount = count
            maxDisSETs = disSETs

        maxDisSets(copy.deepcopy(index+1), copy.deepcopy(disCards), copy.deepcopy(disSETs), copy.deepcopy(count), listOfSets)

    return


if __name__ == '__main__':
    
    shading = {'a' : 0, 's' : 0, 'h' : 0, 'A' : 1, 'S' : 1, 'H' : 1, '@' : 2, '$' : 2, '#' : 2}
    symbol = {'A' : 'A', '@' : 'A', 'a' : 'A', 's' : 'S', 'S' : 'S', '$' : 'S', 'h' : 'H', 'H' : 'H', '#' : 'H'}
    symShad = {('A', 2): '@', ('A', 1) : 'A', ('A', 0) : 'a', ('S', 2): '$', ('S', 1) : 'S', ('S', 0) : 's', ('H', 2): '#', ('H', 1) : 'H', ('H', 0) : 'h'}

    #takes number of cards and the list of cards as input
    N = int(input("Please enter the number cards and then a list of SET cards, one per line.\n"))
    
    #list of cards
    cardList = []
    for i in range(0, N):
        line = input()
        values = line.split()
        card = (values[0], symbol[values[1][0]], shading[values[1][0]], len(values[1]))
        cardList.append(card)

    start_time = time.time()
    
    listOfSets = possibleSets(cardList)
    print(len(listOfSets)) #size of all possible sets
    
    maxCount = 0
    maxDisSETs = []
    maxDisSets(0, set(), set(), 0, listOfSets) #return a list of maximal disjoint SETs
    print(maxCount)
    
    #prints output
    for i in maxDisSETs:
            print ("\n")
            c1 = listOfSets[i][0] 
            c2 = listOfSets[i][1]
            c3 = listOfSets[i][2]
            print(c1[0], " ", symShad[c1[1],c1[2]] * c1[3])
            print(c2[0], " ", symShad[c2[1],c2[2]] * c2[3])
            print(c3[0], " ", symShad[c3[1],c3[2]] * c3[3])


    print("--- %s seconds ---" % (time.time()-start_time))
    
    
