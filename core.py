from PIL import Image, ImageDraw, ImageFont
import platform
import os.path


class canvas:
    def __init__(self, width=1000, height=1000, size=10, row=10, column=10,
                 font=None):
        self.size = size
        self.width = width
        self.height = height
        self.font = font
        self.row = row
        self.column = column
        if self.font is None:
            system = platform.system()
            # Check system neither Windows or Linux
            if system == "WindowsError":
                if os.path.exists("C:/Windows/Fonts/gulim.ttc"):
                    self.font = "C:/Windows/Fonts/gulim.ttc"
                else:
                    self.font = "C:/Windows/Fonts/Arial.ttf"
            elif system == "Linux":
                if os.path.exists("/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf"):
                    self.font = "/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf"
                else:
                    self.font = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

    def createImg(self, text, output="output.png", width=-1, height=-1,
                  xoffset=0, yoffset=0):
        """
            Create a image file(*.png) with specific text
            text = A text that will be written(string or text file)
            width, height = A character's width and height
            xoffset, yoffset = A starting point which font start
        """

        if width == -1:
            width = self.size + 3
        if height == -1:
            height = self.size + 3

        if os.path.exists(text):
            with open(text, mode='r') as file:
                text = "".join(file.readlines())
        print(text)
        img = Image.new("RGBA", (self.width, self.height), color = (0, 0, 0, 0) ) 
        fnt = ImageFont.truetype(self.font, self.size, encoding="UTF-8")

        draw = ImageDraw.Draw(img)
        stroke_color=(128,128,128,128)
        nrow = 0
        ncolumn = 0
        # 구문을 리스트로 받아서, 글씨를 하나하나 그립니다.
        for char in text:
            xpos = (ncolumn * width) + xoffset
            ypos = (nrow * height) + yoffset
            draw.text(
                (xpos, ypos),
                char,
                fill=(255, 255, 255, 255),
                font=fnt,
                anchor="la",
                stroke_width=2,
                stroke_fill=stroke_color
            )

            if ncolumn == self.column:
                nrow += 1
                ncolumn = 0
            else:
                ncolumn += 1
        img.save(output)
