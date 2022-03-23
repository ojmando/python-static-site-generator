from os import mkdir, is_dir
from pathlib import Path


class Site:
    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        mkdir(path=directory, parents=True, exist_ok=True)

    def build(self):
        mkdir(path=self.dest, parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if is_dir(path):
                self.create_dir(path)
