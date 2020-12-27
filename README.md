# drawfontimage
Draw a font into static image file 

# Requirement
```
Python >= 3.X
pillow == 7.2.0
pyqt5
```

# Installation
```
pip install pillow==7.2.0
pip install pyqt5
```

# Usage(temporary)

```
# Make a normal font in RGBA
import core
cv = core.canvas()
cv.createImg("안녕하세요")

# Make a font with outline, specific font, size
cv = core.canvas(font="NanumGothic.ttf", size=15, oline=3)
cv.createImg("폰트, 테두리, 크기 테스트", output="output2.png")
    
# Make a font with other color, row, column
cv = core.canvas(column=5, owidth=2, bgcolor=(128, 0, 0, 255), fcolor=(0, 128, 0, 255), ocolor=(0, 0, 128, 255))
cv.createImg("일이삼사오육칠팔구십", output="output3.png")

# Make a font in RGB mode
cv = core.canvas(mode="RGB")
cv.createImg("알쥐비모드테스트!1234", output="output4.bmp")

```

* * *
    
# TODO
* Add GUI design
* Make image with posterize
* Make image with specific color palette
* Make bitmap mode(without anti-aliasing)

## Thanks to
* 잎사귀소년 - 아이디어 제공