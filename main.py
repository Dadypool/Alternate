import json
import pandas as pd

# Таблица ребёр дружбы
edges = pd.read_csv('C:/Users/dudyp/OneDrive/Рабочий стол/Alternate/HU_edges.csv')

# Список жанров для каждой вершины
with open('C:/Users/dudyp/OneDrive/Рабочий стол/Alternate/HU_genres.json') as json_data:
    data = json.load(json_data)

# Из словаря получаем все 84 жанра и заносим из в список
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

# Для каждой строки создаём словарь с жанрами, которая любит эта вершина, и добавляем их в DataFrame
for i in range(5): #range(len(data)):
    genres_dict = dict.fromkeys(data[str(i)], 1)
    genres = genres.append(genres_dict, ignore_index=True)

# Остальные жанры зануляем
genres = genres.fillna(0)

# Выводим только первые 5 вершин
print(genres.head())
