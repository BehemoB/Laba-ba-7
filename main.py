def merge(*lists): #Создаем функцию
    pustoy_spisok_dlya_vlojenia = [] #По названию переменной все понятно
    for tipa_dobavlenie in pustoy_spisok_dlya_vlojenia: #Вставляем цикл для основного действия
        pustoy_spisok_dlya_vlojenia += tipa_dobavlenie
        pustoy_spisok_dlya_vlojenia.sort()
    return pustoy_spisok_dlya_vlojenia #возвращаем список
print(merge(*lists)) #Соответственно пропечатываем его в ответе

#Честно говоря, это все, на что меня хватило. Надеюсь, оно бует работать(

