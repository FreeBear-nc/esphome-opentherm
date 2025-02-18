# This file contains a schema for all supported sensors, binary sensors and
# inputs of the OpenTherm component.

from typing import Dict, Generic, Tuple, TypeVar, TypedDict

# NotRequired was moved to typing in Python 3.11
# as long as ESPHome supports Python < 3.11, we need to allow both imports
try:
    from typing import NotRequired
except ImportError:
    from typing_extensions import NotRequired

from esphome.const import (
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_KILOWATT,
    UNIT_EMPTY,
    DEVICE_CLASS_COLD,
    DEVICE_CLASS_HEAT,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_PROBLEM,
    DEVICE_CLASS_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    STATE_CLASS_NONE,
)

T = TypeVar("T")
class Schema(Generic[T], Dict[str, T]):
    pass

class EntitySchema(TypedDict):
    description: str
    """Description of the item, based on the OpenTherm spec"""

    message: str
    """OpenTherm message id used to read or write the value"""

    keep_updated: bool
    """Whether the value should be read or write repeatedly (True) or only during
    the initialization phase (False)
    """

    message_data: str
    """Instructions on how to interpret the data in the message
      - flag8_[hb|lb]_[0-7]: data is a byte of single bit flags,
                             this flag is set in the high (hb) or low byte (lb),
                             at position 0 to 7
      - u8_[hb|lb]: data is an unsigned 8-bit integer,
                    in the high (hb) or low byte (lb)
      - s8_[hb|lb]: data is an signed 8-bit integer,
                    in the high (hb) or low byte (lb)
      - f88: data is a signed fixed point value with
              1 sign bit, 7 integer bits, 8 fractional bits
      - u16: data is an unsigned 16-bit integer
      - s16: data is a signed 16-bit integer
    """

class SensorSchema(EntitySchema):
    unit_of_measurement: NotRequired[str]
    accuracy_decimals: int
    device_class: NotRequired[str]
    icon: NotRequired[str]
    state_class: str

SENSORS: Schema[SensorSchema] = Schema({
    "rel_mod_level": SensorSchema({
        "description": "Relative modulation level",
        "unit_of_measurement": UNIT_PERCENT,
        "accuracy_decimals": 2,
        "icon": "mdi:percent",
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "RelModLevel",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "ch_pressure": SensorSchema({
        "description": "Water pressure in CH circuit",
        "unit_of_measurement": "bar",
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_PRESSURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "CHPressure",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "dhw_flow_rate": SensorSchema({
        "description": "Water flow rate in DHW circuit",
        "unit_of_measurement": "l/min",
        "accuracy_decimals": 2,
        "icon": "mdi:waves-arrow-right",
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "DHWFlowRate",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_boiler": SensorSchema({
        "description": "Boiler water temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tboiler",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_dhw": SensorSchema({
        "description": "DHW temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tdhw",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_outside": SensorSchema({
        "description": "Outside temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Toutside",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_ret": SensorSchema({
        "description": "Return water temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tret",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_storage": SensorSchema({
        "description": "Solar storage temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tstorage",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_collector": SensorSchema({
        "description": "Solar collector temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tcollector",
        "keep_updated": True,
        "message_data": "s16",
    }),
    "t_flow_ch2": SensorSchema({
        "description": "Flow water temperature CH2 circuit",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TflowCH2",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_dhw2": SensorSchema({
        "description": "Domestic hot water temperature 2",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Tdhw2",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "t_exhaust": SensorSchema({
        "description": "Boiler exhaust temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Texhaust",
        "keep_updated": True,
        "message_data": "s16",
    }),
    "burner_starts": SensorSchema({
        "description": "Number of starts burner",
        "accuracy_decimals": 0,
        "icon": "mdi:gas-burner",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "SuccessfulBurnerStarts",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "ch_pump_starts": SensorSchema({
        "description": "Number of starts CH pump",
        "accuracy_decimals": 0,
        "icon": "mdi:pump",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "CHPumpStarts",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "dhw_pump_valve_starts": SensorSchema({
        "description": "Number of starts DHW pump/valve",
        "accuracy_decimals": 0,
        "icon": "mdi:water-pump",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "DHWPumpValveStarts",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "dhw_burner_starts": SensorSchema({
        "description": "Number of starts burner during DHW mode",
        "accuracy_decimals": 0,
        "icon": "mdi:gas-burner",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "DHWBurnerStarts",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "burner_operation_hours": SensorSchema({
        "description": "Number of hours that burner is in operation",
        "accuracy_decimals": 0,
        "icon": "mdi:clock-outline",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "BurnerOperationHours",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "ch_pump_operation_hours": SensorSchema({
        "description": "Number of hours that CH pump has been running",
        "accuracy_decimals": 0,
        "icon": "mdi:clock-outline",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "CHPumpOperationHours",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "dhw_pump_valve_operation_hours": SensorSchema({
        "description": "Number of hours that DHW pump has been running or DHW valve has been opened",
        "accuracy_decimals": 0,
        "icon": "mdi:clock-outline",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "DHWPumpValveOperationHours",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "dhw_burner_operation_hours": SensorSchema({
        "description": "Number of hours that burner is in operation during DHW mode",
        "accuracy_decimals": 0,
        "icon": "mdi:clock-outline",
        "state_class": STATE_CLASS_TOTAL_INCREASING,
        "message": "DHWBurnerOperationHours",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "t_dhw_set_ub": SensorSchema({
        "description": "Upper bound for adjustment of DHW setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TdhwSetUBTdhwSetLB",
        "keep_updated": False,
        "message_data": "s8_hb",
    }),
    "t_dhw_set_lb": SensorSchema({
        "description": "Lower bound for adjustment of DHW setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TdhwSetUBTdhwSetLB",
        "keep_updated": False,
        "message_data": "s8_lb",
    }),
    "max_t_set_ub": SensorSchema({
        "description": "Upper bound for adjustment of max CH setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "MaxTSetUBMaxTSetLB",
        "keep_updated": False,
        "message_data": "s8_hb",
    }),
    "max_t_set_lb": SensorSchema({
        "description": "Lower bound for adjustment of max CH setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "MaxTSetUBMaxTSetLB",
        "keep_updated": False,
        "message_data": "s8_lb",
    }),
    "otc_ratio_ub": SensorSchema({
        "description": "Upper bound of OTC curve",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "message": "OTCratio",
        "keep_updated": False,
        "message_data": "s8_hb",
    }),
    "otc_ratio_lb": SensorSchema({
        "description": "Lower bound of OTC curve",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "message": "OTCratio",
        "keep_updated": False,
        "message_data": "s8_lb",
    }),
    "t_dhw_set": SensorSchema({
        "description": "Domestic hot water temperature setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TdhwSet",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "max_t_set": SensorSchema({
        "description": "Maximum allowable CH water setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "MaxTSet",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "otc_hc_ratio": SensorSchema({
        "description": "OTC heat curve ratio",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 2,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "Hcratio",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "oem_fault_code": SensorSchema({
        "description": "OEM fault code",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "message": "ASFflags",
        "keep_updated": True,
        "message_data": "u8_lb",
    }),
    "t_heat_exchanger": SensorSchema({
        "description": "Boiler heat exchanger temperature",
        "unit_of_measurement": UNIT_CELSIUS,
        "accuracy_decimals": 0,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "TboilerHeatExchanger",
        "keep_updated": True,
        "message_data": "s16",
    }),
    "fan_speed": SensorSchema({
        "description": "Boiler fan speed",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "icon": "mdi:fan",
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "BoilerFanSpeedSetpointAndActual",
        "keep_updated": True,
        "message_data": "u8_lb_60",
    }),
    "boiler_flame_current": SensorSchema({
        "description": "Boiler flame current (uA)",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 2,
        "state_class": STATE_CLASS_NONE,
        "message": "FlameCurrent",
        "keep_updated": True,
        "message_data": "f88",
    }),
    "oem_diagnostic_code": SensorSchema({
        "description": "OEM diagnostic code",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "message": "OEMDiagnosticCode",
        "keep_updated": True,
        "message_data": "u16",
    }),
    "max_capacity": SensorSchema({
        "description": "Maximum boiler capacity (KW)",
        "unit_of_measurement": UNIT_KILOWATT,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_MEASUREMENT,
        "disabled_by_default": True,
        "message": "MaxCapacityMinModLevel",
        "keep_updated": False,
        "message_data": "u8_hb",
    }),
    "min_mod_level": SensorSchema({
        "description": "Minimum modulation level",
        "unit_of_measurement": UNIT_PERCENT,
        "accuracy_decimals": 0,
        "icon": "mdi:percent",
        "disabled_by_default": True,
        "state_class": STATE_CLASS_MEASUREMENT,
        "message": "MaxCapacityMinModLevel",
        "keep_updated": False,
        "message_data": "u8_lb",
    }),
    "opentherm_version_device": SensorSchema({
        "description": "Version of OpenTherm implemented by slave",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "disabled_by_default": True,
        "message": "OpenThermVersionSlave",
        "keep_updated": False,
        "message_data": "f88",
    }),
    "device_type": SensorSchema({
        "description": "Slave product type",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "disabled_by_default": True,
        "message": "SlaveVersion",
        "keep_updated": False,
        "message_data": "u8_hb",
    }),
    "device_version": SensorSchema({
        "description": "Slave product version",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "disabled_by_default": True,
        "message": "SlaveVersion",
        "keep_updated": False,
        "message_data": "u8_lb",
    }),

    "device_id": SensorSchema({
        "description": "Slave ID code",
        "unit_of_measurement": UNIT_EMPTY,
        "accuracy_decimals": 0,
        "state_class": STATE_CLASS_NONE,
        "disabled_by_default": True,
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "u8_lb",
    }),
})

class BinarySensorSchema(EntitySchema):
    device_class: NotRequired[str]
    icon: NotRequired[str]

BINARY_SENSORS: Schema = Schema({
    "fault_indication": BinarySensorSchema({
        "description": "Status: Fault indication",
        "device_class": DEVICE_CLASS_PROBLEM,
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_lb_0",
    }),
    "ch_active": BinarySensorSchema({
        "description": "Status: Central Heating active",
        "device_class": DEVICE_CLASS_HEAT,
        "icon": "mdi:radiator",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_lb_1",
    }),
    "dhw_active": BinarySensorSchema({
        "description": "Status: Domestic Hot Water active",
        "device_class": DEVICE_CLASS_HEAT,
        "icon": "mdi:faucet",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_lb_2",
    }),
    "flame_on": BinarySensorSchema({
        "description": "Status: Flame on",
        "device_class": DEVICE_CLASS_HEAT,
        "icon": "mdi:fire",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_lb_3",
    }),
    "cooling_active": BinarySensorSchema({
        "description": "Status: Cooling active",
        "device_class": DEVICE_CLASS_COLD,
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_lb_4",
    }),
    "ch2_active": BinarySensorSchema({
        "description": "Status: Central Heating 2 active",
        "device_class": DEVICE_CLASS_HEAT,
        "icon": "mdi:radiator",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_lb_5",
    }),
    "diagnostic_indication": BinarySensorSchema({
        "description": "Status: Diagnostic event",
        "device_class": DEVICE_CLASS_PROBLEM,
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_lb_6",
    }),
    "dhw_present": BinarySensorSchema({
        "description": "Configuration: DHW present",
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "flag8_hb_0",
    }),
    "control_type_on_off": BinarySensorSchema({
        "description": "Configuration: Control type is on/off",
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "flag8_hb_1",
    }),
    "cooling_supported": BinarySensorSchema({
        "description": "Configuration: Cooling supported",
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "flag8_hb_2",
    }),
    "dhw_storage_tank": BinarySensorSchema({
        "description": "Configuration: DHW storage tank",
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "flag8_hb_3",
    }),
    "controller_pump_control_allowed": BinarySensorSchema({
        "description": "Configuration: Master pump control allowed",
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "flag8_hb_4",
    }),
    "master_pump_control_allowed": BinarySensorSchema({
        "description": "Configuration: Master pump control allowed",
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "flag8_hb_4",
    }),
    "ch2_present": BinarySensorSchema({
        "description": "Configuration: CH2 present",
        "message": "SConfigSMemberIDcode",
        "keep_updated": False,
        "message_data": "flag8_hb_5",
    }),
    "dhw_setpoint_transfer_enabled": BinarySensorSchema({
        "description": "Remote boiler parameters: DHW setpoint transfer enabled",
        "message": "RBPflags",
        "keep_updated": False,
        "message_data": "flag8_hb_0",
    }),
    "max_ch_setpoint_transfer_enabled": BinarySensorSchema({
        "description": "Remote boiler parameters: CH maximum setpoint transfer enabled",
        "message": "RBPflags",
        "keep_updated": False,
        "message_data": "flag8_hb_1",
    }),
    "dhw_setpoint_rw": BinarySensorSchema({
        "description": "Remote boiler parameters: DHW setpoint read/write",
        "message": "RBPflags",
        "keep_updated": False,
        "message_data": "flag8_lb_0",
    }),
    "max_ch_setpoint_rw": BinarySensorSchema({
        "description": "Remote boiler parameters: CH maximum setpoint read/write",
        "message": "RBPflags",
        "keep_updated": False,
        "message_data": "flag8_lb_1",
    }),
    "service_request": BinarySensorSchema({
        "description": "Service Request",
        "message": "ASFflags",
        "keep_updated": True,
        "message_data": "flag8_hb_0",
    }),
    "lockout_reset": BinarySensorSchema({
        "description": "Lockout Reset",
        "message": "ASFflags",
        "keep_updated": True,
        "message_data": "flag8_hb_1",
    }),
    "low_water_pressure": BinarySensorSchema({
        "device_class": DEVICE_CLASS_PROBLEM,
        "description": "Low Water Pressure",
        "message": "ASFflags",
        "keep_updated": True,
        "message_data": "flag8_hb_2",
    }),
    "flame_fault": BinarySensorSchema({
        "device_class": DEVICE_CLASS_PROBLEM,
        "description": "Gas/Flame Fault",
        "message": "ASFflags",
        "keep_updated": True,
        "message_data": "flag8_hb_3",
    }),
    "air_pressure_fault": BinarySensorSchema({
        "device_class": DEVICE_CLASS_PROBLEM,
        "description": "Air Pressure Fault",
        "message": "ASFflags",
        "keep_updated": True,
        "message_data": "flag8_hb_4",
    }),
    "water_over_temperature": BinarySensorSchema({
        "device_class": DEVICE_CLASS_PROBLEM,
        "description": "Water Over Temperature",
        "message": "ASFflags",
        "keep_updated": True,
        "message_data": "flag8_hb_5",
    }),
})

class SwitchSchema(EntitySchema):
    default_mode: str

SWITCHES: Schema[SwitchSchema] = Schema({
    "ch_enable": SwitchSchema({
        "description": "Central Heating enabled",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_hb_0",
        "default_mode": "restore_default_on"
    }),
    "dhw_enable": SwitchSchema({
        "description": "Domestic Hot Water enabled",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_hb_1",
        "default_mode": "restore_default_on"
    }),
    "cooling_enable": SwitchSchema({
        "description": "Cooling enabled",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_hb_2",
        "default_mode": "restore_default_off"
    }),
    "otc_active": SwitchSchema({
        "description": "Outside temperature compensation active",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_hb_3",
        "default_mode": "restore_default_off"
    }),
    "ch2_active": SwitchSchema({
        "description": "Central Heating 2 active",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_hb_4",
        "default_mode": "restore_default_off"
    }),
    "sm_active": SwitchSchema({
        "description": "Summer mode active",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_hb_5",
        "default_mode": "restore_default_off"
    }),
    "dhw_block": SwitchSchema({
        "description": "DHW Blocking",
        "message": "Status",
        "keep_updated": True,
        "message_data": "flag8_hb_6",
        "default_mode": "restore_default_off"
    }),
    "lock_out_reset": SwitchSchema({
        "description": "Boiler Lock-out Reset",
        "message": "RemoteRequest",
        "keep_updated": True,
        "message_data": "flag8_hb_1",
        "default_mode": "restore_default_off"
    }),
})

class AutoConfigure(TypedDict):
    message: str
    message_data: str

class InputSchema(EntitySchema):
    unit_of_measurement: str
    step: float
    range: Tuple[int, int]
    auto_max_value: NotRequired[AutoConfigure]
    auto_min_value: NotRequired[AutoConfigure]

INPUTS: Schema[InputSchema] = Schema({
    "t_set": InputSchema({
        "description": "Control setpoint: temperature setpoint for the boiler's supply water",
        "unit_of_measurement": UNIT_CELSIUS,
        "step": 0.1,
        "message": "TSet",
        "keep_updated": True,
        "message_data": "f88",
        "range": (0, 100),
        "auto_max_value": { "message": "MaxTSet", "message_data": "f88" },
    }),
    "t_set_ch2": InputSchema({
        "description": "Control setpoint 2: temperature setpoint for the boiler's supply water on the second heating circuit",
        "unit_of_measurement": UNIT_CELSIUS,
        "step": 0.1,
        "message": "TsetCH2",
        "keep_updated": True,
        "message_data": "f88",
        "range": (0, 100),
        "auto_max_value": { "message": "MaxTSet", "message_data": "f88" },
    }),
    "cooling_control": InputSchema({
        "description": "Cooling control signal",
        "unit_of_measurement": UNIT_PERCENT,
        "step": 1.0,
        "message": "CoolingControl",
        "keep_updated": True,
        "message_data": "f88",
        "range": (0, 100),
    }),
    "t_dhw_set": InputSchema({
        "description": "Domestic hot water temperature setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "step": 0.1,
        "message": "TdhwSet",
        "keep_updated": True,
        "message_data": "f88",
        "range": (0, 127),
        "auto_min_value": { "message": "TdhwSetUBTdhwSetLB", "message_data": "s8_lb" },
        "auto_max_value": { "message": "TdhwSetUBTdhwSetLB", "message_data": "s8_hb" },
    }),
    "max_t_set": InputSchema({
        "description": "Maximum allowable CH water setpoint",
        "unit_of_measurement": UNIT_CELSIUS,
        "step": 0.1,
        "message": "MaxTSet",
        "keep_updated": True,
        "message_data": "f88",
        "range": (0, 127),
        "auto_min_value": { "message": "MaxTSetUBMaxTSetLB", "message_data": "s8_lb" },
        "auto_max_value": { "message": "MaxTSetUBMaxTSetLB", "message_data": "s8_hb" },
    }),
    "t_room_set": InputSchema({
        "description": "Current room temperature setpoint (informational)",
        "unit_of_measurement": UNIT_CELSIUS,
        "step": 0.1,
        "message": "TrSet",
        "keep_updated": True,
        "message_data": "f88",
        "range": (-40, 127),
    }),
    "t_room_set_ch2": InputSchema({
        "description": "Current room temperature setpoint on CH2 (informational)",
        "unit_of_measurement": UNIT_CELSIUS,
        "step": 0.1,
        "message": "TrSetCH2",
        "keep_updated": True,
        "message_data": "f88",
        "range": (-40, 127),
    }),
    "t_room": InputSchema({
        "description": "Current sensed room temperature (informational)",
        "unit_of_measurement": UNIT_CELSIUS,
        "step": 0.1,
        "message": "Tr",
        "keep_updated": True,
        "message_data": "f88",
        "range": (-40, 127),
    }),
    "max_rel_mod_level": InputSchema({
        "description": "Maximum relative modulation level",
        "unit_of_measurement": UNIT_PERCENT,
        "step": 0.1,
        "icon": "mdi:percent",
        "message": "MaxRelModLevelSetting",
        "keep_updated": True,
        "message_data": "f88",
        "range": (0, 127),
        "auto_min_value": { "message": "MaxCapacityMinModLevel", "message_data": "u8_lb" },
    }),
})
