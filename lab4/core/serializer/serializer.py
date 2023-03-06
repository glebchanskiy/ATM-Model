from lab4.core.serializer.json_engine import JsonEngine
from lab4.core.serializer.yaml_engine import YamlEngine
import os

class Serializer:
    _engine = None

    def __init__(self) -> None:
        path_json = os.path.realpath(os.path.dirname(__file__)) + '/state.json'
        path_yaml = os.path.realpath(os.path.dirname(__file__)) + '/state.yaml'
        # self._engine = JsonEngine(path_json)
        self._engine = YamlEngine(path_yaml)
    
    def serialize(self, data: dict):
        self._engine.dump(data)
       
    def deserialize(self):
        return self._engine.load()