# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_writeTextFile/readWriteFile.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(42, 42))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setIcon(icon)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionNewFile = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFile.setIcon(icon1)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image/save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon4)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setObjectName("actionSettings")
        self.actionCloseFile = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/image/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseFile.setIcon(icon6)
        self.actionCloseFile.setObjectName("actionCloseFile")
        self.toolBar.addAction(self.actionNewFile)
        self.toolBar.addAction(self.actionOpenFile)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionCloseFile)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "read and write text files"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpenFile.setText(_translate("MainWindow", "OpenFile"))
        self.actionOpenFile.setToolTip(_translate("MainWindow", "open text file"))
        self.actionOpenFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNewFile.setText(_translate("MainWindow", "NewFile"))
        self.actionNewFile.setToolTip(_translate("MainWindow", "New text file"))
        self.actionNewFile.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Quit Application"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "save text file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "SaveAs"))
        self.actionSaveAs.setToolTip(_translate("MainWindow", "save as text file"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setToolTip(_translate("MainWindow", "setting text file"))
        self.actionCloseFile.setText(_translate("MainWindow", "CloseFile"))
        self.actionCloseFile.setToolTip(_translate("MainWindow", "close text file"))
        self.actionCloseFile.setShortcut(_translate("MainWindow", "Ctrl+W"))

import icon_rc
