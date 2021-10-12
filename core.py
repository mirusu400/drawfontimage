from PIL import Image, ImageDraw, ImageFont, ImageOps
from ast import literal_eval
import platform
import os.path
import json
import rreader
import re
import math
import chardet

class canvas:
    def __init__(self, font=None, mode="RGBA", size=13, row=10, column=10,
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
        self.image = ""
        self.data = {}
        if mode == "RGB":
            bgcolor = (bgcolor[0], bgcolor[1], bgcolor[2])
            fcolor = (fcolor[0], fcolor[1], fcolor[2])
            ocolor = (ocolor[0], ocolor[1], ocolor[2])

        if self.font is None:
            system = platform.system()
            # Check system neither Windows or Linux
            if system == "Windows":
                if os.path.exists("C:/Windows/Fonts/gulim.ttc"):
                    self.font = "C:/Windows/Fonts/gulim.ttc"
                else:
                    self.font = "C:/Windows/Fonts/Arial.ttf"
            elif system == "Linux":
                if os.path.exists("/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf"):
                    self.font = "/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf"
                else:
                    self.font = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"
    def setJSON(self, file):
        '''
        The function for read bffnt font file Menifest.
        '''
        try:
            with open("./test_manifest.json", "r", encoding="utf-8") as f:
                manifest = json.load(f)
            glyphWidth_dict = manifest["glyphWidths"]
            glyphMap_dict= manifest["glyphMap"]
            self.texture_dict= manifest["textureInfo"]
            self.fontInfo_dict = manifest["fontInfo"]
            self.glyph_dict = dict()
            for key, value in glyphMap_dict.items():
                char_data = glyphWidth_dict[str(value)]
                self.glyph_dict[key] = char_data
            return True
        except:
            return False

    def create(self, text, cwidth=-1, cheight=-1,
            xoffset=0, yoffset=0, mode="a", jsonset = 0, sizeOffset = 0):
        """
            Create a image file(*.png) with specific text
            text = A text that will be written(string or text file)
            cwidth, cheight = A character's width and height
            xoffset, yoffset = A starting point which font start
            jsonset = A bffnt font file's Menifest File. Use setJSON First.
            SizeOffset = font Size offset When you use Menifest JSON File.
        """
        # Check Menifest File.
        if jsonset != 0:
            if os.path.exists(jsonset):
                json_flag = self.setJSON(jsonset)
                if json_flag == False:
                    print("Wrong JSON File. Ignore this setting.")
                    jsonset = 0
                else:
                    cwidth = self.texture_dict["glyph"]["width"] + 1
                    cheight = self.texture_dict["glyph"]["height"] + 1
                    self.size = self.fontInfo_dict["width"] - sizeOffset
            else:
                print("Wrong JSON File. Ignore this setting.")
                jsonset = 0

        # Set character's width
        if cwidth <= 0:
            cwidth = self.size + 3
        if cheight <= 0:
            cheight = self.size + 3

        # Set text
        if os.path.exists(text):
            with open(text, mode='rb') as file:
                textencoding = chardet.detect(file.read())['encoding']
            with open(text, mode='r', encoding=textencoding) as file:
                text = "".join(file.readlines())

        # Set image's width and height
        if self.width == -1:
            if len(text) <= self.column:
                self.width = (len(text) + 1) * cwidth
            else:
                self.width = (self.column + 1) * cwidth
        if self.height == -1:
            self.height = ((len(text) // self.column) + 2) * cheight

        img = Image.new(self.mode, (self.width, self.height), color=self.bgcolor)
        fnt = ImageFont.truetype(self.font, self.size, encoding="UTF-8")

        draw = ImageDraw.Draw(img)

        # Set non-anti-alias
        if mode == "n":
            draw.fontmode = "1"
        nrow = 0
        ncolumn = 0

        # Save dict (for json)
        self.data['width'] = self.width
        self.data['height'] = self.height
        self.data['cwidth'] = cwidth
        self.data['cheight'] = cheight
        self.data['font'] = self.font
        self.data['size'] = self.size
        self.data['outlinewidth'] = self.outlinewidth
        self.data['bgcolor'] = self.bgcolor
        self.data['fontcolor'] = self.fontcolor
        self.data['outlinecolor'] = self.outlinecolor
        self.data['imagemode'] = self.mode
        self.data['fontmode'] = mode
        self.data['character'] = []

        # Draw a chracter into image
        for char in text:
            chardata = {}
            # Get position

            if jsonset != 0:
                if char in self.glyph_dict.keys() and ncolumn != 0:
                    '''
                    for apply font's kerning settings
                    '''
                    xcharoffset = self.glyph_dict[char]["left"]
                else:
                    xcharoffset = 0
            else:
                xcharoffset = 0
            xpos = (ncolumn * cwidth) + xoffset - xcharoffset 
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

            # Save chracter data (for json)
            chardata['char'] = char
            chardata['xpos'] = xpos
            chardata['ypos'] = ypos
            self.data['character'].append(chardata)

        self.image = img
        # img.save(outputfile)
        return img

    def change_palette(self, p):
        palette = p
        colors = []
        # Get palette
        # if RIFF, read riff..
        if os.path.splitext(palette)[1] == '.pal':
            rre = rreader.palette(palette)
            colors = rre.getpalette()

        # if JSON, read json..
        elif os.path.splitext(palette)[1] == '.json':
            with open(palette, 'r', encoding="utf-8") as fjson:
                json_data = json.load(fjson)
                tmp = json_data['color']
                for item in tmp:
                    t = (item[1], item[2], item[3])
                    colors.append(t)
        else:
            raise Exception("Unknown file extension")
        print("Changing colors may take a while.. Please wait....")

        # Linear-searching palettes with each pixel, so the algorithm should be much slow..
        # It takes O(MN^2) which M is numbers of color and N of width and height..
        # Of course, It should be improved, I'll do that..

        im = self.image.load()
        DP = [[[-1 for i in range(257)] for j in range(257)] for k in range(257)]
        for x in range(0, self.width):
            for y in range(0, self.height):
                tidx = -1
                tdifference = 987654321
                if self.mode == "RGBA":
                    r, g, b, a = self.image.getpixel((x, y))
                else:
                    r, g, b = self.image.getpixel((x, y))
                if DP[r][g][b] != -1:
                    tidx = DP[r][g][b]
                else:
                    for idx, item in enumerate(colors):
                        bidx, tr, tg, tb, ta = item
                        tr = int(tr, 16)
                        tg = int(tg, 16)
                        tb = int(tb, 16)
                        ta = int(ta, 16)
                        td = abs(r - tr) + abs(g - tg) + abs(b - tb)
                        if td < tdifference:
                            tidx = idx
                            tdifference = td
                    DP[r][g][b] = tidx
                idx, ar, ag, ab, aa = colors[tidx]
                ar = int(ar, 16)
                ag = int(ag, 16)
                ab = int(ab, 16)
                aa = int(aa, 16)
                if self.mode == "RGBA":
                    im[x, y] = (ar, ag, ab, a)
                else:
                    im[x, y] = (ar, ag, ab)
        return

    def posterize_palette(self, bit):
        im = self.image
        self.image = ImageOps.posterize(im, bit)
        return self.image

    def save(self, o="output.png"):
        self.image.save(o)

    def dump(self, o="output.json"):
        with open(o, 'w', encoding="utf-8") as fjson:
            json.dump(self.data, fjson, indent=4)