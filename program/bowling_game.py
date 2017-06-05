class Game(object):

    global pins_knocked
    pins_knocked = 0


    def record_roll(self, num_pins_knocked):
        global pins_knocked
        pins_knocked += num_pins_knocked

    def get_score(self):
        return pins_knocked
