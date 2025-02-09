# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(591, 476)
        self.connect_pb = QPushButton(Dialog)
        self.connect_pb.setObjectName(u"connect_pb")
        self.connect_pb.setGeometry(QRect(20, 80, 75, 24))
        self.log_pte = QPlainTextEdit(Dialog)
        self.log_pte.setObjectName(u"log_pte")
        self.log_pte.setGeometry(QRect(20, 200, 551, 251))
        self.log_pte.setReadOnly(True)
        self.disconnect_pb = QPushButton(Dialog)
        self.disconnect_pb.setObjectName(u"disconnect_pb")
        self.disconnect_pb.setGeometry(QRect(100, 80, 91, 24))
        self.connection_status_lbl = QLabel(Dialog)
        self.connection_status_lbl.setObjectName(u"connection_status_lbl")
        self.connection_status_lbl.setGeometry(QRect(50, 30, 101, 16))
        self.connection_status_color_lbl = QLabel(Dialog)
        self.connection_status_color_lbl.setObjectName(u"connection_status_color_lbl")
        self.connection_status_color_lbl.setGeometry(QRect(20, 30, 16, 16))
        self.connection_status_color_lbl.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.depoth_path_le = QLineEdit(Dialog)
        self.depoth_path_le.setObjectName(u"depoth_path_le")
        self.depoth_path_le.setGeometry(QRect(330, 30, 241, 21))
        self.list_files_in_path_pb = QPushButton(Dialog)
        self.list_files_in_path_pb.setObjectName(u"list_files_in_path_pb")
        self.list_files_in_path_pb.setGeometry(QRect(330, 80, 121, 24))
        self.checkout_or_add_pb = QPushButton(Dialog)
        self.checkout_or_add_pb.setObjectName(u"checkout_or_add_pb")
        self.checkout_or_add_pb.setGeometry(QRect(460, 80, 111, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.connect_pb.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.disconnect_pb.setText(QCoreApplication.translate("Dialog", u"Disconnect", None))
        self.connection_status_lbl.setText(QCoreApplication.translate("Dialog", u"Connection Status", None))
        self.connection_status_color_lbl.setText("")
        self.depoth_path_le.setText(QCoreApplication.translate("Dialog", u"//depot/main/test_data/...", None))
        self.list_files_in_path_pb.setText(QCoreApplication.translate("Dialog", u"List Files in Path", None))
        self.checkout_or_add_pb.setText(QCoreApplication.translate("Dialog", u"Checkout or Add", None))
    # retranslateUi

