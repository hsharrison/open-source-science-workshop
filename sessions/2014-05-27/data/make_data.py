import numpy as np


def generate_data(length, scale=1):
    return scale*np.random.random((length, 2)).cumsum(1)


def main():
    for idx in range(12):
        np.savetxt('s{:02d}.txt'.format(idx+1),
                   generate_data(np.random.randint(80, 120)))


if __name__ == '__main__':
    main()
