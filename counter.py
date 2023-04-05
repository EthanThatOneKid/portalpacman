class Counter:
    """
    A simple counter class.
    """

    def __init__(self):
        self.count = 0

    def update(self):
        self.count += 1

    def get(self):
        return self.count

    def reset(self):
        self.count = 0
