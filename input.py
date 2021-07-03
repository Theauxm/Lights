import pyaudio, wave, config, time
import numpy as np

def stream():
    data = []

    p = pyaudio.PyAudio()
    frames_per_buffer = int(config.INPUT_RATE / config.FPS)
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=config.INPUT_RATE,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
    for i in range(10):
        data.append(stream.read(frames_per_buffer, exception_on_overflow=False))

    stream.stop_stream()
    stream.close()
    p.terminate()

    return data


data = stream()
for i in data:
    print(np.fromstring(i, 'Float32'))
