d2 = range(2)
c2 = []

for n in d2:
    print(n+1)
    c2.append(1/2)
    print(c2[n])

dices = []

for n in range(10):
    v = []
    if n == 0:
        c = 0
    else:
        c = 1/n
        for x in range(n):
            v.append(x+1)
        
    dices.append([n,c,v])

print(dices)


class dice:
    def __init__(self, plane = 6):
        self.plane = plane
        self.chance = 1/plane
        self.chance_table = self.create_chances(plane)

    def create_chances(self, plane):
        table = []
        for n in range(plane):
            table.append([n+1, self.chance])
        return table

    def view_chances(self):
        pass
        
class throw:
    def __init__(self, *args):
        self.dices = args
        self.dices_number = len(self.dices)
        if self.dices_number == 1:
            print('Need more dices!')
            self.__delete__() 

    def create_table(self):
        pass

    def two_dices_thtow(self, dice1, dice2):
        self.table = []
        for x in dice1.chance_table:
            for y in dice2.chance_table:
                self.table.append([x[0]+y[0],x[1]*y[1]])
        self.table.sort()
        self.data = []
        for i in range(dice1.plane + dice2.plane):
            chance = 0
            for j in self.table:
                if i == j[0]:
                    chance += j[1]
                else:
                    self.data.append([i, chance])
                    chance = 0
            
