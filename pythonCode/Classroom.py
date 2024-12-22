class Classroom:
    def __init__(self, classroom_name, capacity):
        self._classroom_name = classroom_name
        self._capacity = capacity

    @staticmethod
    def from_dict(data):
        return Classroom(data["_classroom_name"], int(data["_capacity"]))

    def get_classroom_name(self):
        return self._classroom_name

    def get_capacity(self):
        return self._capacity