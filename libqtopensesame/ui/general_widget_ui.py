# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/general_widget.ui'
#
# Created: Sat Jul 14 15:26:41 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_general_widget(object):
    def setupUi(self, general_widget):
        general_widget.setObjectName(_fromUtf8("general_widget"))
        general_widget.resize(829, 852)
        self.gridLayout_5 = QtGui.QGridLayout(general_widget)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.spacer = QtGui.QWidget(general_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer.sizePolicy().hasHeightForWidth())
        self.spacer.setSizePolicy(sizePolicy)
        self.spacer.setObjectName(_fromUtf8("spacer"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.spacer)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_3 = QtGui.QWidget(self.spacer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_5 = QtGui.QWidget(self.widget_3)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget_4 = QtGui.QWidget(self.widget_5)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_facebook = QtGui.QLabel(self.widget_4)
        self.label_facebook.setObjectName(_fromUtf8("label_facebook"))
        self.horizontalLayout_2.addWidget(self.label_facebook)
        self.label_twitter = QtGui.QLabel(self.widget_4)
        self.label_twitter.setObjectName(_fromUtf8("label_twitter"))
        self.horizontalLayout_2.addWidget(self.label_twitter)
        self.label_website = QtGui.QLabel(self.widget_4)
        self.label_website.setObjectName(_fromUtf8("label_website"))
        self.horizontalLayout_2.addWidget(self.label_website)
        self.label_cogscinl = QtGui.QLabel(self.widget_4)
        self.label_cogscinl.setObjectName(_fromUtf8("label_cogscinl"))
        self.horizontalLayout_2.addWidget(self.label_cogscinl)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_opensesame = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_opensesame.sizePolicy().hasHeightForWidth())
        self.label_opensesame.setSizePolicy(sizePolicy)
        self.label_opensesame.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_opensesame.setObjectName(_fromUtf8("label_opensesame"))
        self.horizontalLayout.addWidget(self.label_opensesame)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.gridLayout_5.addWidget(self.spacer, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(general_widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.widget = QtGui.QWidget(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(20, 20))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setMargin(0)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.frame_7 = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setMargin(4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.spinbox_width = QtGui.QSpinBox(self.frame_7)
        self.spinbox_width.setMinimum(1)
        self.spinbox_width.setMaximum(10000)
        self.spinbox_width.setObjectName(_fromUtf8("spinbox_width"))
        self.horizontalLayout_3.addWidget(self.spinbox_width)
        self.label_6 = QtGui.QLabel(self.frame_7)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.spinbox_height = QtGui.QSpinBox(self.frame_7)
        self.spinbox_height.setMinimum(1)
        self.spinbox_height.setMaximum(10000)
        self.spinbox_height.setObjectName(_fromUtf8("spinbox_height"))
        self.horizontalLayout_3.addWidget(self.spinbox_height)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.frame_7)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.frame_8 = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_6.setMargin(4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.edit_foreground = color_edit(self.frame_8)
        self.edit_foreground.setObjectName(_fromUtf8("edit_foreground"))
        self.gridLayout_6.addWidget(self.edit_foreground, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_8)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_8)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)
        self.edit_background = color_edit(self.frame_8)
        self.edit_background.setObjectName(_fromUtf8("edit_background"))
        self.gridLayout_6.addWidget(self.edit_background, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 2)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.frame_8)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.frame_2 = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setMargin(4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.widget_font = font_widget(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_font.sizePolicy().hasHeightForWidth())
        self.widget_font.setSizePolicy(sizePolicy)
        self.widget_font.setMinimumSize(QtCore.QSize(10, 10))
        self.widget_font.setObjectName(_fromUtf8("widget_font"))
        self.horizontalLayout_4.addWidget(self.widget_font)
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.frame_2)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_11)
        self.combobox_backend = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_backend.sizePolicy().hasHeightForWidth())
        self.combobox_backend.setSizePolicy(sizePolicy)
        self.combobox_backend.setObjectName(_fromUtf8("combobox_backend"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.combobox_backend)
        self.frame_3 = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.button_backend_settings = QtGui.QCommandLinkButton(self.frame_3)
        self.button_backend_settings.setObjectName(_fromUtf8("button_backend_settings"))
        self.horizontalLayout_6.addWidget(self.button_backend_settings)
        self.button_script_editor = QtGui.QCommandLinkButton(self.frame_3)
        self.button_script_editor.setObjectName(_fromUtf8("button_script_editor"))
        self.horizontalLayout_6.addWidget(self.button_script_editor)
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.frame_3)
        self.horizontalLayout_5.addWidget(self.widget)
        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)

        self.retranslateUi(general_widget)
        QtCore.QMetaObject.connectSlotsByName(general_widget)

    def retranslateUi(self, general_widget):
        general_widget.setWindowTitle(QtGui.QApplication.translate("general_widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_facebook.setToolTip(QtGui.QApplication.translate("general_widget", "Visit Facebook page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_facebook.setText(QtGui.QApplication.translate("general_widget", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.label_twitter.setToolTip(QtGui.QApplication.translate("general_widget", "Visit Twitter page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_twitter.setText(QtGui.QApplication.translate("general_widget", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.label_website.setToolTip(QtGui.QApplication.translate("general_widget", "Visit cogsci.nl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_website.setText(QtGui.QApplication.translate("general_widget", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cogscinl.setText(QtGui.QApplication.translate("general_widget", "<html><head/><body><p>COGSCIdotNL // cognitive science and more</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_opensesame.setText(QtGui.QApplication.translate("general_widget", "OpenSesame [version] [codename]\n"
"Copyright Sebastiaan Mathôt (2010-2012)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("general_widget", "<h3>Back-end</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("general_widget", "<h3>Resolution</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_width.setToolTip(QtGui.QApplication.translate("general_widget", "The display resolution (width) in pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_width.setSuffix(QtGui.QApplication.translate("general_widget", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("general_widget", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_height.setToolTip(QtGui.QApplication.translate("general_widget", "The display resolution (height) in pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_height.setSuffix(QtGui.QApplication.translate("general_widget", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("general_widget", "<h3>Colors</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("general_widget", "Foreground", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("general_widget", "Background", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("general_widget", "<small><i>Examples: \'white\', \'#FFFFFF\'</i></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("general_widget", "<h3>Font</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("general_widget", "<h3>Advanced</h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_backend_settings.setText(QtGui.QApplication.translate("general_widget", "Back-end settings", None, QtGui.QApplication.UnicodeUTF8))
        self.button_script_editor.setText(QtGui.QApplication.translate("general_widget", "Script editor", None, QtGui.QApplication.UnicodeUTF8))

from libqtopensesame.widgets.font_widget import font_widget
from libqtopensesame.widgets.color_edit import color_edit
