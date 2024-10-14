# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BzFOuvBSTz6fd-YCy2OarQTxRaXkX5qC
"""

import pandas as pd

#1. DataFrome yaratish
data = {
    'ism':['Muxlisa', 'Mubina', 'Sarvinoz'],
    'Yoshi':[25, 18, 22],
    'Shahar':['Toshkent', 'Andijon', 'Buhoro']
}
df = pd.DataFrame(data)

#2. Ma'lumotlarni ko'rish
print(df)

#3. Filtirlash
young_people = df[df['Yoshi'] < 30]
print("30 yoshdan kichiklar:\n", young_people)

#4. O'zgartirish
df['Yoshi'] +=1 #Har bir shaxsning yoshini 1ga oshirish
print("Yangilangan DataFrom:\n", df)
#5. CSV formatda saqlash
df.to_csv('data.csv', index=False)