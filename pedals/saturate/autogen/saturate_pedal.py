"""
DO NOT MODIFY THIS FILE
This file was generated using the Pedal Builder App.
Use the Pedal Builder App to make changes to this file.
"""

from default_saturate_pedal import DefaultSaturatePedal
from smooth_saturate_pedal import SmoothSaturatePedal

from pyfx.footswitch import PyFxFootswitch
from pyfx.knob import PyFxKnob
from pyfx.pedal import PyFxPedal


class SaturatePedal(PyFxPedal):
    """Saturate Class"""

    def __init__(self):
        name = "Saturate"
        knobs = {
            "Amount": PyFxKnob(
                name="Amount",
                minimum_value=0,
                maximum_value=40.0,
                default_value=0.0,
                precision=1.0,
                sensitivity=1,
                mode="logarithmic",
                display_enabled=True,
                value=10.0,
            ),
            "Output": PyFxKnob(
                name="Output",
                minimum_value=-50.0,
                maximum_value=0.0,
                default_value=0.0,
                precision=1.0,
                sensitivity=1,
                mode="logarithmic",
                display_enabled=True,
                value=0.14125375446227545,
            ),
        }
        footswitches = {
            "On/Off": PyFxFootswitch(
                name="On/Off",
                footswitch_type="latching",
                default_state=True,
                state=True,
                mode=None,
                modes=None,
                display_enabled=True,
            ),
        }
        variants = {
            "Default": DefaultSaturatePedal(
                name="Default",
                knobs=knobs,
                footswitches=footswitches,
            ),
            "Smooth": SmoothSaturatePedal(
                name="Smooth",
                knobs=knobs,
                footswitches=footswitches,
            ),
        }
        variant = variants["Smooth"]
        pedal_color = "#0000FF"
        text_color = "#FFFFFF"
        super().__init__(
            name=name,
            knobs=knobs,
            footswitches=footswitches,
            variant=variant,
            variants=variants,
            pedal_color=pedal_color,
            text_color=text_color,
        )
