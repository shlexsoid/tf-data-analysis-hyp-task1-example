import pandas as pd
import numpy as np


chat_id = 399623382 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
     res = proportions_ztest([x_success, y_success],
                            [x_cnt, y_cnt],
                            alternative='larger')
    return res.pvalue < 0.08
