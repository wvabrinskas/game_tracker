# game_tracker
A game Win - Loss tracker for use with OBS and Stream Deck. 

*works on Mac OS, Linux, and Windows 10*

# Pre-Setup Instructions
1. *Windows Users*: Please install Python from [here](https://www.python.org/downloads/)

# Install Instructions for Stream Deck and OBS
1. Open up `Stream Deck` software and add two `Open` actions to the board. 
1. Label one action `Win` and the other action `Loss`.
1. Link the `win.py` file to the `Win` action. Link the `lose.py` file to the `Loss` action. 
    - *Windows Users*: Link `win.bat` to `Win` and `loss.bat` to `Loss`
1. Add a new `Text (GDI+)` object to your desired scene in `OBS`. 
1. Make sure to tick `Read from file` and select the `output.txt` file. 
1. You should now be able to tap the `Win` and `Loss` buttons to keep track of your games. 
1. Optionally you can add another button labeled `Reset` and link it to the `reset.py` to reset the score.
    - *Windows Users*: Link `reset.bat` to `Reset`
    - You can also reset the score by either typing in `0-0` in the text file yourself or deleting the `output.txt` file. 
    - The next time you hit `Win` or `Lose` it will add the file back

# Developer Social Contact
1. ![](https://www.seeklogo.net/wp-content/uploads/2015/09/twitter-icon-circle-logo.png =50x50) [Twitter](https://twitter.com/william_vab)
1. [Twitch (wavOW)](https://twitch.tv/wavow)
1. [Twitch (Gaming Night Live)](https://twitch.tv/gamingnightlive)