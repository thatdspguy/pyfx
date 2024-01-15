from typing import NamedTuple

import pytest

from pyfx.exceptions import KnobModeError, KnobNameError, KnobPrecisionError, KnobRangeError
from pyfx.knob import PyFxKnob


class NormalTestInfo(NamedTuple):
    test_id: str
    test_data: dict


class ErrorTestInfo(NamedTuple):
    test_id: str
    test_data: dict
    error: Exception
    error_msg: str = None


"""PyFxKnob.__init__ Normal Tests"""
pyfx_knob_init_normal_test_info = [
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Normal - Default Values",
        test_data={
            "name": "Volume",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Normal - Initial Values",
        test_data={
            "name": "Balance",
            "minimum_value": -10,
            "maximum_value": 10,
            "default_value": 5,
            "precision": 1,
            "sensitivity": 0.5,
            "mode": "logarithmic",
            "display_enabled": True,
            "value": 0,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Normal Case - Linear mode",
        test_data={
            "name": "Volume",
            "mode": "linear",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Normal Case - Logarithmic mode",
        test_data={
            "name": "Volume",
            "mode": "logarithmic",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Edge Case - Default at max",
        test_data={
            "name": "Volume",
            "minimum_value": -10,
            "maximum_value": 10,
            "default_value": 10,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Edge Case - Default at min",
        test_data={
            "name": "Volume",
            "minimum_value": -10,
            "maximum_value": 10,
            "default_value": -10,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Edge Case - Value at max",
        test_data={
            "name": "Volume",
            "minimum_value": -10,
            "maximum_value": 10,
            "value": 10,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Edge Case - Value at min",
        test_data={
            "name": "Volume",
            "minimum_value": -10,
            "maximum_value": 10,
            "value": -10,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.__init__: Edge Case - Precision at threshold",
        test_data={
            "name": "Volume",
            "minimum_value": 0,
            "maximum_value": 1,
            "precision": 1,
        },
    ),
]


@pytest.mark.parametrize(
    "test_id, test_data",
    pyfx_knob_init_normal_test_info,
    ids=[test_info.test_id for test_info in pyfx_knob_init_normal_test_info],
)
def test_pyfx_knob_init_normal_cases(test_id: str, test_data: dict):  # noqa: ARG001
    default_minimum_value = 0
    default_maximum_value = 1
    default_default_value = 0.5
    default_precision = 0.01
    default_sensitivity = 1
    default_mode = "linear"
    default_display_enabled = False
    default_value = 0.5

    expected_minimum_value = test_data.get("minimum_value", default_minimum_value)
    expected_maximum_value = test_data.get("maximum_value", default_maximum_value)
    expected_default_value = test_data.get("default_value", default_default_value)
    expected_precision = test_data.get("precision", default_precision)
    expected_sensitivity = test_data.get("sensitivity", default_sensitivity)
    expected_mode = test_data.get("mode", default_mode)
    expected_display_enabled = test_data.get("display_enabled", default_display_enabled)
    expected_value = test_data.get("value", default_value)
    if expected_mode == "linear":
        expected_minimum_value_linearized = expected_minimum_value
        expected_maximum_value_linearized = expected_maximum_value
        expected_default_value_linearized = expected_default_value
        expected_value_linearized = expected_value
    elif expected_mode == "logarithmic":
        expected_minimum_value_linearized = 10 ** (expected_minimum_value / 20)
        expected_maximum_value_linearized = 10 ** (expected_maximum_value / 20)
        expected_default_value_linearized = 10 ** (expected_default_value / 20)
        expected_value_linearized = 10 ** (expected_value / 20)

    knob = PyFxKnob(**test_data)

    assert knob.name == test_data["name"]
    assert knob.minimum_value == expected_minimum_value
    assert knob.maximum_value == expected_maximum_value
    assert knob.default_value == expected_default_value
    assert knob.precision == expected_precision
    assert knob.sensitivity == expected_sensitivity
    assert knob.mode == expected_mode
    assert knob.display_enabled == expected_display_enabled
    assert knob.value == expected_value
    assert knob.minimum_value_linearized == expected_minimum_value_linearized
    assert knob.maximum_value_linearized == expected_maximum_value_linearized
    assert knob.default_value_linearized == expected_default_value_linearized
    assert knob.value_linearized == expected_value_linearized


"""PyFxKnob.__init__ Error Tests"""
pyfx_knob_init_error_test_info = [
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Min > Max",
        test_data={
            "name": "Volume",
            "minimum_value": 1,
            "maximum_value": 0,
        },
        error=KnobRangeError,
        error_msg="Minimum value must be less than maximum value",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Default above max",
        test_data={
            "name": "Volume",
            "minimum_value": 0,
            "maximum_value": 1,
            "default_value": 2,
        },
        error=KnobRangeError,
        error_msg="Default value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Default below min",
        test_data={
            "name": "Volume",
            "minimum_value": 0,
            "maximum_value": 1,
            "default_value": -1,
        },
        error=KnobRangeError,
        error_msg="Default value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Value above max",
        test_data={
            "name": "Volume",
            "minimum_value": 0,
            "maximum_value": 1,
            "value": 2,
        },
        error=KnobRangeError,
        error_msg="Value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Value below min",
        test_data={
            "name": "Volume",
            "minimum_value": 0,
            "maximum_value": 1,
            "value": -1,
        },
        error=KnobRangeError,
        error_msg="Value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Precision too high",
        test_data={
            "name": "Volume",
            "minimum_value": 0,
            "maximum_value": 1,
            "precision": 2,
        },
        error=KnobPrecisionError,
        error_msg="Precision must be less than (maximum_value - minimum_value)",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Invalid mode",
        test_data={
            "name": "Volume",
            "mode": "test",
        },
        error=KnobModeError,
        error_msg=f"Invalid knob mode. Valid knob modes are {PyFxKnob.valid_modes}",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Name is empty str",
        test_data={
            "name": "",
        },
        error=KnobNameError,
        error_msg="Name must be a non-empty str",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.__init__: Error - Name is None",
        test_data={
            "name": None,
        },
        error=KnobNameError,
        error_msg="Name must be a non-empty str",
    ),
]


@pytest.mark.parametrize(
    "test_id, test_data, error, error_msg",
    pyfx_knob_init_error_test_info,
    ids=[test_info.test_id for test_info in pyfx_knob_init_error_test_info],
)
def test_pyfx_knob_init_error_cases(test_id: str, test_data: dict, error: Exception, error_msg: str):  # noqa: ARG001
    with pytest.raises(error) as exc_info:
        PyFxKnob(**test_data)

    if error_msg is not None:
        assert str(exc_info.value) == error_msg


pyfx_knob_setters_normal_test_info = [
    NormalTestInfo(
        test_id="PyFxKnob.set_minimum_value: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
            },
            "value_name": "minimum_value",
            "setter_name": "set_minimum_value",
            "setter_params": (-1,),
            "expected_value": -1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_maximum_value: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "maximum_value": 1,
            },
            "value_name": "maximum_value",
            "setter_name": "set_maximum_value",
            "setter_params": (2,),
            "expected_value": 2,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_default_value: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "default_value": 0.5,
            },
            "value_name": "default_value",
            "setter_name": "set_default_value",
            "setter_params": (0.25,),
            "expected_value": 0.25,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_precision: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "precision": 0.01,
            },
            "value_name": "precision",
            "setter_name": "set_precision",
            "setter_params": (0.1,),
            "expected_value": 0.1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_sensitivity: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "sensitivity": 1,
            },
            "value_name": "sensitivity",
            "setter_name": "set_sensitivity",
            "setter_params": (0.5,),
            "expected_value": 0.5,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_mode: Normal Case - linear mode",
        test_data={
            "knob_data": {
                "name": "Volume",
                "mode": "logarithmic",
            },
            "value_name": "mode",
            "setter_name": "set_mode",
            "setter_params": ("linear",),
            "expected_value": "linear",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_mode: Normal Case - logarithmic mode",
        test_data={
            "knob_data": {
                "name": "Volume",
                "mode": "linear",
            },
            "value_name": "mode",
            "setter_name": "set_mode",
            "setter_params": ("logarithmic",),
            "expected_value": "logarithmic",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_display_enabled: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "display_enabled": False,
            },
            "value_name": "display_enabled",
            "setter_name": "set_display_enabled",
            "setter_params": (),
            "expected_value": True,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_display_disabled: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "display_enabled": True,
            },
            "value_name": "display_enabled",
            "setter_name": "set_display_disabled",
            "setter_params": (),
            "expected_value": False,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_knob_value: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "value": 0.5,
            },
            "value_name": "value",
            "setter_name": "set_knob_value",
            "setter_params": (0.25,),
            "expected_value": 0.25,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.change_knob_name: Normal Case",
        test_data={
            "knob_data": {
                "name": "Saturate",
            },
            "value_name": "name",
            "setter_name": "change_knob_name",
            "setter_params": ("Distortion",),
            "expected_value": "Distortion",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_default_value: Edge Case - Default at min",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "default_value": 0.5,
            },
            "value_name": "default_value",
            "setter_name": "set_default_value",
            "setter_params": (0,),
            "expected_value": 0,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_default_value: Edge Case - Default at max",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "default_value": 0.5,
            },
            "value_name": "default_value",
            "setter_name": "set_default_value",
            "setter_params": (1,),
            "expected_value": 1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_knob_value: Edge Case - Value at min",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "value": 0.5,
            },
            "value_name": "value",
            "setter_name": "set_knob_value",
            "setter_params": (0,),
            "expected_value": 0,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_knob_value: Edge Case - Value at max",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "value": 0.5,
            },
            "value_name": "value",
            "setter_name": "set_knob_value",
            "setter_params": (1,),
            "expected_value": 1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_precision: Edge Case - Precision at threshold",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "precision": 0.1,
            },
            "value_name": "precision",
            "setter_name": "set_precision",
            "setter_params": (1,),
            "expected_value": 1,
        },
    ),
]


@pytest.mark.parametrize(
    "test_id, test_data",
    pyfx_knob_setters_normal_test_info,
    ids=[test_info.test_id for test_info in pyfx_knob_setters_normal_test_info],
)
def test_pyfx_knob_setters_normal_cases(test_id: str, test_data: dict):  # noqa: ARG001
    knob = PyFxKnob(**test_data["knob_data"])
    knob_value = getattr(knob, test_data["value_name"])
    assert knob_value != test_data["expected_value"]
    setter_fcn = getattr(knob, test_data["setter_name"])
    setter_fcn(*test_data["setter_params"])
    knob_value = getattr(knob, test_data["value_name"])
    assert knob_value == test_data["expected_value"]


pyfx_knob_setters_error_test_info = [
    ErrorTestInfo(
        test_id="PyFxKnob.set_minimum_value: Error - Min > Max",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
            },
            "setter_name": "set_minimum_value",
            "setter_params": (2,),
        },
        error=KnobRangeError,
        error_msg="Minimum value must be less than maximum value",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.set_maximum_value: Error - Max < Min",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
            },
            "setter_name": "set_maximum_value",
            "setter_params": (-1,),
        },
        error=KnobRangeError,
        error_msg="Maximum value must be greater than minimum value",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.set_default_value: Error - Default above max",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "default_value": 0.5,
            },
            "setter_name": "set_default_value",
            "setter_params": (2,),
        },
        error=KnobRangeError,
        error_msg="Default value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.set_default_value: Error - Default below min",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "default_value": 0.5,
            },
            "setter_name": "set_default_value",
            "setter_params": (-1,),
        },
        error=KnobRangeError,
        error_msg="Default value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.set_knob_value: Error - Value above max",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "value": 0.5,
            },
            "setter_name": "set_knob_value",
            "setter_params": (2,),
        },
        error=KnobRangeError,
        error_msg="Value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.set_knob_value: Error - Value below min",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "value": 0.5,
            },
            "setter_name": "set_knob_value",
            "setter_params": (-1,),
        },
        error=KnobRangeError,
        error_msg="Value must be within the minimum and maximum values",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.set_precision: Error - Precision too high",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "precision": 0.1,
            },
            "setter_name": "set_precision",
            "setter_params": (1.1,),
        },
        error=KnobPrecisionError,
        error_msg="Precision must be less than (maximum_value - minimum_value)",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.set_mode: Error - Invalid mode",
        test_data={
            "knob_data": {
                "name": "Volume",
            },
            "setter_name": "set_mode",
            "setter_params": ("test",),
        },
        error=KnobModeError,
        error_msg=f"Invalid log mode. Valid log modes are {PyFxKnob.valid_modes}",
    ),
    ErrorTestInfo(
        test_id="PyFxKnob.change_knob_name: Error - Empty str",
        test_data={
            "knob_data": {
                "name": "Volume",
            },
            "setter_name": "change_knob_name",
            "setter_params": ("",),
        },
        error=KnobNameError,
        error_msg="Name must be a non-empty str",
    ),
]


@pytest.mark.parametrize(
    "test_id, test_data, error, error_msg",
    pyfx_knob_setters_error_test_info,
    ids=[test_info.test_id for test_info in pyfx_knob_setters_error_test_info],
)
def test_pyfx_knob_setters_error_cases(test_id: str, test_data: dict, error: Exception, error_msg: str):  # noqa: ARG001
    knob = PyFxKnob(**test_data["knob_data"])
    setter_fcn = getattr(knob, test_data["setter_name"])

    with pytest.raises(error) as exc_info:
        setter_fcn(*test_data["setter_params"])

    if error_msg is not None:
        assert str(exc_info.value) == error_msg


pyfx_knob_setters_linearized_normal_test_info = [
    NormalTestInfo(
        test_id="PyFxKnob.set_minimum_value (Linearized: linear): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "mode": "linear",
            },
            "value_name": "minimum_value_linearized",
            "setter_name": "set_minimum_value",
            "setter_params": (1,),
            "expected_linearized_value": 1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_minimum_value (Linearized: logarithmic): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "mode": "logarithmic",
            },
            "value_name": "minimum_value_linearized",
            "setter_name": "set_minimum_value",
            "setter_params": (20,),
            "expected_linearized_value": 10,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_maximum_value (Linearized: linear): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "mode": "linear",
            },
            "value_name": "maximum_value_linearized",
            "setter_name": "set_maximum_value",
            "setter_params": (1,),
            "expected_linearized_value": 1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_maximum_value (Linearized: logarithmic): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "mode": "logarithmic",
            },
            "value_name": "maximum_value_linearized",
            "setter_name": "set_maximum_value",
            "setter_params": (20,),
            "expected_linearized_value": 10,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_default_value (Linearized: linear): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "default_value": 50,
                "mode": "linear",
            },
            "value_name": "default_value_linearized",
            "setter_name": "set_default_value",
            "setter_params": (1,),
            "expected_linearized_value": 1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_default_value (Linearized: logarithmic): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "default_value": 50,
                "mode": "logarithmic",
            },
            "value_name": "default_value_linearized",
            "setter_name": "set_default_value",
            "setter_params": (20,),
            "expected_linearized_value": 10,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_knob_value (Linearized: linear): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "value": 50,
                "mode": "linear",
            },
            "value_name": "value_linearized",
            "setter_name": "set_knob_value",
            "setter_params": (1,),
            "expected_linearized_value": 1,
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.set_knob_value (Linearized: logarithmic): Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 100,
                "value": 50,
                "mode": "logarithmic",
            },
            "value_name": "value_linearized",
            "setter_name": "set_knob_value",
            "setter_params": (20,),
            "expected_linearized_value": 10,
        },
    ),
]


@pytest.mark.parametrize(
    "test_id, test_data",
    pyfx_knob_setters_linearized_normal_test_info,
    ids=[test_info.test_id for test_info in pyfx_knob_setters_linearized_normal_test_info],
)
def test_pyfx_knob_setters_linearized_normal_cases(test_id: str, test_data: dict):  # noqa: ARG001
    knob = PyFxKnob(**test_data["knob_data"])
    knob_linearized_value = getattr(knob, test_data["value_name"])
    assert knob_linearized_value != test_data["expected_linearized_value"]
    setter_fcn = getattr(knob, test_data["setter_name"])
    setter_fcn(*test_data["setter_params"])
    knob_linearized_value = getattr(knob, test_data["value_name"])
    assert knob_linearized_value == test_data["expected_linearized_value"]


pyfx_knob_knob_add_and_remove_observer_normal_test_info = [
    NormalTestInfo(
        test_id="PyFxKnob.{add,remove}_set_knob_value_observer: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
            },
            "setter_name": "set_knob_value",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.{add,remove}_change_knob_name_observer: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
            },
            "setter_name": "change_knob_name",
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.{add,remove}_remove_knob_observer: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
            },
            "setter_name": "remove_knob",
        },
    ),
]


@pytest.mark.parametrize(
    "test_id, test_data",
    pyfx_knob_knob_add_and_remove_observer_normal_test_info,
    ids=[test_info.test_id for test_info in pyfx_knob_knob_add_and_remove_observer_normal_test_info],
)
def test_pyfx_knob_add_and_remove_observers_normal_cases(test_id: str, test_data: dict):  # noqa: ARG001
    class TestObserverClass:
        def __init__(self):
            self.value = None

        def observer_cb(self, value):
            self.value = value

    test_observer_class = TestObserverClass()

    knob = PyFxKnob(**test_data["knob_data"])
    observer_adder = getattr(knob, f"add_{test_data['setter_name']}_observer")
    observer_remover = getattr(knob, f"remove_{test_data['setter_name']}_observer")
    observers = getattr(knob, f"_{test_data['setter_name']}_observers")
    assert test_observer_class.observer_cb not in observers
    observer_adder(test_observer_class.observer_cb)
    assert test_observer_class.observer_cb in observers
    observer_remover(test_observer_class.observer_cb)
    assert test_observer_class.observer_cb not in observers


pyfx_knob_knob_notify_observer_normal_test_info = [
    NormalTestInfo(
        test_id="PyFxKnob.notify_set_knob_value_observers: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
                "minimum_value": 0,
                "maximum_value": 1,
                "value": 0.5,
            },
            "setter_name": "set_knob_value",
            "setter_params": (1,),
            "expected_observer_cb_args": (1,),
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.notify_change_knob_name_observers: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
            },
            "setter_name": "change_knob_name",
            "setter_params": ("Gain",),
            "expected_observer_cb_args": ("Volume", "Gain"),
        },
    ),
    NormalTestInfo(
        test_id="PyFxKnob.notify_remove_knob_observers: Normal Case",
        test_data={
            "knob_data": {
                "name": "Volume",
            },
            "setter_name": "remove_knob",
            "setter_params": (),
            "expected_observer_cb_args": ("self",),
        },
    ),
]


@pytest.mark.parametrize(
    "test_id, test_data",
    pyfx_knob_knob_notify_observer_normal_test_info,
    ids=[test_info.test_id for test_info in pyfx_knob_knob_notify_observer_normal_test_info],
)
def test_pyfx_knob_notify_observers_normal_cases(test_id: str, test_data: dict):  # noqa: ARG001
    class TestObserverClass:
        def __init__(self):
            self.args = None
            self.observer_call_cnt = 0

        def observer_cb(self, *args):
            self.args = args
            self.observer_call_cnt += 1

    test_observer_class = TestObserverClass()

    knob = PyFxKnob(**test_data["knob_data"])
    expected_observer_cb_args = tuple(arg if arg != "self" else knob for arg in test_data["expected_observer_cb_args"])
    knob_setter = getattr(knob, test_data["setter_name"])
    observer_adder = getattr(knob, f"add_{test_data['setter_name']}_observer")

    observer_adder(test_observer_class.observer_cb)
    assert test_observer_class.observer_call_cnt == 0
    assert test_observer_class.args is None
    knob_setter(*test_data["setter_params"])
    assert test_observer_class.observer_call_cnt == 1
    assert test_observer_class.args == expected_observer_cb_args
