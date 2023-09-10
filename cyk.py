def cyk(string_input, grammar):
  table = []                                                                    # Create an empty table (2D list) to store parsing results
  for i in range(len(string_input)):                                            # Initialize the table with empty sets for each cell
    table_row = []
    for j in range(len(string_input)):
      table_row.append(set())
    table.append(table_row)

  i = 0                                                                         # Initialize the index variable 'i' to 0 for the outer loop
  while i < len(string_input):                                                  # Iterate over each character in the input string
    char = string_input[i]
    for key, value in grammar.items():                                          # Iterate over the grammar rules
      if char in value:                                                         # Check if the character is in the set of terminals for the current grammar rule 
        table[i][i].add(key)                                                    # If found, add the nonterminal key to the cell in the parsing table
    i += 1                                                                      # Increment the index 'i' for the next character

  for i in range(2, len(string_input) + 1):                                     # Fill in the rest of the table using dynamic programming
    for j in range(len(string_input) - i + 1):
      k = j + i - 1
      for l in range(j, k):
        for key, values in grammar.items():
          for value in values:                                                  # Check if the production is of length 2
            if len(value) == 2:
              A, B = value
              if A in table[j][l] and B in table[l+1][k]:                       # Check if A can derive the substring from j to l and B can derive from l+1 to k
                table[j][k].add(key)                                            # Add the nonterminal key to the cell in the parsing table

  start_symbol = list(grammar.keys())[0]                                        # Determine the start symbol (replace with your actual start symbol)
  result = start_symbol in table[0][len(string_input) - 1]                      # Check if the start symbol is in the top-right cell of the table           

  if result:                                                                    # Print the result based on whether the string can be derived from the grammar
    print("The given string can be derived from the grammar.")
    print()
    for row in table:                                                           # Print the parsing table
      print(row)
      print()
  else:
    print("The given string cannot be derived from the grammar.")



if __name__ == "__main__":
  grammar = {}                                                                  # Define the grammar as a dictionary

  with open('input.txt', 'r') as file:                                          # Read the text file line by line
    for line in file:
      tokens = line.strip().split(' -> ')                                       # Split each line into tokens
      if len(tokens) == 2:
        nonterminal, productions = tokens
        production_list = productions.split(' | ')
        grammar[nonterminal] = production_list

  print("Grammar from the input file: ")
  for key, value in grammar.items():
    print(key, "->", value)                                                     # Print the resulting grammar dictionary
  print()

  input_string = input("Enter string: ")
  print()                                                                       # Input string to parse

  cyk(input_string, grammar)
