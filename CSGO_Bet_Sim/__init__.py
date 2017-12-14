# -------------------------
# CS:GO Bet Simulator
# Charlie Harris
# -------------------------

import random
import itertools
import math

dicectt = ["Dice", "CT", "T", "CT", "T", "CT", "T", "CT", "T", "CT", "T","CT", "T", "CT", "T"]
numberofspins = 100000
betvalue = 1

#-------------------------------------------------------
# Description: Simulates the spin of the roulette wheel
# Prints: The total of each possible outcomes
# Returns: A list of spin outcomes
#-------------------------------------------------------
def spin() :
    dice = 0
    ct = 0
    t = 0
    train = []
    for i in range(numberofspins) :
        r = random.randint(0, 14)
        if dicectt[r] == "Dice" :
            dice += 1
            train.append("Dice")
        elif dicectt[r] == "CT" :
            ct += 1
            train.append("CT")
        elif dicectt[r] == "T":
            t += 1
            train.append("T")
    print("Dice:", dice, "\nCT:", ct, "\nT:", t)
    return train

#-------------------------------------------------------------
# Description: Calculates the biggest train of the same value
# Returns: The largest value train
#-------------------------------------------------------------
def calctrain(results) :
    trains = [sum(1 for _ in group) for key, group in itertools.groupby(results) if key]
    return max(trains)

#--------------------------------------------------
# Description: Calculates the biggest non T train
# Returns: The largest value non T train
#--------------------------------------------------
def notttrain(results) :
    max = 0
    count = 0
    for i in results :
        if i != "T" :
            count += 1
            if count > max :
                max = count
        elif i == "T" :
            count = 0
    return max

#--------------------------------------------------------------------
# Description: Calculates how much money required to stay in betting
# Returns: Money required
#--------------------------------------------------------------------
def reqmoney(biggestnotttrain) :

    return betvalue * math.pow(2, biggestnotttrain + 1) - betvalue

#------------------------------------------
# Main function that runs the program
#-------------------------------------------
def main() :
    print("Total Spins:", numberofspins)
    results = spin()
    print("Results:", results)
    biggesttrain = calctrain(results)
    print("Biggest Value Train:", biggesttrain)
    biggestnotttrain = notttrain(results)
    print("Biggest Non T Train:", biggestnotttrain)
    money = reqmoney(biggestnotttrain)
    print("Required Money:", money)

main()
