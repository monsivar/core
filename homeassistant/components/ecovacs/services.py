"""Ecovacs services."""

import voluptuous as vol

from homeassistant.components.lawn_mower import DOMAIN as LAWN_MOWER_DOMAIN
from homeassistant.components.vacuum import DOMAIN as VACUUM_DOMAIN
from homeassistant.core import HomeAssistant, SupportsResponse, callback
from homeassistant.helpers import config_validation as cv, service

from .const import DOMAIN

SERVICE_RAW_GET_POSITIONS = "raw_get_positions"
SERVICE_SET_AREA_PARAMETER = "set_area_parameter"

ATTR_AREA_ID = "area_id"
ATTR_MOW_HEIGHT_LEVEL = "mow_height_level"
ATTR_CUT_MODE = "cut_mode"
ATTR_OBSTACLE_HEIGHT = "obstacle_height"
ATTR_ANGLE = "angle"


@callback
def async_setup_services(hass: HomeAssistant) -> None:
    """Set up services."""

    # Vacuum Services
    service.async_register_platform_entity_service(
        hass,
        DOMAIN,
        SERVICE_RAW_GET_POSITIONS,
        entity_domain=VACUUM_DOMAIN,
        schema=None,
        func="async_raw_get_positions",
        supports_response=SupportsResponse.ONLY,
    )

    # Lawn mower services
    service.async_register_platform_entity_service(
        hass,
        DOMAIN,
        SERVICE_SET_AREA_PARAMETER,
        entity_domain=LAWN_MOWER_DOMAIN,
        schema={
            vol.Required(ATTR_AREA_ID): cv.string,
            vol.Required(ATTR_MOW_HEIGHT_LEVEL): cv.positive_int,
            vol.Required(ATTR_CUT_MODE): cv.positive_int,
            vol.Required(ATTR_OBSTACLE_HEIGHT): cv.positive_int,
            vol.Required(ATTR_ANGLE): cv.positive_int,
        },
        func="async_set_area_parameter",
    )
