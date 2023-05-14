class Musician(): 
    def __init__(self, name='Random Master'):
        self.name = name
        
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'
    


class Guitarist(Musician): 
    @classmethod
    def get_instrument(cls):
        return "guitar"
    
    def play_solo(cls):
        return "face melting guitar solo"


class Drummer(Musician): 
    @classmethod
    def get_instrument(cls):
        return "drums"
    
    def play_solo(cls):
        return "rattle boom crash"


class Bassist(Musician): 
    @classmethod
    def get_instrument(cls):
        return "bass"
    
    def play_solo(cls):
        return "bom bom buh bom"

class Band(): 
    def __init__(self,name ,members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
    
    @classmethod
    def to_list(cls):
        return cls.instances

if __name__ == '__main__':
    joan = Guitarist("Joan Jett")
    sheila = Drummer("Sheila E.")
    meshell = Bassist("Meshell Ndegeocello")
    nirvana = Band("Nirvana", [])
    jimi = Guitarist("Jimi Hendrix")



