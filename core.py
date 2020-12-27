from PIL import Image, ImageDraw, ImageFont
import platform
import os.path


class canvas:
    def __init__(self, font=None, mode="RGBA", size=12, row=10, column=10,
                 width=-1, height=-1, oline=0,
                 bgcolor=(0, 0, 0, 0), fcolor=(255, 255, 255, 255),
                 ocolor=(0, 0, 0, 255)):
        """
            font = A font file name
            row = Text's row in image (maybe never used)
            column = Text's column in image
            width = Image's width
            height = Image's height
        """
        self.size = size
        self.width = width
        self.height = height
        self.outlinewidth = oline
        self.font = font
        self.row = row
        self.column = column
        self.bgcolor = bgcolor
        self.fontcolor = fcolor
        self.outlinecolor = ocolor
        self.mode = mode
        if mode == "RGB":
            bgcolor = (bgcolor[0], bgcolor[1], bgcolor[2])
            fcolor = (fcolor[0], fcolor[1], fcolor[2])
            ocolor = (ocolor[0], ocolor[1], ocolor[2])

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

    def createImg(self, text, output="output.png", cwidth=-1, cheight=-1,
                  xoffset=0, yoffset=0, mode="t"):
        """
            Create a image file(*.png) with specific text
            text = A text that will be written(string or text file)
            cwidth, cheight = A character's width and height
            xoffset, yoffset = A starting point which font start
        """

        # Set character's width
        if cwidth <= 0:
            cwidth = self.size + 3
        if cheight <= 0:
            cheight = self.size + 3

        # Set text
        if os.path.exists(text):
            with open(text, mode='r') as file:
                text = "".join(file.readlines())

        # Set image's width and height
        if self.width == -1:
            if len(text) <= self.column:
                maxwidth = (len(text) + 1) * cwidth
            else:
                maxwidth = (self.column + 1) * cwidth
        if self.height == -1:
            maxheight = ((len(text) // self.column) + 1) * cheight

        img = Image.new(self.mode, (maxwidth, maxheight), color=self.bgcolor)
        fnt = ImageFont.truetype(self.font, self.size, encoding="UTF-8")

        draw = ImageDraw.Draw(img)
        if self.mode == "b":
            draw.fontmode = "1"
        nrow = 0
        ncolumn = 0
        # Draw a chracter into image
        for char in text:
            # Get position
            xpos = (ncolumn * cwidth) + xoffset
            ypos = (nrow * cheight) + yoffset
            draw.text(
                (xpos, ypos),
                char,
                fill=self.fontcolor,
                font=fnt,
                # https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html#text-anchors
                anchor="la",
                stroke_width=self.outlinewidth,
                stroke_fill=self.outlinecolor
            )

            if ncolumn == (self.column-1):
                nrow += 1
                ncolumn = 0
            else:
                ncolumn += 1


        img.save(output)
