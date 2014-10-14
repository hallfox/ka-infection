# graph: a hash table where keys represent a vertex and values will be
# an adjacency list
# user: a vertex contained in graph
def total_infection(users, graph, v_user, visited=None):
    if visited == None:
        visited = [False for x in users]
    if not visited[v_user]:
        #print("Total infection: Visited vertex {}".format(v_user))
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
def limited_infection(users, graph, limit):
    if limit <= 1:
        raise ValueError("limit is too small") #no

    visited = [False for x in users]
    infected = 0
    for user in graph.keys():
        if visited[user]:
            continue
        classes = bfs_classes(user, graph, visited)
        choices = find_limit(classes, limit - infected)

        print("Selected teachers: " + str(choices))
        for c in choices:
            #infect the teacher
            if not users[c].updated:
                users[c].update()
                print("Limited infection: Updated vertex {}".format(c))
                infected += 1
            #now infect the classroom
            for g in graph[c]:
                if not users[g].updated:
                    print("Limited infection: Updated vertex {}".format(g))
                    users[g].update()
                    infected += 1

        if infected >= limit:
            break

def bfs_classes(user, graph, visited):
    q = queue.Queue()
    classes = [0 for x in graph.keys()]

    q.put(user)
    while not q.empty():
        teacher = q.get()
        print("Limited infection: Visited vertex {}".format(teacher))
        visited[teacher] = True
        classrm = 1
        for stu in graph[teacher]:
            if not visited[stu]:
                classrm += 1
                q.put(stu)
        classes[teacher] = classrm
    return classes

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
        if classes[c] <= 0 or total + classes[c] > n:
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
