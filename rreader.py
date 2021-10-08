import sys
import os
import json
import binascii


class palette():
    def __init__(self, src, dst=""):
        self.src = src
        if not dst:
            self.dst = os.path.splitext(src)[0] + ".json"
        else:
            self.dst = dst
        self.data = {}
        self.size = os.path.getsize(src)
        self.count = (self.size - 0x18) // 4
        self.palette = []
        fin = open(src, "rb")

        # Check the file is correct
        buf = fin.read(4)
        if buf != b'RIFF':
            print("It doesn't seems RIFF(palette) file!")
            sys.exit()

        self.data['size'] = self.size
        self.data['count'] = self.count
        self.data['color'] = []
        fin.seek(0x18)
        for i in range(self.count):
            r = binascii.hexlify(fin.read(1)).decode('utf-8')
            g = binascii.hexlify(fin.read(1)).decode('utf-8')
            b = binascii.hexlify(fin.read(1)).decode('utf-8')
            a = binascii.hexlify(fin.read(1)).decode('utf-8')
            color = (i, r, g, b, a)
            self.data['color'].append(color)
            self.palette.append(color)
        fin.close()
        return

    def dump(self):
        with open(self.dst, 'w', encoding="utf-8") as fjson:
            json.dump(self.data, fjson)

    def getpalette(self):
        return self.palette


if __name__ == "__main__":
    src = sys.argv[1]
    try:
        dst = sys.argv[2]
    except IndexError:
        dst = os.path.splitext(src)[0] + ".json"
    p = palette(src, dst)
    p.getpalette()
    p.dump()