# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'footswitch_component.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

from pyfx.widgets.editable_label_widget import EditableLabelWidget
from pyfx.widgets.footswitch_widget import FootswitchWidget

class Ui_FootswitchComponent(object):
    def setupUi(self, FootswitchComponent):
        if not FootswitchComponent.objectName():
            FootswitchComponent.setObjectName(u"FootswitchComponent")
        FootswitchComponent.resize(101, 119)
        self.verticalLayout = QVBoxLayout(FootswitchComponent)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.footswitch_editbox_placeholder = QWidget(FootswitchComponent)
        self.footswitch_editbox_placeholder.setObjectName(u"footswitch_editbox_placeholder")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footswitch_editbox_placeholder.sizePolicy().hasHeightForWidth())
        self.footswitch_editbox_placeholder.setSizePolicy(sizePolicy)
        self.footswitch_editbox_placeholder.setMinimumSize(QSize(0, 22))

        self.verticalLayout.addWidget(self.footswitch_editbox_placeholder)

        self.footswitch_editbox = QLineEdit(FootswitchComponent)
        self.footswitch_editbox.setObjectName(u"footswitch_editbox")
        self.footswitch_editbox.setEnabled(False)
        sizePolicy.setHeightForWidth(self.footswitch_editbox.sizePolicy().hasHeightForWidth())
        self.footswitch_editbox.setSizePolicy(sizePolicy)
        self.footswitch_editbox.setMaximumSize(QSize(60, 16777215))
        self.footswitch_editbox.setFrame(False)
        self.footswitch_editbox.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.footswitch_editbox, 0, Qt.AlignHCenter)

        self.footswitch_widget = FootswitchWidget(FootswitchComponent)
        self.footswitch_widget.setObjectName(u"footswitch_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.footswitch_widget.sizePolicy().hasHeightForWidth())
        self.footswitch_widget.setSizePolicy(sizePolicy1)
        self.footswitch_widget.setMinimumSize(QSize(0, 0))
        self.footswitch_widget.setMaximumSize(QSize(16777215, 16777215))
        self.footswitch_widget.setCheckable(True)
        self.footswitch_widget.setAutoDefault(False)
        self.footswitch_widget.setFlat(False)

        self.verticalLayout.addWidget(self.footswitch_widget, 0, Qt.AlignHCenter)

        self.footswitch_name = EditableLabelWidget(FootswitchComponent)
        self.footswitch_name.setObjectName(u"footswitch_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.footswitch_name.setFont(font)

        self.verticalLayout.addWidget(self.footswitch_name, 0, Qt.AlignHCenter)


        self.retranslateUi(FootswitchComponent)

        self.footswitch_widget.setDefault(False)


        QMetaObject.connectSlotsByName(FootswitchComponent)
    # setupUi

    def retranslateUi(self, FootswitchComponent):
        FootswitchComponent.setWindowTitle(QCoreApplication.translate("FootswitchComponent", u"FootswitchComponent", None))
        self.footswitch_widget.setText("")
        self.footswitch_name.setText(QCoreApplication.translate("FootswitchComponent", u"Footswitch", None))
    # retranslateUi

