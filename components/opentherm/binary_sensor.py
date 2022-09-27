import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID

from components.opentherm.schema import OPENTHERM_BINARY_SENSORS, BinarySensorSchema
from components.opentherm.validate import create_validation_schema
from . import CONF_OPENTHERM_ID, OpenthermHub, cg_write_component_defines, cg_write_required_messages

DEPENDENCIES = [ 'opentherm' ]

def get_entity_validation_schema(entity: BinarySensorSchema) -> cv.Schema:
    return binary_sensor.binary_sensor_schema(
        device_class = entity["device_class"] if "device_class" in entity else cv._UNDEF,
        icon = entity["icon"] if "icon" in entity else cv._UNDEF
    )

CONFIG_SCHEMA = \
    cv.Schema({ cv.GenerateID(CONF_OPENTHERM_ID): cv.use_id(OpenthermHub) }) \
        .extend(create_validation_schema(OPENTHERM_BINARY_SENSORS, get_entity_validation_schema)) \
        .extend(cv.COMPONENT_SCHEMA)

def required_messages(sensor_keys):
    messages = set()
    for key in sensor_keys:
        match key:
            case "fault_indication" | "ch_active" | "dhw_active" | "flame_on" | "cooling_active" | "ch2_active" | "diagnostic_indication":
                messages.add((True, "Status"))
            case "dhw_present" | "control_type_on_off" | "cooling_supported" | "dhw_storage_tank" | "master_pump_control_allowed" | "ch2_present":
                messages.add((False, "SConfigSMemberIDcode"))
            case "dhw_setpoint_transfer_enabled" | "max_ch_setpoint_transfer_enabled" | "dhw_setpoint_rw" | "max_ch_setpoint_rw":
                messages.add((False, "RBPflags"))
    return messages

async def to_code(config):
    hub = await cg.get_variable(config[CONF_OPENTHERM_ID])

    sensor_keys = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf[CONF_ID]
        if id and id.type == binary_sensor.BinarySensor:
            sens = await binary_sensor.new_binary_sensor(conf)
            cg.add(getattr(hub, f"set_{key}_binary_sensor")(sens))
            sensor_keys.append(key)

    cg_write_required_messages(hub, required_messages(sensor_keys))
    cg_write_component_defines("BINARY_SENSOR", sensor_keys)