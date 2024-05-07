import numpy as np
import pyaudio

# Choose your desired frequency
frequency = 0  # Hz

# Create a time array from 0..1 sampled at 0.05 ms (ie. 44100 kHz)
t = np.linspace(0, 1, int(1 * 44100), False)

# Generate a 20,000 Hz sine wave
note = np.sin(frequency * t * 2 * np.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)

# Start PyAudio and request
p = pyaudio.PyAudio()

# Open a Stream with the required parameters
stream = p.open(format=p.get_format_from_width(audio.dtype.itemsize),
                channels=1,
                rate=44100,
                output=True)

# Play the audio indefinitely
while True:
    stream.write(audio.tobytes())

# Close the stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
