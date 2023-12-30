from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
class BaseFiltre:
    def __init__(self,*args,**kwargs):
        self.name=""
        self.description=""
    def apply(self,image):
        print("Вы не можете вызывать apply для BaseFiltres")


class BlackwiteFiltres(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="Черный-белый фильтр"
        self.description="Преобразует изображение к изображение,состоящего из 2 цветов:Белого и Черного"
    def apply(self,image:Image):
        return image.convert("L")
class LumosFiltres(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="день"
        self.description="Увеличивает яркость изображение"

    def apply(self,image:Image):
        w,n=image.size
        for x in range(w):
            for y in range(n):
                r,g,b=image.getpixel((x,y))
                r=min(255,int(r*1.3))
                g=min(255,int(g*1.3))
                b=min(255,int(b*1.3))
                image.putpixel((x, y), (r, g, b))
        return image
class Noch(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="ночь"
        self.description="Уменьшает яркость изображения"
    def apply(self,image:Image):
        w, n = image.size
        for x in range(w):
            for y in range(n):
                r,g,b=image.getpixel((x,y))
                r =int(r/1.5)
                g = int(g/1.5)
                b = int(b/1.5)
                image.putpixel((x, y), (r, g, b))
        return image

class Upheaval90(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="переворот"
        self.description="переворот изображения на 90 градусов"
    def apply(self,image:Image):
        a=image.rotate(90, expand=True)
        return a

class EasterEgg(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="Маленькая пасхалочка"
        self.description="Добавляет имя автора"
    def apply(self,image:Image):
        d1 = ImageDraw.Draw(image)
        myFont = ImageFont.truetype('ofont.ru_Mistral.ttf', 100)
        d1.text((65,50),"My names Kirill! Good day or Good nigth",fill =(255, 0, 0),font=myFont)
        return image

class Сhangingthekey(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="размытие "
        self.description="Размытия изображения"
    def apply(self,image:Image):
        blur_img = image.filter(ImageFilter.BoxBlur(20))
        return blur_img
class RedbLUE(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="цвета"
        self.description="убирает зеленый,синий и красный цвет!"
    def apply(self,image:Image):
        red, green, blue = image.split()
        return red
        return green
        return blue
class OgrAnche(BaseFiltre):
    def __init__(self):
        super().__init__()
        self.name="цвета"
        self.description="убирает зеленый,синий и красный цвет!"
    def apply(self,image:Image):
        img_gray = (image.convert("L"))
        edges = img_gray.filter(ImageFilter.FIND_EDGES)
        edges.show()
class FiltreRepo:
    def __init__(self):
        self.repo={
            "1":{"name":BlackwiteFiltres().name,"derict":BlackwiteFiltres().description,"instance":BlackwiteFiltres()},
            "2":{"name":LumosFiltres().name,"derict":LumosFiltres().description,"instance":LumosFiltres()},
            "3":{"name":Noch().name,"derict":Noch().description,"instance":Noch()},
            "4":{"name":Upheaval90().name,"derict":Upheaval90().description,"instance":Upheaval90()},
            "5":{"name":Upheaval90().name,"derict":Upheaval90().description,"instance":Upheaval90()},
            "6":{"name":Сhangingthekey().name,"derict":Сhangingthekey().description,"instance":Сhangingthekey()},
            "7":{"name":RedbLUE().name,"derict":RedbLUE().description,"instance":RedbLUE()},
            "8":{"name":OgrAnche().name,"derict":OgrAnche().description,"instance":OgrAnche()},
            ".":{"name":EasterEgg().name,"derict":EasterEgg().description,"instance":EasterEgg()}}
















