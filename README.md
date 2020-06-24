# MarkovDecisionProblem
Implementation of Markov Decision Problem using grid-world enironment

## Usage
Require arguments:<br>
<b>File with world description </b> (eg. world0.txt)<br><br>
Optional arguments: <br>
<b>-mdp</b> -> Run the Markov Decision Problem algorithm and print the result as standard output <br>
<b>-sh</b> -> show the results as figures <br>
<b>-s</b> -> save the results to tmp.* file <br>
<b>-sfn</b> -> change the filename for saved files <br>

## Example of usage
<b>1) Run Markov Decision Problem for world1</b><br>
python main.py world1.txt -mdp

<b>2) Show the results graphically</b><br>
python main.py world1.txt -mdp -sh

<b>3) Show the results graphically and save them to "figures" file</b><br>
python main.py world1.txt -mdp -sh -s -sfn figures

## Gnuplot 
This code use gnuplot library to print the utilities for every iteration. Using gruplot require additional software. Here is the description: https://pypi.org/project/PyGnuplot/
<br>
If you don't want to just Gnuplot, then just change the <b>USE_GNUPLOT</b> flag in main.py to <b>False</b>
