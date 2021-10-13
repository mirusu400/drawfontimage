from PyQt5.QtWidgets import (
    QApplication,
    qApp
)

from PyQt5 import uic
from gui import QtWindowDrawFontImage
import argparse
import sys
import core
import os
import argparse






if __name__ == '__main__':
    # Gui mode
    if len(sys.argv) == 1:
        app = QApplication(sys.argv)
        myWindow = QtWindowDrawFontImage()
        myWindow.show()
        app.exec_()
    else:
        parser = argparse.ArgumentParser(description="Draw font into static image")
        parser.add_argument('text', type=str, help='A string or text file to make image.')
        parser.add_argument('--font', '-f', type=str, default=None, help="Path of custom font")
        parser.add_argument('--size', '-s', type=int, default=16, help="Size of font")
        parser.add_argument('--width', type=int, default=-1, help='Width of canvas')
        parser.add_argument('--height', type=int, default=-1, help="Height of canvas")
        parser.add_argument('--column', '-col', type=int, default=10, help="Number of columns")
        parser.add_argument('--disable-alpha', '-d', action='store_true', help="Disable alpha channel")
        parser.add_argument('--color', '-c', type=str, default='#000000', help="Color of font")
        parser.add_argument('--background-color', '-bg', type=str, default='#FFFFFF', help="Background color of font")
        parser.add_argument('--enable-outline', '-oline', action='store_true', help="Enable outline")
        parser.add_argument('--outline-width', '-owidth', type=int, default=1, help="Outline width")
        parser.add_argument('--outline-color', '-ocolor', type=str, default='#000000', help="Outline color of font")
        parser.add_argument('--character-width', '-cwidth', type=int, default=-1, help="Width of each character")
        parser.add_argument('--character-height', '-cheight', type=int, default=-1, help="Height of each character")
        parser.add_argument('--xoffset', '-x', type=int, default=0, help="X Offset of each character")
        parser.add_argument('--yoffset', '-y', type=int, default=0, help="Y Offset of each character")
        parser.add_argument('--diasble-anti-aliasing', '-dalias', action='store_true', help="Disable anti-aliasing")
        parser.add_argument('--output', '-o', type=str, default='output.png', help="Output file name")
        

        args = parser.parse_args()

        alphamode = "RGB" if args.disable_alpha else "RGBA"
        oline = args.outline_width if args.enable_outline else 0
        aliasmode = "n" if args.diasble_anti_aliasing else "b"
        
        cv = core.canvas(
           font = args.font, mode = alphamode, size = args.size, column = args.column,
           width = args.width, height = args.height, oline = oline,
           bgcolor = args.background_color, fcolor = args.color, ocolor = args.outline_color,
        )

        cv.create(
            args.text, cwidth = args.character_width, cheight = args.character_height,
            xoffset = args.xoffset, yoffset = args.yoffset, mode = aliasmode
        )

        cv.save(args.output)
        

        
