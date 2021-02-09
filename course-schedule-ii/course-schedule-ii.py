from typing import List

class Node:
    def __init__(self):
        self.neighbours = []
        self.indegree = 0

    def add_edge(self, dst):
        if dst not in self.neighbours:
            self.neighbours.append(dst)
            self.indegree += 1

    def remove_edge(self, dst):
        if dst in self.neighbours:
            self.neighbours.remove(dst)
            self.indegree -= 1
        else: return -1
        return self.indegree

    def __repr__(self):
        return str(self.indegree) +":"+ str(self.neighbours)
                
class Graph:
    def __init__(self, nodes):
        self.nodes = [Node() for _ in range(nodes)]
        self.graph = {}
        self.no_incoming = []

    def add_edge(self, src, dst):
        self.nodes[src].add_edge(dst)

    def remove_edge(self, src, dst):
        ind = self.nodes[src].remove_edge(dst)
        if ind == 0:
            self.no_incoming.append(src)

    def remove_node(self, node):
        for n in range(len(self.nodes)):
            self.remove_edge(n, node)
            
    def no_indegrees(self):
        self.no_incoming = [s for s in range(len(self.nodes)) if self.nodes[s].indegree == 0]

    def __repr__(self):
        return str(self.nodes) + " " + str(self.no_incoming)
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = Graph(numCourses)
        course_order = []
        for p in prerequisites:
            courses.add_edge(p[1], p[0])
        courses.no_indegrees()
        print(courses)
        while len(courses.no_incoming) > 0:
            c = courses.no_incoming.pop(0)
            print(c, end=":")
            course_order.append(c)
            for n in courses.nodes[c].neighbours:
                courses.remove_edge(c, n)
                print(n, end=",")
            courses.remove_node(c)
        print(course_order)
        return [] if len(course_order) < numCourses else course_order[::-1]

S = Solution()
print(S.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))

