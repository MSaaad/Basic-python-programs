
class cricket:
    #cricketer=runs
    def __init__(self,name,runs,game):
        self.name= name
        self.runs= runs
        self.game= game

Virat=cricket('Virat',100,'cricket')
Afridi=cricket('Afridi',100,'football')

print(Virat.name)
print(Afridi.runs)
