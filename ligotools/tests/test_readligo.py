import os
import pytest
import numpy as np
from ligotools import readligo as rl 
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json

eventname = ''
eventname = 'GW150914' 
fnjson = "BBH_events_v3.json"
events = json.load(open("data/" + fnjson,"r"))

event = events[eventname]
fn_H1 = event['fn_H1']              # File name for H1 data
fn_L1 = event['fn_L1']              # File name for L1 data
fn_template = event['fn_template']  # File name for template waveform
fs = event['fs']                    # Set sampling rate
tevent = event['tevent']            # Set approximate event GPS time
fband = event['fband']

strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/" + fn_H1, 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata("data/" + fn_L1, 'L1')


#time = time_H1

def test_len_time_h1():
    assert len(time_H1) == 131072





    
   