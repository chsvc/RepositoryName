users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_users = set(users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict_ = {"Общее количество": 0,
         "Уникальные посещения": len(unique_users)}
dict_["Общее количество"] = len(users)
dict_["Уникальные посещения"] = len(unique_users)
print(dict_)