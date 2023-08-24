class Process:
    def __init__(self, duration: int):
        self.duration = duration
        
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, value: int):
        if type(value) != int:
            raise TypeError(f"process duration should be an integer. Got {type(value)} instead.")
        
        self._duration = value
        
    