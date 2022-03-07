try:
    import test567
except ModuleNotFoundError:
    print("No such module exists")

class Equipment():
    def __init__(self, sport_name):

        self.sport_name = sport_name
        print(sport_name)
        #self.sport_equipment = sport_equipment
        #sport_equipment = []
    
    def equipment(self, sport_equipment):
        self.sport_equipment = sport_equipment
        sport_equipment = []
        self.listToStr = ", ".join([str(item) for item in self.sport_equipment]) #convert list to string
        print(self.sport_name, self.sport_equipment)
    
    def __str__(self):
        return f"The sport {self.sport_name} requires the following equipment: {self.sport_equipment}"

if __name__ == '__main__':

   skiing = Equipment("Skiing")
   skiing.sport_equipment = ["helmet", "ski goggles", "skis"]

   print(skiing)
