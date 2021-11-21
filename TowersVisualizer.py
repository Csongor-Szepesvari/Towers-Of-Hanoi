# two parts to the code
# part 1: Visualize a single tower
def towerVisualizer(tower, size):
    tower = list(reversed(tower))
    # first things first, check size, if its even, increase width by 1
    if size%2==0:
        width = size + 3
    else:
        width = size + 2
    height = size + 1 # the height of the tower will always be greater by 1 than max size
    stringLevels = [] # stores strings of each level, starts at the top and goes down
    towerSize = len(tower) # the number of levels at the bottom of stringLevels to fill
    # loop through each level of tower, top to bottom
    for i in range(height):
        out = ""
        
        #start writing tower elements when 
        startWriting = i-(height-towerSize)
        
        for j in range(width):
            #firing blanks
            if i<height-towerSize:
                if j==(width//2):
                    out+="|"
                else:
                    out+=" "
            #writing the tower
            else:
                amount = tower[startWriting]
                #break into 2 cases: amount is even or odd
                if amount%2==0:
                    #when even it will be on 2 sides of the middle
                    #will be filled from [half-amount//2:half-1] and the other side
                    if j in range(width//2-amount//2+1, width//2) or j in range(width//2+1, width//2+amount//2):
                        out+="-"
                    elif j==width//2:
                        out+="|"
                    else:
                        out+=" "
                else:
                    #it will be going through the middle
                    if j in range(width//2-amount//2+1, width//2+amount//2):
                        out+="-"
                    else:
                        out+=" "
                
        stringLevels.append(out)
    for i in range(len(stringLevels)):
        print(stringLevels[i])
        
# part 2: Add each one together


# The visualizer of a tower

