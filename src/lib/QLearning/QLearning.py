import random
import numpy as np
import pickle


class QLearning:
    def __init__(self, actions, states, alpha, gamma, epsilon, model_file=None):
        self.actions = actions
        self.states = states
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        if model_file is not None:
            self.load_model(model_file)
        else:
            self.q_table = np.zeros([len(states['price_trend']), len(states['ichimoku_signal']), len(actions)])

    def get_action(self, state):
        price_trend = state['price_trend']
        ichimoku_signal = state['ichimoku_signal']

        if random.uniform(0, 1) < self.epsilon:
            # Take a random action
            action = random.choice(self.actions)
        else:
            # Take the action with the highest Q-value
            action_values = self.q_table[self.states['price_trend'].index(price_trend)][
                self.states['ichimoku_signal'].index(ichimoku_signal)]
            max_action_value = np.max(action_values)
            max_actions = [a for a in self.actions if action_values[self.actions.index(a)] == max_action_value]
            action = random.choice(max_actions)

        return action

    def update(self, state, action, reward, next_state):
        price_trend = state['price_trend']
        ichimoku_signal = state['ichimoku_signal']
        next_price_trend = next_state['price_trend']
        next_ichimoku_signal = next_state['ichimoku_signal']

        current_value = self.q_table[self.states['price_trend'].index(price_trend)][
            self.states['ichimoku_signal'].index(ichimoku_signal)][self.actions.index(action)]
        max_future_value = np.max(self.q_table[self.states['price_trend'].index(next_price_trend)][
                                      self.states['ichimoku_signal'].index(next_ichimoku_signal)])
        new_value = (1 - self.alpha) * current_value + self.alpha * (reward + self.gamma * max_future_value)
        self.q_table[self.states['price_trend'].index(price_trend)][
            self.states['ichimoku_signal'].index(ichimoku_signal)][self.actions.index(action)] = new_value

    def is_time_to_take_action(self):
        return random.uniform(0, 1) < self.epsilon

    def save_model(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_model(self, file_name):
        with open(file_name, 'rb') as f:
            self.q_table = pickle.load(f)
