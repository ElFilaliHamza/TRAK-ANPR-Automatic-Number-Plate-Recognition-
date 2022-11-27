# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anprMainUIvYtRjG.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(723, 517)
        MainWindow.setStyleSheet(u"")
        self.actionread_image = QAction(MainWindow)
        self.actionread_image.setObjectName(u"actionread_image")
        self.actionclear_outputs = QAction(MainWindow)
        self.actionclear_outputs.setObjectName(u"actionclear_outputs")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.video_view = QLabel(self.centralwidget)
        self.video_view.setObjectName(u"video_view")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_view.sizePolicy().hasHeightForWidth())
        self.video_view.setSizePolicy(sizePolicy)
        self.video_view.setMinimumSize(QSize(600, 250))
        self.video_view.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.video_view.setTextFormat(Qt.PlainText)
        self.video_view.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.video_view, 4, 1, 1, 3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)

        self.stop_video_btn = QPushButton(self.centralwidget)
        self.stop_video_btn.setObjectName(u"stop_video_btn")
        self.stop_video_btn.setMinimumSize(QSize(0, 22))
        self.stop_video_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_video_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(34, 46, 57);\n"
"	border-color: rgb(222, 222, 222);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(33, 55, 63);\n"
"	border:1px solid rgb(133, 215, 222);\n"
"	color: white;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.stop_video_btn, 2, 3, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1, Qt.AlignTop)

        self.plate_img = QLabel(self.centralwidget)
        self.plate_img.setObjectName(u"plate_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plate_img.sizePolicy().hasHeightForWidth())
        self.plate_img.setSizePolicy(sizePolicy1)
        self.plate_img.setMinimumSize(QSize(0, 50))
        self.plate_img.setMaximumSize(QSize(16777215, 70))
        self.plate_img.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.plate_img.setTextFormat(Qt.PlainText)
        self.plate_img.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.plate_img, 5, 1, 1, 3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1, Qt.AlignTop)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(150, 16777215))
        self.label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1, Qt.AlignTop)

        self.plate_text = QLineEdit(self.centralwidget)
        self.plate_text.setObjectName(u"plate_text")
        self.plate_text.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.plate_text.setFont(font)
        self.plate_text.setStyleSheet(u"\n"
"background-color: rgb(30, 49, 57);\n"
"color: rgb(255, 255, 255);")
        self.plate_text.setAlignment(Qt.AlignCenter)
        self.plate_text.setReadOnly(True)

        self.gridLayout.addWidget(self.plate_text, 6, 1, 1, 3)

        self.close_cam_btn = QPushButton(self.centralwidget)
        self.close_cam_btn.setObjectName(u"close_cam_btn")
        self.close_cam_btn.setMinimumSize(QSize(0, 22))
        self.close_cam_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_cam_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(34, 46, 57);\n"
"	border-color: rgb(222, 222, 222);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(33, 55, 63);\n"
"	border:1px solid rgb(133, 215, 222);\n"
"	color: white;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.close_cam_btn, 0, 3, 1, 1)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy2)
        self.clear_btn.setMinimumSize(QSize(0, 22))
        self.clear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(34, 46, 57);\n"
"	border-color: rgb(222, 222, 222);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(33, 55, 63);\n"
"	border:1px solid rgb(133, 215, 222);\n"
"	color: white;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.clear_btn, 0, 0, 1, 1)

        self.open_cam_btn = QPushButton(self.centralwidget)
        self.open_cam_btn.setObjectName(u"open_cam_btn")
        self.open_cam_btn.setMinimumSize(QSize(0, 22))
        self.open_cam_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cam_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(34, 46, 57);\n"
"	border-color: rgb(222, 222, 222);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(33, 55, 63);\n"
"	border:1px solid rgb(133, 215, 222);\n"
"	color: white;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.open_cam_btn, 0, 1, 1, 2)

        self.load_video_btn = QPushButton(self.centralwidget)
        self.load_video_btn.setObjectName(u"load_video_btn")
        self.load_video_btn.setMinimumSize(QSize(0, 22))
        self.load_video_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_video_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(34, 46, 57);\n"
"	border-color: rgb(222, 222, 222);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(33, 55, 63);\n"
"	border:1px solid rgb(133, 215, 222);\n"
"	color: white;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.load_video_btn, 2, 1, 1, 2)

        self.start_recognition_btn = QPushButton(self.centralwidget)
        self.start_recognition_btn.setObjectName(u"start_recognition_btn")
        self.start_recognition_btn.setMinimumSize(QSize(0, 22))
        self.start_recognition_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_recognition_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(34, 46, 57);\n"
"	border-color: rgb(222, 222, 222);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(33, 55, 63);\n"
"	border:1px solid rgb(133, 215, 222);\n"
"	color: white;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.start_recognition_btn, 1, 3, 1, 1)

        self.load_img_btn = QPushButton(self.centralwidget)
        self.load_img_btn.setObjectName(u"load_img_btn")
        self.load_img_btn.setMinimumSize(QSize(0, 22))
        self.load_img_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_img_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(34, 46, 57);\n"
"	border-color: rgb(222, 222, 222);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(33, 55, 63);\n"
"	border:1px solid rgb(133, 215, 222);\n"
"	color: white;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.load_img_btn, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 723, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.mystatusbar = QStatusBar(MainWindow)
        self.mystatusbar.setObjectName(u"mystatusbar")
        MainWindow.setStatusBar(self.mystatusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionread_image)
        self.menuFile.addAction(self.actionclear_outputs)
        self.menuFile.addAction(self.actionexit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionread_image.setText(QCoreApplication.translate("MainWindow", u"load image", None))
        self.actionclear_outputs.setText(QCoreApplication.translate("MainWindow", u"clear outputs", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.video_view.setText(QCoreApplication.translate("MainWindow", u"VIDEO VIEW", None))
        self.stop_video_btn.setText(QCoreApplication.translate("MainWindow", u"Stop Video", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PLATE IMAGE", None))
        self.plate_img.setText(QCoreApplication.translate("MainWindow", u"PLATE IMAGE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PLATE NUMBER", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CAPTURE", None))
        self.plate_text.setText(QCoreApplication.translate("MainWindow", u"PLATE NUMBER", None))
        self.close_cam_btn.setText(QCoreApplication.translate("MainWindow", u"Close Camera", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.open_cam_btn.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.load_video_btn.setText(QCoreApplication.translate("MainWindow", u"load Video", None))
        self.start_recognition_btn.setText(QCoreApplication.translate("MainWindow", u"Start Image Recognition", None))
        self.load_img_btn.setText(QCoreApplication.translate("MainWindow", u"load image", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

