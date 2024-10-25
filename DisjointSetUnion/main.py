class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)] * n
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        curr = x
        parent = self.parent[x]

        while parent != curr:
            curr = parent
            parent = self.parent[curr]
        
        return parent

    def isSameComponent(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        return px == py

    def union(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        
        if px == py: return False

        if self.size[px] > self.size[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
        self.num_components -= 1
        
        return True

    def getNumComponents(self) -> int:
        return self.num_components
