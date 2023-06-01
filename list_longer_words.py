def find_long_words(words,n):
    result=[]
    for word in words:
        if len(word)>n:
            result.append(word)
            return result

words_list=["Apple","banana","Mango","Orange","Gripsss"
            "Goat"]
min_length=int(input("Enter your  minmum length:\n"))
longest_word=find_long_words(words_list,min_length)
print(longest_word)
