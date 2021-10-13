from PyQt5.QtWidgets import (
    QMessageBox,
    QMainWindow,
    QApplication,
    QFileDialog,
)
from PyQt5.QtGui import (
    QIcon,
    QDesktopServices,
)
from PyQt5.QtCore import (
    Qt,
    QUrl
)
from PyQt5 import uic
import core

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

form_class = uic.loadUiType("./form/form.ui")[0]

class QtWindowDrawFontImage(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.first_components = [
            self.rad_fromfile, self.rad_fromtext, self.btn_fromfile, self.line_fromfile, self.edit_fromtext
        ]
        self.second_components = [
            self.chk_useotherfont, self.btn_otherfont, self.line_fromotherfont, self.line_fontsize,
            self.line_textcolor_R, self.line_textcolor_G, self.line_textcolor_B, self.line_textcolor_A,
            self.line_background_R, self.line_background_G, self.line_background_B, self.line_background_A
        ]
        self.third_components = [
            self.chk_useoutline, self.chk_useRGB, self.chk_usealiasing,
            self.line_outline_R, self.line_outline_G, self.line_outline_B, self.line_outline_A, self.line_outline_size
        ]
        self.fourth_components = [
            self.line_column, self.line_iwidth, self.line_iheight,
            self.line_cwidth, self.line_cheight, self.line_xoffset, self.line_yoffset
        ]
        self.fifth_components = [
            self.chk_usespecialpalette, self.btn_spepal, self.line_spepal,
            self.chk_savejson, self.btn_build
        ]
        self.outline_components = [
            self.line_outline_R, self.line_outline_G, self.line_outline_B, self.line_outline_A,
            self.line_outline_size
        ]
        # 1. first components
        self.btn_fromfile.clicked.connect(self.fn_btn_fromfile)
        self.rad_fromfile.clicked.connect(self.fn_rad_fromfile)
        self.rad_fromtext.clicked.connect(self.fn_rad_fromtext)
        self.line_fromfile.textChanged.connect(self.fn_text_changed)
        self.edit_fromtext.textChanged.connect(self.fn_text_changed)
        

        # 2. second components
        self.chk_useotherfont.clicked.connect(self.fn_chk_useotherfont)
        self.btn_otherfont.clicked.connect(self.fn_btn_otherfont)

        # 3. third components
        self.chk_useoutline.clicked.connect(self.fn_chk_useoutline)

        # 5. fifth components
        self.btn_spepal.clicked.connect(self.fn_btn_spepal)
        self.btn_build.clicked.connect(self.fn_btn_build)
        self.chk_usespecialpalette.clicked.connect(self.fn_chk_usespecialpalette)
        return
    
    def fn_btn_build(self):
        text = ""
        font = ""
        palette = ""
        fontsize = 0
        fontcolor = (0, 0, 0, 0)
        backgroundcolor = (0, 0, 0, 0)
        outlinecolor = (0, 0, 0, 0)
        outlinesize = 0
        column = 0
        iwidth = 0
        iheight = 0
        cwidth = 0
        cheight = 0
        xoffset = 0
        yoffset = 0
        useotherfont = self.chk_useotherfont.isChecked()
        useoutline = self.chk_useoutline.isChecked()
        rgbmode = "RGB" if self.chk_useRGB.isChecked() else "RGBA"
        aliasmode = "n" if self.chk_usealiasing.isChecked() else "a"
        usespecialpalette = self.chk_usespecialpalette.isChecked()

        if self.rad_fromfile.isChecked():
            text = self.line_fromfile.text()
        elif self.rad_fromtext.isChecked():
            text = self.edit_fromtext.toPlainText()
        if text == "":
            QMessageBox.warning(self, "Warning", "Please select a text source.")
            return
        
        if useotherfont:
            font = self.line_fromotherfont.text()
            if font == "":
                QMessageBox.warning(self, "Warning", "Please select a font source.")
                return
            
        if usespecialpalette:
            palette = self.line_spepal.text()
            if palette == "":
                QMessageBox.warning(self, "Warning", "Please select a palette source.")
                return
        

        fontsize = int(self.line_fontsize.text())
        if fontsize == 0 or fontsize == "":
            QMessageBox.warning(self, "Warning", "Please input a font size.")
            return
        fontcolor = (int(self.line_textcolor_R.text()), int(self.line_textcolor_G.text()), int(self.line_textcolor_B.text()), int(self.line_textcolor_A.text()))
        backgroundcolor = (int(self.line_background_R.text()), int(self.line_background_G.text()), int(self.line_background_B.text()), int(self.line_background_A.text()))
        
        if useoutline:
            outlinecolor = (int(self.line_outline_R.text()), int(self.line_outline_G.text()), int(self.line_outline_B.text()), int(self.line_outline_A.text()))
            outlinesize = int(self.line_outline_size.text())

        column = int(self.line_column.text()) if self.line_column.text() != "" else 0
        iwidth = int(self.line_iwidth.text()) if self.line_iwidth.text() != "" else 0
        iheight = int(self.line_iheight.text()) if self.line_iheight.text() != "" else 0
        cwidth = int(self.line_cwidth.text()) if self.line_cwidth.text() != "" else 0
        cheight = int(self.line_cheight.text()) if self.line_cheight.text() != "" else 0
        xoffset = int(self.line_xoffset.text()) if self.line_xoffset.text() != "" else 0
        yoffset = int(self.line_yoffset.text()) if self.line_yoffset.text() != "" else 0

        if column == 0:
            QMessageBox.warning(self, "Warning", "Please select a column.")
            return

        # Make canvas, build it
        try:
            cv = core.canvas(font=font, mode=rgbmode, size=fontsize, column=column,
            width=iwidth, height=iheight, fcolor=fontcolor, bgcolor=backgroundcolor,
            ocolor=outlinecolor, oline=outlinesize)
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Error while creating canvas\n{}".format(e))
            return

        outfname = QFileDialog.getSaveFileName(self, 'Save canvas', './', "png (*.png)")[0]
        if outfname == "":
            return

        # Create canvas image
        try:
            cv.create(text, cwidth=cwidth, cheight=cheight, xoffset=xoffset, yoffset=yoffset,
                mode=aliasmode)
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Error while drawing font\n{}".format(e))
            return
    
        # Post-processing
        if usespecialpalette:
            cv.change_palette()
        # TODO: add other post-processing (ex. posterize)

        # Save image
        try:
            cv.save(outfname)
        except SystemError as e:
            QMessageBox.warning(self, "Warning", "Error occurred. This may cause by small canvas size.\nError: {}".format(e))
            raise
            return
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Error while save: {}".format(e))
            return
        reply = QMessageBox.question(self, 'Information', 'Succesfully saved.\nDo you want to open?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QDesktopServices.openUrl(QUrl.fromLocalFile(outfname))
        



    def fn_btn_spepal(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.line_spepal.setText(fname)
        return

    def fn_btn_otherfont(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.line_fromotherfont.setText(fname)
        return
    
    def fn_text_changed(self):
        # print(self.rad_fromfile.isChecked())
        # print(self.rad_fromtext.isChecked())
        line = self.line_fromfile.text()
        text = self.edit_fromtext.toPlainText()
        if line == '' and text == '':
            return
        for comp in self.second_components:
            comp.setEnabled(True)
        for comp in self.third_components:
            comp.setEnabled(True)
        for comp in self.fourth_components:
            comp.setEnabled(True)
        for comp in self.fifth_components:
            comp.setEnabled(True)
        self.fn_chk_useoutline()
        self.fn_chk_useotherfont()
        self.fn_chk_usespecialpalette()
        return
    def fn_chk_usespecialpalette(self):
        if self.chk_usespecialpalette.isChecked():
            self.line_spepal.setEnabled(True)
            self.btn_spepal.setEnabled(True)
        else:
            self.line_spepal.setEnabled(False)
            self.btn_spepal.setEnabled(False)
        return

    def fn_chk_useotherfont(self):
        if self.chk_useotherfont.isChecked():
            self.line_fromotherfont.setEnabled(True)
            self.btn_otherfont.setEnabled(True)
        else:
            self.line_fromotherfont.setEnabled(False)
            self.btn_otherfont.setEnabled(False)
        return

    def fn_chk_useoutline(self):
        if self.chk_useoutline.isChecked():
            for comp in self.outline_components:
                comp.setEnabled(True)
        else:
            for comp in self.outline_components:
                comp.setEnabled(False)

    def fn_rad_fromfile(self):
        self.btn_fromfile.setEnabled(True)
        self.line_fromfile.setEnabled(True)
        self.edit_fromtext.setEnabled(False)
        return
    
    def fn_rad_fromtext(self):
        self.edit_fromtext.setEnabled(True)
        self.btn_fromfile.setEnabled(False)
        self.line_fromfile.setEnabled(False)
        return        

    def fn_btn_fromfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.line_fromfile.setText(fname)
        return