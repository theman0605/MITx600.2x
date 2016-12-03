###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
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
    
    def updateWorkingList(transportList, workingList):
       newList = []
       for entry in workingList:
           if entry[0] not in transportList:
               newList.append(entry)
       return newList
    
    # Initialize mutable cowlist
    workingList = createCowList(cows)

    # Initialize working variables and lists    
    totalWeight = 0.0
    transportList = []
    totalList = []
    
    # Scan through sorted list and add cows into the individual
    # transportList.
    while workingList:    
        for entry in workingList:
            if totalWeight + entry[1] <= limit:
                transportList.append(entry[0])
                totalWeight += entry[1]
        totalList.append(transportList)
        
        # Update workingList and reinitilize variables.
        workingList = updateWorkingList(transportList, workingList)
        totalWeight = 0.0
        transportList = []

    return totalList
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
        
    def createCowList(cows):    
        """Takes dictionary and sorts keys into list"""    
        cowList = []
        for entry in cows:
            cowList.append(entry)
        return cowList
    
    def analyzeOption(transportList, cowWeights, limit):
        """
        Analyzes weights of transport suggestion to see if they meet the
        requirements.  Takes in the option from the generator
        (transportList), the dictionary of cows(cowWeights), and the
        transport limit (limit)
        """
        for entry in transportList:
            totalWeight = 0.0
            for cow in entry:            
                totalWeight += cows[cow]                
                if totalWeight > limit:
                    return False
        return True
            
    # Create mutable list of cow names
    workingList = createCowList(cows)

    # Use helper function above to generate partition brute force list of
    # partitions.  Don't generate them all at once, though!  Will take too
    # long, will be a long list, and it isn't necessary to generate the
    # longer list if a shorter list will work!
    
    options = get_partitions(workingList)
    y = False
    xCount = 0
    trueCombos = []    
    for x in options:    
        xCount +=1        
        y = analyzeOption(x, cows, limit)
        #print(x,y)
        if y == True:    
            trueCombos.append(x)
    trueCombos = sorted(trueCombos, key=len, reverse=False)   
    return trueCombos[0]

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows)
    end = time.time()
    print('Greedy Cow: %d' % (end-start))
    
    start = time.time()
    brute_force_cow_transport(cows)
    end = time.time()
    print('Brute Force Cow: %d' % (end-start))
   


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


