import os
import pytest
import numpy as np
from ligotools import readligo as rl 
from scipy import signal
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



def test_reading_hdf5_L1():
    filename = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain
    assert len(strain) != 0

    
    
def test_reading_hdf5_H1():
    filename = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)
    
    assert len(shortnameList) != 0
    

time = time_H1
dt = time[1] - time[0]

def test_loaddata_H1():
   
    assert len(time_H1) == 131072

    
def test_loaddata_L1():
    
    assert len(strain_L1) == 131072
    
def test_reading_hdf5_L1():
    filename = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)

    assert len(strain) != 0
    assert len(shortnameList) != 0

    
    





    
   