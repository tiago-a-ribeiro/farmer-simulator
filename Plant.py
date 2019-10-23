class Plant:
    def __init__(self, name, stages, max_phase, harvest):
        self.name = name or "NULL_PLANT"
        self.stages = stages or []
        self.max_phase = max_phase or 0
        self.harvest = harvest
        self.phase = 0
        self.max_wither = 2
        self.wither = 0
        self.ready = False
    
    def grow(self):
        if self.phase < self.max_phase:
            self.phase += 1
        if self.phase >= self.max_phase:
            self.ready = True

    def can_harvest(self):
        return self.ready
        
    def get_harvest(self):
        if self.ready:
            return self.harvest
        return None

    def display(self):
        if self.wither < self.max_wither:
            if self.phase < self.max_phase:
                phase = 0
            else:
                phase = 1
            
            return self.stages[phase]

        else:
            return "%"
