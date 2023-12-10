### Airstream Mechanics
airstream mechanics: make air move
	pulmonic egressive
		from lungs
		compressing lungs pushes out air
		inspiration active, expiration passive
	glottalic egressive (ejectives)
		from glottis to outside
		high pressure pocket in vocal tract, action at glottis
			closure in vocal tract
			glottic closes and raised, compressed air between glottis and closure
			anterior closure released results in rapid air flow, pop sound (release burst)
		place of articulation same as pulmonic consonant
	glottalic ingressive (implosives)
		from outside to glottis
		low pressure pocket in vocal tract, action at glottis
			closure in vocal tract
			glottis lowered, opened, voicing continues
			no increase in pressure, no release burst when constriction released
		place of articulation same as pulmonic consonant
	lingual/velaric egressive (clicks)
		from outside to oral cavity
		low pressure pocket in mouth, action at tongue
			one seal in front, one in back
			tongue pulling away creates low pressure pocket in mouth
			release of front seal results in rapid air flow, click sound
		place of articulation = seal location
### The Glottal Source
larynx
	group of cartilage, muscle, ligament that protects entry to trachea
	thyroid cartilage = front wall, cricoid cartilage = back wall
	arytenoids = cartilage pair attached to top of cricoid
	vocal folds attached to thyroid and arytenoids
		vibration
			process
				lung air pressure forces vocal folds open
				when air flows, no pressure
				vocal folds closed
			causes
				myoelastic effect
				bernoulli effect
				two-mass effect
		vocal fold tension determines rate of vibration, affects perceived voice pitch
		opening/closing done by arytenoids
		periodic wave/buzz at vocal folds source of voiced sounds
			periodically constricting airflow results in rhythmic changes in air pressure
glottal source waveform
	not sinusoidal, complex sound
	closing phase faster, sharp angles around open/close result in high frequency energy
	harmonic spacing determined by waveform repetition rate
		lowest harmonics most powerful (voice bar)
			very low frequency regular vertical lines at bottom of spectrogram
	spectrum rises due to formants
voiceless
	vocal folds held apart, free airflow
	no turbulence at vocal folds
whisper
	vocal folds approximated enough to restrict airflow
	turbulence at glottis
voicing
	repetitive open/closing of glottis
	buzzing at larynx
	modal
		periodic cycles, closed for approximately half of cycle
	breathy
		constant airflow through glottis
		opening in back/slight opening across glottis
		cycles regular, no completely-closed phase
		noisier glottal source
	creaky
		back of vocal folds pressed together
		front remains slack, vibrates at very low frequency
		cycles irregular, relatively long closed phase
### Quantifying Pitch and Periodicity
perfectness of repetition varies
prosody: f0 varying continuously
estimating f0 pitch and quantifying periodicity of glottal waveform
	digital acoustic analysis
		treat signal as function
		periodic if $f(x + nP) = f(x) + \varepsilon$ ($\varepsilon$ accounts for random error, less than perfect periodicity)
		best estimate of $P$ minimizes $\varepsilon$
	autocorrelation function
		most likely period, periodicity
		process
			copy signal
			shift copy back in time
			compute correlation of signal to copy
		lag with highest peak is most likely period, turned into f0
			need to specify region to look for peak
	automatic pitch tracking generally reliable with right settings, eyes and ears more reliably accurate (less precise)