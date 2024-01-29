import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
oh_data = pd.get_dummies(data['whoAmI'], prefix='whoAmI')
data = pd.concat([data, oh_data], axis=1)
data.pop('whoAmI')
data.head()
