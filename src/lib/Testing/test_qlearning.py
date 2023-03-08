from src.lib.QLearning.QLearning import QLearning
from src.lib.Testing.helpers import get_price_trend, get_ichimoku_signal, get_reward, take_action

# Define the action space
actions = ['buy', 'sell', 'hold']

# Define the state space
states = {
    'price_trend': ['up', 'down', 'sideways'],
    'ichimoku_signal': ['buy', 'sell', 'neutral']
}

# Initialize the Q-Learning model
model = QLearning(actions=actions, states=states, alpha=0.1, gamma=0.9, epsilon=0.1)

for i in range(len(df) - 1):
    # Get the current state
    state = {
        'price_trend': get_price_trend(df, i),
        'ichimoku_signal': get_ichimoku_signal(df, i)
    }

    # Get the current action from the model
    action = model.get_action(state)

    # Get the next state and reward
    next_state = {
        'price_trend': get_price_trend(df, i + 1),
        'ichimoku_signal': get_ichimoku_signal(df, i + 1)
    }
    reward = get_reward(df, i, action)

    # Update the model with the new information
    model.update(state, action, reward, next_state)

    # Print the current state, action, reward, and next state
    print('State:', state)
    print('Action:', action)
    print('Reward:', reward)
    print('Next State:', next_state)

    # Check if it's time to take action
    if model.is_time_to_take_action():
        take_action(action)

# Save the trained model
model.save_model('qlearning_model.pkl')

