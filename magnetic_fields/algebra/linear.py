import numpy as np

class Vector:
    def __init__(self, coords):
        if isinstance(coords, list):
            self.initFromList(coords)
    
        elif isinstance(coords, np.ndarray):
            self.initFromNativeArray(coords)

    def initFromList(self, coords):
        self.coords = np.array(coords, dtype=np.float32)
    
    def initFromNativeArray(self, coords):
        self.coords = coords

    def x(self):
        return self.coords[0]

    def y(self):
        return self.coords[1]    
    def __repr__(self):
        return f"({self.coords[0]}, {self.coords[1]})"
