import gym
from gym import spaces
import numpy as np
import pandas as pd

class TradingEnv(gym.Env):
    def __init__(self):
        self.df = pd.read_csv('data.csv', index_col=0)
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.df.shape[1],))

    def reset(self):
        self.current_step = 0
        self.profits = 0
        self.bought_price = 0
        self.share = 0
        obs = self.df.iloc[self.current_step].values
        return obs

    def step(self, action):
        self.current_step += 1
        obs = self.df.iloc[self.current_step].values
        reward = 0
        done = False

        if action == 0 and self.share == 0:
            self.bought_price = obs[3]
            self.share = 1
        elif action == 1 and self.share == 1:
            reward = obs[3] - self.bought_price
            self.profits += reward
            self.share = 0

        if self.current_step == len(self.df) - 1:
            done = True

        return obs, reward, done, {}
