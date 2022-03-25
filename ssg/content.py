import re
from collections.abc import Mapping

from yaml import FullLoader, load

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(self, cls, string):
        _, fm, content = self.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)
    
    def __init__(self, metadata, content) -> None:
        self.data = metadata
        self.data["content"] = content
    
    