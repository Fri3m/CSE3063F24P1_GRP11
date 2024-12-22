class Classroom:
    def _init_(self, classroom_name, capacity):
        self._classroom_name = classroom_name
        self._capacity = capacity

    def get_classroom_name(self):
        return self._classroom_name

    def get_capacity(self):
        return self._capacity