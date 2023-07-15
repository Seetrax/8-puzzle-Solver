arra=[1,2,3,4,5,6,7,8,0]
fin=[[1,2,3],[4,5,6],[7,8,0]]
from queue import PriorityQueue
def posi(arr):#Function that gives the position of each element of an array as a dictionary
    f={}
    for i in arr:
        for j in i:
            f[j]=(arr.index(i),i.index(j))
    return f
def s_mandist(d,fin):#Function to calculate sum of manhattan distances of all cells of the puzzle
    su=0
    for i in d:
        su=su+abs(fin[i][0]-d[i][0])+abs(fin[i][1]-d[i][1])
    return su
def adj_states(arr):
    adj=[]
    
    arr2=arr.copy()
    tempd={}
    for i in range(len(arr2)):
        if 0 in arr2[i]:
            k=arr2[i].index(0)
            if k<2:
                temp=arr2[i].copy()
                t=temp[k+1]
                temp[k+1]=0
                temp[k]=t
                arr2[i]=temp
                adj.append(arr2)
                arr2=arr.copy()
           
            if k>0:
                temp=arr2[i].copy()
                t=temp[k-1]
                temp[k-1]=0
                temp[k]=t
                arr2[i]=temp
                adj.append(arr2)
                arr2=arr.copy()
    
            if arr2.index(arr2[i])>0:
                temp1=arr2[i].copy()
                temp2=arr2[i-1].copy()
                t=temp2[k]
                temp2[k]=0
                temp1[k]=t
                arr2[i]=temp1
                arr2[i-1]=temp2
                adj.append(arr2)
                arr2=arr.copy()

            if arr2.index(arr2[i])<2:
                temp1=arr2[i].copy()
                temp2=arr2[i+1].copy()
                t=temp2[k]
                temp2[k]=0
                temp1[k]=t
                arr2[i]=temp1
                arr2[i+1]=temp2
                adj.append(arr2)
                arr2=arr.copy()

    return adj
def no_misp(state,goal):#Function to find no of misplaced tiles given the state of a puzzle
    c=0
    d=posi(state)
    d_f=posi(goal)
    for i in d:
        if(d[i]!=d_f[i]):
            c+=1
    return c
def zero_mandist(state,fin):#Function of find the manhattan dist of cell 0 alone
    return abs(posi(state)[0][0]-posi(fin)[0][0])+abs(posi(state)[0][1]-posi(fin)[0][1])
def printpuz(state):#function to print a puzzle given state of a puzzle
    for i in state:
        for j in i:
            print(j,end=" ")
        print()
def Asearch_smn(ini,goal):#A* search on a given puzzle using sum of manhattan distances as heuristic
    visited=[]
    parent={}
    tree=[]
    move={}
    step=0
    path=[]
    move[(tuple(ini[0]),tuple(ini[1]),tuple(ini[2]))]=0

    
    q3=PriorityQueue()#priority queue to store states in increasing order of f(n)=no of moves req to reach that state + sum of manhattan distances of all cells in that state
    q3.put((move[(tuple(ini[0]),tuple(ini[1]),tuple(ini[2]))]+s_mandist(posi(ini),posi(fin)),ini))

    while ((q3.empty())==False):
        u1=q3.get()
        u=u1[1]
        adj=adj_states(u)
        visited.append(u)
        tree.append(u)

        if u==goal:
            break
        for v in adj:
            if v not in visited:
                move[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]=move[(tuple(u[0]),tuple(u[1]),tuple(u[2]))]+1#Moves requored to reach v is moves req to reach u +1
                #visited.append(v)
                parent[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]=u
                q3.put((move[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]+s_mandist(posi(v),posi(fin)),v))
                
    x=goal
    path.append(x)
        
    while(parent[(tuple(x[0]),tuple(x[1]),tuple(x[2]))] !=ini): #While loop to backtrack from the goal to find the only good moves done by the search
        x = parent[(tuple(x[0]),tuple(x[1]),tuple(x[2]))]
        path.append(x)  
    path.append(ini)
    path = path[::-1]  #reversing path
    return path,len(visited)##Returns steps req to reach goal state and no of explored staets

def Asearch_mt(ini,goal):#Function to perform A* search with no of misplaced tiles as heuristic
    visited=[]
    parent={}
    tree=[]
    move={}
    path=[]
    move[(tuple(ini[0]),tuple(ini[1]),tuple(ini[2]))]=0

    
    q3=PriorityQueue()#Priority queue based on no of misplaced tiles+no moves req to reach the state
    q3.put((move[(tuple(ini[0]),tuple(ini[1]),tuple(ini[2]))]+no_misp(ini,fin),ini))
    
    while ((q3.empty())==False):
        u1=q3.get()
        u=u1[1]
        adj=adj_states(u)
        visited.append(u)
        tree.append(u)

        if u==goal:
            break
        for v in adj:
            if v not in visited:
                move[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]=move[(tuple(u[0]),tuple(u[1]),tuple(u[2]))]+1

                parent[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]=u
                q3.put((move[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]+no_misp(v,fin),v))
                
    x=goal
    path.append(x)    
    while(parent[(tuple(x[0]),tuple(x[1]),tuple(x[2]))]!=ini): #While loop to backtrack from the goal to find the only good moves done by the search
        x = parent[(tuple(x[0]),tuple(x[1]),tuple(x[2]))]
        path.append(x)  
    path.append(ini)
    path = path[::-1]
    return path,len(visited)
def Asearch_zmn(ini,goal):#Function to perform A*search based on zero manhattan as heristic
    visited=[]
    parent={}
    tree=[]
    move={}
    path=[]
    move[(tuple(ini[0]),tuple(ini[1]),tuple(ini[2]))]=0   
    q3=PriorityQueue()#Priority queue with increasing order of (moves req)+(manhattan distance of 0 cell)
    q3.put((move[(tuple(ini[0]),tuple(ini[1]),tuple(ini[2]))]+zero_mandist(ini,fin),ini))
    
    while ((q3.empty())==False):
        u1=q3.get()
        u=u1[1]
        adj=adj_states(u)
        visited.append(u)
        tree.append(u)
     
        if u==goal:
            break
        for v in adj:
            if v not in visited:
                move[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]=move[(tuple(u[0]),tuple(u[1]),tuple(u[2]))]+1
            
                parent[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]=u
                q3.put((move[(tuple(v[0]),tuple(v[1]),tuple(v[2]))]+zero_mandist(v,fin),v))
                
    x=goal
    path.append(x)    
    while(parent[(tuple(x[0]),tuple(x[1]),tuple(x[2]))]!=ini): #While loop to backtrack from the goal to find the only good moves done by the search
        x = parent[(tuple(x[0]),tuple(x[1]),tuple(x[2]))]
        path.append(x)  
    path.append(ini)
    path = path[::-1] 
    return path,len(visited)   


'''m=[]
for i in range(3):#Getting the input initial state
    a=[]
    for j in range(3):
        
        k=int(input())
        a.append(k)
    m.append(a)
tt=Asearch_smn(m,fin)
print(f"Total {len(tt[0])-1} steps are req to reach goal")
j=0
for i in tt[0]:
    print(f"Step {j}")
    printpuz(i)
    print()
    j+=1
print(f"No of Exlpored states {tt[1]}")'''
