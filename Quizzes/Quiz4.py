class Beam:

 

    def __init__(self, height, web_t, flange_w, flange_t, length, lbs_ft):

        self.height = height

        self.web_t = web_t

        self.flange_w = flange_w

        self.flange_t = flange_t

        self.length = length

        self.lbs_ft = lbs_ft

    def total_weight(self):

        return self.lbs_ft * 10

    def box_area(self):

        return self.height * self.flange_w

    def area(self):

        return self.box_area() - (2*(self.height - (2*self.flange_t)) * ((self.flange_w - self.web_t)/2))

w12x35 = Beam(12.50, 0.300, 6.56, 0.52, 10, 35)
print(w12x35)