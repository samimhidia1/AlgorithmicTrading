def get_price_trend(df, i):
    if df['close'][i] > df['close'][i - 1]:
        return 'up'
    elif df['close'][i] < df['close'][i - 1]:
        return 'down'
    else:
        return 'sideways'


def get_ichimoku_signal(df, i):
    if df['tenkan_sen'][i] > df['kijun_sen'][i] and df['close'][i] > df['senkou_span_a'][i]:
        return 'buy'
    elif df['tenkan_sen'][i] < df['kijun_sen'][i] and df['close'][i] < df['senkou_span_b'][i]:
        return 'sell'
    else:
        return 'neutral'


def get_reward(df, i, action):
    if action == 'buy':
        return df['close'][i + 1] - df['close'][i]
    elif action == 'sell':
        return df['close'][i] - df['close'][i + 1]
    else:
        return 0


def take_action(action):
    if action == 'buy':
        # Buy the asset
        pass
    elif action == 'sell':
        # Sell the asset
        pass
    else:
        # Do nothing
        pass
