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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1091, 731)
        self.connect_pb = QPushButton(Dialog)
        self.connect_pb.setObjectName(u"connect_pb")
        self.connect_pb.setGeometry(QRect(20, 80, 75, 24))
        self.log_pte = QPlainTextEdit(Dialog)
        self.log_pte.setObjectName(u"log_pte")
        self.log_pte.setGeometry(QRect(10, 330, 1071, 391))
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
        self.depoth_path_le.setGeometry(QRect(620, 30, 451, 21))
        self.list_files_in_path_pb = QPushButton(Dialog)
        self.list_files_in_path_pb.setObjectName(u"list_files_in_path_pb")
        self.list_files_in_path_pb.setGeometry(QRect(620, 80, 151, 24))
        self.checkout_or_add_pb = QPushButton(Dialog)
        self.checkout_or_add_pb.setObjectName(u"checkout_or_add_pb")
        self.checkout_or_add_pb.setGeometry(QRect(960, 110, 111, 24))
        self.move_to_new_cl_cb = QCheckBox(Dialog)
        self.move_to_new_cl_cb.setObjectName(u"move_to_new_cl_cb")
        self.move_to_new_cl_cb.setGeometry(QRect(960, 80, 111, 20))
        self.delete_all_empty_cls_pb = QPushButton(Dialog)
        self.delete_all_empty_cls_pb.setObjectName(u"delete_all_empty_cls_pb")
        self.delete_all_empty_cls_pb.setGeometry(QRect(620, 120, 151, 24))
        self.changelist_cmbx = QComboBox(Dialog)
        self.changelist_cmbx.setObjectName(u"changelist_cmbx")
        self.changelist_cmbx.setGeometry(QRect(20, 120, 411, 21))
        self.refresh_cls_pb = QPushButton(Dialog)
        self.refresh_cls_pb.setObjectName(u"refresh_cls_pb")
        self.refresh_cls_pb.setGeometry(QRect(440, 120, 75, 24))
        self.revert_files_from_cl_pb = QPushButton(Dialog)
        self.revert_files_from_cl_pb.setObjectName(u"revert_files_from_cl_pb")
        self.revert_files_from_cl_pb.setGeometry(QRect(620, 200, 151, 24))
        self.revert_only_unchanged_cb = QCheckBox(Dialog)
        self.revert_only_unchanged_cb.setObjectName(u"revert_only_unchanged_cb")
        self.revert_only_unchanged_cb.setGeometry(QRect(620, 170, 151, 20))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(800, 190, 131, 121))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shelve_files_pb = QPushButton(self.groupBox)
        self.shelve_files_pb.setObjectName(u"shelve_files_pb")
        self.shelve_files_pb.setGeometry(QRect(20, 20, 91, 24))
        self.unshelve_files_pb = QPushButton(self.groupBox)
        self.unshelve_files_pb.setObjectName(u"unshelve_files_pb")
        self.unshelve_files_pb.setGeometry(QRect(20, 50, 91, 24))
        self.delete_shelved_pb = QPushButton(self.groupBox)
        self.delete_shelved_pb.setObjectName(u"delete_shelved_pb")
        self.delete_shelved_pb.setGeometry(QRect(20, 80, 91, 24))
        self.sync_to_latest_pb = QPushButton(Dialog)
        self.sync_to_latest_pb.setObjectName(u"sync_to_latest_pb")
        self.sync_to_latest_pb.setGeometry(QRect(960, 150, 111, 24))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(950, 190, 121, 81))
        self.conflict_accept_local_rb = QRadioButton(self.groupBox_2)
        self.conflict_accept_local_rb.setObjectName(u"conflict_accept_local_rb")
        self.conflict_accept_local_rb.setGeometry(QRect(10, 20, 101, 20))
        self.conflict_accept_local_rb.setChecked(True)
        self.conflict_accept_depot_rb = QRadioButton(self.groupBox_2)
        self.conflict_accept_depot_rb.setObjectName(u"conflict_accept_depot_rb")
        self.conflict_accept_depot_rb.setGeometry(QRect(10, 50, 101, 20))
        self.submit_pb = QPushButton(Dialog)
        self.submit_pb.setObjectName(u"submit_pb")
        self.submit_pb.setGeometry(QRect(960, 290, 111, 24))
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(799, 70, 131, 91))
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.start_monitor_pb = QPushButton(self.groupBox_3)
        self.start_monitor_pb.setObjectName(u"start_monitor_pb")
        self.start_monitor_pb.setGeometry(QRect(20, 20, 91, 24))
        self.stop_monitor_pb = QPushButton(self.groupBox_3)
        self.stop_monitor_pb.setObjectName(u"stop_monitor_pb")
        self.stop_monitor_pb.setGeometry(QRect(20, 50, 91, 24))

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
        self.move_to_new_cl_cb.setText(QCoreApplication.translate("Dialog", u"Move to new CL", None))
        self.delete_all_empty_cls_pb.setText(QCoreApplication.translate("Dialog", u"Delete all empty CLs", None))
        self.refresh_cls_pb.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.revert_files_from_cl_pb.setText(QCoreApplication.translate("Dialog", u"Revert files from CL", None))
        self.revert_only_unchanged_cb.setText(QCoreApplication.translate("Dialog", u"Revert only unchanged", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Shelves", None))
        self.shelve_files_pb.setText(QCoreApplication.translate("Dialog", u"Shelve files", None))
        self.unshelve_files_pb.setText(QCoreApplication.translate("Dialog", u"Unshelve files", None))
        self.delete_shelved_pb.setText(QCoreApplication.translate("Dialog", u"Delete shelved", None))
        self.sync_to_latest_pb.setText(QCoreApplication.translate("Dialog", u"Sync to latest", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Conflicts Resolution", None))
        self.conflict_accept_local_rb.setText(QCoreApplication.translate("Dialog", u"Accept Local", None))
        self.conflict_accept_depot_rb.setText(QCoreApplication.translate("Dialog", u"Accept Depot", None))
        self.submit_pb.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Monitoring", None))
        self.start_monitor_pb.setText(QCoreApplication.translate("Dialog", u"Start monitor", None))
        self.stop_monitor_pb.setText(QCoreApplication.translate("Dialog", u"Stop monitor", None))
    # retranslateUi

