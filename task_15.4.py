# первая задача
# import string
import re

file_name = input("Введите имя файла: ")
my_file = open(file_name, 'rt', encoding="utf8")
# print(my_file.read())
text_before = my_file.read()
my_file.close()

text = re.sub("[^A-Za-z0-9А-Яа-я ]", "", text_before).split()
# print(text)
# text = [i.strip(string.punctuation) for i in text_before.split()]
# print(text)
count = {}
def word_frequency():
    for word in text:
        if len(word)<=3:
            pass
        elif len(word)>3 and word in count:
            count[word] += 1
        else:
            count[word] = 1
    # print(count)
word_frequency()

def word_max_frequency():
    max_word = max(list(count.items()), key=lambda i: i[1])
    print(f"Слово {max_word[0]} встречается в тексте файла {max_word[1]} раз.")
word_max_frequency()

english_words = re.split(r"[^A-Za-z]", text_before.strip())
# print(english_words)
length_english_word = {}
def english_word_max_len():
    for word in english_words:
        if word not in length_english_word:
            length_english_word[word] = len(word)
        else:
            pass
    max_length = max(list(length_english_word.items()), key=lambda i: i[1])
    print(f"Самое длинное английское слово в тексте файла - {max_length[0]}, длиной в {max_length[1]} символов.")
english_word_max_len()

# следующая задача
import json

with open('jsonfile.json') as file:
    fileObjects = json.load(file)
# print(fileObjects)
# print(type(fileObjects))
sample_answer = {'timestamp': 123,
                 'referer': 'abc(url)',
                 'location': 'abc(url)',
                 'remoteHost': 'abc',
                 'partyId': 'abc',
                 'sessionId': 'abc',
                 'pageViewId': 'abc',
                 'eventType': 'abc (itemBuyEvent или itemViewEvent)',
                 'item_id': 'abc',
                 'item_price': 123,
                 'item_url': 'abc (url)',
                 'basket_price': 'abc',
                 'detectedDuplicate': True,
                 'detectedCorruption': True,
                 'firstInSession': True,
                 'userAgentName': 'abc'
                 }
# print(len(fileObjects))
sample_values_ = list(sample_answer.values())
# print(sample_values_)
sample_class__ = list(type(i) for i in sample_values_)
# print(sample_class__)

def answer_test():
    for i in range(1, (len(fileObjects)+1)):
        object_i = fileObjects[i-1]
        # print(object_i)
        keys_i = object_i.keys()
        # print(keys_i)
        values_i = list(object_i.values())
        # print(values_i)
        types_j = list(type(j) for j in values_i)
        # print(types_j)
        contain_i = 'http' in values_i[1] and 'http' in values_i[2] and 'http' in values_i[10] and 'itemBuyEvent' in values_i[7] or 'itemViewEvent' in values_i[7]
        # print(contain_i)
    if keys_i == sample_answer.keys():
        print("Test for answer keys pass.")
    if types_j == sample_class__ and contain_i:
        print("Test for answer values pass.")

answer_test()