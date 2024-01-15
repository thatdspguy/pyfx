"""
DO NOT MODIFY THIS FILE
This file was generated using the Pedal Builder App.
Use the Pedal Builder App to make changes to this file.
"""

from pyfx.pedal import PyFxPedalVariant


class SaturatePedalVariantBase(PyFxPedalVariant):
    """Saturate Pedal Variant Base Class"""

    """Amount Knob Parameters"""

    @property
    def amount(self):
        return self.knobs["Amount"].value_linearized

    @property
    def amount_min(self):
        return self.knobs["Amount"].minimum_value_linearized

    @property
    def amount_max(self):
        return self.knobs["Amount"].maximum_value_linearized

    @property
    def amount_default(self):
        return self.knobs["Amount"].default_value_linearized

    """Output Knob Parameters"""

    @property
    def output(self):
        return self.knobs["Output"].value_linearized

    @property
    def output_min(self):
        return self.knobs["Output"].minimum_value_linearized

    @property
    def output_max(self):
        return self.knobs["Output"].maximum_value_linearized

    @property
    def output_default(self):
        return self.knobs["Output"].default_value_linearized

    """On/Off Footswitch Parameters"""

    @property
    def on_off(self):
        return self.footswitches["On/Off"].state

    @property
    def on_off_default(self):
        return self.footswitches["On/Off"].default_state
