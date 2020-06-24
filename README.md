# MarkovDecisionProcess
Implementation of Markov Decision Process using grid-world enironment

## Usage
Require arguments:<br>
<b>File with world description </b> (eg. world0.txt)<br>
File <b> world0.txt is equivalent to well-known MDP problem using grid world (eg. here: http://aima.cs.berkeley.edu/). 
<br>
Optional arguments: <br>
<b>-mdp</b> -> Run the Markov Decision Problem algorithm and print the result as standard output <br>
<b>-sh</b> -> show the results as figures <br>
<b>-s</b> -> save the results to tmp.* file <br>
<b>-sfn</b> -> change the filename for saved files <br>

## Example of usage
<b>1) Run Markov Decision Problem for world0</b><br>
python main.py world0.txt -mdp

![obraz](https://user-images.githubusercontent.com/44849247/85585966-c7889280-b640-11ea-936c-7d680dd8e1eb.png)

<b>2) Show the results graphically</b><br>
python main.py world0.txt -mdp -sh

![2020-06-24_17h34_28](https://user-images.githubusercontent.com/44849247/85586269-10d8e200-b641-11ea-9024-f78614f0c2d3.png)
![2020-06-24_17h34_16](https://user-images.githubusercontent.com/44849247/85586275-13d3d280-b641-11ea-88e5-fb753d021fa7.png)
![2020-06-24_17h34_19](https://user-images.githubusercontent.com/44849247/85586283-1504ff80-b641-11ea-97f0-051bcaeb3a51.png)

<b>3) Show the results graphically and save them to "figures" file</b><br>
python main.py world0.txt -mdp -sh -s -sfn figures

## Gnuplot 
This code use gnuplot library to print the utilities for every iteration. Using gruplot require additional software. Here is the description: https://pypi.org/project/PyGnuplot/
<br>
If you don't want to just Gnuplot, then just change the <b>USE_GNUPLOT</b> flag in main.py to <b>False</b>
