from PIL import Image, ImageDraw, ImageFont
import platform
import os.path
class canvas:
    def __init__(self, width=1000, height=1000, size=10, font=None):
        self.size=size
        self.width=width
        self.height=height
        self.font=None
        if font==None:
            system=platform.system()
            # Check system neither Windows or Linux
            if system == "WindowsError":
                if os.path.exists("C:\Windows\Fonts\gulim.ttc"):
                    self.font="C:\Windows\Fonts\gulim.ttc"
                else:
                    self.font="C:\Windows\Fonts\Arial.ttf"
            elif system == "Linux":
                if os.path.exists("/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf"):
                    self.font="/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf"
                else:
                    self.font="/usr/share/fonts/truetype/freefont/FreeMono.ttf"
        
    def createImg(text,width=-1,xPos=0,yPos=0):
        if width == -1:
            width = self.size + 3
        # xPos, yPos = 폰트가 시작될 좌표
        size=self.size 
        img = Image.new("RGBA", (self.width, self.height), color = (0, 0, 0, 0) ) 
        fnt = ImageFont.truetype('gulim.ttf', fontSize, encoding="UTF-8")


        # 각 글씨 별 간격.
        width = 20

        draw = ImageDraw.Draw(img)
        stroke_color=(128,128,128,128)
        # 구문을 리스트로 받아서, 글씨를 하나하나 그립니다.
        for char in text:
            draw.text(
                (xPos,yPos),
                char,
                fill=(255,255,255,255),
                font=fnt,
                anchor="la",
                stroke_width=2,
                stroke_fill=stroke_color) 
            xPos+=width

        img.save("파일명.png") #파일 저장.
