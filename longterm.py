import json

# The name of the text file you must create. Do not change it -
# the marker looks for this exact filename.
OUTFILE = "calculations.txt"


def saveJsonFile():
    try:
        with open('newZooAnimals.json', 'w') as NZA:
            toStore = [
                {
                    "name": "bob",
                    "age": 20,
                    "species": "crocodile"
                },
                {
                    "name": "susan",
                    "age": 10,
                    "species": "pigeon"
                }
            ]
            json.dump(toStore, NZA)
    except FileNotFoundError as Fnf:
        print(f"Could not find file {Fnf.filename}")


def saveTextFile(multiple, valueArray, value2):
    # TODO 1: Start with 'multiple' and multiply it by every value in
    # valueArray, then divide that answer by value2.
    # For example: 5 with [1, 3, 5, 7] and value2 = 2
    #              gives 5*1*3*5*7 = 525, then 525 / 2 = 262.5
    

    result = multiple
    # accumulate and multiply here
    for v in valueArray:
        result = result * v
       

    # TODO 2: Write the multiple used, the full list of values, and the
    # final answer into the file named by OUTFILE.
    # Wrap the file handling in a try/except block and print a friendly
    # message instead of crashing.

    # Hint: remember it is not possible to divide by 0, so that is a
    # pitfall to look out for. If value2 is 0, print a message and
    # write nothing.

    # Hint: opening a file in 'w' mode replaces whatever was there before.
    # Consider which mode you actually want.
    try:                                                 
        result = result / value2                        
        with open(OUTFILE, 'a') as f:                   
            f.write(f"Multiple: {multiple}\n")           
            f.write(f"Values: {valueArray}\n")          
            f.write(f"Divided by: {value2}\n")          
            f.write(f"Answer: {result}\n\n")            
    except ZeroDivisionError:                           
        print("Cannot divide by zero, so nothing was written to the file.")  
    except OSError:                                     
        print("Sorry, there was a problem writing to the file.")

   


def readTextFile(filename):
    # TODO 3: Open the text file you just made and read from it.
    # Wrap it in a try/except block and print a friendly message if the
    # file does not exist.
    try:                                                 
        with open(filename, 'r') as f:                   
            lines = f.readlines()                       
    except FileNotFoundError:                            
        print(f"Sorry, the file {filename} does not exist.")   
        return   

    # TODO 4: Once you have the contents, print them out to the terminal.
    # Think about how to loop through them and print each one nicely.
    for line in lines:                                  
        print(line, end="") 

    


def demo():
    saveTextFile(5, [1, 3, 5, 7], 0)

    # TODO 5: Call saveTextFile with a value2 that is not zero, then
    # display the contents of the file in the terminal.
    saveTextFile(5, [1, 3, 5, 7], 2)                     
    readTextFile(OUTFILE)       


demo()
