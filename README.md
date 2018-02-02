# game_tracker
A game Win - Loss tracker for use with OBS and Stream Deck. 

*works on Mac OS, Linux, and Windows 10*

# Install Instructions for Stream Deck and OBS
1. Open up `Stream Deck` software and add two `Open` actions to the board. 
1. Label one action `Win` and the other action `Loss`.
1. Link the `win.py` file to the `Win` action. Link the `lose.py` file to the `Loss` action. 
1. Add a new `Text (GDI+)` object to your desired scene in `OBS`. 
1. Make sure to tick `Read from file` and select the `output.txt` file. 
1. You should now be able to tap the `Win` and `Loss` buttons to keep track of your games. 
1. Optionally you can add another button labeled `Reset` and link it to the `reset.py` to reset the score.

