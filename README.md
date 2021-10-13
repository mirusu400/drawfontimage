# drawfontimage
![usage](https://github.com/mirusu400/drawfontimage/blob/main/docs/usage.gif?raw=true)

Draw a font into static image file 

# Requirement
```
Python >= 3.X
pillow == 7.2.0
chardet == 4.0.0
pyqt5
```

# Installation
```
pip install pillow==7.2.0
pip install chardet==4.0.0
pip install pyqt5
```

# Functions
* Draw a font.
* Draw a font with outline.
* Draw a font without anti-aliasing.
* Draw a font with posterize.

# Usage
Just double click `index.py` and use GUI frontend.

# Usage (in CLI)
```
usage: index.py [-h] [--font FONT] [--size SIZE] [--width WIDTH] [--height HEIGHT] [--column COLUMN] [--disable-alpha]
                [--color COLOR] [--background-color BACKGROUND_COLOR] [--enable-outline]
                [--outline-width OUTLINE_WIDTH] [--outline-color OUTLINE_COLOR] [--character-width CHARACTER_WIDTH]
                [--character-height CHARACTER_HEIGHT] [--xoffset XOFFSET] [--yoffset YOFFSET]
                [--diasble-anti-aliasing] [--output OUTPUT]
                text

Draw font into static image

positional arguments:
  text                              A string or text file to make image.

optional arguments:
  -h, --help                        show this help message and exit
  --font FONT, -f FONT              Path of custom font
  --size SIZE, -s SIZE              Size of font
  --width WIDTH                     Width of canvas
  --height HEIGHT                   Height of canvas
  --column COLUMN, -col COLUMN      Number of columns
  --disable-alpha, -d               Disable alpha channel
  --color COLOR, -c COLOR           Color of font
  --background-color BACKGROUND_COLOR, -bg BACKGROUND_COLOR
                                    Background color of font
  --enable-outline, -oline
                                    Enable outline
  --outline-width OUTLINE_WIDTH, -owidth OUTLINE_WIDTH
                                    Outline width
  --outline-color OUTLINE_COLOR, -ocolor OUTLINE_COLOR
                                    Outline color of font
  --character-width CHARACTER_WIDTH, -cwidth CHARACTER_WIDTH
                                    Width of each character
  --character-height CHARACTER_HEIGHT, -cheight CHARACTER_HEIGHT
                                    Height of each character
  --xoffset XOFFSET, -x XOFFSET
                                    X Offset of each character
  --yoffset YOFFSET, -y YOFFSET
                                    Y Offset of each character
  --diasble-anti-aliasing, -dalias
                                    Disable anti-aliasing
  --output OUTPUT, -o OUTPUT
                                    Output file name
```
```
index.py "abcdefghijklmnopqrstuvwxyz" --column 15 -c #FFFF00 -bg #00FFFF -oline -owidth 2 -ocolor #FFFFFF -o example1.png
``` 
# Example (Using core.py)

```
# Make a normal font in RGBA
import core
cv = core.canvas()
cv.create("안녕하세요")
cv.save("output1.png")

# Make a font with outline, specific font, size
cv = core.canvas(font="example/NanumGothic.ttf", size=15, oline=3)
cv.create("폰트, 테두리, 크기 테스트")
cv.save("output2.png")
    
# Make a font with other color, row, column
cv = core.canvas(column=5, oline=2, bgcolor=(128, 0, 0, 255), fcolor=(0, 128, 0, 255), ocolor=(0, 0, 128, 255))
cv.create("일이삼사오육칠팔구십")
cv.save("output2.png")

# Make a font in RGB mode
cv = core.canvas(mode="RGB")
cv.create("알쥐비모드테스트!1234")
cv.save("output3.png")

# Make a font in text file
cv = core.canvas()
cv.create("example/simplekorean.txt")
cv.save("output4.png")

# Make a font without anti-aliasing
cv = core.canvas(mode="RGBA")
cv.create("안티앨리어싱없이", mode="n")
cv.save("output5.png")

# Make a font with specific palette
cv = core.canvas(font="example/NanumGothic.ttf", bgcolor=(250,250,250,255), fcolor=(32,16,13,255), size=32)
cv.create("안녕하슈")
cv.save("output6-1.png")
cv.change_palette("./example/TLP.pal")
cv.save("output6-2.png")

# Use Manifest File from exist BFFNT Font
cv = core.canvas(font="example/NanumGothic.ttf", bgcolor=(250,250,250,255), fcolor=(32,16,13,255), size=32)
cv.create("안녕하슈",jsonset = "example/test_manifest.json")
cv.save("output7.png")
```

* * *
    
# TODO
* Save, Load JSON file
* Add custom shadow
* 한국어 지원

## Thanks to
* 잎사귀소년 - 아이디어 제공
