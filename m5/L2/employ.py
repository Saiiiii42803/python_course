

class Employe:

    def __init__(self):
        print(f"contructor called")

    def __del__(self):
        print(f"destructor called")

emp = Employe()

