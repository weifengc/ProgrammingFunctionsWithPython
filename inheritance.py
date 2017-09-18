class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print self.last_name
        print self.eye_color




class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys

    def show_info(self):
        Parent.show_info(self)
        print self.num_of_toys

dad = Parent("Cui", "Black")
child = Child("Cui","Black", 12)

dad.show_info()
child.show_info()
