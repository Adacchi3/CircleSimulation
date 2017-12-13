from model.CircleParticipant import *
from model.GeneralParticipant import *
import numpy as np
import sys, time

def iBuyThisBook(a, c):
    a.money = a.money - c.price
    a.log.append(c.id)
    return

def decision(a, c):
    return (c.book_quality+a.alpha*c.ad*haveIseeit(a,c)+a.beta*c.dm)/3

def haveIseeit(agent, circle):
    if circle.id in agent.circlelist:
        return 1
    else:
        return 0

def doIlikethiscategory(agent, circle):
    if agent.like_category == circle.category:
        return 1
    else:
        return 0

def select_circle(agent, a, b):
    like_a = doIlikethiscategory(agent, a)
    like_b = doIlikethiscategory(agent, b)
    look_a = haveIseeit(agent, a)
    look_b = haveIseeit(agent, b)
    vala = (like_a+agent.alpha*a.ad*look_a+agent.beta*a.dm)/3
    valb = (like_b+agent.alpha*b.ad*look_b+agent.beta*b.dm)/3
    selected = a if vala >= valb else b
    return selected

if __name__ == '__main__':
    general_number = 3500
    circle_number = 800
    steps = 72

    circles = []
    generals = []

    watashi = CircleParticipant(0,48400,0.7,0.5,0.4,1,800)

    logs = np.zeros([steps,circle_number])

    for i in range(circle_number):
        if i == 0 :
            circles.append(watashi)
        else :
            circles.append(CircleParticipant(i))

    for i in range(general_number):
        generals.append(GeneralParticipant(i))
        generals[i].check_ad(circles)
 
    for i in range(steps):
        sys.stdout.write("\r%d/%d" % (i, steps))
        np.random.shuffle(circles)
        for agent in generals:
            if(agent.start<=i and i<agent.start+agent.time):
                #サークル選択処理
                candidates = np.random.choice(circles,5,replace=False)
                selected = CircleParticipant(-1, 0, 0, 0, 0, 0, 0)
                for candidate in candidates:
                    if candidate.id not in agent.log:
                        selected = select_circle(agent, selected, candidate)
                #購買決定処理
                if( decision(agent, selected) > np.random.rand() ):
                    iBuyThisBook(agent, selected)
                    logs[i][selected.id] = logs[i][selected.id]+ 1
        sys.stdout.flush()
        time.sleep(0.01)
    for i in range(logs.shape[0]):
        print(logs[i])