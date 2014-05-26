import os
import numpy as np

N_SUBJECTS = 5
N_TRIALS = 10


def generate_data(length, scale=1):
    return scale*np.random.random((length, 2)).cumsum(1)


def main():
	for subject in range(N_SUBJECTS):
		subject_dir = 's{:02d}'.format(subject + 1)
		os.mkdir(subject_dir)
		for trial in range(N_TRIALS):
			trial_file = os.path.join(subject_dir, 't{:02d}.txt'.format(trial + 1))
			np.savetxt(trial_file, generate_data(np.random.randint(80, 120)))


if __name__ == '__main__':
    main()
