import pandas as pd
import numpy as np
import csv
from hazm import *
from math import log2


### tabe haie mored estefadeh dar hazm
normalizer = Normalizer()
tokenizer = WordTokenizer()
stemmer = Stemmer()



### golobal variation
bow_train = []
epsilon = 0.01
correct_gusse = 0
dictionary_cat = {"رمان" : 0 , "داستان کودک و نوجوانان" : 1 , "کلیات اسلام" : 2 , "داستان کوتاه" : 3 , "مدیریت و کسب و کار" : 4\
                 , "جامعه‌شناسی" : 5}
index_train = ["رمان" , "داستان کودک و نوجوانان" , "کلیات اسلام" , "داستان کوتاه" , "مدیریت و کسب و کار" , "جامعه‌شناسی"]



### be dast avardan bad words and bad punctuation
# my own bad list
bad_punctuation_marks_number = ['،' , ',' , '<' , '>' , '.' , '!' , '(' , ')' , '{' , '}' , '[' , ']' \
                                , '*' , '%' , '«' , '»' , ':' , '-' , '"' , "'" , '؛' , '۰' , '۱' , '۲'\
                                , '۳' , '۴' , '۵' , '۶' , '۷' , '۸' , '۹' , '0' , '1' , '2' , '3' , '4' \
                                , '5' , '6' , '7' , '8' , '9' , ';' , '.' , ' در ' , ' تا ' , ' را ' , ' از ' , ' که ']
# emtiazi 2 read from csv
file = open("sw.csv", "r")
data = list(csv.reader(file))
file.close()
for i in range(len(data)) :
    try :
        string = ' ' + data[i][0] + ' '
        bad_punctuation_marks_number.append(string)
    except :
        continue



### tabe baraie khandan csv ha
def read_csvs():
    dt_train = pd.read_csv("books_train.csv")
    dt_test = pd.read_csv("books_test.csv")
    return dt_train , dt_test

dataframe_train , dataframe_test = read_csvs()



### tabe baraie hazf kalamat dar list bad_punctuation_marks_number
def remove_numbers_marks(dataframe):
    for marks in bad_punctuation_marks_number :
        try :
            dataframe = dataframe.replace(marks , ' ')
        except :
            continue
    return dataframe


### functoin to stemmer words in train and test
def risheyabi(dataframe):
    dataframe = stemmer.stem(dataframe)
    return dataframe


### tabe baraie normalize kardan matn
def normalize_strings(dataframe) :
    dataframe = normalizer.normalize(dataframe)
    return dataframe

### function to edit text train and test
def edit_texts(data) :
    for i in range(len(data)) :
        data['description'][i] = normalize_strings(data['description'][i])
        # data['description'][i] = risheyabi(data['description'][i])
        data['description'][i] = remove_numbers_marks(data['description'][i])
    return data
        
dataframe_train = edit_texts(dataframe_train)
dataframe_test = edit_texts(dataframe_test)


###############################   dataframe algorithm  ###################################
### apply kardan taghirat lazem dar dataframe haie train va test
# dataframe_train = dataframe_train.apply(np.vectorize(remove_numbers_marks))
# dataframe_train = dataframe_train.apply(np.vectorize(normalize_strings))
# dataframe_test = dataframe_test.apply(np.vectorize(remove_numbers_marks))
# dataframe_test = dataframe_test.apply(np.vectorize(normalize_strings))


### dar avardan tamam kalamat va kalamat har categories
def create_list_of_words_for_all_categories(dataframe) :
    cat_roman , cat_kodak_nojavan , cat_eslam , cat_dastan_kotah , cat_modiriat , cat_jamee_shenasi , all_word = '' , '' , '' , '' , '' , '' , ''
    
    for row in range(len(dataframe)) :
        index = dictionary_cat[dataframe['categories'][row]]
        string = dataframe["description"][row] + ' ' + dataframe["title"][row]
        if index == 0 :
            cat_roman = cat_roman + ' ' + string
            all_word = all_word + ' ' + string
        elif index == 1 :
            cat_kodak_nojavan = cat_kodak_nojavan + ' ' + string
            all_word = all_word + ' ' + string
        elif index == 2 :
            cat_eslam = cat_eslam + ' ' + string
            all_word = all_word + ' ' + string
        elif index == 3 :
            cat_dastan_kotah = cat_dastan_kotah + ' ' + string
            all_word = all_word + ' ' + string
        elif index == 4 :
            cat_modiriat = cat_modiriat + ' ' + string
            all_word = all_word + ' ' + string
        elif index == 5 :
            cat_jamee_shenasi = cat_jamee_shenasi + ' ' + string
            all_word = all_word + ' ' + string
            
    return tokenizer.tokenize(all_word) , tokenizer.tokenize(cat_roman) , tokenizer.tokenize(cat_kodak_nojavan) , tokenizer.tokenize(cat_eslam) \
        , tokenizer.tokenize(cat_dastan_kotah) , tokenizer.tokenize(cat_modiriat) , tokenizer.tokenize(cat_jamee_shenasi)

all_word , word_cat_roman , word_cat_kodak_nojavan , word_cat_eslam , \
word_cat_dastan_kotah , word_cat_modiriat , word_cat_jamee_shenasi = create_list_of_words_for_all_categories(dataframe_train)
# ###################################################################################33
# def ppp(lcat) :
#     l = []
#     for word in lcat :
#         word = stemmer.stem(word)
#         l.append(word)
#     return l
# all_word = ppp(all_word)
# word_cat_roman = ppp(word_cat_roman)
# word_cat_kodak_nojavan = ppp(word_cat_kodak_nojavan)
# word_cat_eslam == ppp(word_cat_eslam)
# word_cat_dastan_kotah = ppp(word_cat_dastan_kotah)
# word_cat_modiriat = ppp(word_cat_modiriat)
# word_cat_jamee_shenasi = ppp(word_cat_jamee_shenasi)

# def create_dicts1(list) :
#     dict = {}
#     for word in list :
#         if word in dict :
#             dict[word] += 1
#         else : 
#             dict[word] = 1
#     return dict

# dictionary_all_word = create_dicts1(all_word)
# dictionary_word_roman = create_dicts1(word_cat_roman)
# dictionary_word_kodak_nojavan = create_dicts1(word_cat_kodak_nojavan)
# dictionary_word_eslam = create_dicts1(word_cat_eslam)
# dictionary_word_dastan_kotah = create_dicts1(word_cat_dastan_kotah)
# dictionary_word_modiriat = create_dicts1(word_cat_modiriat)
# dictionary_word_jamee_shenasi = create_dicts1(word_cat_jamee_shenasi)
# #######################################################################################

### function to convert list to dictionary and fill valeu with 0
def create_dicts(list) :
    dict = {}
    for word in list :
        dict[word] = 0
    return dict

dictionary_all_word = create_dicts(all_word)
dictionary_word_roman = create_dicts(word_cat_roman)
dictionary_word_kodak_nojavan = create_dicts(word_cat_kodak_nojavan)
dictionary_word_eslam = create_dicts(word_cat_eslam)
dictionary_word_dastan_kotah = create_dicts(word_cat_dastan_kotah)
dictionary_word_modiriat = create_dicts(word_cat_modiriat)
dictionary_word_jamee_shenasi = create_dicts(word_cat_jamee_shenasi)


### functions to count words and save them in dictionary
def extention_count(list_word , cat_word) :
    for word in list_word :
        dictionary_all_word[word] += 1
        cat_word[word] += 1

def count_words_in_csv (dataframe) :
    for row in range(len(dataframe)) :
        index = dictionary_cat[dataframe['categories'][row]]
        string = dataframe["description"][row] + ' ' + dataframe["title"][row]
        list_word = tokenizer.tokenize(string)
        if index == 0 :
            extention_count(list_word , dictionary_word_roman)
        elif index == 1:
            extention_count(list_word , dictionary_word_kodak_nojavan)
        elif index == 2:
            extention_count(list_word , dictionary_word_eslam)
        elif index == 3:
            extention_count(list_word , dictionary_word_dastan_kotah)
        elif index == 4:
            extention_count(list_word , dictionary_word_modiriat)
        elif index == 5:
            extention_count(list_word , dictionary_word_jamee_shenasi)
            
count_words_in_csv(dataframe_train)

# print(len(dictionary_all_word))
### appends our dictionary to one dictionary for orgenize words
bow_train.append(dictionary_word_roman)
bow_train.append(dictionary_word_kodak_nojavan)
bow_train.append(dictionary_word_eslam)
bow_train.append(dictionary_word_dastan_kotah)
bow_train.append(dictionary_word_modiriat)
bow_train.append(dictionary_word_jamee_shenasi)

## gereftan miangin in list ---> ehtemal ha

def prob_bow_train (list_of_dicts) :
    for i in range(len(list_of_dicts)) :
        for j in list_of_dicts[i].keys() :
            list_of_dicts[i][j] /= len(list_of_dicts[i])
            
prob_bow_train(bow_train)

###############################   dataframe algorithm   #################################

### be dast avardan categories to join dataframe train
# def convert_dict_cat_to_list(dict_cat) :
#     list_categories = []
#     for cat in dict_cat.keys() :
#         list_categories.append(cat)
#     return list_categories

### create dataframe train
# bow_dataframe_train = pd.DataFrame.from_dict(bow_train)
# bow_dataframe_train = bow_dataframe_train.fillna(0)
# bow_dataframe_train['sum'] = bow_dataframe_train.sum(axis = 1)
# sumation = bow_dataframe_train['sum'].to_list()
# bow_dataframe_train = bow_dataframe_train.divide(sumation , axis = 0)
# # list_categories = convert_dict_cat_to_list(dictionary_cat)
# colum_categories = pd.DataFrame(index_train)
# bow_dataframe_train = bow_dataframe_train.join(colum_categories)

### create bow test
def create_bow_test(dataframe):
    all_strings = ''
    string = ''
    list_of_dictionary_of_all_books = []
    list_categories_of_books = []
    for row in range(len(dataframe)) :
        string = dataframe['description'][row] + ' ' + dataframe['title'][row]
        all_strings = all_strings + ' ' + string
        list_categories_of_books.append(dataframe['categories'][row])
        list_of_word_in_one_book = tokenizer.tokenize(string)
        dictionary_of_one_book = create_dicts(list_of_word_in_one_book)
        for word in list_of_word_in_one_book :
            dictionary_of_one_book[word] += 1
        list_of_dictionary_of_all_books.append(dictionary_of_one_book)
            
    return list_of_dictionary_of_all_books , list_categories_of_books

bow_test , categories_of_books = create_bow_test(dataframe_test)


###############################   dataframe algorithm   #################################

# bow_dataframe_test = pd.DataFrame.from_dict(bow_test)
# bow_dataframe_test = bow_dataframe_test.fillna(0)
# colum_categories_books = pd.DataFrame(categories_of_books)
# bow_dataframe_test = bow_dataframe_test.join(colum_categories_books)

# print(bow_dataframe_train)
# print(bow_dataframe_test)

# correct_gusse = 0
# def calculate_probability(dataframe_test , dataframe_train = bow_dataframe_train) :
#     category_book = dataframe_test[0]
#     probability_of_each_cat = []
#     dataframe_test = dataframe_test.to_dict()
#     for i in range(len(index_train)) :
#         probability = 0
#         for word in dataframe_test.keys():
#             try :
#                 # print(word , dataframe_train[word][i])
#                 if dataframe_train[word][i] != 0 :
#                     probability += dataframe_test[word] * log2(dataframe_train[word][i])
#             except :
#                   len_word_cat = find_len_cat(category_book) 
#                   probibility += log2((list_of_dicts_test[book][word] * epsilon) / ((list_of_dicts_test[book][word] * epsilon) + len_word_cat))
#         probability_of_each_cat.append(probability)
#     print(probability_of_each_cat)
#     min_prob = max(probability_of_each_cat)
#     index_prob = probability_of_each_cat.index(min_prob)
#     print(index_prob)
#     global correct_gusse
#     gusse_category = index_train[index_prob]
#     if gusse_category == category_book :
#         correct_gusse += 1
        
        
def find_len_cat(cat):
    indexc = dictionary_cat[cat]
    if indexc == 0 :
        return len(dictionary_word_roman)
    elif indexc == 1 :
        return len(dictionary_word_kodak_nojavan)
    elif indexc == 2 :
        return len(dictionary_word_eslam)
    elif indexc == 3 :
        return len(dictionary_word_dastan_kotah)
    elif indexc == 4 :
        return len(dictionary_word_modiriat)
    elif indexc == 5 :
        return len(dictionary_word_jamee_shenasi)


def calculate_probibility(list_of_dicts_train , list_of_dicts_test , category_of_books) :
    for book in range(len(list_of_dicts_test)) :
        category_book = category_of_books[book]
        probability_of_each_cat = []
        for j in range(len(index_train)) :
            probibility = 0
            for word in list_of_dicts_test[book].keys() :
                try :
                    if list_of_dicts_test[book][word] != 0 :
                        probibility += log2(list_of_dicts_test[book][word] * (list_of_dicts_train[j][word]))
                except:
                    # continue
                    len_word_cat = find_len_cat(category_book) 
                    probibility += log2((list_of_dicts_test[book][word] * epsilon) / ((list_of_dicts_test[book][word] * epsilon) + len_word_cat))
                    
            probability_of_each_cat.append(probibility)
        min_prob = max(probability_of_each_cat)
        index_prob = probability_of_each_cat.index(min_prob)
        global correct_gusse
        gusse_category = index_train[index_prob]
        if gusse_category == category_book :
            correct_gusse += 1

calculate_probibility(bow_train , bow_test , categories_of_books)
print(correct_gusse)
print(correct_gusse / 450 * 100 , "%" , sep='')