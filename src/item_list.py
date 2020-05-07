from item import Item
from item import Treasure
from item import LightSource

item_list = {
    'sword': Item('sword', 'a big scary blade'),
    'ring': Item('ring', 'one ring to rule them all'),
    'hammer': Item('hammer', "not quite mjolnir, but it'll do"),
    'gold': Treasure('gold', 'looks shiny', 10000),
    'diamond': Treasure('diamond', 'very nice cut', 1000),
    'torch': LightSource('torch', 'a beacon of light')
}