# graph: a hash table where keys represent a vertex and values will be
# an adjacency list
# user: a vertex contained in graph
def total_infection(users, graph, v_user, visited=None):
    if visited == None:
        visited = [False for x in users]
    if not visited[v_user]:
        print("Visited vertex {}".format(v_user))
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
        throw Error() #no
    q = queue.Queue()
    q.put(v_init)
    visited = [False for x in users]
    classes = [0 for x in users]
    while not q.empty():
        teacher = q.get()
        visited[teacher] = True
        classrm = 1
        for stu in graph[teacher]:
            classrm += 1
            if not visited[stu]:
                #this creates an overlap if I choose two classrooms where
                #stu is a student in one and a teacher in another
                q.put(stu)
        classes[teacher] = classrm
    #returns a list of classroom numbers to switch to new site, close to N
    choices = find_limit(classes, N)
    for c in choices:
        if c.updated:
            c.update()
        for g in graph[c]
            if g.updated:
                g.update()



class User():
    """Defines a simple user object with a version property that defines
    which site version they're using"""
    def __init__(self):
        self.updated = False
    def update(self):
        self.updated = True
