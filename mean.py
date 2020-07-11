# The mean is the average of all of the numbers in a list
# Add all of the numbers up, then divide that total by
# by how many numbers the are

def mean():
    # Enter a number, or 'q' to quit
    iVal = input("Enter a number for mean calculation (q to quit): ")
    iList = []  # Init empty list
    # Append input to list
    while iVal != 'q':
        iList.append(int(iVal))
        iVal = input("Enter a number for mean calculation (q to quit): ")
    # Sum list items
    iSum = sum(iList)
    # Calculate mean
    iMean = (iSum / len(iList))
    print(f"Mean: {iMean}".format('.2f'))
mean()


