from abc import ABC, abstractmethod
class Royal_Enfield(ABC):
    @abstractmethod
    def cc(self):
        pass
    def gears(self):
        print('6 gears')
class Model1(Royal_Enfield):
    def cc(self):
        print('350 cc_engine')
class Model2(Royal_Enfield):
    def cc(self):
        print('450 cc_engine')
class Model3(Royal_Enfield):
    def cc(self):
        print('650 cc_engine')
user1 = Model3()
user1.gears()
user1.cc()
user2 = Model1()
user2.cc()
user2.gears()
