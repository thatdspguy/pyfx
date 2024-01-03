# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audio_preferences_widget.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_AudioPreferencesWidget(object):
    def setupUi(self, AudioPreferencesWidget):
        if not AudioPreferencesWidget.objectName():
            AudioPreferencesWidget.setObjectName(u"AudioPreferencesWidget")
        AudioPreferencesWidget.resize(500, 504)
        AudioPreferencesWidget.setMinimumSize(QSize(500, 0))
        self.main_layout = QVBoxLayout(AudioPreferencesWidget)
        self.main_layout.setSpacing(8)
        self.main_layout.setObjectName(u"main_layout")
        self.audio_device_groupbox = QGroupBox(AudioPreferencesWidget)
        self.audio_device_groupbox.setObjectName(u"audio_device_groupbox")
        self.audio_device_groupbox_layout = QFormLayout(self.audio_device_groupbox)
        self.audio_device_groupbox_layout.setObjectName(u"audio_device_groupbox_layout")
        self.audio_device_groupbox_layout.setVerticalSpacing(8)
        self.driver_type_label = QLabel(self.audio_device_groupbox)
        self.driver_type_label.setObjectName(u"driver_type_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driver_type_label.sizePolicy().hasHeightForWidth())
        self.driver_type_label.setSizePolicy(sizePolicy)
        self.driver_type_label.setMinimumSize(QSize(130, 0))
        self.driver_type_label.setMaximumSize(QSize(130, 16777215))

        self.audio_device_groupbox_layout.setWidget(0, QFormLayout.LabelRole, self.driver_type_label)

        self.driver_type_combobox = QComboBox(self.audio_device_groupbox)
        self.driver_type_combobox.setObjectName(u"driver_type_combobox")

        self.audio_device_groupbox_layout.setWidget(0, QFormLayout.FieldRole, self.driver_type_combobox)

        self.audio_input_device_label = QLabel(self.audio_device_groupbox)
        self.audio_input_device_label.setObjectName(u"audio_input_device_label")
        sizePolicy.setHeightForWidth(self.audio_input_device_label.sizePolicy().hasHeightForWidth())
        self.audio_input_device_label.setSizePolicy(sizePolicy)
        self.audio_input_device_label.setMinimumSize(QSize(130, 0))
        self.audio_input_device_label.setMaximumSize(QSize(130, 16777215))

        self.audio_device_groupbox_layout.setWidget(1, QFormLayout.LabelRole, self.audio_input_device_label)

        self.audio_input_device_combobox = QComboBox(self.audio_device_groupbox)
        self.audio_input_device_combobox.setObjectName(u"audio_input_device_combobox")

        self.audio_device_groupbox_layout.setWidget(1, QFormLayout.FieldRole, self.audio_input_device_combobox)

        self.audio_output_device_label = QLabel(self.audio_device_groupbox)
        self.audio_output_device_label.setObjectName(u"audio_output_device_label")
        sizePolicy.setHeightForWidth(self.audio_output_device_label.sizePolicy().hasHeightForWidth())
        self.audio_output_device_label.setSizePolicy(sizePolicy)
        self.audio_output_device_label.setMinimumSize(QSize(130, 0))
        self.audio_output_device_label.setMaximumSize(QSize(130, 16777215))

        self.audio_device_groupbox_layout.setWidget(2, QFormLayout.LabelRole, self.audio_output_device_label)

        self.audio_output_device_combobox = QComboBox(self.audio_device_groupbox)
        self.audio_output_device_combobox.setObjectName(u"audio_output_device_combobox")

        self.audio_device_groupbox_layout.setWidget(2, QFormLayout.FieldRole, self.audio_output_device_combobox)

        self.channel_configuration_label = QLabel(self.audio_device_groupbox)
        self.channel_configuration_label.setObjectName(u"channel_configuration_label")
        sizePolicy.setHeightForWidth(self.channel_configuration_label.sizePolicy().hasHeightForWidth())
        self.channel_configuration_label.setSizePolicy(sizePolicy)
        self.channel_configuration_label.setMinimumSize(QSize(130, 0))
        self.channel_configuration_label.setMaximumSize(QSize(130, 16777215))

        self.audio_device_groupbox_layout.setWidget(3, QFormLayout.LabelRole, self.channel_configuration_label)

        self.channel_configuration_button_layout = QHBoxLayout()
        self.channel_configuration_button_layout.setSpacing(10)
        self.channel_configuration_button_layout.setObjectName(u"channel_configuration_button_layout")
        self.channel_configuration_button_layout.setContentsMargins(0, -1, 0, -1)
        self.input_config_button = QPushButton(self.audio_device_groupbox)
        self.input_config_button.setObjectName(u"input_config_button")

        self.channel_configuration_button_layout.addWidget(self.input_config_button)

        self.output_config_button = QPushButton(self.audio_device_groupbox)
        self.output_config_button.setObjectName(u"output_config_button")

        self.channel_configuration_button_layout.addWidget(self.output_config_button)


        self.audio_device_groupbox_layout.setLayout(3, QFormLayout.FieldRole, self.channel_configuration_button_layout)

        self.audio_folder_label = QLabel(self.audio_device_groupbox)
        self.audio_folder_label.setObjectName(u"audio_folder_label")
        sizePolicy.setHeightForWidth(self.audio_folder_label.sizePolicy().hasHeightForWidth())
        self.audio_folder_label.setSizePolicy(sizePolicy)
        self.audio_folder_label.setMinimumSize(QSize(130, 0))
        self.audio_folder_label.setMaximumSize(QSize(130, 16777215))

        self.audio_device_groupbox_layout.setWidget(4, QFormLayout.LabelRole, self.audio_folder_label)

        self.audio_folder_layout = QHBoxLayout()
        self.audio_folder_layout.setSpacing(10)
        self.audio_folder_layout.setObjectName(u"audio_folder_layout")
        self.audio_folder_editbox = QLineEdit(self.audio_device_groupbox)
        self.audio_folder_editbox.setObjectName(u"audio_folder_editbox")

        self.audio_folder_layout.addWidget(self.audio_folder_editbox)

        self.audio_folder_browse_button = QPushButton(self.audio_device_groupbox)
        self.audio_folder_browse_button.setObjectName(u"audio_folder_browse_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.audio_folder_browse_button.sizePolicy().hasHeightForWidth())
        self.audio_folder_browse_button.setSizePolicy(sizePolicy1)
        self.audio_folder_browse_button.setMaximumSize(QSize(60, 16777215))

        self.audio_folder_layout.addWidget(self.audio_folder_browse_button)


        self.audio_device_groupbox_layout.setLayout(4, QFormLayout.FieldRole, self.audio_folder_layout)


        self.main_layout.addWidget(self.audio_device_groupbox)

        self.sample_rate_groupbox = QGroupBox(AudioPreferencesWidget)
        self.sample_rate_groupbox.setObjectName(u"sample_rate_groupbox")
        self.sample_rate_groupbox_layout = QFormLayout(self.sample_rate_groupbox)
        self.sample_rate_groupbox_layout.setObjectName(u"sample_rate_groupbox_layout")
        self.sample_rate_groupbox_layout.setVerticalSpacing(8)
        self.sample_rate_label = QLabel(self.sample_rate_groupbox)
        self.sample_rate_label.setObjectName(u"sample_rate_label")
        sizePolicy.setHeightForWidth(self.sample_rate_label.sizePolicy().hasHeightForWidth())
        self.sample_rate_label.setSizePolicy(sizePolicy)
        self.sample_rate_label.setMinimumSize(QSize(130, 0))
        self.sample_rate_label.setMaximumSize(QSize(200, 16777215))

        self.sample_rate_groupbox_layout.setWidget(0, QFormLayout.LabelRole, self.sample_rate_label)

        self.sample_rate_combobox = QComboBox(self.sample_rate_groupbox)
        self.sample_rate_combobox.setObjectName(u"sample_rate_combobox")

        self.sample_rate_groupbox_layout.setWidget(0, QFormLayout.FieldRole, self.sample_rate_combobox)


        self.main_layout.addWidget(self.sample_rate_groupbox)

        self.latency_group_box = QGroupBox(AudioPreferencesWidget)
        self.latency_group_box.setObjectName(u"latency_group_box")
        self.latency_groupbox_layout = QFormLayout(self.latency_group_box)
        self.latency_groupbox_layout.setObjectName(u"latency_groupbox_layout")
        self.latency_groupbox_layout.setVerticalSpacing(8)
        self.buffer_size_label = QLabel(self.latency_group_box)
        self.buffer_size_label.setObjectName(u"buffer_size_label")
        sizePolicy.setHeightForWidth(self.buffer_size_label.sizePolicy().hasHeightForWidth())
        self.buffer_size_label.setSizePolicy(sizePolicy)
        self.buffer_size_label.setMinimumSize(QSize(130, 0))
        self.buffer_size_label.setMaximumSize(QSize(130, 16777215))

        self.latency_groupbox_layout.setWidget(0, QFormLayout.LabelRole, self.buffer_size_label)

        self.buffer_size_combobox = QComboBox(self.latency_group_box)
        self.buffer_size_combobox.setObjectName(u"buffer_size_combobox")

        self.latency_groupbox_layout.setWidget(0, QFormLayout.FieldRole, self.buffer_size_combobox)


        self.main_layout.addWidget(self.latency_group_box)

        self.test_groupbox = QGroupBox(AudioPreferencesWidget)
        self.test_groupbox.setObjectName(u"test_groupbox")
        self.test_groupbox_layout = QFormLayout(self.test_groupbox)
        self.test_groupbox_layout.setObjectName(u"test_groupbox_layout")
        self.test_groupbox_layout.setVerticalSpacing(8)
        self.test_tone_label = QLabel(self.test_groupbox)
        self.test_tone_label.setObjectName(u"test_tone_label")
        sizePolicy.setHeightForWidth(self.test_tone_label.sizePolicy().hasHeightForWidth())
        self.test_tone_label.setSizePolicy(sizePolicy)
        self.test_tone_label.setMinimumSize(QSize(130, 0))
        self.test_tone_label.setMaximumSize(QSize(130, 16777215))

        self.test_groupbox_layout.setWidget(0, QFormLayout.LabelRole, self.test_tone_label)

        self.test_tone_button = QPushButton(self.test_groupbox)
        self.test_tone_button.setObjectName(u"test_tone_button")
        self.test_tone_button.setCheckable(True)

        self.test_groupbox_layout.setWidget(0, QFormLayout.FieldRole, self.test_tone_button)

        self.tone_volume_label = QLabel(self.test_groupbox)
        self.tone_volume_label.setObjectName(u"tone_volume_label")
        sizePolicy.setHeightForWidth(self.tone_volume_label.sizePolicy().hasHeightForWidth())
        self.tone_volume_label.setSizePolicy(sizePolicy)
        self.tone_volume_label.setMinimumSize(QSize(130, 0))
        self.tone_volume_label.setMaximumSize(QSize(130, 16777215))

        self.test_groupbox_layout.setWidget(1, QFormLayout.LabelRole, self.tone_volume_label)

        self.tone_volume_spinbox = QSpinBox(self.test_groupbox)
        self.tone_volume_spinbox.setObjectName(u"tone_volume_spinbox")
        self.tone_volume_spinbox.setMinimum(-80)
        self.tone_volume_spinbox.setMaximum(0)

        self.test_groupbox_layout.setWidget(1, QFormLayout.FieldRole, self.tone_volume_spinbox)

        self.tone_frequency_label = QLabel(self.test_groupbox)
        self.tone_frequency_label.setObjectName(u"tone_frequency_label")
        sizePolicy.setHeightForWidth(self.tone_frequency_label.sizePolicy().hasHeightForWidth())
        self.tone_frequency_label.setSizePolicy(sizePolicy)
        self.tone_frequency_label.setMinimumSize(QSize(130, 0))
        self.tone_frequency_label.setMaximumSize(QSize(130, 16777215))

        self.test_groupbox_layout.setWidget(2, QFormLayout.LabelRole, self.tone_frequency_label)

        self.tone_frequency_spinbox = QSpinBox(self.test_groupbox)
        self.tone_frequency_spinbox.setObjectName(u"tone_frequency_spinbox")
        self.tone_frequency_spinbox.setMinimum(1)
        self.tone_frequency_spinbox.setMaximum(48000)
        self.tone_frequency_spinbox.setSingleStep(100)
        self.tone_frequency_spinbox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.tone_frequency_spinbox.setValue(440)

        self.test_groupbox_layout.setWidget(2, QFormLayout.FieldRole, self.tone_frequency_spinbox)

        self.cpu_usage_simulator_label = QLabel(self.test_groupbox)
        self.cpu_usage_simulator_label.setObjectName(u"cpu_usage_simulator_label")
        sizePolicy.setHeightForWidth(self.cpu_usage_simulator_label.sizePolicy().hasHeightForWidth())
        self.cpu_usage_simulator_label.setSizePolicy(sizePolicy)
        self.cpu_usage_simulator_label.setMinimumSize(QSize(130, 0))
        self.cpu_usage_simulator_label.setMaximumSize(QSize(130, 16777215))

        self.test_groupbox_layout.setWidget(3, QFormLayout.LabelRole, self.cpu_usage_simulator_label)

        self.simulated_cpu_usage_slider_layout = QHBoxLayout()
        self.simulated_cpu_usage_slider_layout.setSpacing(10)
        self.simulated_cpu_usage_slider_layout.setObjectName(u"simulated_cpu_usage_slider_layout")
        self.simulated_cpu_usage_slider = QSlider(self.test_groupbox)
        self.simulated_cpu_usage_slider.setObjectName(u"simulated_cpu_usage_slider")
        self.simulated_cpu_usage_slider.setMaximum(100)
        self.simulated_cpu_usage_slider.setSliderPosition(0)
        self.simulated_cpu_usage_slider.setOrientation(Qt.Horizontal)

        self.simulated_cpu_usage_slider_layout.addWidget(self.simulated_cpu_usage_slider)

        self.simulated_cpu_usage_editbox = QLineEdit(self.test_groupbox)
        self.simulated_cpu_usage_editbox.setObjectName(u"simulated_cpu_usage_editbox")
        self.simulated_cpu_usage_editbox.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.simulated_cpu_usage_editbox.sizePolicy().hasHeightForWidth())
        self.simulated_cpu_usage_editbox.setSizePolicy(sizePolicy1)
        self.simulated_cpu_usage_editbox.setMaximumSize(QSize(35, 16777215))
        self.simulated_cpu_usage_editbox.setFrame(False)

        self.simulated_cpu_usage_slider_layout.addWidget(self.simulated_cpu_usage_editbox)


        self.test_groupbox_layout.setLayout(3, QFormLayout.FieldRole, self.simulated_cpu_usage_slider_layout)


        self.main_layout.addWidget(self.test_groupbox)

        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.main_layout.addItem(self.vertical_spacer)


        self.retranslateUi(AudioPreferencesWidget)
        self.driver_type_combobox.currentTextChanged.connect(AudioPreferencesWidget.driver_type_changed)
        self.audio_input_device_combobox.currentTextChanged.connect(AudioPreferencesWidget.audio_input_device_changed)
        self.audio_output_device_combobox.currentTextChanged.connect(AudioPreferencesWidget.audio_output_device_changed)
        self.sample_rate_combobox.currentTextChanged.connect(AudioPreferencesWidget.sample_rate_changed)
        self.test_tone_button.toggled.connect(AudioPreferencesWidget.test_tone_button_toggled)
        self.tone_volume_spinbox.valueChanged.connect(AudioPreferencesWidget.test_tone_volume_changed)
        self.tone_frequency_spinbox.valueChanged.connect(AudioPreferencesWidget.test_tone_frequency_changed)
        self.simulated_cpu_usage_slider.valueChanged.connect(AudioPreferencesWidget.simulated_cpu_usage_changed)
        self.audio_folder_browse_button.pressed.connect(AudioPreferencesWidget.audio_folder_browse_button_pressed)
        self.audio_folder_editbox.editingFinished.connect(AudioPreferencesWidget.audio_folder_editing_finished)
        self.input_config_button.pressed.connect(AudioPreferencesWidget.input_config_button_pressed)
        self.output_config_button.pressed.connect(AudioPreferencesWidget.output_config_button_pressed)
        self.buffer_size_combobox.currentIndexChanged.connect(AudioPreferencesWidget.buffer_size_changed)

        self.sample_rate_combobox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(AudioPreferencesWidget)
    # setupUi

    def retranslateUi(self, AudioPreferencesWidget):
        AudioPreferencesWidget.setWindowTitle(QCoreApplication.translate("AudioPreferencesWidget", u"Audio Preferences", None))
        self.audio_device_groupbox.setTitle(QCoreApplication.translate("AudioPreferencesWidget", u"Audio Device", None))
        self.driver_type_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Driver Type", None))
        self.audio_input_device_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Audio Input Device", None))
        self.audio_output_device_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Audio Output Device", None))
        self.channel_configuration_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Channel Configuration", None))
        self.input_config_button.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Input Config", None))
        self.output_config_button.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Output Config", None))
        self.audio_folder_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Audio Folder", None))
        self.audio_folder_browse_button.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Browse", None))
        self.sample_rate_groupbox.setTitle(QCoreApplication.translate("AudioPreferencesWidget", u"Sample Rate", None))
        self.sample_rate_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Sample Rate", None))
        self.latency_group_box.setTitle(QCoreApplication.translate("AudioPreferencesWidget", u"Latency", None))
        self.buffer_size_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Buffer Size", None))
        self.test_groupbox.setTitle(QCoreApplication.translate("AudioPreferencesWidget", u"Test", None))
        self.test_tone_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Test Tone", None))
        self.test_tone_button.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Off", None))
        self.tone_volume_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Tone Volume", None))
        self.tone_volume_spinbox.setSuffix(QCoreApplication.translate("AudioPreferencesWidget", u" dB", None))
        self.tone_frequency_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"Tone Frequency", None))
        self.tone_frequency_spinbox.setSuffix(QCoreApplication.translate("AudioPreferencesWidget", u" Hz", None))
        self.cpu_usage_simulator_label.setText(QCoreApplication.translate("AudioPreferencesWidget", u"CPU Usage Simulator", None))
    # retranslateUi

