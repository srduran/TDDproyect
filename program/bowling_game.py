class Game(object):
    global pins_knocked, strike_score, strike_active, strike_sum_number
    pins_knocked = 0
    strike_score = 0
    strike_active = 'off'
    strike_sum_number = 0

    def record_roll(self, num_pins_knocked):
        global pins_knocked, strike_score, strike_active, strike_sum_number

        if num_pins_knocked == 10:
            strike_active = 'on'
        if strike_active == 'on':
            strike_score += num_pins_knocked
            print strike_score
            strike_sum_number += 1
            if strike_sum_number == 3:
                print "este es el 97?"
                print "pins_knocked", pins_knocked
                pins_knocked += strike_score
                print pins_knocked
                strike_active = 'off'
                strike_score = 0
                strike_sum_number = 0
        else:
            print 'otros numeros'
            pins_knocked += num_pins_knocked

    def get_score(self):
        return pins_knocked

