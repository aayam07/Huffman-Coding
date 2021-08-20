from huffman_art import text

class Node:
    # constructor
    def __init__(self, symbol, frequency, leftnode = None, rightnode = None):
        self.symbol = symbol # assigns the paramater symbol(on RHS) to the symbol variable of class Node
        self.frequency = frequency # assings the parameter frequency(on RHS) to self frequency
        self.leftnode = leftnode # assigns leftnode parameter(on RHS) to self leftnode (assigns None if no argument is passed into the leftnode parameter)
        self.rightnode = rightnode # assigns leftnode parameter(on RHS) to self rightnode (assigns None if no argument is passed into the rightnode parameter)
        self.huff = '' # empty string which adds tree direction as 0 for left and 1 for right (like a edge which is assigned 0 if on left and 1 if on right)

# this function helps to display huffman codes for all the symbols in the newly created huffman tree
# def displayNodes(node, value=''):

# prints Ascii art at start of our program
print(f"{text}\n\n")

# taking user input for string, and converts all the letters into lower case
string_to_compress = input("Enter the string: ").lower()

# converting user input string into a list of individual characters
string_as_list = list(string_to_compress) 

# calculating frequencies of individual characters of the user input string
freq = {} # empty dictionary
for c in string_as_list:
    if c in freq:
        freq[c] = freq[c] + 1 # if character is already present in the freq dictionary then its value is increased by 1
    else:
        freq[c] = 1 # if character is not present then a new key value pair is created where c is key and 1 is its frequency value

# sorting the contents of freq dictionary in descending order of frequency(i.e by its values)
sort_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) # sorts the dictionary by its value and stores in a form of tuples inside a list. Here the second parameter is a sorting mechanism that allows us to sort our dictionary by value. This is an example of a Lambda function, which is a function without a name.

# print(sort_freq[0][0],sort_freq[0][1]) # prints first tuple's first item and second item

print("\nFrequency of individual characters of the string in descending order:\nCharacter\tFrequency")
print("--------------------------")

nodes = [] # empty list
for (key,value) in sort_freq:
    print(f" {key} \t\t {value} ") # extracts key and value of individual tuples from sorted_freq list, then prints it
    nodes.append(Node(key,value)) # in each iteration an object of Node class is created which converts characters & frequencies into huffman tree nodes and is added to list 'nodes' 

while len(nodes) > 1:

    # picking two smallest nodes
    left = nodes[-2]
    right = nodes[-1]
    combined_symbol = left.symbol + right.symbol
    combined_frequency = left.frequency + right.frequency

    # assigning directional values to the left and right nodes above
    left.huff = 0
    right.huff = 1

    # combining the two smallest node above to create a new node which will be the parent of those two smallest nodes and its frequency will be the combined frequency if two smallest nodes
    newNode = Node(combined_symbol, combined_frequency, left, right)

    # removing the two smallest nodes and adding their parent newNode into node list 'nodes'
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)




    








