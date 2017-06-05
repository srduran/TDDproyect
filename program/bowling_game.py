class Game(object):

    def __init__(self):
        self.pins_knocked = 0
        self.strike_score = 0
        self.strike_active = False
        self.strike_sum_number = 0

    def record_roll(self, num_pins_knocked):
        if num_pins_knocked == 10:
            self.strike_active = True
        if self.strike_active == True:
            self.strike_score += num_pins_knocked
            print self.strike_score
            self.strike_sum_number += 1
            if self.strike_sum_number == 3:
                print "este es el 97?"
                print "pins_knocked", self.pins_knocked
                self.pins_knocked += self.strike_score
                print self.pins_knocked
                self.strike_active = False
                self.strike_score = 0
                self.strike_sum_number = 0
        else:
            print 'otros numeros'
            self.pins_knocked += num_pins_knocked

    def get_score(self):
        return self.pins_knocked
