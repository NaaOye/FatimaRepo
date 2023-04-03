
import pyttsx3 as pt
import PySimpleGUI as FATI

engine = pt.init()
Voice_Kind = engine.getProperty('voices')

layout=[
[FATI.Input(key = 'Input'), FATI.Button('Speak', key='Speak_BUTTON')],
[ FATI.Text(' Select Voice Type', key='Voice'), FATI.Radio('Male', 'RADIO1', default=True, key = 'MALE_BUTTON',), FATI.Radio('Female','RADIO1', key='FEMALE_BUTTON')],
]
window = FATI.Window(' Text to speech App', layout )
while True:
    event, values = window.read()
    if event == FATI.WIN_CLOSED:
        break

    elif event == 'Speak_BUTTON':
        text = values['Input']
        
        if values['MALE_BUTTON']:
            engine.setProperty('voice',  Voice_Kind[0].id)
            engine.setProperty('rate', 130)
            engine.setProperty('volume', 10) 


        if values['FEMALE_BUTTON']:
            engine.setProperty('voice', Voice_Kind[1].id)        
            engine.setProperty('rate', 130)
            engine.setProperty('volume', 1.5) 
    engine.say(text)
    engine.runAndWait()

window.read()
        
