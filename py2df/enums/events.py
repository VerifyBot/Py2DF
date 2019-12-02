from .enum_util import AutoSnakeToPascalCaseNameEnum
from enum import auto, unique


@unique
class PlayerEventType(AutoSnakeToPascalCaseNameEnum):
    BREAK_BLOCK = auto()
    BREAK_ITEM = auto()
    CHANGE_SLOT = auto()
    CLICK_ENTITY = auto()
    CLICK_ITEM = auto()
    CLICK_OWN_INV = auto()
    CLICK_PLAYER = auto()
    CLOSE_INV = auto()
    COMMAND = auto()
    CONSUME = auto()
    DAMAGE_ENTITY = auto()
    DEATH = auto()
    DISMOUNT = auto()
    DROP_ITEM = auto()
    ENTITY_DMG_PLAYER = auto()
    FALL_DAMAGE = auto()
    JOIN = auto()
    JUMP = auto()
    KILL_MOB = auto()
    KILL_PLAYER = auto()
    LEFT_CLICK = auto()
    LOOP_EVENT = auto()
    MOB_KILL_PLAYER = auto()
    PICKUP_ITEM = auto()
    PLACE_BLOCK = auto()
    PLAYER_DMG_PLAYER = auto()
    PLAYER_TAKE_DMG = auto()
    PROJ_DMG_PLAYER = auto()
    PROJ_HIT = auto()
    QUIT = auto()
    RESPAWN = auto()
    RIGHT_CLICK = auto()
    RIPTIDE = auto()
    SHOOT_BOW = auto()
    SNEAK = auto()
    START_FLY = auto()
    START_SPRINT = auto()
    STOP_FLY = auto()
    STOP_SPRINT = auto()
    SWAP_HANDS = auto()
    UNSNEAK = auto()
    WALK = auto()


@unique
class EntityEventType(AutoSnakeToPascalCaseNameEnum):
    BLOCK_FALL = auto()
    ENTITY_DEATH = auto()
    ENTITY_DMG = auto()
    ENTITY_DMG_ENTITY = auto()
    ENTITY_KILL_ENTITY = auto()
    FALLING_BLOCK_LAND = auto()
    PROJ_DMG_ENTITY = auto()
    PROJ_KILL_ENTITY = auto()
    VEHICLE_DAMAGE = auto()
