class demo_parent:
    def demo_parent_method(self):
        print("im from parent class")



class demo_child(demo_parent):
    def demo_parent_method(self):
        print("im from child class")


obj_child=demo_child()
obj_child.demo_parent_method()
