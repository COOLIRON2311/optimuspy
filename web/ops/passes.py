import subprocess as sp
from enum import Enum
from pathlib import Path

from django.conf import settings


class Pass():
    '''Проход без аргументов. Не делает оптимизаций.'''
    _args: str = ''
    _c_files: list[Path]

    def __init__(self, c_files: list[Path]) -> None:
        self._c_files = c_files

    @property
    def args(self):
        return self._args

    def run(self) -> int:
        code = 0
        for file in self._c_files:
            print(f"{settings.OPSC_PATH}/opsc {self._args} {file} -o {file}")
            with sp.Popen(f"{settings.OPSC_PATH}/opsc {self._args} {file} -o {file}") as p:
                code = max(code, p.wait())
        return code


class OMPPath(Pass):
    '''Проход с бэкендом OpenMP'''
    _args = '-backend=openmp'


class Passes(Enum):
    NoOptPass = 0
    OMPPath = 1

    @staticmethod
    def get(ind: int, default=None) -> Pass:
        match ind:
            case 0:
                return Pass
            case 1:
                return OMPPath
        return default

    def __str__(self) -> str:
        match self:
            case Passes.NoOptPass:
                return 'Без оптимизации'
            case Passes.OMPPath:
                return 'OpenMP backend'
        return super().__str__()
