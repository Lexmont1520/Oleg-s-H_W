#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import bz2
import json
import string

outDir = 'JsonFolder'
pattern = '.bz2'
bad_word = ['the', 'to', 'a', 'of', 'and', 'is', 'i', 'that', 'it', 'in', 'you', 'for', 'this', 'not', 'be', 
            'are', 'on', 'but', 'have', 'with', 'as', 'if', 'they', 'its', 'or', 'was', 'just', 'what', 'at',
            'an', 'so', 'can', 'all', 'from', 'do', 'dont', 'my', 'by', 'your', 'their', 'no', 'he', 'will', 
            'how', 'up', 'has', 'we', 'who', 'than', 'when', 'im', 'me', 'which']


# In[2]:


def readReddit(reddit_file):
    '''
        Функция для парсинга JSON файлов.
        Возвращает список списков из слов: 
        [['word','word1'],['word2','word3','word4'],......['wordN','wordN+1']]
        А так же удаляет пунктуацию, "плохие" слова, приводит весь текст к нижнему регистру.
    '''
    del_punct = lambda x: ''.join([i for i in x if i not in string.punctuation]) 
    
    with open(reddit_file) as f:
        jsonFile = [json.loads(line) for line in f]
        result = []
        for bodyText in jsonFile:
            if bodyText['body'] != '[deleted]':
                txt = bodyText['body']
                txt = del_punct(txt) 
                txt = ' '.join([i for i in txt.lower().split() if i not in bad_word])
                result.append(txt.split())
        return result


# In[3]:


for filename in os.listdir("./"): # Читаем в текущей папке список файлов
    if filename.endswith(pattern): # Ищем только файлы соответствующие pattern
        filepath = os.path.join(outDir,filename[:-4]) # Путь к папке с именем разархивированного файла
        print("Распаковываем {} в {}".format(filename, filepath))
        zipfile = bz2.BZ2File(filename) # Открываем архив
        data = zipfile.read() # получаем распакованные данные
        open(filepath, 'wb').write(data) # Записываем распакованные данные в файл
        
        # Создаем список слов из всех файлов по очередно
        wordlist=[]
        for i in readReddit(filepath):
            wordlist = wordlist + i
print('Распаковка завершена')


# In[4]:


len(wordlist)


# In[5]:


d = dict.fromkeys(wordlist, 0)

for count in wordlist:
    d[count] += 1

# Сортируем словарь по значению и по убыванию
sorted_by_value = sorted(d.items(), key=lambda x: (x[1],x[0]), reverse=True)

print('TOP20:\n',sorted_by_value[0:20])
print('\nВсего уникальных слов в словаре:', len(sorted_by_value))


# In[6]:


# Запись в файл
with open('top20.json', 'w') as outfile:  
    json.dump(sorted_by_value[0:20], outfile)


# In[7]:


# Проверяем записанный файл
with open('top20.json') as json_file:
    data = json.load(json_file)
print(data)


# In[ ]:




