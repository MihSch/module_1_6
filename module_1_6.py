         #СЛОВАРЬ
#phone_book = {'Miha': 89297941347, 'Max': 88005553535} # пара элем, имя ключ, номер значение
#print(phone_book['Miha'])# ключ неизменяемый обьект/ чтобы обратиться нужно указать ключ
#phone_book['Miha'] = 123456
#phone_book['Anton'] = 777 #то есть добавляет к словарю УДОБНО
#del phone_book['Max'] # макс офф
#phone_book.update({'Sanya': 9888899,# .update добавляет несколько пар элементов одновременно
 #                  'Kolymba': 65446465})
#print(phone_book.get('Max')) #.get обращение к ключу,
# в случае есть ключ не существует вернет к значению NONE и не создаст новый
#в случае none через запятую можно написать текст на вывод
#print(phone_book)
#a = phone_book.pop('Anton') # .pop вытаскивает ключ из значения/вынуть из словарика пару
#list_ = [1,2,3]
#list_.pop(0) #еще один пример поп
#print(list_)
#print(phone_book)
#print(a)
#print(phone_book.keys()) #.keys метод вытаскивает ключи, то есть имена
#print(phone_book.values()) #.values метод вытаскивает значения, то есть номера
#print(phone_book.items()) #.items метод возвращает целые пары ключ+значения
 # на месте ключа находятся не изменяемые типы данных, на месте значения наоборот
         # МНОЖЕСТВА
#set_ = {1,2,3,4,5,6,7,1,2,3,4,'String',True,(1,2,3)} # хранит уникальные значения/выводит без повторений 1234
#list_=[1,2,3,4,2,5]
#print(set(list_))
#list_=set(list_)
#print(list_)
#print(list_.discard(1)) # .discard удаление/
         # не будет выдавать ошибку если элемент не был найден во множестве
#print(list_.remove(1)) # то же удаление но с ошибкой если не найдет элемент
         # можно использовать .pop
#print(list_.add(6)) # add добавляет значение
#print(list_)



my_dict = {'Max': 1800, 'Nick': 1920, 'Rick': 1999}
print(my_dict)
print(my_dict.get('Max'))
print(my_dict.get('Petr'))
my_dict.update({'Klim': 1587, 'Uran': 1212})
a = my_dict.pop("Rick")
print(a)
print(my_dict)

my_set = {1,2,3,4,5,6,7,1,2,3,4,'String',(1,2,3)}
print(my_set)
my_set.update({9,10})
my_set.discard((1,2,3))
print(my_set)