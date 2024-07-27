#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: remeshac
Date: 
Assignment number: HW09
Assignment title:  Working with Text

Citations and acknowledgments:
* 
Molly Halverson help me on this HW

"""
import urllib.request as web
import string


def reverse(text):
    rev_text = text[::-1]
    return rev_text


def removePunctuation(text):
    """Remove punctuation from a text.
    
    Parameter: text, a string object
    Return value: a copy of text with punctuation removed
    """

    newText = ''
    for character in text:
        if character not in string.punctuation:
            newText = newText + character
    return newText

def normalize(text):
    """Normalize a text by making it lowercase and removing punctuation.

    Parameter: text, a string object
    Return value: a normalized copy of text
    """

    newText = text.lower()
    newText = removePunctuation(newText)
    return newText

def splitIntoWords(text):
    """Split a text into words.

    Parameter: text, a string object
    Return value: the list of words in the text
    """

    wordList = []
    prevCharacter = ' '
    word = ''
    for character in text:
        if character not in string.whitespace:
            word = word + character
        elif prevCharacter not in string.whitespace:
            wordList.append(word)
            word = ''
        prevCharacter = character

    if word != '':
        wordList.append(word)

    return wordList

def wordTokens(text):
    """Break a text into words with punctuation removed.
    Parameter: text, a string object
    Return value: a list of word tokens
    """
    newText = normalize(text)
    tokens = splitIntoWords(newText)
    return tokens

def wordCount(text):
    """Count the number of words in a string.

    Parameter: text, a string object
    Return value: the number of words in text
    """
    words = wordTokens(text)
    return len(words)

def wordCountWeb(url):
    webpage = web.urlopen(url)
    rawBytes = webpage.read()
    webpage.close()

    decode_text = rawBytes.decode('utf-8')
    number_of_words = wordCount(decode_text) 
    
    return number_of_words
    
def isHTML(url):
    
    webpage = web.urlopen(url)
    rawBytes = webpage.read()
    webpage.close()
    decode_text = rawBytes.decode('utf-8')
    decode_text = decode_text.lower()
    if '<!doctype html' in decode_text:
        return True
    else:
        return False
    
def string2Digit(digitString):
    digit_int = ord(digitString) - ord('0')
    return digit_int

def username(first, last):
    name_User = last + "_" + first[0]
    return name_User

def main():
    print(isHTML("http://www.w3.org/TR/html4/strict.dtd"))
    print(username('sally', 'brown'))
    
main ()


    
    


