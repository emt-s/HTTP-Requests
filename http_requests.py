# -*- coding: utf-8 -*-
"""HTTP-Requests.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ufAAxeCiqPcqYFxnDMGacuRAcN1Q16B
"""

import requests
Data =requests.get('https://wti.kaust.edu.sa/')
print (Data.text)
x = open("url Data.txt","w") 
 
x.write(Data.text) 
 
 
x.close()