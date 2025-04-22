class Area:
    Area = 0
    AreaCobertura = 0
    def getArea(self):
        return self.Area
    
    def setArea(self,Area):
        self.Area +=  Area

    def setAreaeNode(self,Area):
        self.AreaCobertura = Area

    def getAreaCobertura(self):
        return self.AreaCobertura
    
a = Area()