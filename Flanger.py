import LinearInterpolation_CB as LI
import numpy as np

class Flanger:
    def __init__(self, sample_rate, max_delay_ms):
        self._sample_rate = sample_rate
        self._max_delay_sample = (max_delay_ms / 1000.0) * sample_rate

        self._buffer = LI.CircularBuffer(int(self._max_delay_sample))
        self._lfo_phase = 0.0
        self._lfo_rate_hz = 0.25
        self._lfo_phase_inc = (2 * np.pi * self._lfo_rate_hz / self._sample_rate)

        self._base_delay = 0.010 * sample_rate
        self._base_depth = 0.005 * sample_rate

        self._wet = 0.5
        self._dry = 0.5

    
    def process(self, x):

        y = np.zeros_like(x)
        for n in range(len(x)):
            sin = np.sin(self._lfo_phase)
            self._lfo_phase += self._lfo_phase_inc
            M_n = self._base_delay + sin * self._base_depth

            self._buffer.write_sample(x[n])
            y[n] = x[n] * self._dry + self._buffer.read_sample(M_n) * self._wet
        return y




            


