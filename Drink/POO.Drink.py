class Drink:
    def __init__ (self, name):
        self.__name = name
    def getDetail(self):
        return "La bebida es: " + self.__name
    

class Beer(Drink):
    Count = 0
    def __init__(self, name, brand, alcohol):
        super().__init__(name)
        self.__brand = brand
        self.__alcohol = alcohol
        Beer.Count += 1

    def getDetail(self):
            return super().getDetail() + "de la marca " + self.__brand + ", su graduación alcoholica es de " + str (self.__alcohol)


    @staticmethod
    def getClassInfo():
         return "Se han creado " + str(Beer.Count) + " tipos de cervezas en Antares"
beer1  = Beer("American IPA", "Antares", 7.5)
beer2  = Beer("Kölsch", "Antares", 5)
beer3  = Beer("Scotch", "Antares", 6)
beer4  = Beer("Porter", "Antares", 5.5)
beer5  = Beer("Barley Wine", "Antares", 10)
beer6  = Beer("Lupulada", "Antares", 7.5)
beer7  = Beer("Monasterio", "Antares", 14)
beer8  = Beer("Centinela", "Antares", 14)
beer9  = Beer("Catalina La Grande", "Antares", 11)
beer10 = Beer("20 años", "Antares", 11)
beer11 = Beer("Titánica", "Antares", 20)
beer12 = Beer("Imperial Stout", "Antares", 8.5)
beer13 = Beer("Honey Beer", "Antares", 7.5)
beer14 = Beer("India Pale Ale", "Antares", 6.6)
beer15 = Beer("Playa Grande", "Antares", 5)
beer16 = Beer("Caravana", "Antares", 4.2)
beer17 = Beer("Fin de Tarde", "Antares", 5)
beer18 = Beer("Cuatro 3", "Antares", 7.3)
beer19 = Beer("Creme Stout", "Antares", 7)


print(beer1.getDetail())
print(Beer.getClassInfo())