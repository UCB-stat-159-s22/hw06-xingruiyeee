import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import os
from os.path import exists
from os import remove

import h5py
import json

from ligotools import readligo as rl
from ligotools import utils as ut

eventname = ''
eventname = 'GW150914' 
fnjson = "BBH_events_v3.json"
events = json.load(open("data/" + fnjson,"r"))

event = events[eventname]
fn_H1 = event['fn_H1']              # File name for H1 data
fn_L1 = event['fn_L1']              # File name for L1 data
fn_template = event['fn_template']  # File name for template waveform
fs = event['fs']                    # Set sampling rate


strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/" + fn_H1, 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata("data/" + fn_L1, 'L1')

time = time_H1
dt = time[1] - time[0]

fs = 4096
nfft = 4*fs
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = nfft)
psd_H1 = interp1d(freqs, Pxx_H1)



def test_whiten():
    strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
    assert len(strain_H1_whiten) > 0
    

def test_write_wavfile_function():
    data = np.linspace(0,10,100)
    ut.write_wavfile("audio/temp.wav", 1, data)
    assert exists("audio/temp.wav")
    os.remove("audio/temp.wav")     
    
    
    
def test_reqshift_function():
    strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
    strain_H1_shifted = ut.reqshift(strain_H1_whiten,400.0, fs)
    assert len(strain_H1_shifted) == 131072


# def test_plotting_moved():
    
    
    
    