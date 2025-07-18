'''
Leftover Blocks

You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.

Input: Integer (number of available blocks)
Output: Integer (number of blocks leftover after tallest valid structure built)

Explicit rules:
    - Structures are built with blocks:
        - Blocks are cubes.
        - Cubes are six-sided, have square faces, and have equal
        lengths on all sides.
    - The top layer in the structure consists of a single block.
    - Upper layer blocks must be supported by four lower layer blocks.
    - Lower layer blocks can support more than one upper layer block.
    - Layers are solid structures -- there are no gaps between blocks.

Implicit rules:
    - Layer number correlates with blocks in a layer:
    - The number of blocks in a layer is layer number * layer number.

Questions: 
    - Is a lower layer valid if it has more blocks than it needs? (No)
    - Will there always be left-over blocks? (No)

Data structures: 
    - Perhaps we can use a nested list to represent the structure?
    - Each sublist could represent a layer.


    [
        ['x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ...
    ]

Algorithm: 
    1. Start with:
     - The "number of blocks remaining" is equal to the input.
     - The "current layer number" is layer 0.

    2. Calculate the "current layer number" for the next layer by
    adding 1 to the "current layer number".

    3. Using the new "current layer number", calculate the "number of
    blocks required in this layer" by multiplying the "current
    layer number" by itself.

    4. Determine whether the "number of blocks remaining" is greater
    than or equal to the "number of blocks required in this layer".
        - If there are enough blocks:
            - Subtract the "number of blocks required in this layer"
            from the "number of blocks remaining".
            - Go to step 2.
        - If there aren't enough blocks:
            - Return the "number of blocks remaining".
'''

def calculate_leftover_blocks(n):
    current_layer = 0
    remaining_blocks = n

    required_blocks = (current_layer + 1) ** 2

    while remaining_blocks >= required_blocks:
        remaining_blocks -= required_blocks
        current_layer += 1
        required_blocks = (current_layer + 1) ** 2

    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True