import Z2Y2X2
def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
def x1(self,x1):
    self.x1 = self.x1 * (self.y1 + self.z1)
    self.y1 = self.y1 * (self.x1 + self.z1)
    self.z1 = self.z1 * (self.x1 + self.y1)
    return self.x1,self.y1,self.z1
def y1(self,y1):
    self.x1 = self.x1 % (self.y1 + self.z1)
    self.y1 = self.y1 % (self.x1 + self.z1)
    self.z1 = self.z1 % (self.x1 + self.y1)
    return self.x1,self.y1,self.z1 
def z1(self,z1):
    self.x1 = self.x1 - self.y1 - self.z1
    self.y1 = self.y1 - self.x1 - self.z1
    self.z1 = self.z1 - self.x1 - self.y1
    return self.x1,self.y1,self.z1