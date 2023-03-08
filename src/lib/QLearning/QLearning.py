from qlearning import QLearning

# Define the action space
actions = ['buy', 'sell', 'hold']

# Define the state space
states = {
    'price_trend': ['up', 'down', 'sideways'],
    'ichimoku_signal': ['buy', 'sell', 'neutral']
}

# Initialize the Q-Learning model
model = QLearning(actions=actions, states=states, alpha=0.1, gamma=0.9, epsilon=0.1)
