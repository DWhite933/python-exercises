# Write a printASCIITable() function that displays the ASCII number and its corresponding text character, from 32 to 126. 

def printASCIITable():
    for i in range(32, 127):
        print(i, chr(i))

if __name__ == "__main__":
    printASCIITable()