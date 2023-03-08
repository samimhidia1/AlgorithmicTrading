import numpy as np

q_table = np.zeros([env.observation_space.shape[0], env.action_space.n])

epsilon = 0.1
discount_factor = 0.95
alpha = 0.1

for episode in range(1,10001):
    state = env.reset()
    done = False
    while not done:
        if np.random.uniform() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])