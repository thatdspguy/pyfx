"""
DO NOT MODIFY THIS FILE
This file was generated using the Pedal Builder App.
Use the Pedal Builder App to make changes to this file.
"""

from pyfx.pedal import PyFxPedalVariant


class DelayPedalVariantBase(PyFxPedalVariant):
    """Delay Pedal Variant Base Class"""

    """Feedback Knob Parameters"""

    @property
    def feedback(self):
        return self.knobs["Feedback"].value_linearized

    @property
    def feedback_min(self):
        return self.knobs["Feedback"].minimum_value_linearized

    @property
    def feedback_max(self):
        return self.knobs["Feedback"].maximum_value_linearized

    @property
    def feedback_default(self):
        return self.knobs["Feedback"].default_value_linearized

    """Time Knob Parameters"""

    @property
    def time(self):
        return self.knobs["Time"].value_linearized

    @property
    def time_min(self):
        return self.knobs["Time"].minimum_value_linearized

    @property
    def time_max(self):
        return self.knobs["Time"].maximum_value_linearized

    @property
    def time_default(self):
        return self.knobs["Time"].default_value_linearized

    """Dry/Wet Knob Parameters"""

    @property
    def dry_wet(self):
        return self.knobs["Dry/Wet"].value_linearized

    @property
    def dry_wet_min(self):
        return self.knobs["Dry/Wet"].minimum_value_linearized

    @property
    def dry_wet_max(self):
        return self.knobs["Dry/Wet"].maximum_value_linearized

    @property
    def dry_wet_default(self):
        return self.knobs["Dry/Wet"].default_value_linearized

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
