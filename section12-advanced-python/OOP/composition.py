from inheritance_intro import Decimal


class Leg:
    def __init__(self):
        self.length = 0

    def set_leg_length(self, length):
        self.length = length

    def __repr__(self):
        return "A leg {} inches long".format(Decimal(self.length, 2))


class Back:
    pass


class Chair:
    def __init__(self, num_legs):
        self.legs = [Leg() for leg in range(num_legs)]
        self.back = Back()

    def __repr__(self):
        return "I am a Chair with {} legs and one Back".format(len(self.legs))


c = Chair(4)
c.legs[0].set_leg_length(12)
print(c.legs[0])
