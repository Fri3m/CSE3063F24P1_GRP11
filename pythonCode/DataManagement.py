import json


class DataManagement:

    def saveToJson(self, obj, obj_type):
        match obj_type:
            case "Course":
                self.__saveToJson(obj, f"{obj_type}/{obj.getCourseCode()}.json")

    def __saveToJson(self, obj, file_path_and_name):
        pass

    def loadFromJson(self, name, obj_type):
        pass
