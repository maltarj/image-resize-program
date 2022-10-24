import sys
from qtDesigner.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class ImageResizing(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.open_image)
        self.btnResize.clicked.connect(self.image_resize)
        self.btnSave.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open Image',
            r'/users/public/pictures',
            options=QFileDialog.DontUseNativeDialog
        )
        self.inputOpenArq.setText(image)
        self.original_image = QPixmap(image)
        self.labelImg.setPixmap(self.original_image)
        self.inputWidth.setText(str(self.original_image.width()))
        self.inputHeight.setText(str(self.original_image.height()))

    def image_resize(self):
        width = int(self.inputWidth.text())
        self.new_image = self.original_image.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_image)
        self.inputWidth.setText(str(self.new_image.width()))
        self.inputHeight.setText(str(self.new_image.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save Image',
            r'/users/public/pictures',
            options=QFileDialog.DontUseNativeDialog
        )
        self.new_image.save(image, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resize = ImageResizing()
    resize.show()
    qt.exec_()
