from huffman_art import art

class Node:
    # constructor
    def __init__(self, symbol, frequency, leftnode = None, rightnode = None):
        self.symbol = symbol # assigns the paramater symbol(on RHS) to the symbol variable of class Node
        self.frequency = frequency # assings the parameter frequency(on RHS) to self frequency
        self.leftnode = leftnode # assigns leftnode parameter(on RHS) to self leftnode (assigns None if no argument is passed into the leftnode parameter)
        self.rightnode = rightnode # assigns leftnode parameter(on RHS) to self rightnode (assigns None if no argument is passed into the rightnode parameter)
        self.huffcode = '' # empty string which adds tree direction as 0 for left and 1 for right (like a edge which is assigned 0 if on left and 1 if on right)

coded_dict = {} # empty dictionary to add every symbol as key and its huffman code as value in the displayNodes function below. This dictionary is later used to uncompress our huffman code.

# this function helps to display huffman codes for all the symbols in the newly created huffman tree
def displayNodes(node, huffvalue=''):
    global coded_dict  # declaring coded_dict dictionary as a global variable to use it inside this function
    new_huffValue = huffvalue + str(node.huffcode)
    if node.leftnode:
        displayNodes(node.leftnode, new_huffValue) # calling this same function recursively until the left node of the node is None
    if node.rightnode:
        displayNodes(node.rightnode, new_huffValue) # calling this same function recursively until the right node of the the node is None
    
    if not node.leftnode and not node.rightnode:
        print(f"{node.symbol} \t\t {new_huffValue}")
        coded_dict[node.symbol] = new_huffValue # adds node.symbol as key and new_huffvalue as key's value in coded_dict as a new key-value pair

decoded_string = ''
#function to uncompress the Huffman Code we obtain 
def decode(node, to_decode):
    global decoded_string
    i=0
    huffman_code = ''
    while node.leftnode or node.rightnode:
        if to_decode[i] == '0':
            node = node.leftnode
            huffman_code += str(node.huffcode)
        if to_decode[i] == '1':
            node = node.rightnode
            huffman_code += str(node.huffcode)
        i = i+1

    if node.symbol == "' '": # if single quotation 
        node.symbol = ' ' # then replacing it with a space
        decoded_string += node.symbol
    else:
        decoded_string += node.symbol

    new_to_decode = to_decode.replace(huffman_code,"",1) # replaces the huffman code of a particular symbol with empty string to decode the remaining string bits
    return new_to_decode

# prints Ascii art at start of our program
print(f"{art}\n\n")

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

print("\nFrequency of individual characters of the string in descending order below:\n\nCharacter\tFrequency")
print("--------------------------")

nodes = [] # empty list
for (key,value) in sort_freq:
    if key == ' ':
        key = "' '"
    print(f" {key} \t\t {value} ") # extracts key and value of individual tuples from sorted_freq list, then prints it
    nodes.append(Node(key,value)) # in each iteration an object of Node class is created which converts characters & frequencies into huffman tree nodes and is added to list 'nodes' 

#logic for compression
while len(nodes) > 1:

    # picking two smallest nodes
    left = nodes[-2]
    right = nodes[-1]
    combined_symbol = left.symbol + right.symbol
    combined_frequency = left.frequency + right.frequency

    # assigning directional values to the left and right nodes
    left.huffcode = 0
    right.huffcode = 1

    # combining the two smallest node above to create a new node which will be the parent of those two smallest nodes and its frequency will be the combined frequency if two smallest nodes
    newNode = Node(combined_symbol, combined_frequency, left, right) # newNode is an object of Node class

    # removing the two smallest nodes and adding their parent newNode into node list 'nodes'
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

    # Sorting all the nodes inside list 'nodes' in descending order of their frequencies
    nodes = sorted(nodes, key=lambda x: x.frequency, reverse=True)

# during this instance the 'nodes' list will contain only one node, 
# which would be the root of our tree with the final combined frequency
# and this node will be at index 0 of the list and is passed to displayNodes function as a keyword argument
print("\nCharacters with Huffman Code assigned below:\n\nCharacter\tHuffman Code")
print("----------------------------")
displayNodes(node = nodes[0]) 

# print(coded_dict) # prints the coded_dict dictionary with all the keys and values of encoded huff code

# replacing ' ' key in dictionary with an actual space to print below
if "' '" in coded_dict:
    coded_dict[" "] = coded_dict["' '"]
    del coded_dict["' '"]

code_to_decode = ''
for c in string_to_compress:
        code_to_decode += coded_dict[c] # returns the value associated with character 'c' which is the key of dictionary 'coded_dict'
        
#print(string_to_compress.count(item))
print(f"\nThe required Huffman Code for '{string_to_compress}' is {code_to_decode}\n")


# Uncompression
want_to_uncompress = input("Do you also want to uncompress the Huffman Code above(y/n): ").lower()

if want_to_uncompress == 'y':
    # logic to uncompress
    while code_to_decode != '':
        new_to_decode = decode(node = nodes[0], to_decode = code_to_decode)
        code_to_decode = new_to_decode
    
    print(f"\nThe decoded string for the Huffman Code obtained above is '{decoded_string}'")
else:
    print("Thank You!")      
