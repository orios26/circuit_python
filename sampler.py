import audioio
import touchio
import board
import time
import neopixel

from digitalio import DigitalInOut, Direction

#define pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)

#creat audiofile list and define tempo
audiofiles = ['bd_tek.wav', 'elec_hi_snare.wav', 'elec_symbal.wav', 'bd_zome.wav', 'elec_blip.wav', 'bass_hit_c.wav', 'drum_cowbell.wav']
bpm = 120

#enables speakers
speaker_enable = DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = Direction.OUTPUT
speaker_enable.value = True

#create the touchpads
capPins = (board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.A7)
touchPad = []

for p in range(7):
    touchPad.append(touchio.TouchIn(capPins[p]))

a = audioio.AudioOut(board.A0)

#creating play function
def play_file(filename):
    filepath = './808_samples/' + filename
    f = open(filepath, 'rb')
    wave = audioio.WaveFile(f)
    a.play(wave)
    time.sleep(bpm/960)



while True:
    for i in range(7):
        if touchPad[i].value:
            play_file(audiofiles[i])
            pixels[i] = (0 , 255, 0)
            time.sleep(0.001)
            pixels[i] =(0,0,0)