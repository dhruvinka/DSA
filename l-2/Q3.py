# 3. Write a program to collect a sentence from user and count the frequency of:  
# a. Vowels in a sentence. 
# b. Words in a sentence. 

vowels={'a','e','i','o','u','A','E','I','O','U'}
sentence = "This is the good time to code"
vowel_count = 0
word_count = 0
fre_vi={}
fre_words={}
for char in sentence:
    if char in vowels:
        fre_vi[char]=sentence.count(char)
        vowel_count += 1
words = sentence.split()
for word in words:
    fre_words[word]=sentence.count(word)

word_count = len(words)
print("Number of vowels in the sentence:", vowel_count)
print("Number of words in the sentence:", word_count)
print("Frequency of vowels in the sentence:", fre_vi)
print("Frequency of words in the sentence:", fre_words)