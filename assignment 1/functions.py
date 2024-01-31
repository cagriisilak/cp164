"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-09-18"
-------------------------------------------------------
"""
# Imports

# Constants

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    print(f"Values: {values}")
    clean = False
    cleanlist = []
    cleanlist.append(values[0])
    for i in values:
        for j in cleanlist:
            if j == i:
                clean = True
        if clean == False:
            cleanlist.append(i)
        elif clean == True:
            clean = False
    values = cleanlist[:]
    print(f"Cleaned: {values}")
    return values


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    Leap_year = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                Leap_year = True
        else:
            Leap_year = True
    return Leap_year


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = True
    s = s.lower()
    for i in range(0,len(s)-1):
        j = len(s) -1 - i
        if s[i] != s[j]:
            palindrome = False
    return palindrome
    
def median_scores(fv):
    """
    -------------------------------------------------------
    Determines the median of a series of integers in a file.
    Use: median = median_scores(fv)
    -------------------------------------------------------
    Parameters:
        fv - a file variable for an already open file of integers (file)
    Returns:
        median - the median of the values in the file (float)
    -------------------------------------------------------
    """
    list = []
    string = ''
    for line in fv:
        string = string + line
    list = string.split('\n')
    for i in range(0,len(list)):
        list[i] = int(list[i])
    list.sort()
    if len(list)%2 == 0:
        half = len(list)/2
        half2 = len(list)/2 +1
        median = (list[half] + list[half2])/2
    else:
        half = len(list)//2
        median = list[half]
    return median
        

def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total  = 0
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            if a[i][j] < small:
                small = a[i][j]
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            if a[i][j] > large:
                large = a[i][j]
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            total = total + a[i][j]
    average = total/(len(a)*2)
    return small,large,total,average
    

def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    b = []
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            b.append(a[i][j])
    return b
    
    
def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            if j == (len(a[i])-1):
                print(f"{a[i][j]:>2}",end ='\n')
            else:
                print(f"{a[i][j]:>2} ",end ='')
    b = []
    for i in range(0,len(a[0])):
        b.append([])
    for i in range(0,len(a[i])):
        for j in range(len(a)-1,-1,-1):
            b[i].append(a[j][i])
    return b


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    cap =False
    if word[0].isupper() ==True:
        cap = True
    word_lower = word.lower()
    if word_lower.startswith('a') == True or word_lower.startswith('o') == True or word_lower.startswith('u') == True or word_lower.startswith('i') == True or word_lower.startswith('e') == True:
        word_lower = word_lower + 'way'
        if cap ==True:
            pl = word_lower[0].upper() +word_lower[1:]
        else:
            pl = word_lower
    else:
        vowel_find = -1
        list = ['a','o','u','i','e']
        i = 0
        while vowel_find == -1:
            vowel_find = word_lower.find(list[i])
            if vowel_find == -1:
                i = i+1
        j = vowel_find
        word_lower = word_lower[j:] + word_lower[:j]
        word_lower = word_lower + 'ay'
        if cap ==True:
            pl = word_lower[0].upper() +word_lower[1:]
        else:
            pl = word_lower
    return pl


def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    estring = string
    for i in range(0,26):
        srch = string.count(ALPH[i])
        estring_fake = string.replace(ALPH[i],ciphertext[i],srch)
        for i in range(0,len(estring_fake)):
            if estring_fake[i] != string[i]:
                estring = estring[0:i] + estring_fake[i] + estring[i+1:]
    print(estring)
    fh = open('substitute.txt','a')
    fh.write(f"{estring}\n")
    return estring
        
        
    
