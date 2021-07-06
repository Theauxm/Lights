import math

class SineOscillator:

    def __init__(self, freq, amp):
        self.freq = freq
        self.amp = amp
        self.sample_rate = 44100
        self.angle = 0
        self.offset = 2 * math.pi * self.freq / self.sample_rate

    def process(self):
        """
        amp * sin( 2 * pi * freq / sample_rate ) + amp
        """

        eq = self.amp * math.sin(self.angle) + self.amp
        self.angle += self.offset
        return eq