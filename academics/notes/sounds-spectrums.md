# Sounds and Spectrums
## Sounds and Sinusoids
sound: disturbance in air pressure
	sound waves: pressure waves in human audible range (330 m/s)
waveforms: representation of pressure variation over time
sinusoids
	simplest sounds, pure tones
	oscillatory motion
	single frequency component, frequency not affected by linear filters
	properties
		amplitude: maximal/RMS displacement of air
			$I \propto a^2$, intensity and loudness
		frequency: speed of cycles
		starting phase
	sound propagation
		same power spread out over increasing area, $I = \frac{P}{A}$
			decibel: logarithmic scale of power, $+10 \to \times 10$
			large range of audible, nonlinear amplitude loudness relationship
## Spectral Analysis
fourier transform (see [Fourier Transforms and Convolutions](fourier-transforms-convolutions.md))
waveform: time-domain representation
	amplitude vs time
	frequency not directly represented
spectrum
	amplitude (sound pressure level, dB/Hz) vs frequency
	time not represented
	energy at single frequency = pure tone, sinusoid
## Spectrograms and Resolution
spectrogram: 3d representation of sound
	frequency vs time, amplitude represented by color/darkness
	windowing: looking at subsection of sound
		increasing window increases resolution,  component frequencies more distinguishable
		narrow frequency = high resolution,  wide frequency = low resolution