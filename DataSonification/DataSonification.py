from PIL import Image
import numpy as np
import scipy.signal as signal
import soundfile as sf

# Load image
image_path = 'C:/Users/ADMIN/OneDrive/Desktop/Programs/DataSonification/helix-hst-3240x3240_print.jpg'
image = Image.open(image_path).convert('L')  # Convert to grayscale
image_data = np.array(image)

# Normalize image data to range 0-1
normalized_image_data = image_data / 255.0

# Reshape image data to 1D array
flat_image_data = normalized_image_data.flatten()

# Define audio parameters
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration of audio in seconds

# Apply exponential mapping to emphasize differences
audio_signal = np.exp(flat_image_data * 5)

# Resample to desired duration
audio_signal = signal.resample(audio_signal, int(sample_rate * duration))

# Save audio signal to file
output_file = 'output.wav'
sf.write(output_file, audio_signal, sample_rate)
