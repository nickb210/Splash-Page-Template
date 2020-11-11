#!/usr/bin/env python3
"""
$:~ pyuic5 -x mainwindow.ui -o ui_all_nba.py
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
        def setupUi(self, SplashScreen):
                if SplashScreen.objectName():
                        SplashScreen.setObjectName(u"SplashScreen")
                SplashScreen.setEnabled(True)
                SplashScreen.resize(620, 371)
                self.centralwidget = QWidget(SplashScreen)
                self.centralwidget.setObjectName(u"centralwidget")
                self.main_bg_frame = QFrame(self.centralwidget)
                self.main_bg_frame.setGeometry(QRect(10, 10, 620, 371))
                self.main_bg_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.982955, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(32, 61, 135, 255));\n"
        "border-radius: 20px;")
                self.main_bg_frame.setFrameShape(QFrame.StyledPanel)
                self.main_bg_frame.setFrameShadow(QFrame.Raised)
                self.main_bg_frame.setObjectName(u"main_bg_frame")
                self.frame = QFrame(self.main_bg_frame)
                self.frame.setGeometry(QRect(10, 60, 121, 251))
                self.frame.setToolTip("")
                self.frame.setStyleSheet("image: url(/Users/nicholausbrell/Desktop/all_nba_app/images/nba-logo-transparent.png);\n"
        "")
                self.frame.setFrameShape(QFrame.StyledPanel)
                self.frame.setFrameShadow(QFrame.Raised)
                self.frame.setObjectName(u"frame")
                self.welcome_label = QLabel(self.main_bg_frame)
                self.welcome_label.setGeometry(QRect(140, 60, 351, 111))
                font = QFont()
                font.setFamily("DIN Condensed")
                font.setPointSize(70)
                font.setBold(True)
                font.setItalic(False)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(False)
                self.welcome_label.setFont(font)
                self.welcome_label.setToolTip("")
                self.welcome_label.setStyleSheet("background-color: transparent;")
                self.welcome_label.setAlignment(Qt.AlignCenter)
                self.welcome_label.setObjectName("welcome_label")
                self.initialzing_label = QLabel(self.main_bg_frame)
                self.initialzing_label.setGeometry(QRect(180, 150, 291, 61))
                font = QFont()
                font.setFamily("DIN Condensed")
                font.setPointSize(40)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.initialzing_label.setFont(font)
                self.initialzing_label.setStyleSheet("background-color: transparent;")
                self.initialzing_label.setObjectName("initialzing_label")
                self.wait_label = QLabel(self.main_bg_frame)
                self.wait_label.setGeometry(QRect(350, 200, 200, 16))
                self.wait_label.setStyleSheet("background-color: transparent")
                self.wait_label.setObjectName("wait_label")
                self.designedby_label = QLabel(self.main_bg_frame)
                self.designedby_label.setGeometry(QRect(110, 320, 401, 20))
                font = QFont()
                font.setFamily("Al Nile")
                self.designedby_label.setFont(font)
                self.designedby_label.setStyleSheet("background-color: transparent;")
                self.designedby_label.setAlignment(Qt.AlignBottom|QtCore.Qt.AlignHCenter)
                self.designedby_label.setObjectName("designedby_label")
                self.progressBar = QProgressBar(self.main_bg_frame)
                self.progressBar.setGeometry(QRect(180, 250, 311, 51))
                self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
                self.progressBar.setValue(24)
                self.progressBar.setObjectName("progressBar")
                SplashScreen.setCentralWidget(self.centralwidget)

                self.retranslateUi(SplashScreen)
                QMetaObject.connectSlotsByName(SplashScreen)
        def retranslateUi(self, SplashScreen):
                _translate = QtCore.QCoreApplication.translate
                SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
                self.welcome_label.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" color:#000000;\">Welcome</span></p></body></html>"))
                self.initialzing_label.setText(_translate("SplashScreen", "<strong>Initializing</strong> All-NBA App"))
                self.wait_label.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" color:#ffffff;\">Please Wait ...</span></p></body></html>"))
                self.designedby_label.setText(_translate("SplashScreen", "Designed and Created By @NickBrell"))