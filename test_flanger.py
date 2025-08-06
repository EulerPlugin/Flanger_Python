import Flanger as Fl
import numpy as np
import sounddevice as sd
import soundfile as sf

fs = 48000
duration = 3.0 

t = np.linspace(0, duration, int(fs * duration), endpoint=False)

x = 0.5 * np.sin(2 * np.pi * 440 * t)

flanger = Fl.Flanger(fs, 20)
y = flanger.process(x)

sd.play(y, fs)
sd.wait()

sf.write("flanger_output.wav", y, fs)