import pyaudio
import wave

CHUNK = 1024
SAMPLE_FORMAT = pyaudio.paInt16
channels = 2
fs = 44100
seconds = 1

port = pyaudio.PyAudio()

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)


for i in range(int(fs / chunk * seconds)):
    print(stream.read(chunk))


stream.stop_stream()
stream.close()
p.terminate()

print('Finished')
