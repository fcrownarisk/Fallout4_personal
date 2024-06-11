import X1Y1Z1
def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
def x2(self,x2):
    self.x2 = self.x2 *  self.y2 * self.z2
    self.y2 = self.y2 *  self.x2 * self.z2
    self.z2 = self.z2 *  self.x2 * self.y2
    return self.x2,self.y2,self.z2
def y2(self,y2):
    self.x2 = self.x2 %  self.y2 % self.z2
    self.y2 = self.y2 %  self.x2 % self.z2
    self.z2 = self.z2 %  self.x2 % self.y2
    return self.x2,self.y2,self.z2 
def z2(self,z2):
    self.x2 = self.x2 + self.y2 + self.z2
    self.y2 = self.y2 + self.x2 + self.z2
    self.z2 = self.z2 + self.x2 + self.y2
    return self.x2,self.y2,self.z2