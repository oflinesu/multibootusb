# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multibootusb-new.ui'
#
# Created: Thu Jan 30 18:13:43 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(537, 448)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("tools/multibootusb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.create = QtGui.QPushButton(self.tab_3)
        self.create.setObjectName(_fromUtf8("create"))
        self.gridLayout.addWidget(self.create, 5, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.tab_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 2)
        self.close = QtGui.QPushButton(self.tab_3)
        self.close.setObjectName(_fromUtf8("close"))
        self.gridLayout.addWidget(self.close, 5, 2, 1, 1)
        self.listWidget = QtGui.QListWidget(self.tab_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 4, 1)
        self.browse_iso = QtGui.QPushButton(self.tab_3)
        self.browse_iso.setObjectName(_fromUtf8("browse_iso"))
        self.gridLayout.addWidget(self.browse_iso, 4, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 3)
        self.labelstep1 = QtGui.QLabel(self.tab_3)
        self.labelstep1.setObjectName(_fromUtf8("labelstep1"))
        self.gridLayout.addWidget(self.labelstep1, 0, 4, 1, 1)
        self.labelstep2 = QtGui.QLabel(self.tab_3)
        self.labelstep2.setObjectName(_fromUtf8("labelstep2"))
        self.gridLayout.addWidget(self.labelstep2, 4, 4, 1, 1)
        self.labelstep3 = QtGui.QLabel(self.tab_3)
        self.labelstep3.setObjectName(_fromUtf8("labelstep3"))
        self.gridLayout.addWidget(self.labelstep3, 5, 4, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.tab_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 5)
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.uninstall = QtGui.QPushButton(self.groupBox)
        self.uninstall.setObjectName(_fromUtf8("uninstall"))
        self.gridLayout_5.addWidget(self.uninstall, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout.addWidget(self.groupBox, 3, 2, 1, 2)
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.usb_dev = QtGui.QLabel(self.groupBox_6)
        self.usb_dev.setObjectName(_fromUtf8("usb_dev"))
        self.verticalLayout_5.addWidget(self.usb_dev)
        self.usb_label = QtGui.QLabel(self.groupBox_6)
        self.usb_label.setObjectName(_fromUtf8("usb_label"))
        self.verticalLayout_5.addWidget(self.usb_label)
        self.usb_mount = QtGui.QLabel(self.groupBox_6)
        self.usb_mount.setObjectName(_fromUtf8("usb_mount"))
        self.verticalLayout_5.addWidget(self.usb_mount)
        self.usb_size_ttl = QtGui.QLabel(self.groupBox_6)
        self.usb_size_ttl.setObjectName(_fromUtf8("usb_size_ttl"))
        self.verticalLayout_5.addWidget(self.usb_size_ttl)
        self.usb_size_avl = QtGui.QLabel(self.groupBox_6)
        self.usb_size_avl.setObjectName(_fromUtf8("usb_size_avl"))
        self.verticalLayout_5.addWidget(self.usb_size_avl)
        self.gridLayout.addWidget(self.groupBox_6, 2, 2, 1, 2)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.detect_usb = QtGui.QPushButton(self.groupBox_11)
        self.detect_usb.setObjectName(_fromUtf8("detect_usb"))
        self.horizontalLayout_8.addWidget(self.detect_usb)
        self.verticalLayout_11.addWidget(self.groupBox_11)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 2, 1, 2)
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.status = QtGui.QLabel(self.tab_3)
        self.status.setText(_fromUtf8(""))
        self.status.setObjectName(_fromUtf8("status"))
        self.gridLayout.addWidget(self.status, 6, 0, 1, 5)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.syslinux_ab = QtGui.QWidget()
        self.syslinux_ab.setObjectName(_fromUtf8("syslinux_ab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.syslinux_ab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.syslinux_ab)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.install_syslinux = QtGui.QPushButton(self.groupBox_2)
        self.install_syslinux.setObjectName(_fromUtf8("install_syslinux"))
        self.gridLayout_3.addWidget(self.install_syslinux, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.install_sys_all = QtGui.QRadioButton(self.groupBox_2)
        self.install_sys_all.setObjectName(_fromUtf8("install_sys_all"))
        self.gridLayout_3.addWidget(self.install_sys_all, 1, 0, 1, 2)
        self.install_sys_only = QtGui.QRadioButton(self.groupBox_2)
        self.install_sys_only.setObjectName(_fromUtf8("install_sys_only"))
        self.gridLayout_3.addWidget(self.install_sys_only, 0, 0, 1, 2)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.syslinux_ab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.edit_syslinux = QtGui.QPushButton(self.groupBox_3)
        self.edit_syslinux.setObjectName(_fromUtf8("edit_syslinux"))
        self.gridLayout_4.addWidget(self.edit_syslinux, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 2)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.syslinux_ab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.ram_iso_2048 = QtGui.QRadioButton(self.groupBox_5)
        self.ram_iso_2048.setObjectName(_fromUtf8("ram_iso_2048"))
        self.gridLayout_7.addWidget(self.ram_iso_2048, 4, 4, 1, 1)
        self.ram_iso_1024 = QtGui.QRadioButton(self.groupBox_5)
        self.ram_iso_1024.setObjectName(_fromUtf8("ram_iso_1024"))
        self.gridLayout_7.addWidget(self.ram_iso_1024, 4, 3, 1, 1)
        self.ram_iso_256 = QtGui.QRadioButton(self.groupBox_5)
        self.ram_iso_256.setObjectName(_fromUtf8("ram_iso_256"))
        self.gridLayout_7.addWidget(self.ram_iso_256, 4, 0, 1, 1)
        self.browse_iso_qemu = QtGui.QPushButton(self.groupBox_5)
        self.browse_iso_qemu.setObjectName(_fromUtf8("browse_iso_qemu"))
        self.gridLayout_7.addWidget(self.browse_iso_qemu, 2, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 5)
        self.ram_iso_512 = QtGui.QRadioButton(self.groupBox_5)
        self.ram_iso_512.setObjectName(_fromUtf8("ram_iso_512"))
        self.gridLayout_7.addWidget(self.ram_iso_512, 4, 1, 1, 1)
        self.boot_iso_qemu = QtGui.QPushButton(self.groupBox_5)
        self.boot_iso_qemu.setObjectName(_fromUtf8("boot_iso_qemu"))
        self.gridLayout_7.addWidget(self.boot_iso_qemu, 6, 4, 1, 1)
        self.ram_iso_768 = QtGui.QRadioButton(self.groupBox_5)
        self.ram_iso_768.setObjectName(_fromUtf8("ram_iso_768"))
        self.gridLayout_7.addWidget(self.ram_iso_768, 4, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_7.addWidget(self.lineEdit_2, 2, 0, 1, 4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_7.addWidget(self.label_3, 6, 0, 1, 4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.ram_usb_768 = QtGui.QRadioButton(self.groupBox_4)
        self.ram_usb_768.setObjectName(_fromUtf8("ram_usb_768"))
        self.gridLayout_8.addWidget(self.ram_usb_768, 2, 2, 1, 1)
        self.ram_usb_256 = QtGui.QRadioButton(self.groupBox_4)
        self.ram_usb_256.setObjectName(_fromUtf8("ram_usb_256"))
        self.gridLayout_8.addWidget(self.ram_usb_256, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 5)
        self.ram_usb_1024 = QtGui.QRadioButton(self.groupBox_4)
        self.ram_usb_1024.setObjectName(_fromUtf8("ram_usb_1024"))
        self.gridLayout_8.addWidget(self.ram_usb_1024, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_8.addWidget(self.label_4, 4, 0, 1, 4)
        self.ram_usb_512 = QtGui.QRadioButton(self.groupBox_4)
        self.ram_usb_512.setObjectName(_fromUtf8("ram_usb_512"))
        self.gridLayout_8.addWidget(self.ram_usb_512, 2, 1, 1, 1)
        self.boot_usb_qemu = QtGui.QPushButton(self.groupBox_4)
        self.boot_usb_qemu.setObjectName(_fromUtf8("boot_usb_qemu"))
        self.gridLayout_8.addWidget(self.boot_usb_qemu, 4, 4, 1, 1)
        self.ram_usb_2048 = QtGui.QRadioButton(self.groupBox_4)
        self.ram_usb_2048.setObjectName(_fromUtf8("ram_usb_2048"))
        self.gridLayout_8.addWidget(self.ram_usb_2048, 2, 4, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem8, 5, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.settings = QtGui.QWidget()
        self.settings.setObjectName(_fromUtf8("settings"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.settings)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox_7 = QtGui.QGroupBox(self.settings)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_8.addWidget(self.checkBox)
        self.label_8 = QtGui.QLabel(self.groupBox_9)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_8.addWidget(self.label_8)
        self.gridLayout_11.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_10)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_9.addWidget(self.checkBox_2)
        self.label_9 = QtGui.QLabel(self.groupBox_10)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        self.gridLayout_11.addWidget(self.groupBox_10, 0, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_11)
        self.gridLayout_9.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.groupBox_8 = QtGui.QGroupBox(self.settings)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_8)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_12.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_8)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_12.addWidget(self.label_10, 1, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_12)
        self.gridLayout_9.addWidget(self.groupBox_8, 2, 0, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.settings, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem10, 1, 0, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem11, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_10.addWidget(self.label_5, 1, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem12, 1, 2, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_10)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "multibootusb", None))
        self.create.setText(_translate("Dialog", "Create", None))
        self.close.setText(_translate("Dialog", "Close", None))
        self.browse_iso.setText(_translate("Dialog", "Browse ISO", None))
        self.labelstep1.setText(_translate("Dialog",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Step 1</span></p></body></html>",
                                           None))
        self.labelstep2.setText(_translate("Dialog",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Step 2</span></p></body></html>",
                                           None))
        self.labelstep3.setText(_translate("Dialog",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Step 3</span></p></body></html>",
                                           None))
        self.groupBox.setTitle(_translate("Dialog", "Uninstall (Optional)", None))
        self.uninstall.setText(_translate("Dialog", "Uninstall Distro", None))
        self.groupBox_6.setTitle(_translate("Dialog", "USB Details", None))
        self.usb_dev.setText(_translate("Dialog", "Drive ::", None))
        self.usb_label.setText(_translate("Dialog", "Label ::", None))
        self.usb_mount.setText(_translate("Dialog", "Mount::", None))
        self.usb_size_ttl.setText(_translate("Dialog", "Size Total ::", None))
        self.usb_size_avl.setText(_translate("Dialog", "Size Avail ::", None))
        self.groupBox_11.setTitle(_translate("Dialog", "Detect USB", None))
        self.detect_usb.setText(_translate("Dialog", "Referesh USB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "MultiBootUSB", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Install Syslinux", None))
        self.install_syslinux.setText(_translate("Dialog", "Install", None))
        self.install_sys_all.setText(_translate("Dialog", "Install syslinux and copy all required files.", None))
        self.install_sys_only.setText(
            _translate("Dialog", "Install only syslinux (existing configurations will not be altred).", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Edit syslinux.cfg", None))
        self.edit_syslinux.setText(_translate("Dialog", "Edit", None))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"justify\">Using this option user can edit syslinux.cfg file directly. It directly uses </p><p align=\"justify\">default editor of host system. Be careful while editing syslinux.cfg file.</p></body></html>",
                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.syslinux_ab), _translate("Dialog", "Syslinux", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Boot ISO", None))
        self.ram_iso_2048.setText(_translate("Dialog", "2048 MB", None))
        self.ram_iso_1024.setText(_translate("Dialog", "1024 MB", None))
        self.ram_iso_256.setText(_translate("Dialog", "256 MB", None))
        self.browse_iso_qemu.setText(_translate("Dialog", "Browse ISO", None))
        self.label_7.setText(
            _translate("Dialog", "<html><head/><body><p>Best way to check downloaded iso. </p></body></html>", None))
        self.ram_iso_512.setText(_translate("Dialog", "512 MB", None))
        self.boot_iso_qemu.setText(_translate("Dialog", "Boot ISO", None))
        self.ram_iso_768.setText(_translate("Dialog", "768 MB", None))
        self.label_3.setText(_translate("Dialog", "Choose desired RAM and click on Boot ISO button.", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Boot USB", None))
        self.ram_usb_768.setText(_translate("Dialog", "768 MB", None))
        self.ram_usb_256.setText(_translate("Dialog", "256 MB", None))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"justify\">Use this option if you want to check USB installation.</p></body></html>",
                                        None))
        self.ram_usb_1024.setText(_translate("Dialog", "1024 MB", None))
        self.label_4.setText(_translate("Dialog", "Choose desired RAM and click on Boot USB button.", None))
        self.ram_usb_512.setText(_translate("Dialog", "512 MB", None))
        self.boot_usb_qemu.setText(_translate("Dialog", "Boot USB", None))
        self.ram_usb_2048.setText(_translate("Dialog", "2048 MB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "QEMU", None))
        self.groupBox_7.setTitle(_translate("Dialog", "Persistance", None))
        self.groupBox_9.setTitle(_translate("Dialog", "Ubuntu", None))
        self.checkBox.setText(_translate("Dialog", "Enable persistance", None))
        self.label_8.setText(_translate("Dialog",
                                        "<html><head/><body><p>Enable if you would like </p><p>to have persistancefor </p><p>ubuntu and its derivatives.</p></body></html>",
                                        None))
        self.groupBox_10.setTitle(_translate("Dialog", "Debian", None))
        self.checkBox_2.setText(_translate("Dialog", "Enable persistance", None))
        self.label_9.setText(_translate("Dialog",
                                        "<html><head/><body><p>Enable if you would like </p><p>to have persistancefor </p><p>debian and its derivatives.</p></body></html>",
                                        None))
        self.groupBox_8.setTitle(_translate("Dialog", "Update", None))
        self.checkBox_3.setText(_translate("Dialog", "Check update", None))
        self.label_10.setText(_translate("Dialog",
                                         "<html><head/><body><p>Enable this option if you would like to recieve update information </p><p>right in to your desktop.</p></body></html>",
                                         None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("Dialog", "Settings", None))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\">An advanced bootable usb creator with option to install/uninstall </p><p align=\"center\">multiple distros. This software is written in python and pyqt. </p><p align=\"center\">Copyright 2010-2014 Sundar</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Author(s)</span>: Sundar, Ian Bruce</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Licence:</span> GPL version 2 or later</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Home page</span>: <a href=\" http://multibootusb.org\"><span style=\" text-decoration: underline; color:#0000ff;\">http://multibootusb.org</span></a></p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Help/Email:</span> feedback.multibootusb@gmail.com</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Source Code:</span><a href=\"https://github.com/mbusb/multibootusb\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/mbusb/multibootusb</span></a></p><p><br/></p></body></html>",
                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "About", None))

