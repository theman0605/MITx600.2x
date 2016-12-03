# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),
         ('Wannabe',2.7, 1.2)]

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """

    workingList = songs[:]
    if workingList[0][2] <= max_size:
        workingSize = workingList[0][2]
        returnList = [workingList[0][0]]
        for entry in sorted(workingList[1:], key=lambda entry: entry[2]):
            if entry[2] + workingSize <= max_size:
                returnList.append(entry[0])
                workingSize += entry[2]
            else:
                break
        return returnList
    else:
        return []

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """

    if L == []:
        return('no solution')
    
    multList = []
    workingSum = s    
    multiplier = 0    
    for entry in L:
        while workingSum >= 0:
            if entry * multiplier <= workingSum:
                multiplier += 1
            else:
                multList.append(multiplier - 1)
                break
        multiplier = 0
        workingSum -= entry * multList[-1]
    finalTest = 0
    for idx, entry in enumerate(L):
        finalTest += entry * multList[idx]
    if finalTest == s:
        return sum(multList)
    else:
        return('no solution')

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE    
    def subsequences(iterable, length):
        return [iterable[i: i + length] for i in range(len(iterable) - length + 1)]
    
    maxSum = 0
    for i in range(len(L)+1):
        a = subsequences(L, i)
        for entry in a:
            if sum(entry) > maxSum:
                maxSum = sum(entry)
    return(maxSum)
            
    