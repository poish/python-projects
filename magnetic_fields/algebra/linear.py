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
