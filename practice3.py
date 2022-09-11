# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# election_data.close()
# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)



# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# ## Using the open() function with the "w" mode we will write data to the file.
# #open(file_to_save, "w")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")

# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # # Write some data to the file.
    #  txt_file.write("Hello World")

    # Write three counties to the file.
    #  txt_file.write("Arapahoe, ")
    #  txt_file.write("Denver, ")
    #  txt_file.write("Jefferson, ")

     #txt_file.write("Arapahoe, Denver, Jefferson")
     #txt_file.write("Arapahoe\nDenver\nJefferson")
     txt_file.write("Counties in the Election\n------------------------\nArapahoe, Denver, Jefferson")

     






