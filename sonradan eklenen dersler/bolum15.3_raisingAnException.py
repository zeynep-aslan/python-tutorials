# x=10
# if x>5:
#     raise ValueError('x, 5 den buyuk olamazz')  # hata fırlattık
# ValueError oldugunu biz karar verdik

def colorize(text, color):
    colors = ("blue", "green", "red")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalidir")

    if type(color) is not str:
        raise TypeError("color str tipinde olmalidir")

    if color not in colors:
        raise ValueError("gecersiz bir renk ismi")

    print(f"{text} {color} renk olarak ekrana yazdirildi.")

try:
    colorize("selam", "blue")  # selam blue renk olarak ekrana yazdirildi.
    colorize("selam", "yellow")  # gecersiz bir renk ismi  

except (TypeError, ValueError) as e:
    print(e)
    
