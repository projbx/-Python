# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Treug:
    def __init__(self,a,b,c):
        self.a=a # a = (x1,y1)
        self.b=b # b = (x2,y2)
        self.c=c # c = (x3,y3)
    def area(self):
        opred = ((a[0]-c[0])*(b[1]-c[1])-(a[1]-c[1])*(b[0]-c[0]))
        if opred < 0:
            opred *= -1
        S = opred/2
        return S
    def lensides(self):
        AB = 0.5 ** ((a[0]-b[0])**2+(a[1]-b[1])**2)
        BC = 0.5 ** ((b[0]-c[0])**2+(b[1]-c[1])**2)
        CA = 0.5 ** ((c[0]-a[0])**2+(c[1]-a[1])**2)
        return (AB,BC,CA)

    def heights(self):
        sA,sB,sC = self.lensides()
        Streug = self.area()
        return (2*Streug/sA,2*Streug/sB,2*Streug/sC)
    
    def perimetr(self):
        sideA,sideB,sideC = self.lensides()
        return sideA+sideB+sideC

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class NotRBTrapez(Exception):
    pass

class RBTrapez:
    def __init__(self,a,b,c,d):
        #Здесь должна быть куча формул (чистая математика, геометрия), которая вычисляет, что среди данных
        #4 точек найдутся 2 пары, через которые проходят параллельные прямые,
        #при этом длины отрезков, которые образуют эти пары, не равны.
        #(т.е. параллелограмм, прямоугольник, квадрат трапецией не считаем). - общее условие трапеции
        # А так же непаррллельные отрезки равны - доп. условия для равнобочной трапеции
        #
        #if <вышеописанные условия> != True:
        #   raise NotRBTrapez('Данные точки не образуют равнобочную трапецию')
        #
        #AD||BC, AB=CD
        self.a=a # a = (x1,y1)
        self.b=b # b = (x2,y2)
        self.c=c # c = (x3,y3)
        self.d=d # d = (x4,y4)

    def lensides(self):
        AB = 0.5 ** ((a[0]-b[0])**2+(a[1]-b[1])**2)
        BC = 0.5 ** ((b[0]-c[0])**2+(b[1]-c[1])**2)
        CD = 0.5 ** ((c[0]-d[0])**2+(c[1]-d[1])**2)
        DA = 0.5 ** ((d[0]-a[0])**2+(d[1]-a[1])**2)
        return (AB,BC,CD,DA)

    def height(self):
        sA,sB,sC,sD = self.lensides()
        H = 0.5 ** (sC**2 - (((sA-sB)**2+sC**2-sD**2)/(2*(sA-sB)))**2)
        return H
    
    def perimetr(self):
        sideA,sideB,sideC = self.lensides()
        return sideA+sideB+sideC

    def area(self):
        sA,sB,sC,sD = self.lensides()
        H = self.height()
        S=(sD+sB)*H/2
        return S


        
