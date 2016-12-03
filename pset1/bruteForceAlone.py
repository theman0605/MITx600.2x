#From codereview.stackexchange.com                    

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

## Uncomment the following code  and run this file
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

    
brute_force_cow_transport({'MooMoo': 50, 'Lotus': 40, 'Horns': 25, 'Boo': 20, 'Milkshake': 40, 'Miss Bella': 25}, 100)
            
    