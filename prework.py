# This program draws a tree based on the height entered by the user.

symbol = "#"  # The character used to draw the tree

height = int(input("Enter the height of the tree: "))

while height <= 0 or height > 23:
    if height <= 0:
        print("The height must be greater than 0.")
    else:
        print("The tree is too tall. Please enter a height of 23 or less.")

    height = int(input("Enter the height of the tree: "))

print(f"\nDrawing a tree of height {height} using '{symbol}':\n")

for row in range(height):
    spaces = (height - row - 1) * " "  # Calculate the number of spaces before the tree symbols
    tree = (2 * row + 1) * symbol      # Find the number of symbols we will need for this row
    print(spaces + tree)               # and print each row of the tree to create the final shape


