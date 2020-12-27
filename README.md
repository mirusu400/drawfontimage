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

# Example(temporary)

```
# Make a normal font in RGBA
import core
cv = core.canvas()
cv.create("안녕하세요")

# Make a font with outline, specific font, size
cv = core.canvas(font="example/NanumGothic.ttf", size=15, oline=3)
cv.create("폰트, 테두리, 크기 테스트", output="output2.png")
    
# Make a font with other color, row, column
cv = core.canvas(column=5, oline=2, bgcolor=(128, 0, 0, 255), fcolor=(0, 128, 0, 255), ocolor=(0, 0, 128, 255))
cv.create("일이삼사오육칠팔구십", output="output3.png")

# Make a font in RGB mode
cv = core.canvas(mode="RGB")
cv.create("알쥐비모드테스트!1234", output="output4.bmp")

# Make a font in text file
cv = core.canvas()
cv.create("example/simplekorean.txt", output="output5.png")

# Make a font without anti-aliasing
cv = core.canvas(mode="RGBA")
cv.create("안티앨리어싱없이", output="output6.png", mode="n")

```

* * *
    
# TODO
* Add GUI design
* Make image with posterize
* Make image with specific color palette
* Fix outline when turn off anti-aliasing

## Thanks to
* 잎사귀소년 - 아이디어 제공