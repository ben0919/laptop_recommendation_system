from sklearn.naive_bayes import GaussianNB
from joblib import dump, load
import numpy as np
import pandas as pd

test = pd.DataFrame(columns=['communication', 'social', 'word_processing',
                             'entertainment', 'reading', 'coding', 'creation', 'high', 'low', 'medium', 'apple_0', 'apple_1', 'depart_1', 'depart_2', 'depart_3'])
function = ['communication', 'social', 'word_processing',
            'entertainment', 'reading', 'coding', 'creation']
money_level = ['high', 'low', 'medium']
model = load("joblib_RL_Model_NB.pkl")
print('歡迎來到筆電系統推薦小顧問')
use = input(
    "請選擇您使用筆電最需要的三種功能：\n1. 通訊\n2. 社交\n3. 文書處理\n4. 娛樂\n5. 閱讀\n6. 寫程式\n7. 圖影音創作\n(ex:4 5 6):")
department = input("請問就讀哪個科系？\n1. 電資學院及其相關科系\n2. 理工學院及其相關科系\n3. 其他\n:")
use_list = use.split(' ')
apple = input("您是否有使用其他apple產品？(yes/no): ")
money = input("您一個月擁有多少生活費？[low=8000以下, medium=8001~11999, high=12000以上]: ")
for i in function:
    if i in use_list:
        test.loc[0, i] = 1
    else:
        test.loc[0, i] = 0
for i in money_level:
    if i == money:
        test.loc[0, i] = 1
    else:
        test.loc[0, i] = 0
if apple == 'yes':
    test.loc[0, 'apple_0'] = 0
    test.loc[0, 'apple_1'] = 1
else:
    test.loc[0, 'apple_1'] = 0
    test.loc[0, 'apple_0'] = 1
if department == 1:
    test.loc[0, 'depart_1'] = 1
    test.loc[0, 'depart_2'] = 0
    test.loc[0, 'depart_3'] = 0
elif department == 2:
    test.loc[0, 'depart_1'] = 0
    test.loc[0, 'depart_2'] = 1
    test.loc[0, 'depart_3'] = 0
else:
    test.loc[0, 'depart_1'] = 0
    test.loc[0, 'depart_2'] = 0
    test.loc[0, 'depart_3'] = 1
system = model.predict(test)
print('依照您的需求，您比較適合購買%s的筆電！' % system[0])
