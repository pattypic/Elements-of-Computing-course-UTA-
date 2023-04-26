# File: Benford.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 03/28/2023
# Description of Program: 
# This program reads census data from a file and calculates the frequency distribution of the first digit of the population counts for 
# cities in the US. The Benford's Law is used to compare the calculated distribution with the expected distribution of leading digits. 
# The results are written to a file named "benford.txt".
import os.path

def main():
    # Create dictionary for leading digit counts
    lead_counts = {str(i): 0 for i in range(1, 10)}
    
    #Accept from the user the name of a file, containing the census data. If no file of that name exists, print an error message and quit
    fileName = input("Enter the name of the file containing the census data: ")
    # check if file exists
    if not os.path.isfile(fileName):
        print("Error: file not found.")
        return
    # Opens file and reads contents
    CSfile = open(fileName, 'r')
    next(CSfile) #skip h eader
    # Initalize variables
    total_populations = 0
    unique_pop = set()
    # loops through each line of the file
    for line in CSfile:
        # Parse the line to extract the population number
        population_str = line.strip().split()[-1]
        # Check if population is a valid integer
        if population_str.isdigit():
            population = int(population_str)
            # Add population to set
            unique_pop.add(population)
            # Get the first digit of the population and increment its count
            first_digit = str(population)[0]
            lead_counts[first_digit] += 1
            # Increment the total number of populations
            total_populations += 1
        
    CSfile.close()
    # Write results to file
    print("Output written to benford.txt")
    BEN = open('benford.txt', 'w')
    BEN.write(f"Total number of cities: {total_populations}\n")
    BEN.write(f"Unique population count: {len(unique_pop)}\n")
    BEN.write("First digit frequency distributions:\n")
    BEN.write("Digit    Count   Percentage\n")
    for digit in range(1, 10):
        digit_str = str(digit)
        count = lead_counts[digit_str]
        percent = count / total_populations * 100
        BEN.write(f"{digit_str}\t\t {count}\t {percent:.1f}\n")
    BEN.close()

main()