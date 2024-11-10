
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""


def mergeAlternately( word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    word1_count = 0
    word2_count = 0
    output = ""
    for i in range(len(word1) + len(word2)):
        if not i % 2:
            if word1_count < len(word1):
                output = "".join([output,word1[word1_count]])
                word1_count+=1
            else:
                output = "".join([output,word2[word2_count:]])
                break
        else:
            if word2_count < len(word2):
                output = "".join([output,word2[word2_count]])
                word2_count+=1
            else:
                output = "".join([output,word1[word1_count:]])
                break
    print(output)

mergeAlternately("xyz", "abc")