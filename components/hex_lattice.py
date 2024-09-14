import gdsfactory as gf
import math

class HexLattice():
    def __init__(self, 
                 a: float, 
                 elem: gf.Component):
        self.a = a
        self.elem = elem
    
    @gf.cell
    def generate(self, 
                 n_rows: int,
                 n_holes: int) -> gf.Component:
        
        component = gf.Component()
        for i in range(n_rows):
            for j in range(n_holes):
                if i%2 == 0:
                    component.add_ref(component=self.elem).dmove((j*self.a, 
                                                                  i*self.a*math.sqrt(3)/2))
                if i%2 == 1 and j <= n_holes-2:
                    component.add_ref(component=self.elem).dmove(((2*j+1)*(self.a/2), 
                                                                   i*self.a*math.sqrt(3)/2))
        return component
    
    def disordered():
        pass