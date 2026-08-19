"""Helpers for Ecovacs mower area parameters."""

from typing import Final

MOW_HEIGHT_MIN: Final = 3.0
MOW_HEIGHT_MAX: Final = 8.0
MOW_HEIGHT_STEP: Final = 0.5

CUT_MODE_GENTLE: Final = "gentle 0,35m/s"
CUT_MODE_EFFICIENT: Final = "efficient 0,5m/s"

CUT_MODE_TO_OPTION: Final = {
    7: CUT_MODE_GENTLE,
    4: CUT_MODE_EFFICIENT,
}

OPTION_TO_CUT_MODE: Final = {
    option: cut_mode for cut_mode, option in CUT_MODE_TO_OPTION.items()
}

OBSTACLE_MODE_SHORT_GRASS: Final = "short_grass <10cm"
OBSTACLE_MODE_NORMAL: Final = "normal <15cm"
OBSTACLE_MODE_HIGH_GRASS: Final = "high_grass <20cm"

OBSTACLE_HEIGHT_TO_OPTION: Final = {
    1: OBSTACLE_MODE_SHORT_GRASS,
    2: OBSTACLE_MODE_NORMAL,
    3: OBSTACLE_MODE_HIGH_GRASS,
}

OPTION_TO_OBSTACLE_HEIGHT: Final = {
    option: obstacle_height
    for obstacle_height, option in OBSTACLE_HEIGHT_TO_OPTION.items()
}


def mow_height_level_to_cm(level: int) -> float:
    """Convert an Ecovacs mowing height level to centimeters."""
    return (17 - level) / 2


def mow_height_cm_to_level(height: float) -> int:
    """Convert mowing height in centimeters to an Ecovacs level."""
    return int(17 - height * 2)


def area_angle_to_degrees(angle: int) -> int:
    """Convert an Ecovacs area angle to the angle shown to the user."""
    return (270 - angle) % 360


def degrees_to_area_angle(angle: int) -> int:
    """Convert a user-facing mowing angle to the Ecovacs representation."""
    return (270 - angle) % 360
