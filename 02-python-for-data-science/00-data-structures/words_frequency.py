"""
Words Frequency in a Sentence
Count Word Frequency

Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596165#overview

Parameters:

sentence (str): The input sentence where you need to count the frequency of each word.

Returns:

A dictionary where the keys are words from the sentence and the values are their corresponding frequencies.

Example:

Input: "hello world hello"
Output: {'hello': 2, 'world': 1}

Input: "the quick brown fox jumps over the lazy dog"
Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
"""
def count_word_frequency(sentence):
    count_dict = {}
    words_list = sentence.split()
    for word in words_list:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return count_dict
if __name__ == "__main__":
    sample_input = "the quick brown fox jumps over the lazy dog"
    print("Output : ",count_word_frequency(sample_input))