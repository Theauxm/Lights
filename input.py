import pyaudio, wave, config, time
import numpy as np

def stream():
    with open('hi.txt', 'a') as f:
        data = []

        p = pyaudio.PyAudio()
        frames_per_buffer = int(config.INPUT_RATE / config.FPS)
        stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=config.INPUT_RATE,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
        curr = time.gmtime()[4]
        while curr + 4 > time.gmtime()[4]:
            for x in stream.read(frames_per_buffer, exception_on_overflow=False):
                f.write(str(x) + '\n')

    stream.stop_stream()
    stream.close()
    p.terminate()

    return data


data = stream()
mini = 0
for i in data:
    x = list(np.frombuffer(i, dtype=np.int16))
    if mini < max(x):
        mini = max(x)

print(mini)
