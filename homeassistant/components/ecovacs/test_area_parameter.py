"""Tests for Ecovacs mower area parameter helpers."""

import pytest

from homeassistant.components.ecovacs.area_parameter import (
    CUT_MODE_EFFICIENT,
    CUT_MODE_GENTLE,
    CUT_MODE_TO_OPTION,
    OBSTACLE_HEIGHT_TO_OPTION,
    OBSTACLE_MODE_HIGH_GRASS,
    OBSTACLE_MODE_NORMAL,
    OBSTACLE_MODE_SHORT_GRASS,
    OPTION_TO_CUT_MODE,
    OPTION_TO_OBSTACLE_HEIGHT,
    area_angle_to_degrees,
    degrees_to_area_angle,
    mow_height_cm_to_level,
    mow_height_level_to_cm,
)


@pytest.mark.parametrize(
    ("level", "height"),
    [
        (11, 3.0),
        (10, 3.5),
        (9, 4.0),
        (8, 4.5),
        (7, 5.0),
        (6, 5.5),
        (5, 6.0),
        (4, 6.5),
        (3, 7.0),
        (2, 7.5),
        (1, 8.0),
    ],
)
def test_mow_height_conversion(level: int, height: float) -> None:
    """Test conversion between mowing height level and centimeters."""
    assert mow_height_level_to_cm(level) == height
    assert mow_height_cm_to_level(height) == level


@pytest.mark.parametrize(
    ("raw_angle", "degrees"),
    [
        (180, 90),
        (145, 125),
        (216, 54),
        (0, 270),
    ],
)
def test_area_angle_conversion(raw_angle: int, degrees: int) -> None:
    """Test conversion between raw and user-facing mowing angles."""
    assert area_angle_to_degrees(raw_angle) == degrees
    assert degrees_to_area_angle(degrees) == raw_angle


def test_cut_mode_mapping() -> None:
    """Test cutting mode mapping."""
    assert CUT_MODE_TO_OPTION == {
        7: CUT_MODE_GENTLE,
        4: CUT_MODE_EFFICIENT,
    }
    assert OPTION_TO_CUT_MODE == {
        CUT_MODE_GENTLE: 7,
        CUT_MODE_EFFICIENT: 4,
    }


def test_obstacle_height_mapping() -> None:
    """Test obstacle height mapping."""
    assert OBSTACLE_HEIGHT_TO_OPTION == {
        1: OBSTACLE_MODE_SHORT_GRASS,
        2: OBSTACLE_MODE_NORMAL,
        3: OBSTACLE_MODE_HIGH_GRASS,
    }
    assert OPTION_TO_OBSTACLE_HEIGHT == {
        OBSTACLE_MODE_SHORT_GRASS: 1,
        OBSTACLE_MODE_NORMAL: 2,
        OBSTACLE_MODE_HIGH_GRASS: 3,
    }
