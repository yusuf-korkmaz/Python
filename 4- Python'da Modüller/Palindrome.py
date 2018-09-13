# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:03:20 2016

@author: yusufkorkmaz

Belirlenen string in polindrome olup olmadığını test eden
ve sonuç olarak True veya False dönen bir modül.

isPalindrome(string,recursive veya iterative) metodu yer almakta
    Parametre olarak String ve 0 değeri girdiğinizde recursive çalışmakta
    Parametre olarak String ve 1 değeri girdiğinizde iterative çalışmakta
"""


def isPalindrome(text:str,metod:int) -> bool:
    """
    
isPalindrome metodu verilen string'i istenen metoda göre palindrome olup olmadığını sorgular
    Parametre:
        String ve 0 değeri girdiğinizde recursive çalışmakta
        String ve 1 değeri girdiğinizde iterative çalışmakta
    """
    if(metod == 0):
        return palindrome_recursive(text,metod)
    elif(metod == 1):
        return palindrome_iterative(text)
    else:
        print("Ikinci parametre olarak 0 veya 1 değerini girmeniz gerekiyor {} için".format(text))
        return False

def palindrome_recursive(text,n):
    if(" " in text) :
        text = trim_lower_recursive(text)
    if(n >= len(text)):
        return True
    else:
        if(text[n] == text[len(text)-n-1]):
            return palindrome_recursive(text,n+1)
        else:
            return False
        

def palindrome_iterative(text):
    text=trim_lower_iterative(text)
    for i in range(len(text)):
        if(text[i]==text[len(text)-i-1]):
            palindrome=True
        else:
            return False
    return palindrome

def trim_lower_recursive(text):
    text_current = text.lower()
    if(" " in text_current):
        index = text_current.index(" ")
        text_current = text_current[:index] + text_current[index+1:]
        text_current = trim_lower_recursive(text_current)
    return text_current

def trim_lower_iterative(text):
    text_current = text.lower()
    while ( " " in text_current ):
        text_current = text_current.replace(" ","")
    return text_current

def trim_lower_string_metod(text): 
    text= text.lower()
    text_dizi=text.split(" ")
    text_without_space = "".join(text_dizi)
    return text_without_space
    