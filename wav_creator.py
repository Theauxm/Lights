import math
import numpy as np

class SineOscillator:

    def __init__(self, freq, amp):
        self.freq = freq
        self.amp = amp
        self.sample_rate = 44100
        self.angle = 0
        self.offset = 2 * math.pi * self.freq / self.sample_rate

    def process(self):
        """
        amp * sin( 2 * pi * freq / sample_rate )
        """

        eq = self.amp * math.sin(self.angle)
        self.angle += self.offset
        return eq

def main():
    sec = 10
    sineosc = SineOscillator(440, 0.5)

    with open('sin_wave.txt', 'a') as f:
        for i in range(sineosc.sample_rate * sec):
            sample = sineosc.process() * 32767
            sample = np.int16(sample)
            f.write(str(sample) + '\n')
	

if __name__ == "__main__":
	main()
