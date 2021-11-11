import json
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

''' Создаём DataFrame распределения жанров по пользователям'''

# Список жанров для каждой вершины
with open('C:/Users/dudyp/OneDrive/Рабочий стол/Alternate/HU_genres.json') as json_data:
    data = json.load(json_data)

# Из словаря получаем все 84 жанра и заносим их в список
genres_list = []

for k in data.keys():
    for g in data[k]:
        if not(g in genres_list):
            genres_list.append(g)
            if len(genres_list) == 84:
                break

# Сортируем список с жанрами
genres_list.sort()

# Создаём пустой DataFrame с жанрами в виде столбцов
genres = pd.DataFrame(columns=genres_list)

# Для каждой строки создаём словарь с жанрами, которые содержит эта вершина, и добавляем их в DataFrame
# P.S: для постройки полной таблицы стереть 'range(5):' и убрать '#' для 'range(len(data)):'
for i in range(5): #range(len(data)):
    genres_dict = dict.fromkeys(data[str(i)], 1)
    genres = genres.append(genres_dict, ignore_index=True)

# Остальные жанры зануляем
genres = genres.fillna(0)

# Выводим таблицу
# P.S: при 'range(5):' выводятся только первые 5 строк
print(genres)

'''Теперь создаём граф дружбы'''

# Таблица ребёр дружбы
edges = pd.read_csv('C:/Users/dudyp/OneDrive/Рабочий стол/Alternate/HU_edges.csv')

# Выведем таблицу рёбер
print(edges)

# Для проверки работоспобности выведем первые 5 ребёр
edges_demo = edges.head()

# Строим граф по рёбрам edges
# P.S: для полного графа вместо параметра edges_demo поставить edges
Graph_friendship = nx.from_pandas_edgelist(edges_demo, source='node_1', target='node_2', create_using=nx.Graph())

# Рисуем граф с перыми 5 рёбрами
nx.draw_circular(Graph_friendship, with_labels=True)

plt.show()
