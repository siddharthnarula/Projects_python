
            
def read_book(title_path):
        with open(title_path,"r",encoding="utf8") as current_file:
            text=current_file.read()
            text=text.replace("\n","").replace("\r","")
        return text
    
def count_words_fast(text):
    text=text.lower()
    ham=0
    skip=[".","'",",",'"',";",":"]
    for s in skip:
        text=text.replace(s,"")

    word_count=Counter(text.split(" "))
    return word_count




def word(word_count):
    '''Return No of words and frequesncies'''
    num_unique=len(word_count)
    count=word_count.values()
    return(num_unique,count)

from collections import Counter
import os
import pandas as pd
stats=pd.DataFrame(columns=("Language","Author","Title","Length","Unique"))
title_num=1
book_dir="./Books"
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" +language):
        for title in os .listdir(book_dir +"/"+language +"/" + author):
            if title=="Hamlet.txt":
                inputfile=book_dir +"/"+language +"/" + author + "/" + title
                text=read_book(inputfile)
                print(inputfile)
                (num_unique,count)=word(count_words_fast(text))
                stats.loc[title_num]=language,author.capitalize(),title.replace(".txt",""),sum(count),num_unique
                title_num+=1
'''          
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
subset=stats[stats.Language=="English"]
plt.loglog(subset.Length, subset.Unique,"o",label="English",color="crimson")


subset=stats[stats.Language=="French"]
plt.loglog(subset.Length, subset.Unique,"o",label="French",color="forestgreen")

subset=stats[stats.Language=="German"]
plt.loglog(subset.Length, subset.Unique,"o",label="German",color="orange")

subset=stats[stats.Language=="Portuguese"]
plt.loglog(subset.Length, subset.Unique,"o",label="Portugese",color="blueviolet")

plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of Unique words")
plt.savefig("lang_plot.pdf")'''