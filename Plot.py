class Plot:
    def __init__(self, position):
        self.item = None
        self.image = "-"
        self.position = position
        
        self.is_tilled = False
        self.has_plant = False
        self.is_watered = False

    def get_image(self):
        return self.image
    
    def get_position(self):
        return self.position

    def get_is_tilled(self):
        return self.is_tilled

    def get_has_plant(self):
        return self.has_plant
    
    def get_item(self):
        return self.item

    def set_image(self, image):
        self.image = image

    def till(self):
        if self.has_plant:
            print("Plot " + self.position + " has a plant on it")
            return False
        elif self.is_tilled:
            print("Plot " + self.position + " is already tilled")
            return False
        else:
            self.is_tilled = True
            self.set_image("~")
            print("Tilled at: " + self.position)
            return True

    def un_till(self):
        self.is_tilled = False
        self.set_image("-")
    
    def water(self):
        if not self.is_watered:
            self.is_watered = True
        
        print("You watered " + self.position)
        return True
   
    def plant(self, plant):
        if self.is_tilled:
            if not self.has_plant:
                self.has_plant = True
                self.item = plant
                print("Planted seed on " + self.position)
                return True
            else:
                print("Plot " + self.position + " has a plant on it")
        else:
            print("Plot " + self.position + " is not tilled")

    def can_harvest(self):
        if self.has_plant:
            if not self.item.can_harvest():
                print("Plot " + self.position + " is not harvestable yet")
                return False
            else:
                return self.item.can_harvest()
        else:
            print("Plot " + self.position + " does not have a plant")

    def get_harvest(self):
        harvest = self.item.get_harvest()
        print("You harvested " + harvest.get_name() + " from plot: " + self.position)
        self.has_plant = False
        self.item = None
        return harvest

    def update(self):
        if self.has_plant:
            if self.is_watered:
                self.item.grow()
        #Unwater and untill
        self.is_watered = False
        self.is_tilled = False

    def display(self):
        if self.is_tilled:
            if self.has_plant:
                return self.item.display()
            else:
                return "~" 
        else:
            return "-" 