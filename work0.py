# %%
import PIL
import random
from PIL import Image,ImageFont,ImageDraw

def number_add (num):
    picture=Image.open("F:\workspace\pythontest\draw.jpg")
    x,y=picture.size
    draw=ImageDraw.Draw(picture)
    font_add=ImageFont.truetype('C:\Windows\Fonts\AGENCYR.ttf',50)
    draw.text((x-40,30),'%d'%num,fill=(255,0,0),font=font_add)
    picture.show()

if __name__ == "__main__":
    num=random.randint(1,10)
    number_add (num)


