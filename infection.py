# graph: a hash table where keys represent a vertex and values will be
# an adjacency list
# user: a vertex contained in graph
def total_infection(users, graph, v_user, visited=None):
    if visited == None:
        visited = [False for x in users]
    if not visited[v_user]:
        print("Total infection: Visited vertex {}".format(v_user))
        visited[v_user] = True
        users[v_user].update()
        for v_u in graph[v_user]:
            total_infection(users, graph, v_u, visited)

#I want to keep all students of the same classroom (teacher:students) on the same version
#This means when I find a teacher, the teacher and their students will be considered
#for an upgrade. After assembling a list of classrooms, find the most optimal
#combination (greedy?) of users to upgrade. It's okay if a teacher has a different
#version, but not optimal.
import queue

#users: a list of User objects
#graph: a dict that associates the index of a user with a list indeces of other users,
#showing a teacher -> students relationship
#v_init: the index of the user where the infection spreads from
#limit: approximately the number of people to be infected, not exact
def limited_infection(users, graph, v_init, limit):
    if limit <= 1:
        raise ValueError("limit is too small") #no
    q = queue.Queue()
    q.put(v_init)
    visited = [False for x in users]
    classes = [0 for x in users]
    while not q.empty():
        teacher = q.get()
        print("Limited infection: Visited vertex {}".format(teacher))
        visited[teacher] = True
        classrm = 1
        for stu in graph[teacher]:
            classrm += 1
            if not visited[stu]:
                #this creates an overlap if I choose two classrooms where
                #stu is a student in one and a teacher in another
                q.put(stu)
        classes[teacher] = classrm
    choices = find_limit(classes, limit)
    print("Selected teachers: " + str(choices))
    for c in choices:
        #infect the teacher
        if not users[c].updated:
            users[c].update()
        #now infect the class
        for g in graph[c]:
            if not users[g].updated:
                print("Limited infection: Updated vertex {}".format(g))
                users[g].update()

#returns a list of classroom numbers to switch to new site, close to limit
#classes: a list whose indeces correspond to the size of each class
#n: the limit we want to approach
def find_limit(classes, n):
    total = 0
    rooms = []
    print("Classroom sizes: " + str(classes))
    for c in range(len(classes)):
        if total >= n:
            break
        if classes[c] <= 1 or total + classes[c] > n:
            continue
        else:
            total += classes[c]
            rooms.append(c)
    return rooms

class User():
    """Defines a simple user object with a version property that defines
    which site version they're using"""
    def __init__(self):
        self.updated = False
    def update(self):
        self.updated = True
