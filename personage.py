import abc 
from enum import Enum
import math


class Personage(abc.ABC):
    @abc.abstractmethod
    def __init__(self, nom  ): 
        self.nom = nom
        self.point_de_vie = 100
        self.position =  Position(0,2)
        self.niveau = Utilitaires.TEST


    def attaquer(self, personnage):

















class Utilitaires(Enum):
    DEBUTANT =1 
    INTERMEDIAIRE =2
    EXPERT =3



class Position: 
    def __init__(self, m_x , m_y):
        self._m_x = m_x
        self._m_y = m_y
    @property()
    def get_x(self):
        return self._m_x
    @property()
    def get_y(self):
        return self._m_y
    
    def set_x(self, m_x):
        self._m_x = m_x
    
    def set_y(self, m_y):
        self._m_y = m_y

    def set_xy(self, m_x, m_y):
        self._m_x = m_x
        self._m_y = m_y
  

    def distance(self , position):
        math.sqrt(self._m_x-position.get_y**2 + self._m_y - position.get_x**2)

    def is_PositionCorrect(self):
        return position.get_x = 1 


class Direction(Enum):
    NORD =1
    SUD =2 
    EST =3
    OUEST =4




    def testDistance(): 
        position1 = Mock()
        position.x = 1 
        assert is_PositionCorrect(position1)

