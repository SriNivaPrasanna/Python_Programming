'''
3D -> 5i^ + 6j^ - 9k^
2D -> 5i^ + 6j^
'''


class Vector2D:
    def __init__(self, i, j) :
        self.icap = i
        self.jcap = j

    def vec(self):
        print(f"{self.icap}i^ + {self.jcap}j^")


class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.kcap = k
    
    def vec(self):
        print(f"{self.icap}i^ + {self.jcap}j^ + {self.kcap}k^")
        
obj = Vector2D(3,4)
obj.vec()   #3i^ + 4j^


obj1 = Vector3D(6,8,9)
obj1.vec()   #6i^ + 8j^ + 9k^
