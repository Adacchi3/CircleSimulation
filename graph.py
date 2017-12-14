from matplotlib import pyplot as plt
import numpy as np
import datetime

if __name__ == '__main__':
    yes = np.load('log/20171214115537/yes.npy')
    print(yes.shape)
    no = np.load('log/20171214115537/no.npy')
    print(no.shape)

    yes_average = np.average(np.average(yes, axis=2), axis=1)
    print(yes_average)

    no_average = np.average(np.average(no, axis=2), axis=1)
    print(no_average)

    times = []

    for i in range(6):
        for j in range(12):
            time = "{0}:{1}".format(i+10,j*5)
            times.append(time)

    print(len(times))
    """
    plt.plot(yes_average, label="effect")
    plt.plot(no_average, label="no effect")
    plt.title("the average of sale books on each time")
    plt.xlabel("time")
    plt.ylabel("book")
    plt.legend()
    plt.show()
    """

    """
    yes_number = [0] * len(yes_average)
    for i in range(len(yes_average)):
        yes_number[i] = yes_number[i-1]+yes_average[i] if i != 0 else yes_average[i]

    no_number = [0] * len(no_average)
    for i in range(len(no_average)):
        no_number[i] = no_number[i-1]+no_average[i] if i != 0 else no_average[i]

    print(np.sum(yes_average))
    print(np.sum(no_average))
    
    plt.bar(range(len(yes_number)),yes_number, label="effect")
    plt.bar(range(len(no_number)),no_number, label="no effect")
    plt.title("the sum of sale books on each time")
    plt.xlabel("time")
    plt.ylabel("book")
    plt.legend()
    plt.show()
    """

    watashi = np.average(yes, axis=2)
    watashi = watashi[:,0]
    anata = np.average(no, axis=2)
    anata = anata[:,0]

    kibo = [0] * len(watashi)
    for i in range(len(watashi)):
        kibo[i] = kibo[i-1]+watashi[i] if i != 0 else watashi[i]

    genjitsu = [0] * len(anata)
    for i in range(len(anata)):
        genjitsu[i] = genjitsu[i-1]+anata[i] if i != 0 else anata[i]


    print(np.sum(watashi))
    print(np.sum(anata))

    plt.bar(range(len(kibo)),kibo)
    plt.bar(range(len(genjitsu)),genjitsu)
    plt.show()

    