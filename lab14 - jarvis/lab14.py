import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    


class ConvexHull:

    def __init__(self) -> None:
        self.points = []

    def insert_point(self,p):
        self.points.append(Point(p[0],p[1]))

    def get_egde(self):
        edge = self.points[0]
        for el in self.points[1:]:
            if el.x < edge.x:
                edge = el
            if el.x == edge.x and el.y < edge.y:
                edge = el
        return edge
    
    def curve(self,p,q,r):
        test = (q.y - p.y)*(r.x - q.x) - (r.y - q.y)*(q.x - p.x)
        if test > 0:
            return "R"
        elif test < 0:
            return "L"
        else:
            return "I"
   
    def distance(self, x, y):
        return np.sqrt((y.x - x.x)**2 + (y.y - x.y)**2)

    def jarvis(self):
        result = []
        p = self.get_egde()
        result.append(p)
        
        while True:
            q = self.points[(self.points.index(p)+1) % len(self.points)]
            for r in self.points:
                if r != p and r != q:
                    if self.curve(p,q,r) == "R":
                        q = r
            result.append(q)
            p = q
            if p == result[0]:
                result.pop(-1)
                break
            
        return result
    
    def jarvis2(self):
        result = []
        p = self.get_egde()
        result.append(p)
        
        while True:
            q = self.points[(self.points.index(p)+1) % len(self.points)]
            for r in self.points:
                if r != p and r != q:
                    if self.curve(p,q,r) == "R":
                        q = r
                    if self.curve(p,q,r) == "I":
                        if (self.distance(p,q) < self.distance(p,r)) and (self.distance(q,r) < self.distance(p,r)):
                            q = r  
            result.append(q)
            p = q
            if p == result[0]:
                result.pop(-1)
                break
            
        return result


input = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
jar = ConvexHull()
for el in input:
    jar.insert_point(el)

print(jar.jarvis())
print(jar.jarvis2())

