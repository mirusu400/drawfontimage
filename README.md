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
Just open `index.py` and use GUI frontend.

# Example (in CLU)

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
