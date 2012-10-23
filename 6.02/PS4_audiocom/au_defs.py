import pyaudio

# Link configuration
FORMAT = pyaudio.paFloat32
CHANNELS = 1
SAMPLES_PER_SECOND = 8000
AMPLITUDE = 0.5
DC = 0.5
#DC=0

PREAMBLE_BITS = 32
PREAMBLE_BIT_LEN = 256
SECOND_CARRIER_LEN = 1024
CARRIER_CYCLES_PER_SECOND = 2000