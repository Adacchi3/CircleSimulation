from model.CircleParticipant import *
from model.GeneralParticipant import *
import numpy as np
import sys, time
import math
from matplotlib import pyplot as plt

def iBuyThisBook(a, c):
    a.money = a.money - c.price
    a.log.append(c.id)
    return

def decision(a, c):
    return (c.book_quality+a.alpha*c.ad*haveIseeit(a,c)+a.beta*c.dm)/3

def decision2(a, c):
    return c.book_quality

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

def select_circle2(agent, a, b):
    like_a = doIlikethiscategory(agent, a)
    like_b = doIlikethiscategory(agent, b)
    #look_a = haveIseeit(agent, a)
    #look_b = haveIseeit(agent, b)
    #vala = (like_a+agent.alpha*a.ad*look_a+agent.beta*a.dm)/3
    #valb = (like_b+agent.alpha*b.ad*look_b+agent.beta*b.dm)/3
    vala = like_a
    valb = like_b
    selected = a if vala >= valb else b
    return selected

if __name__ == '__main__':
    general_number = 3500
    circle_number = 800
    steps = 72
    N = 20
    circles = []
    generals = []

    watashi = CircleParticipant(0,48400,0.7,0.5,0.4,1,800)

    logs = np.zeros([steps,circle_number,N])

    for i in range(circle_number):
        if i == 0 :
            circles.append(watashi)
        else :
            circles.append(CircleParticipant(i))

    for i in range(general_number):
        generals.append(GeneralParticipant(i))
        generals[i].check_ad(circles)

    for n in range(N):
        for i in range(steps):
            sys.stdout.write("\r%d回目：%d/%d" % (n+1, i+1, steps))
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
                        logs[i][selected.id][n] = logs[i][selected.id][n]+ 1
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    #宣伝なしの場合
    #logs2で計測してますよ。
    circles = []
    generals = []
    logs2 = np.zeros([steps,circle_number,N])

    for i in range(circle_number):
        if i == 0 :
            circles.append(watashi)
        else :
            circles.append(CircleParticipant(i))

    for i in range(general_number):
        generals.append(GeneralParticipant(i))
        generals[i].check_ad(circles)

    for n in range(N):
        for i in range(steps):
            sys.stdout.write("\r%d回目：%d/%d" % (n+1, i+1, steps))
            np.random.shuffle(circles)
            for agent in generals:
                if(agent.start<=i and i<agent.start+agent.time):
                    #サークル選択処理
                    candidates = np.random.choice(circles,5,replace=False)
                    selected = CircleParticipant(-1, 0, 0, 0, 0, 0, 0)
                    for candidate in candidates:
                        if candidate.id not in agent.log:
                            selected = select_circle2(agent, selected, candidate)
                    #購買決定処理
                    if( decision2(agent, selected) > np.random.rand() ):
                        iBuyThisBook(agent, selected)
                        logs2[i][selected.id][n] = logs2[i][selected.id][n]+ 1
            sys.stdout.flush()
            time.sleep(0.01)
        print()


    #宣伝ありの売り上げ数平均
    A = np.average(logs, axis=2)
    A = np.average(A, axis=1)

    #宣伝ありの私のサークルの冊数売り上げ
    B = np.average(logs, axis=2)
    B = B[:,0]

    #宣伝なしの売り上げ数平均
    C = np.average(logs2, axis=2)
    C = np.average(C, axis=1)

    #宣伝なしの私のサークルの冊数売り上げ
    D = np.average(logs2, axis=2)
    D = D[:,0]

    #これは棒グラフ用
    #C = [0] * len(A)
    #for i in range(len(A)):
    #    C[i] = C[i-1]+A[i] if i != 0 else A[i]

    plt.plot(A)
    plt.plot(B)
    plt.plot(C)
    plt.plot(D)
    plt.show()