from Objects import Trigger
import pygame
from pygame.locals import *

def get_room(x):
    return {
        0: [[[1, Trigger("GotoRoom", pygame.Rect(0,0,0,0), {"placeWhere": "DoorUp", "gotoWhere": "DoorDownEntrance", "leadsToRoom": 1})]
                ,[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, "L", "DoorUp", 0],[2, "DoorUp", 0],[2, "DoorUp", 0], [1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, "DoorUp", 0],[2, "DoorUp", 0],[2, "DoorUp", 0],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "DoorUpEntrance"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0, "Stalker"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2, "L", 0],[2, 0]],
            [[1],[1],[0],[0],[0],[0],[0],[0, "Player"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2, 0],[2, 0]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[2, 0],[2, 0]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[1, "Corner"],[1],[1],[1],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[2, 0],[2, 0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[2, 0],[2, 0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[2, 0],[2, 0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "Stalker"],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "Stalker"],[0, "Stalker"],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "DoorDownEntrance"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]],

        1: [[[1, Trigger("GotoRoom", pygame.Rect(0,0,0,0), {"placeWhere": "DoorDown", "gotoWhere": "DoorUpEntrance", "leadsToRoom": 0}), Trigger("GotoRoom", pygame.Rect(0,0,0,0), {"placeWhere": "DoorLeft", "gotoWhere": "DoorRightEntrance", "leadsToRoom": 2})]
                ,[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, "L", "DoorUp", 0],[2, "DoorUp", 0],[2, "DoorUp", 0], [1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, "DoorUp", 0],[2, "DoorUp", 0],[2, "DoorUp", 0],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "DoorUpEntrance"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0, "Stalker"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2, "L", 0],[2, 0]],
            [[1],[1],[0],[0],[0],[0],[0],[0, "Player"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2, 0],[2, 0]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2, 0],[2, 0]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[2, "DoorLeft"],[2,"DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[2, "DoorLeft"],[2,"DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[2, "DoorLeft"],[2,"DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "Stalker"],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "Stalker"],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "DoorDownEntrance"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]],


        2: [[[1, Trigger("GotoRoom", pygame.Rect(0,0,0,0), {"placeWhere": "DoorLeft", "gotoWhere": "DoorRightEntrance", "leadsToRoom": 3})]
                ,[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, "L", "DoorUp", 0],[2, "DoorUp", 0],[2, "DoorUp", 0], [1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, "DoorUp", 0],[2, "DoorUp", 0],[2, "DoorUp", 0],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "DoorUpEntrance"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0, "Stalker"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0, "Player"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[2, "DoorLeft"],[2,"DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2, "DoorRight"],[2, "DoorRight"]],
            [[2, "DoorLeft"],[2,"DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "DoorRightEntrance"],[2, "DoorRight"],[2, "DoorRight"]],
            [[2, "DoorLeft"],[2,"DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2, "DoorRight"],[2, "DoorRight"]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "Stalker"],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "Stalker"],[0],[0],[1],[1]],
            [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "DoorDownEntrance"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
            [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[2, 0, "DoorDown"],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]],


        3:  [[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
             [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
             [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[2, 0, "DoorLeft"],[2, 0, "DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0, "Player"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[2, 0, "DoorLeft"],[2, 0, "DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[2, 0, "DoorLeft"],[2, 0, "DoorLeft"],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]],
             [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
             [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]],


    }[x]