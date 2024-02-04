#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m*n - 1
        while beg < end:
            mid = (beg + end)//2
            if matrix[mid//m][mid%m] < target:
                beg = mid + 1
            else:
                end = mid
        return matrix[beg//m][beg%m] == target


# In[10]:


def count_word_frequencies(input_string):
    # Split the input string into words
    words = input_string.split()

    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

def find_highest_frequency_word(input_string):
    word_freq = count_word_frequencies(input_string)

    # Find the word with the highest frequency
    highest_freq_word = max(word_freq, key=word_freq.get)

    return highest_freq_word, len(highest_freq_word)

# Example usage
input_str = "write write write all the number from from from 1 to 100"
highest_word, highest_word_length = find_highest_frequency_word(input_str)
print(f"The highest-frequency word is '{highest_word}' with a length of {highest_word_length}.")


