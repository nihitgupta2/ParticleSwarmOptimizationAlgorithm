# Nihit Gupta
import math
import random
import matplotlib.pyplot as plt
import numpy as np


def cost_calculator(x,y):
    #function to calculate the z value using the six-hump camelback problem with x and y values
    z = ((4-(2.1*pow(x,2))+(pow(x,4)/3))*pow(x,2)) + (x*y) + ((-4+(4*pow(y,2)))*pow(y,2))
    return z

def psoAlgorithm(iterations,w,c1,c2,vmax,vmin,swarmSize):
    bestFitnessPerIter = []
    avgFitnessPerIter = []
    pBestMatrix = [[None,None] for iter in range(swarmSize)]
    gbest = [round(random.uniform(-1.0,1.0),6),round(random.uniform(-1.0,1.0),6)]  #entire swarm is neighbourhood
    gbestValue = cost_calculator(gbest[0],gbest[1])
    gbestindex = None
    swarm = []
    for i in range(swarmSize):
        tempValX = round(random.uniform(5.0,-5.0))
        tempValY = round(random.uniform(5.0,-5.0))
        tempValVx = round(random.uniform(0,0.2))
        tempValVy = round(random.uniform(0,0.2))
        tempParticleVal = cost_calculator(tempValX,tempValY)
        pBestMatrix[i] = [tempValX,tempValY]
        swarm.append({
            'x' : tempValX,
            'y' : tempValY,
            'vx' : tempValVx,
            'vy' : tempValVy,
            'pbest' : [tempValX,tempValY],
            'pbestValue' : tempParticleVal,
        })
    
    for i in range(iterations):
        flag = 0
        for j in range(swarmSize):
            vxTemp = (w*swarm[j]['vx'])+((c1/2)*(swarm[j]['pbest'][0]-swarm[j]['x']))+((c2/2)*(gbest[0]-swarm[j]['x']))
            vyTemp = (w*swarm[j]['vy'])+((c1/2)*(swarm[j]['pbest'][1]-swarm[j]['y']))+((c2/2)*(gbest[1]-swarm[j]['y']))
            xTemp = swarm[j]['x'] + vxTemp
            yTemp = swarm[j]['y'] + vyTemp
            pbestTemp = cost_calculator(xTemp,yTemp)
            if pbestTemp<swarm[j]['pbestValue']:    #goal is to minimize
                swarm[j]['pbestValue']=pbestTemp
                swarm[j]['pbest'] = [xTemp,yTemp]
            swarm[j]['x']=xTemp
            swarm[j]['y']=yTemp
            swarm[j]['vx']=vxTemp
            swarm[j]['vy']=vyTemp
            if pbestTemp<gbestValue:
                gbestValue = pbestTemp
                gbestindex = j
                flag = 1
        if flag==1:
            gbest[0] = swarm[gbestindex]['x']
            gbest[1] = swarm[gbestindex]['y']

        bestFitness = 10000
        avgFitness = 0
        for k in range(swarmSize):
            fitnessParticle  = cost_calculator(swarm[k]['x'],swarm[k]['y'])
            avgFitness += fitnessParticle
            if fitnessParticle<bestFitness:
                bestFitness = fitnessParticle
        avgFitness = avgFitness/swarmSize
        bestFitnessPerIter.append(bestFitness)
        avgFitnessPerIter.append(avgFitness)
    return gbest,gbestValue,bestFitnessPerIter,avgFitnessPerIter

def main():
    iterations = 75
    c1,c2 = 1.15,1.15
    w = 0.85
    vmax,vmin = 2,2
    swarmSize = 50
    resBest,rbestValue,rbestFitnessPerIter,ravgFitnessPerIter = psoAlgorithm(iterations,w,c1,c2,vmax,vmin,swarmSize)
    resBest = [round(resBest[0],7),round(resBest[1],7)]
    rbestValue = round(rbestValue,7)
    print(resBest)
    print(rbestValue)
    iterXComponenet = [i+1 for i in range(iterations)]
    fig,(ax1,ax2) = plt.subplots(1,2)
    fig.suptitle("Graphs")
    ax1.plot(iterXComponenet,rbestFitnessPerIter)
    ax1.set_title("Best Solution Vs Iteration")
    ax2.plot(iterXComponenet,ravgFitnessPerIter)
    ax2.set_title("Average value of solution Vs Iteration")
    plt.show()
    return True


if __name__ == '__main__':
    main()
