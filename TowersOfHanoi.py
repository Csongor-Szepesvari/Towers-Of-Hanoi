# Towers of Hanoi fun implementation
a = [] #the towers
b = []
c = []
# The variable that designates how big the tower is
SIZE = 10
for i in range(SIZE):
    a.append(SIZE-i)
#how many moves made
moves = 0

def solver(size, fromTower, toTower, spare):
    global moves
    #too hard to solve
    #we solve smaller problem
    if size==1:
        toTower.append(fromTower.pop())
        moves+=1
        print(a, b, c)
    else:
        solver(size-1, fromTower, spare, toTower)
        toTower.append(fromTower.pop())
        moves+=1
        print(a, b, c)
        solver(size-1, spare, toTower, fromTower)

# The visualizer of a tower
def towerVisualizer(tower):
    # create SIZE amount of strings of form ### (when size is 3)
    output = []
    # check the length of tower, on the last length iterations draw the numbers
    towerSize = len(tower)
    for i in range(SIZE+1):
        out = ""
        #start writing tower elements when 
        startWriting = i-(SIZE+1-towerSize)
        for j in range(SIZE+2):
            if i<SIZE+1-towerSize:
                if j==((SIZE+2)//2):
                    out+="|"
                else:
                    out+=" "
            else:
                amount = tower[startWriting]
                if j==0 or j==SIZE+1:
                    out+=" "
                #break into 2 cases: amount is even or odd
                if amount%2==0:
                    #when even it will be on 2 sides of the middle
                    pass
                else:
                    #it will be going through the middle
                    pass
                
        output.append(out)
    for i in range(len(output)):
        print(output[i])
    