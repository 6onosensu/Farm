class Player:
    def __init__(self):
        self.money = 500
        self.farm_land = {
            1: {'is_planted': False,
                'crop_type': None, 'growth_stage': 0},
            2: {'is_planted': False,
                'crop_type': None, 'growth_stage': 0},
            3: {'is_planted': False,
                'crop_type': None, 'growth_stage': 0},
            4: {'is_planted': False,
                'crop_type': None, 'growth_stage': 0},
            5: {'is_planted': False,
                'crop_type': None, 'growth_stage': 0}
            }
        self.inventory = {
            'seeds': {'type': 'potato', 'quantity': 10},
            }

    def add_item(item):
        # self.inventory.update(item)
        pass

    def plant():
        pass

    def harvest():
        pass

    def buy():
        pass

    def sell():
        pass
