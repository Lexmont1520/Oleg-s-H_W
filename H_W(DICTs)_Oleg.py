#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={} 
n=0  
Q = int(input('Введите количество строк для ввода команд:'))
print('Введите команду:\n        ADD word1 word2 — добавить в словарь пару синонимов (word1, word2)\n        COUNT word — узнать количество синонимов слова word\n        CHECK word1 word2 — проверить, являются ли слова word1 и word2 синонимами')

while n < Q:
    input_str = input().lower().split()
    command = input_str[0] # Выделяем команду (ADD, COUNT, CHECK)
    
    if command == 'add': # ADD word1 word2
        key, val = input_str[1], input_str[2] # Это word1 и word2
        d[key] = val # Пишем в словарь key -> value
    
    elif command == 'count': # COUNT word1
        word = input_str[1]
        cnt = 0 
        for key, value in d.items(): # Получаем из словоря (key, value)
            if word == value:
                cnt +=1
            if word == key:
                cnt +=1
        print(cnt) 
    elif command == 'check': # CHECK word1 word2
        word = [input_str[1], input_str[2]] # это [word1, word2]
        flag = 'NO' # Флаг по умолчаню NO
        for key, value in d.items():
            if [key, value] == word or [value, key] == word: # Сравниваем построчно
                flag = "YES"
        print(flag)
        
    else:
        print('Ошибка ввода')
    
    n +=1 


# In[ ]:


print("Наш заполненный словарь:\n", d)


# In[ ]:


print("Ключи в словаре:\n", d.keys())


# In[ ]:


print("Значения в словаре:\n", d.values())


# In[ ]:


print("Пары в словаре:\n", d.items())


# In[ ]:




