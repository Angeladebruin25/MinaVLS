from __future__ import division
from __future__ import print_function

from psychopy import visual, event, core, logging
import os

datapath = 'D:\\Mina\\ScriptVLS\\Question\\'



win = visual.Window(fullscr=False, size=[1100, 800], units='pix', monitor='testMonitor', color=[1,1,1])


myRatingScale = visual.RatingScale(win, low=0, high=100, marker='slider',
    tickMarks=[0, 50, 100], stretch=1.5, tickHeight=1.5, acceptPreText = 'Lala', lineColor = 'Black', textColor = 'Black', 
    labels=["0%", "50%", "100%"])
txt = "Por favor, indique la frecuencia con la que ha cambiado de una lengua a otra en la ultima tarea "
myItem = visual.TextStim(win, text=txt, height=.05, units='norm', color=[-1,-1,-1])

# show & update until a response has been made
while myRatingScale.noResponse:
    myItem.draw()
    myRatingScale.draw()
    win.flip()
    if event.getKeys(['escape']):
        core.quit()

print('Example 4: rating =', myRatingScale.getRating())

win.close()
core.quit()