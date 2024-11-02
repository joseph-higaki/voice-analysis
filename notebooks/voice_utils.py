import parselmouth
import numpy as np


def draw_spectrogram(plt, snd, dynamic_range=70):
    spectrogram = snd.to_spectrogram()
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")

def draw_intensity(plt, snd):
    intensity = snd.to_intensity()
    plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
    plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("intensity [dB]")

def draw_pitch(plt, snd):
    pitch = snd.to_pitch()
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN to not plot
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan    
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=1)    
    plt.ylim(0, np.nanmax(pitch_values))  
    plt.ylabel("fundamental frequency [Hz]")
    plt.xlabel("time [secs]")
    



