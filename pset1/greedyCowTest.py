# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:27:45 2016

@author: stanleykolis
"""

limit = 10.0

cows = {'Maggie': 3, 'Henrietta': 9, 'Lola': 2, 'Oreo': 6, 'Betsy': 9,
        'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Florence': 2, 'Herman': 7}

def createCowList(cows):    
        """Takes dictionary and sorts into lst of tuples based on weight"""    
        def getKey(item):
            """Helper function to sort copy of dict"""
            return item[1]
        
        # Convert dict into list of tuples and sort
        cowList = []
        for entry in cows:
            cowList.append((entry, cows[entry]))
        return sorted(cowList, key=getKey, reverse=True)
        