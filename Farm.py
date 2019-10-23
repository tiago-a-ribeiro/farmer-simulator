from Plot import Plot
from Player import Player

num_to_alpha = {
     0 : 'A',  1 : 'B',  2 : 'C',
     3 : 'D',  4 : 'E',  5 : 'F',
     6 : 'G',  7 : 'H',  8 : 'I',
     9 : 'J', 10 : 'K', 11 : 'L',
    12 : 'M', 13 : 'N', 14 : 'O',
    15 : 'P', 16 : 'Q', 17 : 'R',
    18 : 'S', 19 : 'T', 20 : 'U',
    21 : 'V', 22 : 'W', 23 : 'X',
    24 : 'Y', 25 : 'Z'
}

alpha_to_num = {
    'A' : 0,  'B' : 1,  'C' : 2,
    'D' : 3,  'E' : 4,  'F' : 5,
    'G' : 6,  'H' : 7,  'I' : 8,
    'J' : 9,  'K' : 10, 'L' : 11,
    'M' : 12, 'N' : 13, 'O' : 14,
    'P' : 15, 'Q' : 16, 'R' : 17,
    'S' : 18, 'T' : 19, 'U' : 20,
    'V' : 21, 'W' : 22, 'x' : 23,
    'Y' : 24, 'Z' : 25
}


class Farm:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.positions = []

        self.plots = []
        for j in range(self.height):
            self.plots.append([])
            for i in range(self.width):
                position = num_to_alpha[i] + str(j)
                self.positions.append(position)
                self.plots[j].append(Plot(position))

    def get_yx(self, position):
        y = int(position[1])
        x = alpha_to_num[position[0]]

        return y, x

    def get_positions(self):
        return self.positions
    
    def get_item(self, position):
        y, x = self.get_yx(position)
        return self.plots[y][x].get_item()

    def has_position(self, position):
        if position in self.positions:
            return True
        else:
            print("Invalid position: " + position)
            return False

    def get_boxconsumption(self, start, end, task):
        consumptions = 0

        y_start, x_start = self.get_yx(start)
        y_end, x_end = self.get_yx(end)

        y_max = max(y_start, y_end)
        y_min = min(y_start, y_end)
        x_max = max(x_start, x_end)
        x_min = min(x_start, x_end)

        for j in range(y_min, y_max+1):
            for i in range(x_min, x_max+1):
                y_plot, x_plot = self.get_yx(self.plots[j][i].get_position())
                
                # If the plot is within the bounds of players given positions then we add to amount of consumptions
                if y_plot >= y_min and y_plot <= y_max and x_plot >= x_min and x_plot <= x_max:
                    consumptions += 1

        return consumptions * task

    def box(self, start, end, task):
        y_start, x_start = self.get_yx(start)
        y_end, x_end = self.get_yx(end)

        y_max = max(y_start, y_end)
        y_min = min(y_start, y_end)
        x_max = max(x_start, x_end)
        x_min = min(x_start, x_end)

        # Check first to see if you can boxtill
        for j in range(y_min, y_max+1):
            for i in range(x_min, x_max+1):
                y_plot, x_plot = self.get_yx(self.plots[j][i].get_position())
                
                # If the plot is within the bounds of players given positions then we check it
                if y_plot >= y_min and y_plot <= y_max and x_plot >= x_min and x_plot <= x_max:
                    if task == "TILL":
                        if self.plots[j][i].get_is_tilled() or self.plots[j][i].get_has_plant():
                            print("You cannot till on the box you have given.")
                            return False

        # If function doesnt return False, will till
        for j in range(y_min, y_max+1):
            for i in range(x_min, x_max+1):
                y_plot, x_plot = self.get_yx(self.plots[j][i].get_position())

                if y_plot >= y_min and y_plot <= y_max and x_plot >= x_min and x_plot <= x_max:
                    if task == "TILL":
                        self.plots[j][i].till()
                    elif task == "WATER":
                        self.plots[j][i].water()
        
        return True

    def is_tilled(self, position):
        y, x = self.get_yx(position)
        return self.plots[y][x].is_tilled

    def till(self, position):
        y, x = self.get_yx(position)
        return self.plots[y][x].till()

    def water(self, position):
        y, x = self.get_yx(position)
        return self.plots[y][x].water()

    def plant(self, position, plant):
        y, x = self.get_yx(position)
        return self.plots[y][x].plant(plant)

    def update(self):
        for j in range(self.height):
            for i in range(self.width):
                self.plots[j][i].update()

    def get_harvest(self, position):
        y, x = self.get_yx(position)
        return self.plots[y][x].get_harvest()

    def can_harvest(self, position):
        y, x = self.get_yx(position)
        return self.plots[y][x].can_harvest()

    # Display function
    def display(self):
        print("")

        # Creates the first 'A B C...' row
        row_title = "  "
        for num in range(self.width):
            row_title = row_title + "   " + num_to_alpha[num]    
        print(row_title)

        # Creates the border variable that is used later on
        border = "   ~"
        border = border + "~~~~" * (self.width) 
        print(border)


        # Print out the plots in order starting from height 0 then going completely across the width
        for h in range(0, self.height):
            row = " " + str(h) + " |"
            for w in range(0, self.width):
                row = row + " " + self.plots[h][w].display() + " |" 
            print(row)
            print(border)
        
        print("")