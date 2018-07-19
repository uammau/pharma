from drugsAVL import drugsAVL
import sys
import datetime, time

def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False

def readFile(inputFileName, outputFileName):
    
    # Opens the input file and reads all lines (May be changed to read line by line to reduce memory overload)
    f = open(inputFileName, "r")
    lines = f.readlines()
    
    # Declaration of Drugs tree
    tree = drugsAVL()
    # Sets counter of lines
    curLine = 0
    # Sets counter of successful cases
    successful = 0
    # Sets counter of errors
    errors = 0
    
    # Initializes counter of inserted
    inserted = 0
    
    # Cycle to insert line by line to the drugsAVL
    for line in lines:
        error = False
        if (curLine != 0):
            
            lineDivided = line.split(",")
            
            # Validates values (basically only the cost
            if (is_number_tryexcept(lineDivided[4]) == False):
                successful -= 1
                errors += 1
                error = True
                print('[FAIL]: test_' + str(curLine))
            else:
                inserted = tree.insert(lineDivided[3], lineDivided[3] + ',' + lineDivided[1] + ',' + lineDivided[2], lineDivided[4])
                print('[PASS]: test_' + str(curLine))

            successful += 1 # We can add it all the times, because we substracted 1 if there was an error in the name
        
        # increases counters
        curLine += 1
        
    curLine -= 1 # Substracting line 1
        
##    timeStamp = datetime.datetime.now().timestamp()
    t = datetime.datetime.now()
    timeStamp = time.mktime(t.timetuple()) + t.microsecond / 1E6
    
    print ('[ ' + time.strftime("%a %b %d %H:%M:%S %Z %Y", time.gmtime(timeStamp)) + ' ] : ' + str(successful) + ' of ' + str(curLine) + ' tests passed')
        
    costs = None
    tree.root.createCostsAVL(costs, outputFileName)
    
if __name__ == '__main__':
    if (len(sys.argv) < 2):
        inputFile = '../input/itcont.txt'
        outputFile = '../output/top_cost_drug.txt'
    else:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    readFile (inputFile, outputFile)
    
    

        
        
        