# -*- coding: utf-8 -*-
import sys, os

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *
class Label(QLabel):

	def __init__(self):
		super().__init__()
		self.image = False
		self.imagePath = False
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasImage():
			self.image = True
			event.accept()
		elif event.mimeData().hasUrls():
			self.imagePath = True
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		if self.image:
			self.setPixmap(QPixmap(event.mimeData().imageData()))
		elif self.imagePath:
			if len(event.mimeData().urls()) > 0:
				imagePath = (event.mimeData().urls()[0].toLocalFile())
				self.setPixmap(QPixmap(imagePath))

class Combo(QComboBox):

	def __init__(self, title, parent):
		super(Combo, self).__init__( parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, e):
		print( e)
		if e.mimeData().hasText():
			e.accept()
		else:
			e.ignore()

	def dropEvent(self, e):
		self.addItem(e.mimeData().text())

class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		lo = QFormLayout()
		lo.addRow(QLabel("请把左边的文本拖拽到右边的下拉菜单中"))
		edit = QLineEdit()
		edit.setDragEnabled(True)
		com = Combo("Button", self)
		lo.addRow(edit,com)
		vlayout = QVBoxLayout()
		vlayout.addLayout(lo)
		vlayout.addWidget(Label())
		self.setLayout(vlayout)
		self.setWindowTitle('简单拖拽例子')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec_())
