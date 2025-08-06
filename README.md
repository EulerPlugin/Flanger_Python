# Flanger_Python

<p align = "center">
<img width="597" height="379" alt="image" src="https://github.com/user-attachments/assets/03e20637-3647-4e19-935f-6307aa0e0798" />
</p>

- This project implements a digital flanger effect in Python, based on a variable delay line modulated by a low-frequency oscillator (LFO).
- A sine-wave LFO at 0.25 Hz modulates the delay time around a base delay of 10 milliseconds. 
- The implementation uses a circular buffer with linear interpolation to handle fractional delay values. 
- Both dry and wet signals are mixed equally at 0.5.

<br>
<br>

The purpose of this project is to verify the behavior of the flanger algorithm in an offline, non-realtime environment. 
It serves as a functional prototype to evaluate the effect’s sonic characteristics and modulation behavior before implementing it as a real-time audio plugin.

The next step is to port this logic into a __JUCE-based plugin, where the DSP code will be integrated into a proper plugin__ processor with realtime constraints and GUI-controllable parameters.
