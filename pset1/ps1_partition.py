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

# Uncomment the following code  and run this file
# to see what get_partitions does if you want to visualize it:

entrySum = 0
a = get_partitions(range(3))
for entry in a:
    print (entry, len(entry))
    if len(entry) ==  1:
        print(entry)
    else:
        print(str(entry) + ' - Length is > 1')
        print('Breaking out of loop')
        break
print("That's it...for now!")


for item in a:
    print('Printing item: ' + str(item) + '-' + str(type(item)))
    for entry in item:
        print('     Printing entry: ' + str(entry) + ': ' + str(type(entry)))
        for letter in entry:
            print('          Printing letter: ' + str(letter))
            
    