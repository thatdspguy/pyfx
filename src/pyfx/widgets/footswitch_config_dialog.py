from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractButton, QDialog, QDialogButtonBox, QListWidgetItem

from pyfx.footswitch import PyFxFootswitch
from pyfx.logger import pyfx_log
from pyfx.ui.footswitch_config_dialog_ui import Ui_FootswitchConfigDialog


class FootswitchConfigDialog(QDialog, Ui_FootswitchConfigDialog):
    """
    Dialog for configuring the settings of a footswitch, including type, default state, modes, and display options.
    """

    def __init__(self, footswitch: PyFxFootswitch):
        """
        Initializes the FootswitchConfigDialog with a specified footswitch.

        :param footswitch: The PyFxFootswitch object to configure.
        """
        super().__init__()
        self.setupUi(self)
        self.footswitch = footswitch

        # Initialize the dialog's UI elements based on the footswitch's settings
        self.footswitch_type_combobox.setCurrentText(footswitch.footswitch_type)
        self.enable_display_checkbox.setChecked(footswitch.display_enabled)

        if footswitch.footswitch_type == "momentary":
            self.default_combobox.setCurrentText("on" if footswitch.default_state else "off")
        elif footswitch.footswitch_type == "mode":
            for mode in footswitch.modes:
                self.add_mode(mode)

        # Connect UI signals to the dialog's methods
        self.footswitch_type_combobox.currentTextChanged.connect(self.change_footswitch_type_settings)
        self.add_mode_button.pressed.connect(self.add_mode)
        self.remove_mode_button.pressed.connect(self.remove_selected_mode)
        self.move_mode_up_button.pressed.connect(self.move_selected_mode_up)
        self.move_mode_down_button.pressed.connect(self.move_selected_mode_down)
        self.button_box.clicked.connect(self.button_box_clicked)

        # Adjust UI based on the initial footswitch type
        self.change_footswitch_type_settings(footswitch.footswitch_type)

    def button_box_clicked(self, button: QAbstractButton):
        """
        Handles the button box click event. Updates the footswitch configuration based on the dialog's settings
        if the apply button was clicked.

        :param button: The button that was clicked.
        """
        standard_button = self.button_box.standardButton(button)
        if standard_button == QDialogButtonBox.Apply:
            pyfx_log.debug("Footswitch Config applied")
            self.apply_changes()
        else:
            pyfx_log.debug("Footswitch Config aborted")
            self.reject()

    def apply_changes(self):
        """
        Applies the changes made in the dialog to the footswitch.
        """
        footswitch_type = self.footswitch_type_combobox.currentText()
        self.footswitch.set_footswitch_type(footswitch_type)
        if self.enable_display_checkbox.isChecked():
            self.footswitch.set_display_enabled()
        else:
            self.footswitch.set_display_disabled()
        if footswitch_type == "latching":
            self.footswitch.set_state(True)
            self.footswitch.set_default_state(True)
            self.footswitch.set_modes(None)
        elif footswitch_type == "momentary":
            default_state = self.default_combobox.currentText() == "on"
            self.footswitch.set_default_state(default_state)
            self.footswitch.set_state(default_state)
            self.footswitch.set_modes(None)
        elif footswitch_type == "mode":
            modes = [self.modes_list.item(i).text() for i in range(self.modes_list.count())]
            self.footswitch.set_modes(modes)
            self.footswitch.set_default_state(None)
            self.footswitch.set_state(None)
        super().accept()

    def change_footswitch_type_settings(self, footswitch_type: str):
        """
        Updates the dialog UI based on the selected footswitch type.

        :param footswitch_type: The type of the footswitch ('latching', 'momentary', or 'mode').
        """
        pyfx_log.debug(f"Footswitch type changed to {footswitch_type}")
        if footswitch_type == "latching":
            self.hide_mode_widgets()
            self.hide_default_state_widgets()
        elif footswitch_type == "momentary":
            self.hide_mode_widgets()
            self.show_default_state_widgets()
        elif footswitch_type == "mode":
            self.hide_default_state_widgets()
            self.show_mode_widgets()
        self.adjustSize()

    def hide_default_state_widgets(self):
        """Hides the widgets related to the default state of the footswitch."""
        self.default_combobox.hide()
        self.default_label.hide()

    def show_default_state_widgets(self):
        """Shows the widgets related to the default state of the footswitch."""
        self.default_combobox.show()
        self.default_label.show()

    def hide_mode_widgets(self):
        """Hides the widgets related to the mode configuration of the footswitch."""
        self.modes_label.hide()
        self.modes_list.hide()
        self.add_mode_button.hide()
        self.remove_mode_button.hide()
        self.move_mode_up_button.hide()
        self.move_mode_down_button.hide()

    def show_mode_widgets(self):
        """Shows the widgets related to the mode configuration of the footswitch."""
        self.modes_label.show()
        self.modes_list.show()
        self.add_mode_button.show()
        self.remove_mode_button.show()
        self.move_mode_up_button.show()
        self.move_mode_down_button.show()

    def add_mode(self, name: Optional[str] = None):
        """
        Adds a new mode to the footswitch configuration.

        :param name: An optional name for the new mode. If not provided, a default name is generated.
        """
        if name is None:
            mode_idx = self.modes_list.count() + 1
            name = f"Mode {mode_idx}"
        item = QListWidgetItem(name, self.modes_list)
        item.setFlags(item.flags() | Qt.ItemIsEditable)

    def remove_selected_mode(self):
        """Removes the currently selected mode from the footswitch configuration."""
        selected_item = self.modes_list.currentItem()
        if selected_item:
            row = self.modes_list.row(selected_item)
            self.modes_list.takeItem(row)

    def move_selected_mode_up(self):
        """Moves the currently selected mode up in the modes list."""
        row = self.modes_list.currentRow()
        if row > 0:
            item = self.modes_list.takeItem(row)
            self.modes_list.insertItem(row - 1, item)
            self.modes_list.setCurrentRow(row - 1)

    def move_selected_mode_down(self):
        """Moves the currently selected mode down in the modes list."""
        row = self.modes_list.currentRow()
        if row < self.modes_list.count() - 1:
            item = self.modes_list.takeItem(row)
            self.modes_list.insertItem(row + 1, item)
            self.modes_list.setCurrentRow(row + 1)

    def keyPressEvent(self, event):  # noqa: N802
        """
        Overrides the default key press event to handle specific key actions.

        :param event: The key press event.
        """
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            event.ignore()
        else:
            super().keyPressEvent(event)
