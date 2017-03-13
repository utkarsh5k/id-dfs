class Node:
    def __init__(self, vno, isGoalState):
        self.stateNo = vno
        self.next_nodes = []
        self.isGoalState = isGoalState
    def add_edge(self, vertex):
        self.next_nodes.append(vertex)

totalStates = 15
targetState = 14

states = []

for i in xrange(totalStates):
    isGoal = False
    if i == targetState:
        isGoal = True
    newState = Node(i, isGoal)
    states.append(newState)

for i in xrange( ( (totalStates+1) / 2 ) - 1):
    states[i].add_edge((2*i) + 1)
    states[i].add_edge((2*i) + 2)

start_state = 0

def dfs(current_state, current_depth):
    if current_depth < 0:
        return False
    else:
        print current_state
        if states[current_state].isGoalState == True:
            return True
        current_depth -= 1
        for next_state in states[current_state].next_nodes:
            success = dfs(next_state, current_depth)
            if success == True:
                return True
        return False

def iddfs(start_state, max_depth):
    for i in xrange(max_depth+1):
        success = dfs(start_state, i)
        print success
        if success == True:
            return True, i
    return False, -1

success, node = iddfs(0, 4)
if success == True:
    print "Solution found at depth %d" % (node)
else:
    print "No solutions exist in the given depth"
