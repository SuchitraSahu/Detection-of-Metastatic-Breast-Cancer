# -*- coding: utf-8 -*-
"""Csv files combine

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ricLfazYFZYmZPBhUlAWxTLM1lH7jbpv
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
result = pd.read_csv('/content/drive/MyDrive/Breast Cancer DataSET/Deep Features/resnet_gap/resnet_gap_final_29.csv')
print(len(result))

import pandas as pd
aa = pd.read_csv('/content/drive/MyDrive/Breast Cancer DataSET/Deep Features/resnet_gap/resnet_gap_final_15.csv')
aa["target"] = "0"
aa.head()