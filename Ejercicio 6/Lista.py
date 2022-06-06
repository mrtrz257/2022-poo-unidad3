from zope.interface import implementer

from Nodo import Nodo
from Interfaces import Interfaces
from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa

@implementer(Interfaces)

class Manejador:
    __comienzo = None
    def __init__(self):
        self.__comienzo = None
