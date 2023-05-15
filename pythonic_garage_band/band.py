class Musician():
    '''
    A base class for all musicians. It has an instance variable (name)
    and methods (__str__) and (__repr__). Subclasses should override (get_instrument)
    and (play_solo) methods.
    '''
    def __init__(self, name='Random Master'):
        self.name = name
        
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'
    


class Guitarist(Musician): 
    '''
    A subclass of (Musician) with a class method (get_instrument) which
    returns (guitar) and an instance method (play_solo) which returns a guitar solo.
    '''
    @classmethod
    def get_instrument(cls):
        return "guitar"
    
    def play_solo(cls):
        return "face melting guitar solo"


class Drummer(Musician):
    '''
    A subclass of (Musician) with a class method (get_instrument) which
    returns (drums) and an instance method (play_solo) which returns drum sounds.
    '''
    @classmethod
    def get_instrument(cls):
        return "drums"
    
    def play_solo(cls):
        return "rattle boom crash"


class Bassist(Musician):
    '''
    A subclass of (Musician) with a class method (get_instrument) which
    returns (bass) and an instance method (play_solo) which returns bass sounds.
    '''
    @classmethod
    def get_instrument(cls):
        return "bass"
    
    def play_solo(cls):
        return "bom bom buh bom"

class Band():
    '''
    A class to manage instances of (Musician) subclasses. It has instance
    variables (name) and (members), and methods (play_solos) to return a list of 
    solos played by all band members, and (to_list) to return a list of all (Band)
    instances created.
    '''
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



