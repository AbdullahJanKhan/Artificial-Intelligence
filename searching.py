class node:
    def __init__(self, state, parent, action, totalCost):
        self.state=state
        self.parent=parent
        self.action=action
        self.totalCost=totalCost

graph={
    'A':node('A', None, ['B', 'C', 'E'], None),
    'B':node('B', None, ['A', 'D', 'E'], None),
    'C':node('C', None, ['A', 'F', 'G'], None),
    'D':node('D', None, ['B', 'E'], None),
    'E':node('E', None, ['A', 'B', 'D'], None),
    'F':node('F', None, ['C'], None),
    'G':node('G', None, ['C'], None)
}

graphW={
    'A':node('A', None, [('B',6), ('C',9), ('E',1)], 0),
    'B':node('B', None, [('A',6), ('D',3), ('E', 4)], 0),
    'C':node('C', None, [('A',9), ('F',2), ('G',3)], 0),
    'D':node('D', None, [('B',3), ('E',5), ('F',7)], 0),
    'E':node('E', None, [('A',1), ('B',4), ('D',5), ('F', 6)], 0),
    'F':node('F', None, [('C',2), ('E',6), ('D',7)], 0),
    'G':node('G', None, [('C',3)], 0)
}


def BFS(graph, initial, goal):
    front=[initial]
    explored=[]

    while  len(front)>0:
        temp=front.pop(0)
        if(temp == goal):
            print(action_seqe(graph, initial, goal))
            break
        explored.append(temp)
        for i in graph[temp].action:
            if i in front or i in explored:
                continue
            else:
                front.append(i)
                graph[i].parent=temp

def DFS(graph, initial, goal):
    front=[initial]
    explored=[]
    while len(front)!=0:
        temp = front.pop(len(front)-1)
        explored.append(temp)
        print(temp)
        childs=0
        for child in graph[temp].action:
            if child not in front and child not in explored:
                graph[child].parent=temp
                if graph[child].state == goal:
                    print(explored)
                    return action_seqe(graph, initial, goal)
                childs+=1
                front.append(child)
        if childs==0:
            del explored[len(explored)-1]

def action_seqe(graph, initial, goal):
    solution=[goal]
    c_parent=graph[goal].parent
    while c_parent != None:
        solution.append(c_parent)
        c_parent = graph[c_parent].parent
    solution.reverse()
    return solution

def findMin(front):
    minV=99999
    node = ''
    for i in front:
        if minV>front[i][1]:
            minV=front[i][1]
            node=i
    return node

def UCS(graph, initial, goal):
    front=dict()
    front[initial]=(None,0)
    explored=[]

    while len(front)!=0:
        cNode=findMin(front)
        del front[cNode]
        if graph[cNode].state ==  goal:
            return action_seqe(graph, initial, goal)
        explored.append(cNode)
        for child in graph[cNode].action:
            cCost = child[1] + graph[cNode].totalCost
            if child[0] not in front and child[0] not in explored:
                graph[child[0]].parent = cNode
                graph[child[0]].totalCost = cCost
                front[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
            elif child[0] in front:
                if front[child[0]][1] < cCost:
                    graph[child[0]].parent = front[child[0]][0]
                    graph[child[0]].totalCost = front[child[0]][1]
                else:
                    front[child[0]] = (cNode,cCost)
                    graph[child[0]].parent = front[child[0]][0]
                    graph[child[0]].totalCost = front[child[0]][1]




BFS(graph, 'C', ' B')
print(DFS(graph,'C', 'B'))
print(UCS(graphW, 'C', 'B'))