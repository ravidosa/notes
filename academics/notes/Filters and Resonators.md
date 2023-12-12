### Resonance
speech relies on changing timbre (spectral envelope)
	done using resonators in vocal tracts
resonators
	prefer to vibrate at resonance frequencies
	amplify frequency components near resonant frequencies
	vocal tract, instruments
	resonance
		frequency based on stiffness, mass of material
		model as mass on spring
		heavy compliant = low frequency, light rigid = high frequency
		damping: loss of energy over time
			low friction = low damping, high friction = high damping, less periodic vibration
			Q factor
		complex have multiple resonant frequencies
		characteristic resonance
	vocal tract
		tube of air
		pressure waves between mouth and larynx
		standing waves
		resonant frequencies determined by tube length
			longer tube, lower resonance
		resonate at integer multiples of resonant frequencies
### Acoustic Filters
see [AC Circuit Analysis](AC%20Circuit%20Analysis.md), [Filter Theory](Filter%20Theory.md)
filter: removes components of signal
	acoustic filter: alter relative frequency component of sound (spectral envelope)
	physical structures with cavities
		pushing buttons on saxophone changes pitch, timbre
		changing vocal tract configuration produces different speech sounds
	linear filters: change amplitude but not frequency
		no new frequencies can be added/existing frequencies erased
		most real filters
		represented using only addition/subtraction/multiplication
		filter frequency response: how much frequency attenuated
			low pass, high pass, band pass
		output sum of input and filter
		instruments are band pass, narrow pass bands at precise frequencies
			center affects pitch, shape affects timbre
		resonators are band pass, power decreases away from resonance frequency
			frequency response,  spectral envelope dependent on shape
			uniform scaling
				spectrum shape preserved, scaling dependent on resonator length
				sounds like difference in size
	nonlinear filters: frequencies interact, new frequencies possible
		distorted signal
### Source-Filter Theory
source is input sound, filter shapes sound
vocal tract is filter
source determines periodicity and pitch, filter determines timbre
filter operations
	input sound spectrum + filter frequency response = output sound spectrum
speech sources
	voicing: periodic source
	noise: aperiodic source
	transients: aperiodic source
glottal waveform
	not sinusoidal
	many high energy harmonics, give voices sounds timbre
filtered noise, transients follow filter frequency response
source/filter independence
	filter frequency response changes spectral envelope/timbre, pitch unchanged
	fundamental frequency changes pitch/harmonics, spectral envelope unchanged