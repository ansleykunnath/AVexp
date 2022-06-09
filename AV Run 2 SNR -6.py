#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on May 19, 2022, at 13:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastma2n E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# set speaker sound to three quarters of the way
# set all audio files to 1.0 volume, the SNR files to 0.47 (AV files have no volume)

from psychopy import locale_setup
from psychopy import prefs
from time import time
from time import sleep
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
#from win32com.client import Dispatch
import os  # handy system and path functions
import sys  # to get file system encoding
import random # useful to generate a random number in a loop
import psychopy.iohub as io
import socket
import json
from psychopy.hardware import keyboard
from psychopy.sound import Sound

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'AV Run 2'  # from the Builder filename that created this script
expInfo = {'participant': '001', 'session': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\home\\kernel\\Documents\\AV Run 2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Array with stimuli in the order they are presented. This array will be used to send the triggers to Kernel
stimuli_order = ['event_rest', 'event_written', 'event_rest', 'event_visual', 'event_rest', 'event_audio', 'event_rest', 'event_audiovisual', 'event_rest',
                             'event_written', 'event_rest', 'event_audio', 'event_rest', 'event_visual', 'event_rest', 'event_audiovisual', 'event_rest', 
                             'event_visual', 'event_rest', 'event_audio', 'event_rest', 'event_audiovisual', 'event_rest', 'event_written', 'event_rest',
                             'event_visual', 'event_rest', 'event_written', 'event_rest', 'event_audio', 'event_rest', 'event_audiovisual', 'event_rest',
                             'event_written', 'event_rest', 'event_audiovisual', 'event_rest', 'event_visual', 'event_rest', 'event_audio', 'event_rest']

timestamp = time()
data_to_send = {
    "id": 1,
    "timestamp": int(timestamp * 1e9),
    "event": 'start_experiment',
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='display_stimuli', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "SNR_Selection"
SNR_SelectionClock = core.Clock()
SNR_Response = visual.TextBox2(
     win, text='...', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='SNR_Response',
     autoLog=True,
)
text = visual.TextStim(win=win, name='text',
    text='Enter SNR (-7 to 15)\n\n\n\n\n\n\nPress enter to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
enter_call = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
InstructionsA = visual.TextStim(win=win, name='InstructionsA',
    text="Welcome to the experiment!\n\nYou will see and hear a woman saying words. Your job is to decide whether each word belongs in one of the following two categories:\n\n1- animals\n 2- action verbs     \n\nAfter each word, indicate your choice using the keypad. \n\n\nTry to answer as accurately as possible. If you're not sure, just make your best guess.\n\n\n(Press 3 to continue.)",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_instruction_A = keyboard.Keyboard()

# Initialize components for Routine "InstructionsB_3"
InstructionsB_3Clock = core.Clock()
end_instruction_B = keyboard.Keyboard()
InstructionsB = visual.TextStim(win=win, name='InstructionsB',
    text='\n\nTake a minute to familarize yourself with the words in this section.\n\nAnimals:\nBear, Bee, Bird, Bug, Calf, Cat, Crab, Dog, Duck, Fish, Frog, Goose, Hen, Horse, Moth, Mouse, Rat, Sheep, Snake, Toad\n\nAction verbs:\nCatch, Chat, Cheer, Cut, Fall, Fold, Guess, Knock, Look, Press, Read, Ride, Run, Take, Teach, Tell, Thank, Toss, Walk, Wish\n\n \n\n\n(Press 3 to continue.)',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "InstructionsC_2"
InstructionsC_2Clock = core.Clock()
end_instruction_c = keyboard.Keyboard()
InstructionsC = visual.TextStim(win=win, name='InstructionsC',
    text="\nSometimes the word will be written, spoken, audiovisual, or visual only where you'll have to try and lipread. Also, sometimes there will be background noise that will make it hard to hear. \n\n\nListen carefully, try to remain still, and look at the white circle in the middle of the screen between words.\n\n\n\n\n\n\n\n(Press 3 to continue.)",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "wait_time__1"
wait_time__1Clock = core.Clock()
one_last_thing = visual.TextStim(win=win, name='one_last_thing',
    text='One last thing:\n\n\n\n\n\nPlease wait until you see this screen...',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "sample_response"
sample_responseClock = core.Clock()
response_sample = visual.ImageStim(
    win=win,
    name='response_sample', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "wait_time_2"
wait_time_2Clock = core.Clock()
before_you_go = visual.TextStim(win=win, name='before_you_go',
    text='\n\n\n\n\n\n\n\n... to type your answer.\n\n\n\n\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "lipreading_trial"
lipreading_trialClock = core.Clock()
lipreading = visual.TextStim(win=win, name='lipreading',
    text="Now let's try a lipreading question for practice.\n\n\n\n\n\n\n(Press 3 to continue.)",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
lipreading_key = keyboard.Keyboard()

# Initialize components for Routine "goose_video"
goose_videoClock = core.Clock()
response_sample2 = visual.ImageStim(
    win=win,
    name='response_sample2', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
goose_visual = visual.MovieStim3(
    win=win, name='goose_visual', units='pix',
    noAudio = True,
    filename='/home/kernel/Documents/goose4_Vonly.avi',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    depth=-1.0,
    )
response = keyboard.Keyboard()

# Initialize components for Routine "correct_answer1"
correct_answer1Clock = core.Clock()
goose_correct = visual.TextStim(win=win, name='goose_correct',
    text='\nThat time, the woman said "goose," so the answer was 1 for animal.\n\n\nRemember that it\'s okay to guess!',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "let_s_get_started"
let_s_get_startedClock = core.Clock()
let_s_start = visual.TextStim(win=win, name='let_s_start',
    text='\n\n\n\n\n\n\n\n\nPlease wait.\n\n\n\n\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_start = keyboard.Keyboard()

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "written_stimulus"
written_stimulusClock = core.Clock()
start_of_w_stim = visual.TextStim(win=win, name='start_of_w_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
writ_response = keyboard.Keyboard()
response_prompt = visual.ImageStim(
    win=win,
    name='response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "first_V"
first_VClock = core.Clock()
first_v_response_prompt = visual.ImageStim(
    win=win,
    name='first_v_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
first_v_response = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "first_A"
first_AClock = core.Clock()
first_a_response_prompt = visual.ImageStim(
    win=win,
    name='first_a_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
first_a_response = keyboard.Keyboard()
first_a_stim = sound.Sound('A', secs=1.2, stereo=True, hamming=True,
    name='first_a_stim')
first_a_stim.setVolume(1.0)
black_screen_with_dot = visual.ImageStim(
    win=win,
    name='black_screen_with_dot', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sound_1 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(0.47)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "first_AV_2"
first_AV_2Clock = core.Clock()
first_AV_response = keyboard.Keyboard()
first_AV_response_prompt = visual.ImageStim(
    win=win,
    name='first_AV_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sound_1_AV = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_1_AV')
sound_1_AV.setVolume(0.47)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "second_written"
second_writtenClock = core.Clock()
second_writ_response = keyboard.Keyboard()
second_written_response_prompt = visual.ImageStim(
    win=win,
    name='second_written_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
second_w_stim = visual.TextStim(win=win, name='second_w_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "second_A"
second_AClock = core.Clock()
second_a_response = keyboard.Keyboard()
second_a_response_prompt = visual.ImageStim(
    win=win,
    name='second_a_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
black_screen_with_dot_2 = visual.ImageStim(
    win=win,
    name='black_screen_with_dot_2', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sound_2_a = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_2_a')
sound_2_a.setVolume(0.47)
second_a_stim = sound.Sound('A', secs=1.2, stereo=True, hamming=True,
    name='second_a_stim')
second_a_stim.setVolume(1.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "second_V"
second_VClock = core.Clock()
second_v_response_prompt = visual.ImageStim(
    win=win,
    name='second_v_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
second_v_response = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "second_AV"
second_AVClock = core.Clock()
second_AV_response = keyboard.Keyboard()
second_AV_response_prompt = visual.ImageStim(
    win=win,
    name='second_AV_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sound_2_av = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_2_av')
sound_2_av.setVolume(0.47)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "third_V"
third_VClock = core.Clock()
third_v_response = keyboard.Keyboard()
third_v_response_prompt = visual.ImageStim(
    win=win,
    name='third_v_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "third_A"
third_AClock = core.Clock()
third_a_stim = sound.Sound('A', secs=1.2, stereo=True, hamming=True,
    name='third_a_stim')
third_a_stim.setVolume(1.0)
third_a_repsonse_prompt = visual.ImageStim(
    win=win,
    name='third_a_repsonse_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
third_a_response = keyboard.Keyboard()
sound_3_a = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_3_a')
sound_3_a.setVolume(0.47)
black_screen_with_dot_3 = visual.ImageStim(
    win=win,
    name='black_screen_with_dot_3', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "third_AV"
third_AVClock = core.Clock()
third_AV_response_prompt = visual.ImageStim(
    win=win,
    name='third_AV_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
third_AV_response = keyboard.Keyboard()
sound_3_av = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_3_av')
sound_3_av.setVolume(0.47)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "third_written"
third_writtenClock = core.Clock()
third_writ_response = keyboard.Keyboard()
third_w_stim = visual.TextStim(win=win, name='third_w_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
third_response_prompt = visual.ImageStim(
    win=win,
    name='third_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fourth_V"
fourth_VClock = core.Clock()
fourth_v_response = keyboard.Keyboard()
fourth_v_response_prompt = visual.ImageStim(
    win=win,
    name='fourth_v_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fourth_written"
fourth_writtenClock = core.Clock()
fourth_writ_response = keyboard.Keyboard()
fourth_response_prompt = visual.ImageStim(
    win=win,
    name='fourth_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fourth_w_stim = visual.TextStim(win=win, name='fourth_w_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fourth_A"
fourth_AClock = core.Clock()
fourth_a_response_ = keyboard.Keyboard()
fourth_a_response_prompt = visual.ImageStim(
    win=win,
    name='fourth_a_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
black_screen_with_dot_4 = visual.ImageStim(
    win=win,
    name='black_screen_with_dot_4', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sound_4_a = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_4_a')
sound_4_a.setVolume(0.47)
fourth_a_stim = sound.Sound('A', secs=1.2, stereo=True, hamming=True,
    name='fourth_a_stim')
fourth_a_stim.setVolume(1.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fourth_AV_3"
fourth_AV_3Clock = core.Clock()
fourth_AV_response_prompt = visual.ImageStim(
    win=win,
    name='fourth_AV_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sound_4_av = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_4_av')
sound_4_av.setVolume(0.47)
fourth_AV_response = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fifth_written"
fifth_writtenClock = core.Clock()
fifth_response_prompt = visual.ImageStim(
    win=win,
    name='fifth_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fifth_writ_response = keyboard.Keyboard()
fifth_w_stim = visual.TextStim(win=win, name='fifth_w_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fifth_AV"
fifth_AVClock = core.Clock()
fifth_AV_response_prompt = visual.ImageStim(
    win=win,
    name='fifth_AV_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fifth_AV_response = keyboard.Keyboard()
sound_5_av = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_5_av')
sound_5_av.setVolume(0.47)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fifth_V"
fifth_VClock = core.Clock()
fifth_v_response_prompt = visual.ImageStim(
    win=win,
    name='fifth_v_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fifth_v_response = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation15sec"
fixation15secClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fifth_A"
fifth_AClock = core.Clock()
fifth_a_response = keyboard.Keyboard()
fifth_a_response_prompt = visual.ImageStim(
    win=win,
    name='fifth_a_response_prompt', units='cm', 
    image='/home/kernel/Downloads/fNIRS circle_and_text.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
black_screen_with_dot_5 = visual.ImageStim(
    win=win,
    name='black_screen_with_dot_5', units='cm', 
    image='/home/kernel/Downloads/fNIRS images_circle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(40,22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sound_5_a = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_5_a')
sound_5_a.setVolume(0.47)
fifth_a_stim = sound.Sound('A', secs=1.2, stereo=True, hamming=True,
    name='fifth_a_stim')
fifth_a_stim.setVolume(1.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "goodbye_"
goodbye_Clock = core.Clock()
the_end_txt = visual.TextStim(win=win, name='the_end_txt',
    text='\n\n\n\n\n\n\n\nThe end!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
goodbye_response = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "SNR_Selection"-------
continueRoutine = True
# update component parameters for each repeat
SNR_Response.reset()
enter_call.keys = []
enter_call.rt = []
_enter_call_allKeys = []
# keep track of which components have finished
SNR_SelectionComponents = [SNR_Response, text, enter_call]
for thisComponent in SNR_SelectionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SNR_SelectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SNR_Selection"-------
while continueRoutine:
    # get current time
    t = SNR_SelectionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SNR_SelectionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SNR_Response* updates
    if SNR_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SNR_Response.frameNStart = frameN  # exact frame index
        SNR_Response.tStart = t  # local t and not account for scr refresh
        SNR_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SNR_Response, 'tStartRefresh')  # time at next scr refresh
        SNR_Response.setAutoDraw(True)
    if SNR_Response.status == STARTED:
        if bool(enter_call.status==FINISHED):
            # keep track of stop time/frame for later
            SNR_Response.tStop = t  # not accounting for scr refresh
            SNR_Response.frameNStop = frameN  # exact frame index
            win.timeOnFlip(SNR_Response, 'tStopRefresh')  # time at next scr refresh
            SNR_Response.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        if bool(enter_call.status==FINISHED):
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *enter_call* updates
    waitOnFlip = False
    if enter_call.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_call.frameNStart = frameN  # exact frame index
        enter_call.tStart = t  # local t and not account for scr refresh
        enter_call.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_call, 'tStartRefresh')  # time at next scr refresh
        enter_call.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter_call.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter_call.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter_call.status == STARTED and not waitOnFlip:
        theseKeys = enter_call.getKeys(keyList=['return'], waitRelease=False)
        _enter_call_allKeys.extend(theseKeys)
        if len(_enter_call_allKeys):
            enter_call.keys = _enter_call_allKeys[-1].name  # just the last key pressed
            enter_call.rt = _enter_call_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SNR_SelectionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SNR_Selection"-------
for thisComponent in SNR_SelectionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SNR_Response.text',SNR_Response.text)
thisExp.addData('SNR_Response.started', SNR_Response.tStartRefresh)
thisExp.addData('SNR_Response.stopped', SNR_Response.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
real_var = SNR_Response.text
real_var = real_var.rstrip()

# Set volume parameters according to SNR

# check responses
if enter_call.keys in ['', [], None]:  # No response was made
    enter_call.keys = None
thisExp.addData('enter_call.keys',enter_call.keys)
if enter_call.keys != None:  # we had a response
    thisExp.addData('enter_call.rt', enter_call.rt)
thisExp.addData('enter_call.started', enter_call.tStartRefresh)
thisExp.addData('enter_call.stopped', enter_call.tStopRefresh)
thisExp.nextEntry()
# the Routine "SNR_Selection" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
end_instruction_A.keys = []
end_instruction_A.rt = []
_end_instruction_A_allKeys = []
# keep track of which components have finished
trialComponents = [InstructionsA, end_instruction_A]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsA* updates
    if InstructionsA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsA.frameNStart = frameN  # exact frame index
        InstructionsA.tStart = t  # local t and not account for scr refresh
        InstructionsA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsA, 'tStartRefresh')  # time at next scr refresh
        InstructionsA.setAutoDraw(True)
    if InstructionsA.status == STARTED:
        if bool(end_instruction_A.status==FINISHED):
            # keep track of stop time/frame for later
            InstructionsA.tStop = t  # not accounting for scr refresh
            InstructionsA.frameNStop = frameN  # exact frame index
            win.timeOnFlip(InstructionsA, 'tStopRefresh')  # time at next scr refresh
            InstructionsA.setAutoDraw(False)
    
    # *end_instruction_A* updates
    waitOnFlip = False
    if end_instruction_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_instruction_A.frameNStart = frameN  # exact frame index
        end_instruction_A.tStart = t  # local t and not account for scr refresh
        end_instruction_A.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_instruction_A, 'tStartRefresh')  # time at next scr refresh
        end_instruction_A.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_instruction_A.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_instruction_A.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_instruction_A.status == STARTED and not waitOnFlip:
        theseKeys = end_instruction_A.getKeys(keyList=['left','right','space','3','num_3'], waitRelease=False)
        _end_instruction_A_allKeys.extend(theseKeys)
        if len(_end_instruction_A_allKeys):
            end_instruction_A.keys = _end_instruction_A_allKeys[-1].name  # just the last key pressed
            end_instruction_A.rt = _end_instruction_A_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------kmoim
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionsA.started', InstructionsA.tStartRefresh)
thisExp.addData('InstructionsA.stopped', InstructionsA.tStopRefresh)
# check responses
if end_instruction_A.keys in ['', [], None]:  # No response was made
    end_instruction_A.keys = None
thisExp.addData('end_instruction_A.keys',end_instruction_A.keys)
if end_instruction_A.keys != None:  # we had a response
    thisExp.addData('end_instruction_A.rt', end_instruction_A.rt)
thisExp.addData('end_instruction_A.started', end_instruction_A.tStartRefresh)
thisExp.addData('end_instruction_A.stopped', end_instruction_A.tStopRefresh)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionsB_3"-------
continueRoutine = True
# update component parameters for each repeat
end_instruction_B.keys = []
end_instruction_B.rt = []
_end_instruction_B_allKeys = []
# keep track of which components have finished
InstructionsB_3Components = [end_instruction_B, InstructionsB]
for thisComponent in InstructionsB_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsB_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionsB_3"-------
while continueRoutine:
    # get current time
    t = InstructionsB_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsB_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_instruction_B* updates
    waitOnFlip = False
    if end_instruction_B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_instruction_B.frameNStart = frameN  # exact frame index
        end_instruction_B.tStart = t  # local t and not account for scr refresh
        end_instruction_B.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_instruction_B, 'tStartRefresh')  # time at next scr refresh
        end_instruction_B.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_instruction_B.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_instruction_B.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_instruction_B.status == STARTED and not waitOnFlip:
        theseKeys = end_instruction_B.getKeys(keyList=['left','right','space','1','2','3','num_3'], waitRelease=False)
        _end_instruction_B_allKeys.extend(theseKeys)
        if len(_end_instruction_B_allKeys):
            end_instruction_B.keys = _end_instruction_B_allKeys[-1].name  # just the last key pressed
            end_instruction_B.rt = _end_instruction_B_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *InstructionsB* updates
    if InstructionsB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsB.frameNStart = frameN  # exact frame index
        InstructionsB.tStart = t  # local t and not account for scr refresh
        InstructionsB.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsB, 'tStartRefresh')  # time at next scr refresh
        InstructionsB.setAutoDraw(True)
    if InstructionsB.status == STARTED:
        if bool(end_instruction_B.status==FINISHED):
            # keep track of stop time/frame for later
            InstructionsB.tStop = t  # not accounting for scr refresh
            InstructionsB.frameNStop = frameN  # exact frame index
            win.timeOnFlip(InstructionsB, 'tStopRefresh')  # time at next scr refresh
            InstructionsB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsB_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionsB_3"-------
for thisComponent in InstructionsB_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_instruction_B.keys in ['', [], None]:  # No response was made
    end_instruction_B.keys = None
thisExp.addData('end_instruction_B.keys',end_instruction_B.keys)
if end_instruction_B.keys != None:  # we had a response
    thisExp.addData('end_instruction_B.rt', end_instruction_B.rt)
thisExp.addData('end_instruction_B.started', end_instruction_B.tStartRefresh)
thisExp.addData('end_instruction_B.stopped', end_instruction_B.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('InstructionsB.started', InstructionsB.tStartRefresh)
thisExp.addData('InstructionsB.stopped', InstructionsB.tStopRefresh)
# the Routine "InstructionsB_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionsC_2"-------
continueRoutine = True
# update component parameters for each repeat
end_instruction_c.keys = []
end_instruction_c.rt = []
_end_instruction_c_allKeys = []
# keep track of which components have finished
InstructionsC_2Components = [end_instruction_c, InstructionsC]
for thisComponent in InstructionsC_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsC_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionsC_2"-------
while continueRoutine:
    # get current time
    t = InstructionsC_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsC_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_instruction_c* updates
    waitOnFlip = False
    if end_instruction_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_instruction_c.frameNStart = frameN  # exact frame index
        end_instruction_c.tStart = t  # local t and not account for scr refresh
        end_instruction_c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_instruction_c, 'tStartRefresh')  # time at next scr refresh
        end_instruction_c.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_instruction_c.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_instruction_c.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_instruction_c.status == STARTED and not waitOnFlip:
        theseKeys = end_instruction_c.getKeys(keyList=['left','right','space','3','num_3'], waitRelease=False)
        _end_instruction_c_allKeys.extend(theseKeys)
        if len(_end_instruction_c_allKeys):
            end_instruction_c.keys = _end_instruction_c_allKeys[-1].name  # just the last key pressed
            end_instruction_c.rt = _end_instruction_c_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *InstructionsC* updates
    if InstructionsC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsC.frameNStart = frameN  # exact frame index
        InstructionsC.tStart = t  # local t and not account for scr refresh
        InstructionsC.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsC, 'tStartRefresh')  # time at next scr refresh
        InstructionsC.setAutoDraw(True)
    if InstructionsC.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > InstructionsC.tStartRefresh + end_instruction_c.status==FINISHED-frameTolerance:
            # keep track of stop time/frame for later
            InstructionsC.tStop = t  # not accounting for scr refresh
            InstructionsC.frameNStop = frameN  # exact frame index
            win.timeOnFlip(InstructionsC, 'tStopRefresh')  # time at next scr refresh
            InstructionsC.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsC_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionsC_2"-------
for thisComponent in InstructionsC_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_instruction_c.keys in ['', [], None]:  # No response was made
    end_instruction_c.keys = None
thisExp.addData('end_instruction_c.keys',end_instruction_c.keys)
if end_instruction_c.keys != None:  # we had a response
    thisExp.addData('end_instruction_c.rt', end_instruction_c.rt)
thisExp.addData('end_instruction_c.started', end_instruction_c.tStartRefresh)
thisExp.addData('end_instruction_c.stopped', end_instruction_c.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('InstructionsC.started', InstructionsC.tStartRefresh)
thisExp.addData('InstructionsC.stopped', InstructionsC.tStopRefresh)
# the Routine "InstructionsC_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait_time__1"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
wait_time__1Components = [one_last_thing]
for thisComponent in wait_time__1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_time__1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wait_time__1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = wait_time__1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_time__1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_last_thing* updates
    if one_last_thing.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        one_last_thing.frameNStart = frameN  # exact frame index
        one_last_thing.tStart = t  # local t and not account for scr refresh
        one_last_thing.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_last_thing, 'tStartRefresh')  # time at next scr refresh
        one_last_thing.setAutoDraw(True)
    if one_last_thing.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > one_last_thing.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            one_last_thing.tStop = t  # not accounting for scr refresh
            one_last_thing.frameNStop = frameN  # exact frame index
            win.timeOnFlip(one_last_thing, 'tStopRefresh')  # time at next scr refresh
            one_last_thing.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_time__1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_time__1"-------
for thisComponent in wait_time__1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_last_thing.started', one_last_thing.tStartRefresh)
thisExp.addData('one_last_thing.stopped', one_last_thing.tStopRefresh)

# ------Prepare to start Routine "sample_response"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
sample_responseComponents = [response_sample]
for thisComponent in sample_responseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_response"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sample_responseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_responseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *response_sample* updates
    if response_sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response_sample.frameNStart = frameN  # exact frame index
        response_sample.tStart = t  # local t and not account for scr refresh
        response_sample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response_sample, 'tStartRefresh')  # time at next scr refresh
        response_sample.setAutoDraw(True)
    if response_sample.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > response_sample.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            response_sample.tStop = t  # not accounting for scr refresh
            response_sample.frameNStop = frameN  # exact frame index
            win.timeOnFlip(response_sample, 'tStopRefresh')  # time at next scr refresh
            response_sample.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_responseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_response"-------
for thisComponent in sample_responseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('response_sample.started', response_sample.tStartRefresh)
thisExp.addData('response_sample.stopped', response_sample.tStopRefresh)

# ------Prepare to start Routine "wait_time_2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
wait_time_2Components = [before_you_go]
for thisComponent in wait_time_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_time_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wait_time_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = wait_time_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_time_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *before_you_go* updates
    if before_you_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        before_you_go.frameNStart = frameN  # exact frame index
        before_you_go.tStart = t  # local t and not account for scr refresh
        before_you_go.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(before_you_go, 'tStartRefresh')  # time at next scr refresh
        before_you_go.setAutoDraw(True)
    if before_you_go.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > before_you_go.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            before_you_go.tStop = t  # not accounting for scr refresh
            before_you_go.frameNStop = frameN  # exact frame index
            win.timeOnFlip(before_you_go, 'tStopRefresh')  # time at next scr refresh
            before_you_go.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_time_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_time_2"-------
for thisComponent in wait_time_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('before_you_go.started', before_you_go.tStartRefresh)
thisExp.addData('before_you_go.stopped', before_you_go.tStopRefresh)

# ------Prepare to start Routine "lipreading_trial"-------
continueRoutine = True
# update component parameters for each repeat
lipreading_key.keys = []
lipreading_key.rt = []
_lipreading_key_allKeys = []
# keep track of which components have finished
lipreading_trialComponents = [lipreading, lipreading_key]
for thisComponent in lipreading_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
lipreading_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "lipreading_trial"-------
while continueRoutine:
    # get current time
    t = lipreading_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=lipreading_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *lipreading* updates
    if lipreading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lipreading.frameNStart = frameN  # exact frame index
        lipreading.tStart = t  # local t and not account for scr refresh
        lipreading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lipreading, 'tStartRefresh')  # time at next scr refresh
        lipreading.setAutoDraw(True)
    if lipreading.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lipreading.tStartRefresh + lipreading_key.status==FINISHED-frameTolerance:
            # keep track of stop time/frame for later
            lipreading.tStop = t  # not accounting for scr refresh
            lipreading.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lipreading, 'tStopRefresh')  # time at next scr refresh
            lipreading.setAutoDraw(False)
    
    # *lipreading_key* updates
    waitOnFlip = False
    if lipreading_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lipreading_key.frameNStart = frameN  # exact frame index
        lipreading_key.tStart = t  # local t and not account for scr refresh
        lipreading_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lipreading_key, 'tStartRefresh')  # time at next scr refresh
        lipreading_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(lipreading_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(lipreading_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if lipreading_key.status == STARTED and not waitOnFlip:
        theseKeys = lipreading_key.getKeys(keyList=['num_3'], waitRelease=False)
        _lipreading_key_allKeys.extend(theseKeys)
        if len(_lipreading_key_allKeys):
            lipreading_key.keys = _lipreading_key_allKeys[-1].name  # just the last key pressed
            lipreading_key.rt = _lipreading_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lipreading_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "lipreading_trial"-------
for thisComponent in lipreading_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('lipreading.started', lipreading.tStartRefresh)
thisExp.addData('lipreading.stopped', lipreading.tStopRefresh)
# check responses
if lipreading_key.keys in ['', [], None]:  # No response was made
    lipreading_key.keys = None
thisExp.addData('lipreading_key.keys',lipreading_key.keys)
if lipreading_key.keys != None:  # we had a response
    thisExp.addData('lipreading_key.rt', lipreading_key.rt)
thisExp.addData('lipreading_key.started', lipreading_key.tStartRefresh)
thisExp.addData('lipreading_key.stopped', lipreading_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "lipreading_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "goose_video"-------
continueRoutine = True
# update component parameters for each repeat
response.keys = []
response.rt = []
_response_allKeys = []
# keep track of which components have finished
goose_videoComponents = [response_sample2, goose_visual, response]
for thisComponent in goose_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goose_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goose_video"-------
while continueRoutine:
    # get current time
    t = goose_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goose_videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *response_sample2* updates
    if response_sample2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        response_sample2.frameNStart = frameN  # exact frame index
        response_sample2.tStart = t  # local t and not account for scr refresh
        response_sample2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response_sample2, 'tStartRefresh')  # time at next scr refresh
        response_sample2.setAutoDraw(True)
    if response_sample2.status == STARTED:
        if bool(response.status==FINISHED):
            # keep track of stop time/frame for later
            response_sample2.tStop = t  # not accounting for scr refresh
            response_sample2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(response_sample2, 'tStopRefresh')  # time at next scr refresh
            response_sample2.setAutoDraw(False)
    
    # *goose_visual* updates
    if goose_visual.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goose_visual.frameNStart = frameN  # exact frame index
        goose_visual.tStart = t  # local t and not account for scr refresh
        goose_visual.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goose_visual, 'tStartRefresh')  # time at next scr refresh
        goose_visual.setAutoDraw(True)
    
    # *response* updates
    waitOnFlip = False
    if response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        response.frameNStart = frameN  # exact frame index
        response.tStart = t  # local t and not account for scr refresh
        response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
        response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if response.status == STARTED and not waitOnFlip:
        theseKeys = response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
        _response_allKeys.extend(theseKeys)
        if len(_response_allKeys):
            response.keys = _response_allKeys[-1].name  # just the last key pressed
            response.rt = _response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goose_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goose_video"-------
for thisComponent in goose_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('response_sample2.started', response_sample2.tStartRefresh)
thisExp.addData('response_sample2.stopped', response_sample2.tStopRefresh)
goose_visual.stop()
# check responses
if response.keys in ['', [], None]:  # No response was made
    response.keys = None
thisExp.addData('response.keys',response.keys)
if response.keys != None:  # we had a response
    thisExp.addData('response.rt', response.rt)
thisExp.addData('response.started', response.tStartRefresh)
thisExp.addData('response.stopped', response.tStopRefresh)
thisExp.nextEntry()
# the Routine "goose_video" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "correct_answer1"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
correct_answer1Components = [goose_correct]
for thisComponent in correct_answer1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
correct_answer1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "correct_answer1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = correct_answer1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=correct_answer1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goose_correct* updates
    if goose_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goose_correct.frameNStart = frameN  # exact frame index
        goose_correct.tStart = t  # local t and not account for scr refresh
        goose_correct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goose_correct, 'tStartRefresh')  # time at next scr refresh
        goose_correct.setAutoDraw(True)
    if goose_correct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > goose_correct.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            goose_correct.tStop = t  # not accounting for scr refresh
            goose_correct.frameNStop = frameN  # exact frame index
            win.timeOnFlip(goose_correct, 'tStopRefresh')  # time at next scr refresh
            goose_correct.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in correct_answer1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "correct_answer1"-------
for thisComponent in correct_answer1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goose_correct.started', goose_correct.tStartRefresh)
thisExp.addData('goose_correct.stopped', goose_correct.tStopRefresh)

# ------Prepare to start Routine "let_s_get_started"-------
continueRoutine = True
# update component parameters for each repeat
end_start.keys = []
end_start.rt = []
_end_start_allKeys = []
# keep track of which components have finished
let_s_get_startedComponents = [let_s_start, end_start]
for thisComponent in let_s_get_startedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
let_s_get_startedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "let_s_get_started"-------
while continueRoutine:
    # get current time
    t = let_s_get_startedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=let_s_get_startedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *let_s_start* updates
    if let_s_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        let_s_start.frameNStart = frameN  # exact frame index
        let_s_start.tStart = t  # local t and not account for scr refresh
        let_s_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(let_s_start, 'tStartRefresh')  # time at next scr refresh
        let_s_start.setAutoDraw(True)
    if let_s_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > let_s_start.tStartRefresh + end_start.status==FINISHED-frameTolerance:
            # keep track of stop time/frame for later
            let_s_start.tStop = t  # not accounting for scr refresh
            let_s_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(let_s_start, 'tStopRefresh')  # time at next scr refresh
            let_s_start.setAutoDraw(False)
    
    # *end_start* updates
    waitOnFlip = False
    if end_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_start.frameNStart = frameN  # exact frame index
        end_start.tStart = t  # local t and not account for scr refresh
        end_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_start, 'tStartRefresh')  # time at next scr refresh
        end_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_start.status == STARTED and not waitOnFlip:
        theseKeys = end_start.getKeys(keyList=['return'], waitRelease=False)
        _end_start_allKeys.extend(theseKeys)
        if len(_end_start_allKeys):
            end_start.keys = _end_start_allKeys[-1].name  # just the last key pressed
            end_start.rt = _end_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in let_s_get_startedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "let_s_get_started"-------
for thisComponent in let_s_get_startedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('let_s_start.started', let_s_start.tStartRefresh)
thisExp.addData('let_s_start.stopped', let_s_start.tStopRefresh)
# check responses
if end_start.keys in ['', [], None]:  # No response was made
    end_start.keys = None
thisExp.addData('end_start.keys',end_start.keys)
if end_start.keys != None:  # we had a response
    thisExp.addData('end_start.rt', end_start.rt)
thisExp.addData('end_start.started', end_start.tStartRefresh)
thisExp.addData('end_start.stopped', end_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "let_s_get_started" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



timestamp = time()
data_to_send = {
    "id": 2,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[0],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
    
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
written_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/written stimuli.xlsx'),
    seed=None, name='written_loop')
thisExp.addLoop(written_loop)  # add the loop to the experiment
thisWritten_loop = written_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWritten_loop.rgb)

if thisWritten_loop != None:
    for paramName in thisWritten_loop:
        exec('{} = thisWritten_loop[paramName]'.format(paramName))
for thisWritten_loop in written_loop:
    currentLoop = written_loop
    data_to_send = {
            "id": 3,
            "timestamp": int(timestamp * 1e9),
            "event": stimuli_order[1],
            "value": "1"
            }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisWritten_loop.rgb)
    if thisWritten_loop != None:
        for paramName in thisWritten_loop:
            exec('{} = thisWritten_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "written_stimulus"-------
    continueRoutine = True
    # update component parameters for each repeat
    start_of_w_stim.setText(writ_stim)
    writ_response.keys = []
    writ_response.rt = []
    _writ_response_allKeys = []
    # keep track of which components have finished
    written_stimulusComponents = [start_of_w_stim, writ_response, response_prompt]
    for thisComponent in written_stimulusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        timestamp = time()
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    written_stimulusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "written_stimulus"-------
    while continueRoutine:
        # get current time
        t = written_stimulusClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=written_stimulusClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *start_of_w_stim* updates
        if start_of_w_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_of_w_stim.frameNStart = frameN  # exact frame index
            start_of_w_stim.tStart = t  # local t and not account for scr refresh
            start_of_w_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_of_w_stim, 'tStartRefresh')  # time at next scr refresh
            start_of_w_stim.setAutoDraw(True)
        if start_of_w_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_of_w_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                start_of_w_stim.tStop = t  # not accounting for scr refresh
                start_of_w_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_of_w_stim, 'tStopRefresh')  # time at next scr refresh
                start_of_w_stim.setAutoDraw(False)
        
        # *writ_response* updates
        waitOnFlip = False
        if writ_response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            writ_response.frameNStart = frameN  # exact frame index
            writ_response.tStart = t  # local t and not account for scr refresh
            writ_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(writ_response, 'tStartRefresh')  # time at next scr refresh
            writ_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(writ_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(writ_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if writ_response.status == STARTED and not waitOnFlip:
            theseKeys = writ_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _writ_response_allKeys.extend(theseKeys)
            if len(_writ_response_allKeys):
                writ_response.keys = _writ_response_allKeys[-1].name  # just the last key pressed
                writ_response.rt = _writ_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *response_prompt* updates
        if response_prompt.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            response_prompt.frameNStart = frameN  # exact frame index
            response_prompt.tStart = t  # local t and not account for scr refresh
            response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_prompt, 'tStartRefresh')  # time at next scr refresh
            response_prompt.setAutoDraw(True)
        if response_prompt.status == STARTED:
            if bool(writ_response.status==FINISHED):
                # keep track of stop time/frame for later
                response_prompt.tStop = t  # not accounting for scr refresh
                response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response_prompt, 'tStopRefresh')  # time at next scr refresh
                response_prompt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in written_stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "written_stimulus"-------
    for thisComponent in written_stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    written_loop.addData('start_of_w_stim.started', start_of_w_stim.tStartRefresh)
    written_loop.addData('start_of_w_stim.stopped', start_of_w_stim.tStopRefresh)
    # check responses
    if writ_response.keys in ['', [], None]:  # No response was made
        writ_response.keys = None
    written_loop.addData('writ_response.keys',writ_response.keys)
    if writ_response.keys != None:  # we had a response
        written_loop.addData('writ_response.rt', writ_response.rt)
    written_loop.addData('writ_response.started', writ_response.tStartRefresh)
    written_loop.addData('writ_response.stopped', writ_response.tStopRefresh)
    written_loop.addData('response_prompt.started', response_prompt.tStartRefresh)
    written_loop.addData('response_prompt.stopped', response_prompt.tStopRefresh)
    # the Routine "written_stimulus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    written_loop.addData('blank.started', blank.tStartRefresh)
    written_loop.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'written_loop'

timestamp = time()
data_to_send = {
    "id": 4,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[2],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
first_v_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/first V.xlsx'),
    seed=None, name='first_v_trials')
thisExp.addLoop(first_v_trials)  # add the loop to the experiment
thisFirst_v_trial = first_v_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_v_trial.rgb)
if thisFirst_v_trial != None:
    for paramName in thisFirst_v_trial:
        exec('{} = thisFirst_v_trial[paramName]'.format(paramName))
for thisFirst_v_trial in first_v_trials:
    currentLoop = first_v_trials
    timestamp = time()
    data_to_send = {
        "id": 5,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[3],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_v_trial.rgb)
    if thisFirst_v_trial != None:
        for paramName in thisFirst_v_trial:
            exec('{} = thisFirst_v_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "first_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    first_v_movies = visual.MovieStim3(
        win=win, name='first_v_movies', units='pix',
        noAudio = True,
        filename=first_V,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False, anchor='center',
        depth=0.0,
        )
    first_v_response.keys = []
    first_v_response.rt = []
    _first_v_response_allKeys = []
    # keep track of which components have finished
    first_VComponents = [first_v_movies, first_v_response_prompt, first_v_response]
    for thisComponent in first_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    first_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "first_V"-------
    while continueRoutine:
        # get current time
        t = first_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=first_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *first_v_movies* updates
        if first_v_movies.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            first_v_movies.frameNStart = frameN  # exact frame index
            first_v_movies.tStart = t  # local t and not account for scr refresh
            first_v_movies.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_v_movies, 'tStartRefresh')  # time at next scr refresh
            first_v_movies.setAutoDraw(True)
        if first_v_movies.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > first_v_movies.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                first_v_movies.tStop = t  # not accounting for scr refresh
                first_v_movies.frameNStop = frameN  # exact frame index
                win.timeOnFlip(first_v_movies, 'tStopRefresh')  # time at next scr refresh
                first_v_movies.setAutoDraw(False)
        
        # *first_v_response_prompt* updates
        if first_v_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            first_v_response_prompt.frameNStart = frameN  # exact frame index
            first_v_response_prompt.tStart = t  # local t and not account for scr refresh
            first_v_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_v_response_prompt, 'tStartRefresh')  # time at next scr refresh
            first_v_response_prompt.setAutoDraw(True)
        if first_v_response_prompt.status == STARTED:
            if bool(first_v_response.status==FINISHED):
                # keep track of stop time/frame for later
                first_v_response_prompt.tStop = t  # not accounting for scr refresh
                first_v_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(first_v_response_prompt, 'tStopRefresh')  # time at next scr refresh
                first_v_response_prompt.setAutoDraw(False)
        
        # *first_v_response* updates
        waitOnFlip = False
        if first_v_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            first_v_response.frameNStart = frameN  # exact frame index
            first_v_response.tStart = t  # local t and not account for scr refresh
            first_v_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_v_response, 'tStartRefresh')  # time at next scr refresh
            first_v_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(first_v_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(first_v_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if first_v_response.status == STARTED and not waitOnFlip:
            theseKeys = first_v_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _first_v_response_allKeys.extend(theseKeys)
            if len(_first_v_response_allKeys):
                first_v_response.keys = _first_v_response_allKeys[-1].name  # just the last key pressed
                first_v_response.rt = _first_v_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in first_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "first_V"-------
    for thisComponent in first_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_v_movies.stop()
    first_v_trials.addData('first_v_response_prompt.started', first_v_response_prompt.tStartRefresh)
    first_v_trials.addData('first_v_response_prompt.stopped', first_v_response_prompt.tStopRefresh)
    # check responses
    if first_v_response.keys in ['', [], None]:  # No response was made
        first_v_response.keys = None
    first_v_trials.addData('first_v_response.keys',first_v_response.keys)
    if first_v_response.keys != None:  # we had a response
        first_v_trials.addData('first_v_response.rt', first_v_response.rt)
    first_v_trials.addData('first_v_response.started', first_v_response.tStartRefresh)
    first_v_trials.addData('first_v_response.stopped', first_v_response.tStopRefresh)
    # the Routine "first_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_v_trials.addData('blank.started', blank.tStartRefresh)
    first_v_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'first_v_trials'

timestamp = time()
data_to_send = {
    "id": 6,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[4],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
first_A_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/first A.xlsx'),
    seed=None, name='first_A_trials')
thisExp.addLoop(first_A_trials)  # add the loop to the experiment
thisFirst_A_trial = first_A_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_A_trial.rgb)
if thisFirst_A_trial != None:
    for paramName in thisFirst_A_trial:
        exec('{} = thisFirst_A_trial[paramName]'.format(paramName))
for thisFirst_A_trial in first_A_trials:
    currentLoop = first_A_trials
    timestamp = time()
    data_to_send = {
        "id": 7,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[5],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_A_trial.rgb)
    if thisFirst_A_trial != None:
        for paramName in thisFirst_A_trial:
            exec('{} = thisFirst_A_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "first_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    first_a_response.keys = []
    first_a_response.rt = []
    _first_a_response_allKeys = []
    first_a_stim.setSound(first_A, hamming=True)
    first_a_stim.setVolume(1.0, log=False)
    SNR_file_num = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_1.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_1.setVolume(0.47, log=False)
    # keep track of which components have finished
    first_AComponents = [first_a_response_prompt, first_a_response, first_a_stim, black_screen_with_dot, sound_1]
    for thisComponent in first_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    first_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "first_A"-------
    while continueRoutine:
        # get current time
        t = first_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=first_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *first_a_response_prompt* updates
        if first_a_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            first_a_response_prompt.frameNStart = frameN  # exact frame index
            first_a_response_prompt.tStart = t  # local t and not account for scr refresh
            first_a_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_a_response_prompt, 'tStartRefresh')  # time at next scr refresh
            first_a_response_prompt.setAutoDraw(True)
        if first_a_response_prompt.status == STARTED:
            if bool(first_a_response.status==FINISHED):
                # keep track of stop time/frame for later
                first_a_response_prompt.tStop = t  # not accounting for scr refresh
                first_a_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(first_a_response_prompt, 'tStopRefresh')  # time at next scr refresh
                first_a_response_prompt.setAutoDraw(False)
        
        # *first_a_response* updates
        waitOnFlip = False
        if first_a_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            first_a_response.frameNStart = frameN  # exact frame index
            first_a_response.tStart = t  # local t and not account for scr refresh
            first_a_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_a_response, 'tStartRefresh')  # time at next scr refresh
            first_a_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(first_a_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(first_a_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if first_a_response.status == STARTED and not waitOnFlip:
            theseKeys = first_a_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _first_a_response_allKeys.extend(theseKeys)
            if len(_first_a_response_allKeys):
                first_a_response.keys = _first_a_response_allKeys[-1].name  # just the last key pressed
                first_a_response.rt = _first_a_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop first_a_stim
        if first_a_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            first_a_stim.frameNStart = frameN  # exact frame index
            first_a_stim.tStart = t  # local t and not account for scr refresh
            first_a_stim.tStartRefresh = tThisFlipGlobal  # on global time
            first_a_stim.play(when=win)  # sync with win flip
        
        # *black_screen_with_dot* updates
        if black_screen_with_dot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_screen_with_dot.frameNStart = frameN  # exact frame index
            black_screen_with_dot.tStart = t  # local t and not account for scr refresh
            black_screen_with_dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_screen_with_dot, 'tStartRefresh')  # time at next scr refresh
            black_screen_with_dot.setAutoDraw(True)
        if black_screen_with_dot.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_screen_with_dot.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                black_screen_with_dot.tStop = t  # not accounting for scr refresh
                black_screen_with_dot.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_screen_with_dot, 'tStopRefresh')  # time at next scr refresh
                black_screen_with_dot.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in first_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "first_A"-------
    for thisComponent in first_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_A_trials.addData('first_a_response_prompt.started', first_a_response_prompt.tStartRefresh)
    first_A_trials.addData('first_a_response_prompt.stopped', first_a_response_prompt.tStopRefresh)
    # check responses
    if first_a_response.keys in ['', [], None]:  # No response was made
        first_a_response.keys = None
    first_A_trials.addData('first_a_response.keys',first_a_response.keys)
    if first_a_response.keys != None:  # we had a response
        first_A_trials.addData('first_a_response.rt', first_a_response.rt)
    first_A_trials.addData('first_a_response.started', first_a_response.tStartRefresh)
    first_A_trials.addData('first_a_response.stopped', first_a_response.tStopRefresh)
    first_a_stim.stop()  # ensure sound has stopped at end of routine
    first_A_trials.addData('first_a_stim.started', first_a_stim.tStartRefresh)
    first_A_trials.addData('first_a_stim.stopped', first_a_stim.tStopRefresh)
    first_A_trials.addData('black_screen_with_dot.started', black_screen_with_dot.tStartRefresh)
    first_A_trials.addData('black_screen_with_dot.stopped', black_screen_with_dot.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    first_A_trials.addData('sound_1.started', sound_1.tStartRefresh)
    first_A_trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    # the Routine "first_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_A_trials.addData('blank.started', blank.tStartRefresh)
    first_A_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'first_A_trials'

timestamp = time()
data_to_send = {
    "id": 8,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[6],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
first_AV_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/First AV.xlsx'),
    seed=None, name='first_AV_trials')
thisExp.addLoop(first_AV_trials)  # add the loop to the experiment
thisFirst_AV_trial = first_AV_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_AV_trial.rgb)
if thisFirst_AV_trial != None:
    for paramName in thisFirst_AV_trial:
        exec('{} = thisFirst_AV_trial[paramName]'.format(paramName))
for thisFirst_AV_trial in first_AV_trials:
    currentLoop = first_AV_trials
    timestamp = time()
    data_to_send = {
        "id": 9,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[7],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_AV_trial.rgb)
    if thisFirst_AV_trial != None:
        for paramName in thisFirst_AV_trial:
            exec('{} = thisFirst_AV_trial[paramName]'.format(paramName))
            
    # ------Prepare to start Routine "first_AV_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    first_AV_response.keys = []
    first_AV_response.rt = []
    _first_AV_response_allKeys = []
    SNR_file_num_1av = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_1_AV.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_1av+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_1_AV.setVolume(0.47, log=False)
    first_AV_stim = visual.MovieStim3(
        win=win, name='first_AV_stim', units='pix',
        noAudio = False,
        filename=first_AV,
        ori=0.0, pos=(0, 0), size=(720,480), opacity=None,
        loop=False, anchor='center',
        depth=-3.0,
        )
    first_AV_stim.reset()
    # keep track of which components have finished
    first_AV_2Components = [first_AV_response, first_AV_response_prompt, sound_1_AV, first_AV_stim]
    for thisComponent in first_AV_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    first_AV_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "first_AV_2"-------
    while continueRoutine:
        # get current time
        t = first_AV_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=first_AV_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *first_AV_response* updates
        waitOnFlip = False
        if first_AV_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            first_AV_response.frameNStart = frameN  # exact frame index
            first_AV_response.tStart = t  # local t and not account for scr refresh
            first_AV_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_AV_response, 'tStartRefresh')  # time at next scr refresh
            first_AV_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(first_AV_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(first_AV_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if first_AV_response.status == STARTED and not waitOnFlip:
            theseKeys = first_AV_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _first_AV_response_allKeys.extend(theseKeys)
            if len(_first_AV_response_allKeys):
                first_AV_response.keys = _first_AV_response_allKeys[-1].name  # just the last key pressed
                first_AV_response.rt = _first_AV_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *first_AV_response_prompt* updates
        if first_AV_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            first_AV_response_prompt.frameNStart = frameN  # exact frame index
            first_AV_response_prompt.tStart = t  # local t and not account for scr refresh
            first_AV_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_AV_response_prompt, 'tStartRefresh')  # time at next scr refresh
            first_AV_response_prompt.setAutoDraw(True)
        if first_AV_response_prompt.status == STARTED:
            if bool(first_AV_response.status==FINISHED):
                # keep track of stop time/frame for later
                first_AV_response_prompt.tStop = t  # not accounting for scr refresh
                first_AV_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(first_AV_response_prompt, 'tStopRefresh')  # time at next scr refresh
                first_AV_response_prompt.setAutoDraw(False)
        # start/stop sound_1_AV
        if sound_1_AV.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1_AV.frameNStart = frameN  # exact frame index
            sound_1_AV.tStart = t  # local t and not account for scr refresh
            sound_1_AV.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1_AV.play(when=win)  # sync with win flip
        if sound_1_AV.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1_AV.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1_AV.tStop = t  # not accounting for scr refresh
                sound_1_AV.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1_AV, 'tStopRefresh')  # time at next scr refresh
                sound_1_AV.stop()
        
        # *first_AV_stim* updates
        if first_AV_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            first_AV_stim.frameNStart = frameN  # exact frame index
            first_AV_stim.tStart = t  # local t and not account for scr refresh
            first_AV_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_AV_stim, 'tStartRefresh')  # time at next scr refresh
            first_AV_stim.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in first_AV_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "first_AV_2"-------
    for thisComponent in first_AV_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if first_AV_response.keys in ['', [], None]:  # No response was made
        first_AV_response.keys = None
    first_AV_trials.addData('first_AV_response.keys',first_AV_response.keys)
    if first_AV_response.keys != None:  # we had a response
        first_AV_trials.addData('first_AV_response.rt', first_AV_response.rt)
    first_AV_trials.addData('first_AV_response.started', first_AV_response.tStartRefresh)
    first_AV_trials.addData('first_AV_response.stopped', first_AV_response.tStopRefresh)
    first_AV_trials.addData('first_AV_response_prompt.started', first_AV_response_prompt.tStartRefresh)
    first_AV_trials.addData('first_AV_response_prompt.stopped', first_AV_response_prompt.tStopRefresh)
    sound_1_AV.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_1_AV.started', sound_1_AV.tStartRefresh)
    thisExp.addData('sound_1_AV.stopped', sound_1_AV.tStopRefresh)
    first_AV_stim.stop()
    # the Routine "first_AV_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_AV_trials.addData('blank.started', blank.tStartRefresh)
    first_AV_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'first_AV_trials'


# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

timestamp = time()
data_to_send = {
    "id": 10,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[8],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
second_written_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Second Written.xlsx'),
    seed=None, name='second_written_trials')
thisExp.addLoop(second_written_trials)  # add the loop to the experiment
thisSecond_written_trial = second_written_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSecond_written_trial.rgb)
if thisSecond_written_trial != None:
    for paramName in thisSecond_written_trial:
        exec('{} = thisSecond_written_trial[paramName]'.format(paramName))
        
for thisSecond_written_trial in second_written_trials:
    currentLoop = second_written_trials
    timestamp = time()
    data_to_send = {
        "id": 11,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[9],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisSecond_written_trial.rgb)
    if thisSecond_written_trial != None:
        for paramName in thisSecond_written_trial:
            exec('{} = thisSecond_written_trial[paramName]'.format(paramName))
            
    # ------Prepare to start Routine "second_written"-------
    continueRoutine = True
    # update component parameters for each repeat
    second_writ_response.keys = []
    second_writ_response.rt = []
    _second_writ_response_allKeys = []
    second_w_stim.setText(second_W)
    # keep track of which components have finished
    second_writtenComponents = [second_writ_response, second_written_response_prompt, second_w_stim]
    for thisComponent in second_writtenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    second_writtenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "second_written"-------
    while continueRoutine:
        # get current time
        t = second_writtenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=second_writtenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *second_writ_response* updates
        waitOnFlip = False
        if second_writ_response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            second_writ_response.frameNStart = frameN  # exact frame index
            second_writ_response.tStart = t  # local t and not account for scr refresh
            second_writ_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_writ_response, 'tStartRefresh')  # time at next scr refresh
            second_writ_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(second_writ_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(second_writ_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if second_writ_response.status == STARTED and not waitOnFlip:
            theseKeys = second_writ_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _second_writ_response_allKeys.extend(theseKeys)
            if len(_second_writ_response_allKeys):
                second_writ_response.keys = _second_writ_response_allKeys[-1].name  # just the last key pressed
                second_writ_response.rt = _second_writ_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *second_written_response_prompt* updates
        if second_written_response_prompt.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            second_written_response_prompt.frameNStart = frameN  # exact frame index
            second_written_response_prompt.tStart = t  # local t and not account for scr refresh
            second_written_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_written_response_prompt, 'tStartRefresh')  # time at next scr refresh
            second_written_response_prompt.setAutoDraw(True)
        if second_written_response_prompt.status == STARTED:
            if bool(second_writ_response.status==FINISHED):
                # keep track of stop time/frame for later
                second_written_response_prompt.tStop = t  # not accounting for scr refresh
                second_written_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(second_written_response_prompt, 'tStopRefresh')  # time at next scr refresh
                second_written_response_prompt.setAutoDraw(False)
        
        # *second_w_stim* updates
        if second_w_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            second_w_stim.frameNStart = frameN  # exact frame index
            second_w_stim.tStart = t  # local t and not account for scr refresh
            second_w_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_w_stim, 'tStartRefresh')  # time at next scr refresh
            second_w_stim.setAutoDraw(True)
        if second_w_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > second_w_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                second_w_stim.tStop = t  # not accounting for scr refresh
                second_w_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(second_w_stim, 'tStopRefresh')  # time at next scr refresh
                second_w_stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in second_writtenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "second_written"-------
    for thisComponent in second_writtenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if second_writ_response.keys in ['', [], None]:  # No response was made
        second_writ_response.keys = None
    second_written_trials.addData('second_writ_response.keys',second_writ_response.keys)
    if second_writ_response.keys != None:  # we had a response
        second_written_trials.addData('second_writ_response.rt', second_writ_response.rt)
    second_written_trials.addData('second_writ_response.started', second_writ_response.tStartRefresh)
    second_written_trials.addData('second_writ_response.stopped', second_writ_response.tStopRefresh)
    second_written_trials.addData('second_written_response_prompt.started', second_written_response_prompt.tStartRefresh)
    second_written_trials.addData('second_written_response_prompt.stopped', second_written_response_prompt.tStopRefresh)
    second_written_trials.addData('second_w_stim.started', second_w_stim.tStartRefresh)
    second_written_trials.addData('second_w_stim.stopped', second_w_stim.tStopRefresh)
    # the Routine "second_written" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_written_trials.addData('blank.started', blank.tStartRefresh)
    second_written_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'second_written_trials'

timestamp = time()
data_to_send = {
    "id": 12,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[10],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
second_a_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Second A.xlsx'),
    seed=None, name='second_a_trials')
thisExp.addLoop(second_a_trials)  # add the loop to the experiment
thisSecond_a_trial = second_a_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSecond_a_trial.rgb)

if thisSecond_a_trial != None:
    for paramName in thisSecond_a_trial:
        exec('{} = thisSecond_a_trial[paramName]'.format(paramName))
for thisSecond_a_trial in second_a_trials:
    currentLoop = second_a_trials
    timestamp = time()
    data_to_send = {
        "id": 13,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[11],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisSecond_a_trial.rgb)
    if thisSecond_a_trial != None:
        for paramName in thisSecond_a_trial:
            exec('{} = thisSecond_a_trial[paramName]'.format(paramName))


    # ------Prepare to start Routine "second_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    second_a_response.keys = []
    second_a_response.rt = []
    _second_a_response_allKeys = []
    SNR_file_num_2a = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_2_a.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_2a+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_2_a.setVolume(0.47, log=False)
    second_a_stim.setSound(second_A, hamming=True)
    second_a_stim.setVolume(1.0, log=False)
    # keep track of which components have finished
    second_AComponents = [second_a_response, second_a_response_prompt, black_screen_with_dot_2, sound_2_a, second_a_stim]
    for thisComponent in second_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    second_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "second_A"-------
    while continueRoutine:
        # get current time
        t = second_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=second_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *second_a_response* updates
        waitOnFlip = False
        if second_a_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            second_a_response.frameNStart = frameN  # exact frame index
            second_a_response.tStart = t  # local t and not account for scr refresh
            second_a_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_a_response, 'tStartRefresh')  # time at next scr refresh
            second_a_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(second_a_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(second_a_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if second_a_response.status == STARTED and not waitOnFlip:
            theseKeys = second_a_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _second_a_response_allKeys.extend(theseKeys)
            if len(_second_a_response_allKeys):
                second_a_response.keys = _second_a_response_allKeys[-1].name  # just the last key pressed
                second_a_response.rt = _second_a_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *second_a_response_prompt* updates
        if second_a_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            second_a_response_prompt.frameNStart = frameN  # exact frame index
            second_a_response_prompt.tStart = t  # local t and not account for scr refresh
            second_a_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_a_response_prompt, 'tStartRefresh')  # time at next scr refresh
            second_a_response_prompt.setAutoDraw(True)
        if second_a_response_prompt.status == STARTED:
            if bool(second_a_response.status==FINISHED):
                # keep track of stop time/frame for later
                second_a_response_prompt.tStop = t  # not accounting for scr refresh
                second_a_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(second_a_response_prompt, 'tStopRefresh')  # time at next scr refresh
                second_a_response_prompt.setAutoDraw(False)
        
        # *black_screen_with_dot_2* updates
        if black_screen_with_dot_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_screen_with_dot_2.frameNStart = frameN  # exact frame index
            black_screen_with_dot_2.tStart = t  # local t and not account for scr refresh
            black_screen_with_dot_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_screen_with_dot_2, 'tStartRefresh')  # time at next scr refresh
            black_screen_with_dot_2.setAutoDraw(True)
        if black_screen_with_dot_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_screen_with_dot_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                black_screen_with_dot_2.tStop = t  # not accounting for scr refresh
                black_screen_with_dot_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_screen_with_dot_2, 'tStopRefresh')  # time at next scr refresh
                black_screen_with_dot_2.setAutoDraw(False)
        # start/stop sound_2_a
        if sound_2_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2_a.frameNStart = frameN  # exact frame index
            sound_2_a.tStart = t  # local t and not account for scr refresh
            sound_2_a.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2_a.play(when=win)  # sync with win flip
        if sound_2_a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2_a.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2_a.tStop = t  # not accounting for scr refresh
                sound_2_a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2_a, 'tStopRefresh')  # time at next scr refresh
                sound_2_a.stop()
        # start/stop second_a_stim
        if second_a_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            second_a_stim.frameNStart = frameN  # exact frame index
            second_a_stim.tStart = t  # local t and not account for scr refresh
            second_a_stim.tStartRefresh = tThisFlipGlobal  # on global time
            second_a_stim.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in second_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "second_A"-------
    for thisComponent in second_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if second_a_response.keys in ['', [], None]:  # No response was made
        second_a_response.keys = None
    second_a_trials.addData('second_a_response.keys',second_a_response.keys)
    if second_a_response.keys != None:  # we had a response
        second_a_trials.addData('second_a_response.rt', second_a_response.rt)
    second_a_trials.addData('second_a_response.started', second_a_response.tStartRefresh)
    second_a_trials.addData('second_a_response.stopped', second_a_response.tStopRefresh)
    second_a_trials.addData('second_a_response_prompt.started', second_a_response_prompt.tStartRefresh)
    second_a_trials.addData('second_a_response_prompt.stopped', second_a_response_prompt.tStopRefresh)
    second_a_trials.addData('black_screen_with_dot_2.started', black_screen_with_dot_2.tStartRefresh)
    second_a_trials.addData('black_screen_with_dot_2.stopped', black_screen_with_dot_2.tStopRefresh)
    sound_2_a.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_2_a.started', sound_2_a.tStartRefresh)
    thisExp.addData('sound_2_a.stopped', sound_2_a.tStopRefresh)
    second_a_stim.stop()  # ensure sound has stopped at end of routine
    second_a_trials.addData('second_a_stim.started', second_a_stim.tStartRefresh)
    second_a_trials.addData('second_a_stim.stopped', second_a_stim.tStopRefresh)
    # the Routine "second_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_a_trials.addData('blank.started', blank.tStartRefresh)
    second_a_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'second_a_trials'

timestamp = time()
data_to_send = {
    "id": 14,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[12],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
second_v_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Second V.xlsx'),
    seed=None, name='second_v_trials')
thisExp.addLoop(second_v_trials)  # add the loop to the experiment
thisSecond_v_trial = second_v_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSecond_v_trial.rgb)
if thisSecond_v_trial != None:
    for paramName in thisSecond_v_trial:
        exec('{} = thisSecond_v_trial[paramName]'.format(paramName))
for thisSecond_v_trial in second_v_trials:
    currentLoop = second_v_trials
    timestamp = time()
    data_to_send = {
        "id": 15,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[13],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisSecond_v_trial.rgb)
    if thisSecond_v_trial != None:
        for paramName in thisSecond_v_trial:
            exec('{} = thisSecond_v_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "second_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    second_v_response.keys = []
    second_v_response.rt = []
    _second_v_response_allKeys = []
    second_v_movies = visual.MovieStim3(
        win=win, name='second_v_movies', units='pix',
        noAudio = True,
        filename=second_V,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False, anchor='center',
        depth=-2.0,
        )
    # keep track of which components have finished
    second_VComponents = [second_v_response_prompt, second_v_response, second_v_movies]
    for thisComponent in second_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    second_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "second_V"-------
    while continueRoutine:
        # get current time
        t = second_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=second_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *second_v_response_prompt* updates
        if second_v_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            second_v_response_prompt.frameNStart = frameN  # exact frame index
            second_v_response_prompt.tStart = t  # local t and not account for scr refresh
            second_v_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_v_response_prompt, 'tStartRefresh')  # time at next scr refresh
            second_v_response_prompt.setAutoDraw(True)
        if second_v_response_prompt.status == STARTED:
            if bool(second_v_response.status==FINISHED):
                # keep track of stop time/frame for later
                second_v_response_prompt.tStop = t  # not accounting for scr refresh
                second_v_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(second_v_response_prompt, 'tStopRefresh')  # time at next scr refresh
                second_v_response_prompt.setAutoDraw(False)
        
        # *second_v_response* updates
        waitOnFlip = False
        if second_v_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            second_v_response.frameNStart = frameN  # exact frame index
            second_v_response.tStart = t  # local t and not account for scr refresh
            second_v_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_v_response, 'tStartRefresh')  # time at next scr refresh
            second_v_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(second_v_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(second_v_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if second_v_response.status == STARTED and not waitOnFlip:
            theseKeys = second_v_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _second_v_response_allKeys.extend(theseKeys)
            if len(_second_v_response_allKeys):
                second_v_response.keys = _second_v_response_allKeys[-1].name  # just the last key pressed
                second_v_response.rt = _second_v_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *second_v_movies* updates
        if second_v_movies.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            second_v_movies.frameNStart = frameN  # exact frame index
            second_v_movies.tStart = t  # local t and not account for scr refresh
            second_v_movies.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_v_movies, 'tStartRefresh')  # time at next scr refresh
            second_v_movies.setAutoDraw(True)
        if second_v_movies.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > second_v_movies.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                second_v_movies.tStop = t  # not accounting for scr refresh
                second_v_movies.frameNStop = frameN  # exact frame index
                win.timeOnFlip(second_v_movies, 'tStopRefresh')  # time at next scr refresh
                second_v_movies.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in second_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "second_V"-------
    for thisComponent in second_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_v_trials.addData('second_v_response_prompt.started', second_v_response_prompt.tStartRefresh)
    second_v_trials.addData('second_v_response_prompt.stopped', second_v_response_prompt.tStopRefresh)
    # check responses
    if second_v_response.keys in ['', [], None]:  # No response was made
        second_v_response.keys = None
    second_v_trials.addData('second_v_response.keys',second_v_response.keys)
    if second_v_response.keys != None:  # we had a response
        second_v_trials.addData('second_v_response.rt', second_v_response.rt)
    second_v_trials.addData('second_v_response.started', second_v_response.tStartRefresh)
    second_v_trials.addData('second_v_response.stopped', second_v_response.tStopRefresh)
    second_v_movies.stop()
    # the Routine "second_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_v_trials.addData('blank.started', blank.tStartRefresh)
    second_v_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'second_v_trials'

timestamp = time()
data_to_send = {
    "id": 16,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[14],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
second_AV_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Second AV.xlsx'),
    seed=None, name='second_AV_trials')
thisExp.addLoop(second_AV_trials)  # add the loop to the experiment
thisSecond_AV_trial = second_AV_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSecond_AV_trial.rgb)
if thisSecond_AV_trial != None:
    for paramName in thisSecond_AV_trial:
        exec('{} = thisSecond_AV_trial[paramName]'.format(paramName))
for thisSecond_AV_trial in second_AV_trials:
    currentLoop = second_AV_trials
    timestamp = time()
    data_to_send = {
        "id": 17,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[15],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisSecond_AV_trial.rgb)
    if thisSecond_AV_trial != None:
        for paramName in thisSecond_AV_trial:
            exec('{} = thisSecond_AV_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "second_AV"-------
    continueRoutine = True
    # update component parameters for each repeat
    second_AV_response.keys = []
    second_AV_response.rt = []
    _second_AV_response_allKeys = []
    SNR_file_num_2av = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_2_av.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_2av+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_2_av.setVolume(0.47, log=False)
    second_AV_stim = visual.MovieStim3(
        win=win, name='second_AV_stim', units='pix',
        noAudio = False,
        filename=second_AV,
        ori=0.0, pos=(0, 0), size=(720,480), opacity=None,
        loop=False, anchor='center',
        depth=-3.0,
        )
    second_AV_stim.reset()
    # keep track of which components have finished
    second_AVComponents = [second_AV_response, second_AV_response_prompt, sound_2_av, second_AV_stim]
    for thisComponent in second_AVComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    second_AVClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "second_AV"
    while continueRoutine:
        # get current time
        t = second_AVClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=second_AVClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *second_AV_response* updates
        waitOnFlip = False
        if second_AV_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            second_AV_response.frameNStart = frameN  # exact frame index
            second_AV_response.tStart = t  # local t and not account for scr refresh
            second_AV_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_AV_response, 'tStartRefresh')  # time at next scr refresh
            second_AV_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(second_AV_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(second_AV_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if second_AV_response.status == STARTED and not waitOnFlip:
            theseKeys = second_AV_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _second_AV_response_allKeys.extend(theseKeys)
            if len(_second_AV_response_allKeys):
                second_AV_response.keys = _second_AV_response_allKeys[-1].name  # just the last key pressed
                second_AV_response.rt = _second_AV_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *second_AV_response_prompt* updates
        if second_AV_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            second_AV_response_prompt.frameNStart = frameN  # exact frame index
            second_AV_response_prompt.tStart = t  # local t and not account for scr refresh
            second_AV_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_AV_response_prompt, 'tStartRefresh')  # time at next scr refresh
            second_AV_response_prompt.setAutoDraw(True)
        if second_AV_response_prompt.status == STARTED:
            if bool(second_AV_response.status==FINISHED):
                # keep track of stop time/frame for later
                second_AV_response_prompt.tStop = t  # not accounting for scr refresh
                second_AV_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(second_AV_response_prompt, 'tStopRefresh')  # time at next scr refresh
                second_AV_response_prompt.setAutoDraw(False)
        # start/stop sound_2_av
        if sound_2_av.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2_av.frameNStart = frameN  # exact frame index
            sound_2_av.tStart = t  # local t and not account for scr refresh
            sound_2_av.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2_av.play(when=win)  # sync with win flip
        if sound_2_av.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2_av.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2_av.tStop = t  # not accounting for scr refresh
                sound_2_av.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2_av, 'tStopRefresh')  # time at next scr refresh
                sound_2_av.stop()
        
        # *second_AV_stim* updates
        if second_AV_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            second_AV_stim.frameNStart = frameN  # exact frame index
            second_AV_stim.tStart = t  # local t and not account for scr refresh
            second_AV_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_AV_stim, 'tStartRefresh')  # time at next scr refresh
            second_AV_stim.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in second_AVComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "second_AV"-------
    for thisComponent in second_AVComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if second_AV_response.keys in ['', [], None]:  # No response was made
        second_AV_response.keys = None
    second_AV_trials.addData('second_AV_response.keys',second_AV_response.keys)
    if second_AV_response.keys != None:  # we had a response
        second_AV_trials.addData('second_AV_response.rt', second_AV_response.rt)
    second_AV_trials.addData('second_AV_response.started', second_AV_response.tStartRefresh)
    second_AV_trials.addData('second_AV_response.stopped', second_AV_response.tStopRefresh)
    second_AV_trials.addData('second_AV_response_prompt.started', second_AV_response_prompt.tStartRefresh)
    second_AV_trials.addData('second_AV_response_prompt.stopped', second_AV_response_prompt.tStopRefresh)
    sound_2_av.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_2_av.started', sound_2_av.tStartRefresh)
    thisExp.addData('sound_2_av.stopped', sound_2_av.tStopRefresh)
    second_AV_stim.stop()
    # the Routine "second_AV" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    second_AV_trials.addData('blank.started', blank.tStartRefresh)
    second_AV_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'second_AV_trials'

timestamp = time()
data_to_send = {
    "id": 18,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[16],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
third_v_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Third V.xlsx'),
    seed=None, name='third_v_trials')
thisExp.addLoop(third_v_trials)  # add the loop to the experiment
thisThird_v_trial = third_v_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisThird_v_trial.rgb)
if thisThird_v_trial != None:
    for paramName in thisThird_v_trial:
        exec('{} = thisThird_v_trial[paramName]'.format(paramName))
for thisThird_v_trial in third_v_trials:
    currentLoop = third_v_trials
    timestamp = time()
    data_to_send = {
        "id": 19,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[17],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisThird_v_trial.rgb)
    if thisThird_v_trial != None:
        for paramName in thisThird_v_trial:
            exec('{} = thisThird_v_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "third_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    third_v_response.keys = []
    third_v_response.rt = []
    _third_v_response_allKeys = []
    third_v_movies = visual.MovieStim3(
        win=win, name='third_v_movies', units='pix',
        noAudio = True,
        filename=third_V,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False, anchor='center',
        depth=-2.0,
        )
    # keep track of which components have finished
    third_VComponents = [third_v_response, third_v_response_prompt, third_v_movies]
    for thisComponent in third_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    third_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "third_V"-------
    while continueRoutine:
        # get current time
        t = third_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=third_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *third_v_response* updates
        waitOnFlip = False
        if third_v_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            third_v_response.frameNStart = frameN  # exact frame index
            third_v_response.tStart = t  # local t and not account for scr refresh
            third_v_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_v_response, 'tStartRefresh')  # time at next scr refresh
            third_v_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(third_v_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(third_v_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if third_v_response.status == STARTED and not waitOnFlip:
            theseKeys = third_v_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _third_v_response_allKeys.extend(theseKeys)
            if len(_third_v_response_allKeys):
                third_v_response.keys = _third_v_response_allKeys[-1].name  # just the last key pressed
                third_v_response.rt = _third_v_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *third_v_response_prompt* updates
        if third_v_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            third_v_response_prompt.frameNStart = frameN  # exact frame index
            third_v_response_prompt.tStart = t  # local t and not account for scr refresh
            third_v_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_v_response_prompt, 'tStartRefresh')  # time at next scr refresh
            third_v_response_prompt.setAutoDraw(True)
        if third_v_response_prompt.status == STARTED:
            if bool(third_v_response.status==FINISHED):
                # keep track of stop time/frame for later
                third_v_response_prompt.tStop = t  # not accounting for scr refresh
                third_v_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(third_v_response_prompt, 'tStopRefresh')  # time at next scr refresh
                third_v_response_prompt.setAutoDraw(False)
        
        # *third_v_movies* updates
        if third_v_movies.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            third_v_movies.frameNStart = frameN  # exact frame index
            third_v_movies.tStart = t  # local t and not account for scr refresh
            third_v_movies.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_v_movies, 'tStartRefresh')  # time at next scr refresh
            third_v_movies.setAutoDraw(True)
        if third_v_movies.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > third_v_movies.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                third_v_movies.tStop = t  # not accounting for scr refresh
                third_v_movies.frameNStop = frameN  # exact frame index
                win.timeOnFlip(third_v_movies, 'tStopRefresh')  # time at next scr refresh
                third_v_movies.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in third_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "third_V"-------
    for thisComponent in third_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if third_v_response.keys in ['', [], None]:  # No response was made
        third_v_response.keys = None
    third_v_trials.addData('third_v_response.keys',third_v_response.keys)
    if third_v_response.keys != None:  # we had a response
        third_v_trials.addData('third_v_response.rt', third_v_response.rt)
    third_v_trials.addData('third_v_response.started', third_v_response.tStartRefresh)
    third_v_trials.addData('third_v_response.stopped', third_v_response.tStopRefresh)
    third_v_trials.addData('third_v_response_prompt.started', third_v_response_prompt.tStartRefresh)
    third_v_trials.addData('third_v_response_prompt.stopped', third_v_response_prompt.tStopRefresh)
    third_v_movies.stop()
    # the Routine "third_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    third_v_trials.addData('blank.started', blank.tStartRefresh)
    third_v_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'third_v_trials'

timestamp = time()
data_to_send = {
    "id": 20,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[18],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
third_A_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Third A.xlsx'),
    seed=None, name='third_A_trials')
thisExp.addLoop(third_A_trials)  # add the loop to the experiment
thisThird_A_trial = third_A_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisThird_A_trial.rgb)
if thisThird_A_trial != None:
    for paramName in thisThird_A_trial:
        exec('{} = thisThird_A_trial[paramName]'.format(paramName))
for thisThird_A_trial in third_A_trials:
    currentLoop = third_A_trials
    timestamp = time()
    data_to_send = {
        "id": 21,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[19],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisThird_A_trial.rgb)
    if thisThird_A_trial != None:
        for paramName in thisThird_A_trial:
            exec('{} = thisThird_A_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "third_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    third_a_stim.setSound(third_A, hamming=True)
    third_a_stim.setVolume(1.0, log=False)
    third_a_response.keys = []
    third_a_response.rt = []
    _third_a_response_allKeys = []
    SNR_file_num_3a = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_3_a.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_3a+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_3_a.setVolume(0.47, log=False)
    # keep track of which components have finished
    third_AComponents = [third_a_stim, third_a_repsonse_prompt, third_a_response, sound_3_a, black_screen_with_dot_3]
    for thisComponent in third_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    third_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "third_A"-------
    while continueRoutine:
        # get current time
        t = third_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=third_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop third_a_stim
        if third_a_stim.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            third_a_stim.frameNStart = frameN  # exact frame index
            third_a_stim.tStart = t  # local t and not account for scr refresh
            third_a_stim.tStartRefresh = tThisFlipGlobal  # on global time
            third_a_stim.play()  # start the sound (it finishes automatically)
        
        # *third_a_repsonse_prompt* updates
        if third_a_repsonse_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            third_a_repsonse_prompt.frameNStart = frameN  # exact frame index
            third_a_repsonse_prompt.tStart = t  # local t and not account for scr refresh
            third_a_repsonse_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_a_repsonse_prompt, 'tStartRefresh')  # time at next scr refresh
            third_a_repsonse_prompt.setAutoDraw(True)
        if third_a_repsonse_prompt.status == STARTED:
            if bool(third_a_response.status==FINISHED):
                # keep track of stop time/frame for later
                third_a_repsonse_prompt.tStop = t  # not accounting for scr refresh
                third_a_repsonse_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(third_a_repsonse_prompt, 'tStopRefresh')  # time at next scr refresh
                third_a_repsonse_prompt.setAutoDraw(False)
        
        # *third_a_response* updates
        waitOnFlip = False
        if third_a_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            third_a_response.frameNStart = frameN  # exact frame index
            third_a_response.tStart = t  # local t and not account for scr refresh
            third_a_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_a_response, 'tStartRefresh')  # time at next scr refresh
            third_a_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(third_a_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(third_a_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if third_a_response.status == STARTED and not waitOnFlip:
            theseKeys = third_a_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _third_a_response_allKeys.extend(theseKeys)
            if len(_third_a_response_allKeys):
                third_a_response.keys = _third_a_response_allKeys[-1].name  # just the last key pressed
                third_a_response.rt = _third_a_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_3_a
        if sound_3_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3_a.frameNStart = frameN  # exact frame index
            sound_3_a.tStart = t  # local t and not account for scr refresh
            sound_3_a.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3_a.play(when=win)  # sync with win flip
        if sound_3_a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3_a.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_3_a.tStop = t  # not accounting for scr refresh
                sound_3_a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3_a, 'tStopRefresh')  # time at next scr refresh
                sound_3_a.stop()
        
        # *black_screen_with_dot_3* updates
        if black_screen_with_dot_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_screen_with_dot_3.frameNStart = frameN  # exact frame index
            black_screen_with_dot_3.tStart = t  # local t and not account for scr refresh
            black_screen_with_dot_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_screen_with_dot_3, 'tStartRefresh')  # time at next scr refresh
            black_screen_with_dot_3.setAutoDraw(True)
        if black_screen_with_dot_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_screen_with_dot_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                black_screen_with_dot_3.tStop = t  # not accounting for scr refresh
                black_screen_with_dot_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_screen_with_dot_3, 'tStopRefresh')  # time at next scr refresh
                black_screen_with_dot_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in third_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "third_A"-------
    for thisComponent in third_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    third_a_stim.stop()  # ensure sound has stopped at end of routine
    third_A_trials.addData('third_a_stim.started', third_a_stim.tStart)
    third_A_trials.addData('third_a_stim.stopped', third_a_stim.tStop)
    third_A_trials.addData('third_a_repsonse_prompt.started', third_a_repsonse_prompt.tStartRefresh)
    third_A_trials.addData('third_a_repsonse_prompt.stopped', third_a_repsonse_prompt.tStopRefresh)
    # check responses
    if third_a_response.keys in ['', [], None]:  # No response was made
        third_a_response.keys = None
    third_A_trials.addData('third_a_response.keys',third_a_response.keys)
    if third_a_response.keys != None:  # we had a response
        third_A_trials.addData('third_a_response.rt', third_a_response.rt)
    third_A_trials.addData('third_a_response.started', third_a_response.tStartRefresh)
    third_A_trials.addData('third_a_response.stopped', third_a_response.tStopRefresh)
    sound_3_a.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_3_a.started', sound_3_a.tStartRefresh)
    thisExp.addData('sound_3_a.stopped', sound_3_a.tStopRefresh)
    third_A_trials.addData('black_screen_with_dot_3.started', black_screen_with_dot_3.tStartRefresh)
    third_A_trials.addData('black_screen_with_dot_3.stopped', black_screen_with_dot_3.tStopRefresh)
    # the Routine "third_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    third_A_trials.addData('blank.started', blank.tStartRefresh)
    third_A_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'third_A_trials'

timestamp = time()
data_to_send = {
    "id": 22,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[20],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
third_av_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Third AV.xlsx'),
    seed=None, name='third_av_trials')
thisExp.addLoop(third_av_trials)  # add the loop to the experiment
thisThird_av_trial = third_av_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisThird_av_trial.rgb)
if thisThird_av_trial != None:
    for paramName in thisThird_av_trial:
        exec('{} = thisThird_av_trial[paramName]'.format(paramName))
for thisThird_av_trial in third_av_trials:
    currentLoop = third_av_trials
    timestamp = time()
    data_to_send = {
        "id": 23,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[21],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisThird_av_trial.rgb)
    if thisThird_av_trial != None:
        for paramName in thisThird_av_trial:
            exec('{} = thisThird_av_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "third_AV"-------
    continueRoutine = True
    # update component parameters for each repeat
    third_AV_response.keys = []
    third_AV_response.rt = []
    _third_AV_response_allKeys = []
    SNR_file_num_3av = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_3_av.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_3av+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_3_av.setVolume(0.47, log=False)
    third_AV_stim = visual.MovieStim3(
        win=win, name='third_AV_stim', units='pix',
        noAudio = False,
        filename=third_AV,
        ori=0.0, pos=(0, 0), size=(720,480), opacity=None,
        loop=False, anchor='center',
        depth=-3.0,
        )
    third_AV_stim.reset()
    # keep track of which components have finished
    third_AVComponents = [third_AV_response_prompt, third_AV_response, sound_3_av, third_AV_stim]
    for thisComponent in third_AVComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    third_AVClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "third_AV"-------
    while continueRoutine:
        # get current time
        t = third_AVClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=third_AVClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *third_AV_response_prompt* updates
        if third_AV_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            third_AV_response_prompt.frameNStart = frameN  # exact frame index
            third_AV_response_prompt.tStart = t  # local t and not account for scr refresh
            third_AV_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_AV_response_prompt, 'tStartRefresh')  # time at next scr refresh
            third_AV_response_prompt.setAutoDraw(True)
        if third_AV_response_prompt.status == STARTED:
            if bool(third_AV_response.status==FINISHED):
                # keep track of stop time/frame for later
                third_AV_response_prompt.tStop = t  # not accounting for scr refresh
                third_AV_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(third_AV_response_prompt, 'tStopRefresh')  # time at next scr refresh
                third_AV_response_prompt.setAutoDraw(False)
        
        # *third_AV_response* updates
        waitOnFlip = False
        if third_AV_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            third_AV_response.frameNStart = frameN  # exact frame index
            third_AV_response.tStart = t  # local t and not account for scr refresh
            third_AV_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_AV_response, 'tStartRefresh')  # time at next scr refresh
            third_AV_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(third_AV_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(third_AV_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if third_AV_response.status == STARTED and not waitOnFlip:
            theseKeys = third_AV_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _third_AV_response_allKeys.extend(theseKeys)
            if len(_third_AV_response_allKeys):
                third_AV_response.keys = _third_AV_response_allKeys[-1].name  # just the last key pressed
                third_AV_response.rt = _third_AV_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_3_av
        if sound_3_av.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3_av.frameNStart = frameN  # exact frame index
            sound_3_av.tStart = t  # local t and not account for scr refresh
            sound_3_av.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3_av.play(when=win)  # sync with win flip
        if sound_3_av.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3_av.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_3_av.tStop = t  # not accounting for scr refresh
                sound_3_av.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3_av, 'tStopRefresh')  # time at next scr refresh
                sound_3_av.stop()
        
        # *third_AV_stim* updates
        if third_AV_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            third_AV_stim.frameNStart = frameN  # exact frame index
            third_AV_stim.tStart = t  # local t and not account for scr refresh
            third_AV_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_AV_stim, 'tStartRefresh')  # time at next scr refresh
            third_AV_stim.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in third_AVComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "third_AV"-------
    for thisComponent in third_AVComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    third_av_trials.addData('third_AV_response_prompt.started', third_AV_response_prompt.tStartRefresh)
    third_av_trials.addData('third_AV_response_prompt.stopped', third_AV_response_prompt.tStopRefresh)
    # check responses
    if third_AV_response.keys in ['', [], None]:  # No response was made
        third_AV_response.keys = None
    third_av_trials.addData('third_AV_response.keys',third_AV_response.keys)
    if third_AV_response.keys != None:  # we had a response
        third_av_trials.addData('third_AV_response.rt', third_AV_response.rt)
    third_av_trials.addData('third_AV_response.started', third_AV_response.tStartRefresh)
    third_av_trials.addData('third_AV_response.stopped', third_AV_response.tStopRefresh)
    sound_3_av.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_3_av.started', sound_3_av.tStartRefresh)
    thisExp.addData('sound_3_av.stopped', sound_3_av.tStopRefresh)
    third_AV_stim.stop()
    # the Routine "third_AV" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    third_av_trials.addData('blank.started', blank.tStartRefresh)
    third_av_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'third_av_trials'

timestamp = time()
data_to_send = {
    "id": 24,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[22],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
third_w_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Third W.xlsx'),
    seed=None, name='third_w_trials')
thisExp.addLoop(third_w_trials)  # add the loop to the experiment
thisThird_w_trial = third_w_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisThird_w_trial.rgb)
if thisThird_w_trial != None:
    for paramName in thisThird_w_trial:
        exec('{} = thisThird_w_trial[paramName]'.format(paramName))
for thisThird_w_trial in third_w_trials:
    currentLoop = third_w_trials
    timestamp = time()
    data_to_send = {
        "id": 25,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[23],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisThird_w_trial.rgb)
    if thisThird_w_trial != None:
        for paramName in thisThird_w_trial:
            exec('{} = thisThird_w_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "third_written"-------
    continueRoutine = True
    # update component parameters for each repeat
    third_writ_response.keys = []
    third_writ_response.rt = []
    _third_writ_response_allKeys = []
    third_w_stim.setText(third_W)
    # keep track of which components have finished
    third_writtenComponents = [third_writ_response, third_w_stim, third_response_prompt]
    for thisComponent in third_writtenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    third_writtenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "third_written"-------
    while continueRoutine:
        # get current time
        t = third_writtenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=third_writtenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *third_writ_response* updates
        waitOnFlip = False
        if third_writ_response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            third_writ_response.frameNStart = frameN  # exact frame index
            third_writ_response.tStart = t  # local t and not account for scr refresh
            third_writ_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_writ_response, 'tStartRefresh')  # time at next scr refresh
            third_writ_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(third_writ_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(third_writ_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if third_writ_response.status == STARTED and not waitOnFlip:
            theseKeys = third_writ_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _third_writ_response_allKeys.extend(theseKeys)
            if len(_third_writ_response_allKeys):
                third_writ_response.keys = _third_writ_response_allKeys[-1].name  # just the last key pressed
                third_writ_response.rt = _third_writ_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *third_w_stim* updates
        if third_w_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            third_w_stim.frameNStart = frameN  # exact frame index
            third_w_stim.tStart = t  # local t and not account for scr refresh
            third_w_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_w_stim, 'tStartRefresh')  # time at next scr refresh
            third_w_stim.setAutoDraw(True)
        if third_w_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > third_w_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                third_w_stim.tStop = t  # not accounting for scr refresh
                third_w_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(third_w_stim, 'tStopRefresh')  # time at next scr refresh
                third_w_stim.setAutoDraw(False)
        
        # *third_response_prompt* updates
        if third_response_prompt.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            third_response_prompt.frameNStart = frameN  # exact frame index
            third_response_prompt.tStart = t  # local t and not account for scr refresh
            third_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_response_prompt, 'tStartRefresh')  # time at next scr refresh
            third_response_prompt.setAutoDraw(True)
        if third_response_prompt.status == STARTED:
            if bool(third_writ_response.status==FINISHED):
                # keep track of stop time/frame for later
                third_response_prompt.tStop = t  # not accounting for scr refresh
                third_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(third_response_prompt, 'tStopRefresh')  # time at next scr refresh
                third_response_prompt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in third_writtenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "third_written"-------
    for thisComponent in third_writtenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if third_writ_response.keys in ['', [], None]:  # No response was made
        third_writ_response.keys = None
    third_w_trials.addData('third_writ_response.keys',third_writ_response.keys)
    if third_writ_response.keys != None:  # we had a response
        third_w_trials.addData('third_writ_response.rt', third_writ_response.rt)
    third_w_trials.addData('third_writ_response.started', third_writ_response.tStartRefresh)
    third_w_trials.addData('third_writ_response.stopped', third_writ_response.tStopRefresh)
    third_w_trials.addData('third_w_stim.started', third_w_stim.tStartRefresh)
    third_w_trials.addData('third_w_stim.stopped', third_w_stim.tStopRefresh)
    third_w_trials.addData('third_response_prompt.started', third_response_prompt.tStartRefresh)
    third_w_trials.addData('third_response_prompt.stopped', third_response_prompt.tStopRefresh)
    # the Routine "third_written" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    third_w_trials.addData('blank.started', blank.tStartRefresh)
    third_w_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'third_w_trials'

timestamp = time()
data_to_send = {
    "id": 26,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[24],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fourth_v_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fourth V.xlsx'),
    seed=None, name='fourth_v_trials')
thisExp.addLoop(fourth_v_trials)  # add the loop to the experiment
thisFourth_v_trial = fourth_v_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFourth_v_trial.rgb)
if thisFourth_v_trial != None:
    for paramName in thisFourth_v_trial:
        exec('{} = thisFourth_v_trial[paramName]'.format(paramName))
for thisFourth_v_trial in fourth_v_trials:
    currentLoop = fourth_v_trials
    timestamp = time()
    data_to_send = {
        "id": 27,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[25],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFourth_v_trial.rgb)
    if thisFourth_v_trial != None:
        for paramName in thisFourth_v_trial:
            exec('{} = thisFourth_v_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "fourth_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    fourth_v_response.keys = []
    fourth_v_response.rt = []
    _fourth_v_response_allKeys = []
    fourth_v_movies = visual.MovieStim3(
        win=win, name='fourth_v_movies', units='pix',
        noAudio = True,
        filename=fourth_V,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False, anchor='center',
        depth=-1.0,
        )
    # keep track of which components have finished
    fourth_VComponents = [fourth_v_response, fourth_v_movies, fourth_v_response_prompt]
    for thisComponent in fourth_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fourth_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fourth_V"-------
    while continueRoutine:
        # get current time
        t = fourth_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fourth_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fourth_v_response* updates
        waitOnFlip = False
        if fourth_v_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_v_response.frameNStart = frameN  # exact frame index
            fourth_v_response.tStart = t  # local t and not account for scr refresh
            fourth_v_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_v_response, 'tStartRefresh')  # time at next scr refresh
            fourth_v_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fourth_v_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fourth_v_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fourth_v_response.status == STARTED and not waitOnFlip:
            theseKeys = fourth_v_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fourth_v_response_allKeys.extend(theseKeys)
            if len(_fourth_v_response_allKeys):
                fourth_v_response.keys = _fourth_v_response_allKeys[-1].name  # just the last key pressed
                fourth_v_response.rt = _fourth_v_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fourth_v_movies* updates
        if fourth_v_movies.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_v_movies.frameNStart = frameN  # exact frame index
            fourth_v_movies.tStart = t  # local t and not account for scr refresh
            fourth_v_movies.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_v_movies, 'tStartRefresh')  # time at next scr refresh
            fourth_v_movies.setAutoDraw(True)
        if fourth_v_movies.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fourth_v_movies.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fourth_v_movies.tStop = t  # not accounting for scr refresh
                fourth_v_movies.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fourth_v_movies, 'tStopRefresh')  # time at next scr refresh
                fourth_v_movies.setAutoDraw(False)
        
        # *fourth_v_response_prompt* updates
        if fourth_v_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_v_response_prompt.frameNStart = frameN  # exact frame index
            fourth_v_response_prompt.tStart = t  # local t and not account for scr refresh
            fourth_v_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_v_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fourth_v_response_prompt.setAutoDraw(True)
        if fourth_v_response_prompt.status == STARTED:
            if bool(fourth_v_response.status==FINISHED):
                # keep track of stop time/frame for later
                fourth_v_response_prompt.tStop = t  # not accounting for scr refresh
                fourth_v_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fourth_v_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fourth_v_response_prompt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fourth_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fourth_V"-------
    for thisComponent in fourth_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if fourth_v_response.keys in ['', [], None]:  # No response was made
        fourth_v_response.keys = None
    fourth_v_trials.addData('fourth_v_response.keys',fourth_v_response.keys)
    if fourth_v_response.keys != None:  # we had a response
        fourth_v_trials.addData('fourth_v_response.rt', fourth_v_response.rt)
    fourth_v_trials.addData('fourth_v_response.started', fourth_v_response.tStartRefresh)
    fourth_v_trials.addData('fourth_v_response.stopped', fourth_v_response.tStopRefresh)
    fourth_v_movies.stop()
    fourth_v_trials.addData('fourth_v_response_prompt.started', fourth_v_response_prompt.tStartRefresh)
    fourth_v_trials.addData('fourth_v_response_prompt.stopped', fourth_v_response_prompt.tStopRefresh)
    # the Routine "fourth_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourth_v_trials.addData('blank.started', blank.tStartRefresh)
    fourth_v_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fourth_v_trials'

timestamp = time()
data_to_send = {
    "id": 28,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[26],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fourth_w_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fourth W.xlsx'),
    seed=None, name='fourth_w_trials')
thisExp.addLoop(fourth_w_trials)  # add the loop to the experiment
thisFourth_w_trial = fourth_w_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFourth_w_trial.rgb)
if thisFourth_w_trial != None:
    for paramName in thisFourth_w_trial:
        exec('{} = thisFourth_w_trial[paramName]'.format(paramName))
for thisFourth_w_trial in fourth_w_trials:
    currentLoop = fourth_w_trials
    timestamp = time()
    data_to_send = {
        "id": 29,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[27],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFourth_w_trial.rgb)
    if thisFourth_w_trial != None:
        for paramName in thisFourth_w_trial:
            exec('{} = thisFourth_w_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "fourth_written"-------
    continueRoutine = True
    # update component parameters for each repeat
    fourth_writ_response.keys = []
    fourth_writ_response.rt = []
    _fourth_writ_response_allKeys = []
    fourth_w_stim.setText(fourth_W)
    # keep track of which components have finished
    fourth_writtenComponents = [fourth_writ_response, fourth_response_prompt, fourth_w_stim]
    for thisComponent in fourth_writtenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fourth_writtenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fourth_written"-------
    while continueRoutine:
        # get current time
        t = fourth_writtenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fourth_writtenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fourth_writ_response* updates
        waitOnFlip = False
        if fourth_writ_response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            fourth_writ_response.frameNStart = frameN  # exact frame index
            fourth_writ_response.tStart = t  # local t and not account for scr refresh
            fourth_writ_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_writ_response, 'tStartRefresh')  # time at next scr refresh
            fourth_writ_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fourth_writ_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fourth_writ_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fourth_writ_response.status == STARTED and not waitOnFlip:
            theseKeys = fourth_writ_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fourth_writ_response_allKeys.extend(theseKeys)
            if len(_fourth_writ_response_allKeys):
                fourth_writ_response.keys = _fourth_writ_response_allKeys[-1].name  # just the last key pressed
                fourth_writ_response.rt = _fourth_writ_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fourth_response_prompt* updates
        if fourth_response_prompt.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            fourth_response_prompt.frameNStart = frameN  # exact frame index
            fourth_response_prompt.tStart = t  # local t and not account for scr refresh
            fourth_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fourth_response_prompt.setAutoDraw(True)
        if fourth_response_prompt.status == STARTED:
            if bool(fourth_writ_response.status==FINISHED):
                # keep track of stop time/frame for later
                fourth_response_prompt.tStop = t  # not accounting for scr refresh
                fourth_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fourth_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fourth_response_prompt.setAutoDraw(False)
        
        # *fourth_w_stim* updates
        if fourth_w_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_w_stim.frameNStart = frameN  # exact frame index
            fourth_w_stim.tStart = t  # local t and not account for scr refresh
            fourth_w_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_w_stim, 'tStartRefresh')  # time at next scr refresh
            fourth_w_stim.setAutoDraw(True)
        if fourth_w_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fourth_w_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fourth_w_stim.tStop = t  # not accounting for scr refresh
                fourth_w_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fourth_w_stim, 'tStopRefresh')  # time at next scr refresh
                fourth_w_stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fourth_writtenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fourth_written"-------
    for thisComponent in fourth_writtenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if fourth_writ_response.keys in ['', [], None]:  # No response was made
        fourth_writ_response.keys = None
    fourth_w_trials.addData('fourth_writ_response.keys',fourth_writ_response.keys)
    if fourth_writ_response.keys != None:  # we had a response
        fourth_w_trials.addData('fourth_writ_response.rt', fourth_writ_response.rt)
    fourth_w_trials.addData('fourth_writ_response.started', fourth_writ_response.tStartRefresh)
    fourth_w_trials.addData('fourth_writ_response.stopped', fourth_writ_response.tStopRefresh)
    fourth_w_trials.addData('fourth_response_prompt.started', fourth_response_prompt.tStartRefresh)
    fourth_w_trials.addData('fourth_response_prompt.stopped', fourth_response_prompt.tStopRefresh)
    fourth_w_trials.addData('fourth_w_stim.started', fourth_w_stim.tStartRefresh)
    fourth_w_trials.addData('fourth_w_stim.stopped', fourth_w_stim.tStopRefresh)
    # the Routine "fourth_written" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourth_w_trials.addData('blank.started', blank.tStartRefresh)
    fourth_w_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fourth_w_trials'

timestamp = time()
data_to_send = {
    "id": 30,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[28],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fourth_a_response = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fourth A.xlsx'),
    seed=None, name='fourth_a_response')
thisExp.addLoop(fourth_a_response)  # add the loop to the experiment
thisFourth_a_response = fourth_a_response.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFourth_a_response.rgb)
if thisFourth_a_response != None:
    for paramName in thisFourth_a_response:
        exec('{} = thisFourth_a_response[paramName]'.format(paramName))
for thisFourth_a_response in fourth_a_response:
    currentLoop = fourth_a_response
    timestamp = time()
    data_to_send = {
        "id": 31,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[29],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFourth_a_response.rgb)
    if thisFourth_a_response != None:
        for paramName in thisFourth_a_response:
            exec('{} = thisFourth_a_response[paramName]'.format(paramName))

    # ------Prepare to start Routine "fourth_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    fourth_a_response_.keys = []
    fourth_a_response_.rt = []
    _fourth_a_response__allKeys = []
    SNR_file_num_4a = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_4_a.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_4a+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_4_a.setVolume(0.47, log=False)
    fourth_a_stim.setSound(fourth_A, hamming=True)
    fourth_a_stim.setVolume(1.0, log=False)
    # keep track of which components have finished
    fourth_AComponents = [fourth_a_response_, fourth_a_response_prompt, black_screen_with_dot_4, sound_4_a, fourth_a_stim]
    for thisComponent in fourth_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fourth_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fourth_A"-------
    while continueRoutine:
        # get current time
        t = fourth_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fourth_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fourth_a_response_* updates
        waitOnFlip = False
        if fourth_a_response_.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_a_response_.frameNStart = frameN  # exact frame index
            fourth_a_response_.tStart = t  # local t and not account for scr refresh
            fourth_a_response_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_a_response_, 'tStartRefresh')  # time at next scr refresh
            fourth_a_response_.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fourth_a_response_.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fourth_a_response_.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fourth_a_response_.status == STARTED and not waitOnFlip:
            theseKeys = fourth_a_response_.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fourth_a_response__allKeys.extend(theseKeys)
            if len(_fourth_a_response__allKeys):
                fourth_a_response_.keys = _fourth_a_response__allKeys[-1].name  # just the last key pressed
                fourth_a_response_.rt = _fourth_a_response__allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fourth_a_response_prompt* updates
        if fourth_a_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_a_response_prompt.frameNStart = frameN  # exact frame index
            fourth_a_response_prompt.tStart = t  # local t and not account for scr refresh
            fourth_a_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_a_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fourth_a_response_prompt.setAutoDraw(True)
        if fourth_a_response_prompt.status == STARTED:
            if bool(fourth_a_response_.status==FINISHED):
                # keep track of stop time/frame for later
                fourth_a_response_prompt.tStop = t  # not accounting for scr refresh
                fourth_a_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fourth_a_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fourth_a_response_prompt.setAutoDraw(False)
        
        # *black_screen_with_dot_4* updates
        if black_screen_with_dot_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_screen_with_dot_4.frameNStart = frameN  # exact frame index
            black_screen_with_dot_4.tStart = t  # local t and not account for scr refresh
            black_screen_with_dot_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_screen_with_dot_4, 'tStartRefresh')  # time at next scr refresh
            black_screen_with_dot_4.setAutoDraw(True)
        if black_screen_with_dot_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_screen_with_dot_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                black_screen_with_dot_4.tStop = t  # not accounting for scr refresh
                black_screen_with_dot_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_screen_with_dot_4, 'tStopRefresh')  # time at next scr refresh
                black_screen_with_dot_4.setAutoDraw(False)
        # start/stop sound_4_a
        if sound_4_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_4_a.frameNStart = frameN  # exact frame index
            sound_4_a.tStart = t  # local t and not account for scr refresh
            sound_4_a.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4_a.play(when=win)  # sync with win flip
        if sound_4_a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4_a.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_4_a.tStop = t  # not accounting for scr refresh
                sound_4_a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4_a, 'tStopRefresh')  # time at next scr refresh
                sound_4_a.stop()
        # start/stop fourth_a_stim
        if fourth_a_stim.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_a_stim.frameNStart = frameN  # exact frame index
            fourth_a_stim.tStart = t  # local t and not account for scr refresh
            fourth_a_stim.tStartRefresh = tThisFlipGlobal  # on global time
            fourth_a_stim.play()  # start the sound (it finishes automatically)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fourth_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fourth_A"-------
    for thisComponent in fourth_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if fourth_a_response_.keys in ['', [], None]:  # No response was made
        fourth_a_response_.keys = None
    fourth_a_response.addData('fourth_a_response_.keys',fourth_a_response_.keys)
    if fourth_a_response_.keys != None:  # we had a response
        fourth_a_response.addData('fourth_a_response_.rt', fourth_a_response_.rt)
    fourth_a_response.addData('fourth_a_response_.started', fourth_a_response_.tStartRefresh)
    fourth_a_response.addData('fourth_a_response_.stopped', fourth_a_response_.tStopRefresh)
    fourth_a_response.addData('fourth_a_response_prompt.started', fourth_a_response_prompt.tStartRefresh)
    fourth_a_response.addData('fourth_a_response_prompt.stopped', fourth_a_response_prompt.tStopRefresh)
    fourth_a_response.addData('black_screen_with_dot_4.started', black_screen_with_dot_4.tStartRefresh)
    fourth_a_response.addData('black_screen_with_dot_4.stopped', black_screen_with_dot_4.tStopRefresh)
    sound_4_a.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_4_a.started', sound_4_a.tStartRefresh)
    thisExp.addData('sound_4_a.stopped', sound_4_a.tStopRefresh)
    fourth_a_stim.stop()  # ensure sound has stopped at end of routine
    fourth_a_response.addData('fourth_a_stim.started', fourth_a_stim.tStart)
    fourth_a_response.addData('fourth_a_stim.stopped', fourth_a_stim.tStop)
    # the Routine "fourth_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourth_a_response.addData('blank.started', blank.tStartRefresh)
    fourth_a_response.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fourth_a_response'

timestamp = time()
data_to_send = {
    "id": 32,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[30],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fourth_AV_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fourth AV.xlsx'),
    seed=None, name='fourth_AV_trials')
thisExp.addLoop(fourth_AV_trials)  # add the loop to the experiment
thisFourth_AV_trial = fourth_AV_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFourth_AV_trial.rgb)
if thisFourth_AV_trial != None:
    for paramName in thisFourth_AV_trial:
        exec('{} = thisFourth_AV_trial[paramName]'.format(paramName))
for thisFourth_AV_trial in fourth_AV_trials:
    currentLoop = fourth_AV_trials
    timestamp = time()
    data_to_send = {
        "id": 33,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[31],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFourth_AV_trial.rgb)
    if thisFourth_AV_trial != None:
        for paramName in thisFourth_AV_trial:
            exec('{} = thisFourth_AV_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "fourth_AV_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    fourth_AV_stim = visual.MovieStim3(
        win=win, name='fourth_AV_stim', units='pix',
        noAudio = False,
        filename=fourth_AV,
        ori=0.0, pos=(0, 0), size=(720,480), opacity=None,
        loop=False, anchor='center',
        depth=-1.0,
        )
    fourth_AV_stim.reset()
    SNR_file_num_4av = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_4_av.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_4av+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_4_av.setVolume(0.47, log=False)
    fourth_AV_response.keys = []
    fourth_AV_response.rt = []
    _fourth_AV_response_allKeys = []
    # keep track of which components have finished
    fourth_AV_3Components = [fourth_AV_response_prompt, fourth_AV_stim, sound_4_av, fourth_AV_response]
    for thisComponent in fourth_AV_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fourth_AV_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fourth_AV_3"-------
    while continueRoutine:
        # get current time
        t = fourth_AV_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fourth_AV_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fourth_AV_response_prompt* updates
        if fourth_AV_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_AV_response_prompt.frameNStart = frameN  # exact frame index
            fourth_AV_response_prompt.tStart = t  # local t and not account for scr refresh
            fourth_AV_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_AV_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fourth_AV_response_prompt.setAutoDraw(True)
        if fourth_AV_response_prompt.status == STARTED:
            if bool(fourth_AV_response.status==FINISHED):
                # keep track of stop time/frame for later
                fourth_AV_response_prompt.tStop = t  # not accounting for scr refresh
                fourth_AV_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fourth_AV_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fourth_AV_response_prompt.setAutoDraw(False)
        
        # *fourth_AV_stim* updates
        if fourth_AV_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_AV_stim.frameNStart = frameN  # exact frame index
            fourth_AV_stim.tStart = t  # local t and not account for scr refresh
            fourth_AV_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_AV_stim, 'tStartRefresh')  # time at next scr refresh
            fourth_AV_stim.setAutoDraw(True)
        # start/stop sound_4_av
        if sound_4_av.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_4_av.frameNStart = frameN  # exact frame index
            sound_4_av.tStart = t  # local t and not account for scr refresh
            sound_4_av.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4_av.play(when=win)  # sync with win flip
        if sound_4_av.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4_av.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_4_av.tStop = t  # not accounting for scr refresh
                sound_4_av.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4_av, 'tStopRefresh')  # time at next scr refresh
                sound_4_av.stop()
        
        # *fourth_AV_response* updates
        waitOnFlip = False
        if fourth_AV_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fourth_AV_response.frameNStart = frameN  # exact frame index
            fourth_AV_response.tStart = t  # local t and not account for scr refresh
            fourth_AV_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourth_AV_response, 'tStartRefresh')  # time at next scr refresh
            fourth_AV_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fourth_AV_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fourth_AV_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fourth_AV_response.status == STARTED and not waitOnFlip:
            theseKeys = fourth_AV_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fourth_AV_response_allKeys.extend(theseKeys)
            if len(_fourth_AV_response_allKeys):
                fourth_AV_response.keys = _fourth_AV_response_allKeys[-1].name  # just the last key pressed
                fourth_AV_response.rt = _fourth_AV_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fourth_AV_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fourth_AV_3"-------
    for thisComponent in fourth_AV_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourth_AV_trials.addData('fourth_AV_response_prompt.started', fourth_AV_response_prompt.tStartRefresh)
    fourth_AV_trials.addData('fourth_AV_response_prompt.stopped', fourth_AV_response_prompt.tStopRefresh)
    fourth_AV_stim.stop()
    sound_4_av.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_4_av.started', sound_4_av.tStartRefresh)
    thisExp.addData('sound_4_av.stopped', sound_4_av.tStopRefresh)
    # check responses
    if fourth_AV_response.keys in ['', [], None]:  # No response was made
        fourth_AV_response.keys = None
    fourth_AV_trials.addData('fourth_AV_response.keys',fourth_AV_response.keys)
    if fourth_AV_response.keys != None:  # we had a response
        fourth_AV_trials.addData('fourth_AV_response.rt', fourth_AV_response.rt)
    fourth_AV_trials.addData('fourth_AV_response.started', fourth_AV_response.tStartRefresh)
    fourth_AV_trials.addData('fourth_AV_response.stopped', fourth_AV_response.tStopRefresh)
    # the Routine "fourth_AV_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourth_AV_trials.addData('blank.started', blank.tStartRefresh)
    fourth_AV_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fourth_AV_trials'

timestamp = time()
data_to_send = {
    "id": 34,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[32],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fifth_w_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fifth W.xlsx'),
    seed=None, name='fifth_w_trials')
thisExp.addLoop(fifth_w_trials)  # add the loop to the experiment
thisFifth_w_trial = fifth_w_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFifth_w_trial.rgb)
if thisFifth_w_trial != None:
    for paramName in thisFifth_w_trial:
        exec('{} = thisFifth_w_trial[paramName]'.format(paramName))
for thisFifth_w_trial in fifth_w_trials:
    currentLoop = fifth_w_trials
    timestamp = time()
    data_to_send = {
        "id": 35,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[33],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFifth_w_trial.rgb)
    if thisFifth_w_trial != None:
        for paramName in thisFifth_w_trial:
            exec('{} = thisFifth_w_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "fifth_written"-------
    continueRoutine = True
    # update component parameters for each repeat
    fifth_writ_response.keys = []
    fifth_writ_response.rt = []
    _fifth_writ_response_allKeys = []
    fifth_w_stim.setText(fifth_W)
    # keep track of which components have finished
    fifth_writtenComponents = [fifth_response_prompt, fifth_writ_response, fifth_w_stim]
    for thisComponent in fifth_writtenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fifth_writtenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fifth_written"-------
    while continueRoutine:
        # get current time
        t = fifth_writtenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fifth_writtenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fifth_response_prompt* updates
        if fifth_response_prompt.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            fifth_response_prompt.frameNStart = frameN  # exact frame index
            fifth_response_prompt.tStart = t  # local t and not account for scr refresh
            fifth_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fifth_response_prompt.setAutoDraw(True)
        if fifth_response_prompt.status == STARTED:
            if bool(fifth_writ_response.status==FINISHED):
                # keep track of stop time/frame for later
                fifth_response_prompt.tStop = t  # not accounting for scr refresh
                fifth_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fifth_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fifth_response_prompt.setAutoDraw(False)
        
        # *fifth_writ_response* updates
        waitOnFlip = False
        if fifth_writ_response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            fifth_writ_response.frameNStart = frameN  # exact frame index
            fifth_writ_response.tStart = t  # local t and not account for scr refresh
            fifth_writ_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_writ_response, 'tStartRefresh')  # time at next scr refresh
            fifth_writ_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fifth_writ_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fifth_writ_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fifth_writ_response.status == STARTED and not waitOnFlip:
            theseKeys = fifth_writ_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fifth_writ_response_allKeys.extend(theseKeys)
            if len(_fifth_writ_response_allKeys):
                fifth_writ_response.keys = _fifth_writ_response_allKeys[-1].name  # just the last key pressed
                fifth_writ_response.rt = _fifth_writ_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fifth_w_stim* updates
        if fifth_w_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_w_stim.frameNStart = frameN  # exact frame index
            fifth_w_stim.tStart = t  # local t and not account for scr refresh
            fifth_w_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_w_stim, 'tStartRefresh')  # time at next scr refresh
            fifth_w_stim.setAutoDraw(True)
        if fifth_w_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fifth_w_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fifth_w_stim.tStop = t  # not accounting for scr refresh
                fifth_w_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fifth_w_stim, 'tStopRefresh')  # time at next scr refresh
                fifth_w_stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fifth_writtenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fifth_written"-------
    for thisComponent in fifth_writtenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fifth_w_trials.addData('fifth_response_prompt.started', fifth_response_prompt.tStartRefresh)
    fifth_w_trials.addData('fifth_response_prompt.stopped', fifth_response_prompt.tStopRefresh)
    # check responses
    if fifth_writ_response.keys in ['', [], None]:  # No response was made
        fifth_writ_response.keys = None
    fifth_w_trials.addData('fifth_writ_response.keys',fifth_writ_response.keys)
    if fifth_writ_response.keys != None:  # we had a response
        fifth_w_trials.addData('fifth_writ_response.rt', fifth_writ_response.rt)
    fifth_w_trials.addData('fifth_writ_response.started', fifth_writ_response.tStartRefresh)
    fifth_w_trials.addData('fifth_writ_response.stopped', fifth_writ_response.tStopRefresh)
    fifth_w_trials.addData('fifth_w_stim.started', fifth_w_stim.tStartRefresh)
    fifth_w_trials.addData('fifth_w_stim.stopped', fifth_w_stim.tStopRefresh)
    # the Routine "fifth_written" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fifth_w_trials.addData('blank.started', blank.tStartRefresh)
    fifth_w_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fifth_w_trials'

timestamp = time()
data_to_send = {
    "id": 36,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[34],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fifth_AV_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fifth AV.xlsx'),
    seed=None, name='fifth_AV_trials')
thisExp.addLoop(fifth_AV_trials)  # add the loop to the experiment
thisFifth_AV_trial = fifth_AV_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFifth_AV_trial.rgb)
if thisFifth_AV_trial != None:
    for paramName in thisFifth_AV_trial:
        exec('{} = thisFifth_AV_trial[paramName]'.format(paramName))
for thisFifth_AV_trial in fifth_AV_trials:
    currentLoop = fifth_AV_trials
    timestamp = time()
    data_to_send = {
        "id": 37,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[35],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFifth_AV_trial.rgb)
    if thisFifth_AV_trial != None:
        for paramName in thisFifth_AV_trial:
            exec('{} = thisFifth_AV_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "fifth_AV"-------
    continueRoutine = True
    # update component parameters for each repeat
    fifth_AV_response.keys = []
    fifth_AV_response.rt = []
    _fifth_AV_response_allKeys = []
    SNR_file_num_5av = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_5_av.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_5av+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_5_av.setVolume(0.47, log=False)
    fifth_AV_stim = visual.MovieStim3(
        win=win, name='fifth_AV_stim', units='pix',
        noAudio = False,
        filename=fifth_AV,
        ori=0.0, pos=(0, 0), size=(720,480), opacity=None,
        loop=False, anchor='center',
        depth=-3.0,
        )
    fifth_AV_stim.reset()
    # keep track of which components have finished
    fifth_AVComponents = [fifth_AV_response_prompt, fifth_AV_response, sound_5_av, fifth_AV_stim]
    for thisComponent in fifth_AVComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fifth_AVClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fifth_AV"-------
    while continueRoutine:
        # get current time
        t = fifth_AVClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fifth_AVClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fifth_AV_response_prompt* updates
        if fifth_AV_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_AV_response_prompt.frameNStart = frameN  # exact frame index
            fifth_AV_response_prompt.tStart = t  # local t and not account for scr refresh
            fifth_AV_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_AV_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fifth_AV_response_prompt.setAutoDraw(True)
        if fifth_AV_response_prompt.status == STARTED:
            if bool(fifth_AV_response.status==FINISHED):
                # keep track of stop time/frame for later
                fifth_AV_response_prompt.tStop = t  # not accounting for scr refresh
                fifth_AV_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fifth_AV_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fifth_AV_response_prompt.setAutoDraw(False)
        
        # *fifth_AV_response* updates
        waitOnFlip = False
        if fifth_AV_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_AV_response.frameNStart = frameN  # exact frame index
            fifth_AV_response.tStart = t  # local t and not account for scr refresh
            fifth_AV_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_AV_response, 'tStartRefresh')  # time at next scr refresh
            fifth_AV_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fifth_AV_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fifth_AV_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fifth_AV_response.status == STARTED and not waitOnFlip:
            theseKeys = fifth_AV_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fifth_AV_response_allKeys.extend(theseKeys)
            if len(_fifth_AV_response_allKeys):
                fifth_AV_response.keys = _fifth_AV_response_allKeys[-1].name  # just the last key pressed
                fifth_AV_response.rt = _fifth_AV_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_5_av
        if sound_5_av.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5_av.frameNStart = frameN  # exact frame index
            sound_5_av.tStart = t  # local t and not account for scr refresh
            sound_5_av.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5_av.play(when=win)  # sync with win flip
        if sound_5_av.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5_av.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_5_av.tStop = t  # not accounting for scr refresh
                sound_5_av.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5_av, 'tStopRefresh')  # time at next scr refresh
                sound_5_av.stop()
        
        # *fifth_AV_stim* updates
        if fifth_AV_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_AV_stim.frameNStart = frameN  # exact frame index
            fifth_AV_stim.tStart = t  # local t and not account for scr refresh
            fifth_AV_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_AV_stim, 'tStartRefresh')  # time at next scr refresh
            fifth_AV_stim.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fifth_AVComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fifth_AV"-------
    for thisComponent in fifth_AVComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fifth_AV_trials.addData('fifth_AV_response_prompt.started', fifth_AV_response_prompt.tStartRefresh)
    fifth_AV_trials.addData('fifth_AV_response_prompt.stopped', fifth_AV_response_prompt.tStopRefresh)
    # check responses
    if fifth_AV_response.keys in ['', [], None]:  # No response was made
        fifth_AV_response.keys = None
    fifth_AV_trials.addData('fifth_AV_response.keys',fifth_AV_response.keys)
    if fifth_AV_response.keys != None:  # we had a response
        fifth_AV_trials.addData('fifth_AV_response.rt', fifth_AV_response.rt)
    fifth_AV_trials.addData('fifth_AV_response.started', fifth_AV_response.tStartRefresh)
    fifth_AV_trials.addData('fifth_AV_response.stopped', fifth_AV_response.tStopRefresh)
    sound_5_av.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_5_av.started', sound_5_av.tStartRefresh)
    thisExp.addData('sound_5_av.stopped', sound_5_av.tStopRefresh)
    fifth_AV_stim.stop()
    # the Routine "fifth_AV" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fifth_AV_trials.addData('blank.started', blank.tStartRefresh)
    fifth_AV_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fifth_AV_trials'

timestamp = time()
data_to_send = {
    "id": 38,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[36],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fifth_V_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fifth V.xlsx'),
    seed=None, name='fifth_V_trials')
thisExp.addLoop(fifth_V_trials)  # add the loop to the experiment
thisFifth_V_trial = fifth_V_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFifth_V_trial.rgb)
if thisFifth_V_trial != None:
    for paramName in thisFifth_V_trial:
        exec('{} = thisFifth_V_trial[paramName]'.format(paramName))
for thisFifth_V_trial in fifth_V_trials:
    currentLoop = fifth_V_trials
    timestamp = time()
    data_to_send = {
        "id": 39,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[37],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFifth_V_trial.rgb)
    if thisFifth_V_trial != None:
        for paramName in thisFifth_V_trial:
            exec('{} = thisFifth_V_trial[paramName]'.format(paramName))
            
    # ------Prepare to start Routine "fifth_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    fifth_v_response.keys = []
    fifth_v_response.rt = []
    _fifth_v_response_allKeys = []
    fifth_v_movies = visual.MovieStim3(
        win=win, name='fifth_v_movies', units='pix',
        noAudio = True,
        filename=fifth_V,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False, anchor='center',
        depth=-2.0,
        )
    # keep track of which components have finished
    fifth_VComponents = [fifth_v_response_prompt, fifth_v_response, fifth_v_movies]
    for thisComponent in fifth_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fifth_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fifth_V"-------
    while continueRoutine:
        # get current time
        t = fifth_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fifth_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fifth_v_response_prompt* updates
        if fifth_v_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_v_response_prompt.frameNStart = frameN  # exact frame index
            fifth_v_response_prompt.tStart = t  # local t and not account for scr refresh
            fifth_v_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_v_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fifth_v_response_prompt.setAutoDraw(True)
        if fifth_v_response_prompt.status == STARTED:
            if bool(fifth_v_response.status==FINISHED):
                # keep track of stop time/frame for later
                fifth_v_response_prompt.tStop = t  # not accounting for scr refresh
                fifth_v_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fifth_v_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fifth_v_response_prompt.setAutoDraw(False)
        
        # *fifth_v_response* updates
        waitOnFlip = False
        if fifth_v_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_v_response.frameNStart = frameN  # exact frame index
            fifth_v_response.tStart = t  # local t and not account for scr refresh
            fifth_v_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_v_response, 'tStartRefresh')  # time at next scr refresh
            fifth_v_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fifth_v_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fifth_v_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fifth_v_response.status == STARTED and not waitOnFlip:
            theseKeys = fifth_v_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fifth_v_response_allKeys.extend(theseKeys)
            if len(_fifth_v_response_allKeys):
                fifth_v_response.keys = _fifth_v_response_allKeys[-1].name  # just the last key pressed
                fifth_v_response.rt = _fifth_v_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fifth_v_movies* updates
        if fifth_v_movies.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_v_movies.frameNStart = frameN  # exact frame index
            fifth_v_movies.tStart = t  # local t and not account for scr refresh
            fifth_v_movies.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_v_movies, 'tStartRefresh')  # time at next scr refresh
            fifth_v_movies.setAutoDraw(True)
        if fifth_v_movies.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fifth_v_movies.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fifth_v_movies.tStop = t  # not accounting for scr refresh
                fifth_v_movies.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fifth_v_movies, 'tStopRefresh')  # time at next scr refresh
                fifth_v_movies.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fifth_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fifth_V"-------
    for thisComponent in fifth_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fifth_V_trials.addData('fifth_v_response_prompt.started', fifth_v_response_prompt.tStartRefresh)
    fifth_V_trials.addData('fifth_v_response_prompt.stopped', fifth_v_response_prompt.tStopRefresh)
    # check responses
    if fifth_v_response.keys in ['', [], None]:  # No response was made
        fifth_v_response.keys = None
    fifth_V_trials.addData('fifth_v_response.keys',fifth_v_response.keys)
    if fifth_v_response.keys != None:  # we had a response
        fifth_V_trials.addData('fifth_v_response.rt', fifth_v_response.rt)
    fifth_V_trials.addData('fifth_v_response.started', fifth_v_response.tStartRefresh)
    fifth_V_trials.addData('fifth_v_response.stopped', fifth_v_response.tStopRefresh)
    fifth_v_movies.stop()
    # the Routine "fifth_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fifth_V_trials.addData('blank.started', blank.tStartRefresh)
    fifth_V_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fifth_V_trials'

timestamp = time()
data_to_send = {
    "id": 40,
    "timestamp": int(timestamp * 1e9),
    "event": stimuli_order[38],
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))
# ------Prepare to start Routine "fixation15sec"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation15secComponents = [image]
for thisComponent in fixation15secComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation15secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation15sec"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation15secClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation15secClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation15secComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation15sec"-------
for thisComponent in fixation15secComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fifth_A_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/home/kernel/Documents/Fifth A.xlsx'),
    seed=None, name='fifth_A_trials')
thisExp.addLoop(fifth_A_trials)  # add the loop to the experiment
thisFifth_A_trial = fifth_A_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFifth_A_trial.rgb)
if thisFifth_A_trial != None:
    for paramName in thisFifth_A_trial:
        exec('{} = thisFifth_A_trial[paramName]'.format(paramName))
for thisFifth_A_trial in fifth_A_trials:
    currentLoop = fifth_A_trials
    timestamp = time()
    data_to_send = {
        "id": 41,
        "timestamp": int(timestamp * 1e9),
        "event": stimuli_order[39],
        "value": "1"
        }
    event = json.dumps(data_to_send).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(event, ("239.128.35.86", 7891))
    # abbreviate parameter names if possible (e.g. rgb = thisFifth_A_trial.rgb)
    if thisFifth_A_trial != None:
        for paramName in thisFifth_A_trial:
            exec('{} = thisFifth_A_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "fifth_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    fifth_a_response.keys = []
    fifth_a_response.rt = []
    _fifth_a_response_allKeys = []
    SNR_file_num_5a = str(random.randint(1,40)) # selecting a random file number for SNR value
    sound_5_a.setSound('/home/kernel/Documents/_Intensity66/'+real_var+'_'+SNR_file_num_5a+'_norm'+'.wav', secs=2.0, hamming=True)
    sound_5_a.setVolume(0.47, log=False)
    fifth_a_stim.setSound(fifth_A, hamming=True)
    fifth_a_stim.setVolume(1.0, log=False)
    # keep track of which components have finished
    fifth_AComponents = [fifth_a_response, fifth_a_response_prompt, black_screen_with_dot_5, sound_5_a, fifth_a_stim]
    for thisComponent in fifth_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fifth_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fifth_A"-------
    while continueRoutine:
        # get current time
        t = fifth_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fifth_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fifth_a_response* updates
        waitOnFlip = False
        if fifth_a_response.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_a_response.frameNStart = frameN  # exact frame index
            fifth_a_response.tStart = t  # local t and not account for scr refresh
            fifth_a_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_a_response, 'tStartRefresh')  # time at next scr refresh
            fifth_a_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fifth_a_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fifth_a_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fifth_a_response.status == STARTED and not waitOnFlip:
            theseKeys = fifth_a_response.getKeys(keyList=['1','2','num_1','num_2'], waitRelease=False)
            _fifth_a_response_allKeys.extend(theseKeys)
            if len(_fifth_a_response_allKeys):
                fifth_a_response.keys = _fifth_a_response_allKeys[-1].name  # just the last key pressed
                fifth_a_response.rt = _fifth_a_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fifth_a_response_prompt* updates
        if fifth_a_response_prompt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_a_response_prompt.frameNStart = frameN  # exact frame index
            fifth_a_response_prompt.tStart = t  # local t and not account for scr refresh
            fifth_a_response_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fifth_a_response_prompt, 'tStartRefresh')  # time at next scr refresh
            fifth_a_response_prompt.setAutoDraw(True)
        if fifth_a_response_prompt.status == STARTED:
            if bool(fifth_a_response.status==FINISHED):
                # keep track of stop time/frame for later
                fifth_a_response_prompt.tStop = t  # not accounting for scr refresh
                fifth_a_response_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fifth_a_response_prompt, 'tStopRefresh')  # time at next scr refresh
                fifth_a_response_prompt.setAutoDraw(False)
        
        # *black_screen_with_dot_5* updates
        if black_screen_with_dot_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_screen_with_dot_5.frameNStart = frameN  # exact frame index
            black_screen_with_dot_5.tStart = t  # local t and not account for scr refresh
            black_screen_with_dot_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_screen_with_dot_5, 'tStartRefresh')  # time at next scr refresh
            black_screen_with_dot_5.setAutoDraw(True)
        if black_screen_with_dot_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_screen_with_dot_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                black_screen_with_dot_5.tStop = t  # not accounting for scr refresh
                black_screen_with_dot_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_screen_with_dot_5, 'tStopRefresh')  # time at next scr refresh
                black_screen_with_dot_5.setAutoDraw(False)
        # start/stop sound_5_a
        if sound_5_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5_a.frameNStart = frameN  # exact frame index
            sound_5_a.tStart = t  # local t and not account for scr refresh
            sound_5_a.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5_a.play(when=win)  # sync with win flip
        if sound_5_a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5_a.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_5_a.tStop = t  # not accounting for scr refresh
                sound_5_a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5_a, 'tStopRefresh')  # time at next scr refresh
                sound_5_a.stop()
        # start/stop fifth_a_stim
        if fifth_a_stim.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fifth_a_stim.frameNStart = frameN  # exact frame index
            fifth_a_stim.tStart = t  # local t and not account for scr refresh
            fifth_a_stim.tStartRefresh = tThisFlipGlobal  # on global time
            fifth_a_stim.play()  # start the sound (it finishes automatically)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fifth_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fifth_A"-------
    for thisComponent in fifth_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if fifth_a_response.keys in ['', [], None]:  # No response was made
        fifth_a_response.keys = None
    fifth_A_trials.addData('fifth_a_response.keys',fifth_a_response.keys)
    if fifth_a_response.keys != None:  # we had a response
        fifth_A_trials.addData('fifth_a_response.rt', fifth_a_response.rt)
    fifth_A_trials.addData('fifth_a_response.started', fifth_a_response.tStartRefresh)
    fifth_A_trials.addData('fifth_a_response.stopped', fifth_a_response.tStopRefresh)
    fifth_A_trials.addData('fifth_a_response_prompt.started', fifth_a_response_prompt.tStartRefresh)
    fifth_A_trials.addData('fifth_a_response_prompt.stopped', fifth_a_response_prompt.tStopRefresh)
    fifth_A_trials.addData('black_screen_with_dot_5.started', black_screen_with_dot_5.tStartRefresh)
    fifth_A_trials.addData('black_screen_with_dot_5.stopped', black_screen_with_dot_5.tStopRefresh)
    sound_5_a.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_5_a.started', sound_5_a.tStartRefresh)
    thisExp.addData('sound_5_a.stopped', sound_5_a.tStopRefresh)
    fifth_a_stim.stop()  # ensure sound has stopped at end of routine
    fifth_A_trials.addData('fifth_a_stim.started', fifth_a_stim.tStart)
    fifth_A_trials.addData('fifth_a_stim.stopped', fifth_a_stim.tStop)
    # the Routine "fifth_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fifth_A_trials.addData('blank.started', blank.tStartRefresh)
    fifth_A_trials.addData('blank.stopped', blank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fifth_A_trials'


# ------Prepare to start Routine "goodbye_"-------
continueRoutine = True
# update component parameters for each repeat
goodbye_response.keys = []
goodbye_response.rt = []
_goodbye_response_allKeys = []
# keep track of which components have finished
goodbye_Components = [the_end_txt, goodbye_response]
for thisComponent in goodbye_Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbye_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye_"-------
while continueRoutine:
    # get current time
    t = goodbye_Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbye_Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *the_end_txt* updates
    if the_end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        the_end_txt.frameNStart = frameN  # exact frame index
        the_end_txt.tStart = t  # local t and not account for scr refresh
        the_end_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(the_end_txt, 'tStartRefresh')  # time at next scr refresh
        the_end_txt.setAutoDraw(True)
    if the_end_txt.status == STARTED:
        if bool(goodbye_response.status==FINISHED):
            # keep track of stop time/frame for later
            the_end_txt.tStop = t  # not accounting for scr refresh
            the_end_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(the_end_txt, 'tStopRefresh')  # time at next scr refresh
            the_end_txt.setAutoDraw(False)
    
    # *goodbye_response* updates
    waitOnFlip = False
    if goodbye_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye_response.frameNStart = frameN  # exact frame index
        goodbye_response.tStart = t  # local t and not account for scr refresh
        goodbye_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye_response, 'tStartRefresh')  # time at next scr refresh
        goodbye_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(goodbye_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(goodbye_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if goodbye_response.status == STARTED and not waitOnFlip:
        theseKeys = goodbye_response.getKeys(keyList=['space'], waitRelease=False)
        _goodbye_response_allKeys.extend(theseKeys)
        if len(_goodbye_response_allKeys):
            goodbye_response.keys = _goodbye_response_allKeys[-1].name  # just the last key pressed
            goodbye_response.rt = _goodbye_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbye_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye_"-------
for thisComponent in goodbye_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('the_end_txt.started', the_end_txt.tStartRefresh)
thisExp.addData('the_end_txt.stopped', the_end_txt.tStopRefresh)
# check responses
if goodbye_response.keys in ['', [], None]:  # No response was made
    goodbye_response.keys = None
thisExp.addData('goodbye_response.keys',goodbye_response.keys)
if goodbye_response.keys != None:  # we had a response
    thisExp.addData('goodbye_response.rt', goodbye_response.rt)
thisExp.addData('goodbye_response.started', goodbye_response.tStartRefresh)
thisExp.addData('goodbye_response.stopped', goodbye_response.tStopRefresh)
thisExp.nextEntry()
# the Routine "goodbye_" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

timestamp = time()
data_to_send = {
    "id": 42,
    "timestamp": int(timestamp * 1e9),
    "event": 'end_experiment',
    "value": "1"
    }
event = json.dumps(data_to_send).encode("utf-8")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(event, ("239.128.35.86", 7891))

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
