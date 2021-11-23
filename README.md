<!-- image -->
<div align="center" id="top"> 
  <img src=images/idea.png width="400" />
  &#xa0;
</div>

<h1 align="center"> markov-decision-process-grid-world </h1>
<h2 align="center"> Implementation of Markov Decision Process using grid-world enironment </h2>

<!-- https://shields.io/ -->
<p align="center">
  <img alt="Top language" src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python">
  <img alt="Status" src="https://img.shields.io/badge/Status-done-green?style=for-the-badge">
  <img alt="Code size" src="https://img.shields.io/github/languages/code-size/KamilGos/markov-decision-process-grid-world?style=for-the-badge">
</p>

<!-- table of contents -->
<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#package-content">Content</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#eyes-implementation">Implementation</a> &#xa0; | &#xa0;
  <a href="#microscope-tests">Tests</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="#technologist-author">Author</a> &#xa0; | &#xa0;
</p>

<br>

---

<center>

You can find the implementation of Q-Learning algorithm (reinforcement learning) using grid-world environment here: [github.com/KamilGos/qlearning-grid-world](https://github.com/KamilGos/qlearning-grid-world)

</center>

---

## :dart: About ##
Project is an implementation of Markov Decision Process using "Grid World". 

## :package: Content
 * [data](data) - three example worlds
 * [sources](sources) - source files
 * [main.py](main.py) - main executable file

## :checkered_flag: Starting ##
```bash
# Clone this project
$ git clone https://github.com/KamilGos/markov-decision-process-grid-world

# Access
$ cd markov-decision-process-grid-world

# Run the project
usage: main.py [-h] [-mdp] [-sh] [-s] [-sfn SAVE_FILENAME] world_filename

positional arguments:
  world_filename        Chosen world filename. Eg. "world1.txt"

optional arguments:
  -h, --help            show this help message and exit
  -mdp, --mrun          Run Markov Decision Problem algorithm
  -sh, --show           Show figures
  -s, --save            Save figures and data to tmp.* To change filename use: -sfn [filename]
  -sfn SAVE_FILENAME, --save_filename SAVE_FILENAME
                        Change saved figures file names. Use -sfn [filename] (DO NOT USE FILE EXTENSION!)

# Example of usage:

# Run MDP for world1
$ python main.py data/world1.txt -mdp

# Run MDP for world1 and show the results graphically
$ python main.py data/world1.txt -mdp -sh

# Run MDP for world1, show the results graphically and save them to "figures" file
$ python main.py data/world1.txt -mdp -sh -s -sfn figures
```


## :eyes: Implementation ##
<h2>Grid World</h2>
Inside 'data' folder you can find three prepared, ready world. Hovever you can create your own world using the following file structure:

<div align="center">

| Structure   | Exampple    |
|--------------- | --------------- |
|   <img src=images/world_structure.png width="600" />  |   <img src=images/world1_structure.png width="100" /> |

</div>

The graphical representation of these worlds is shown in picture below. White colour means that the considered state is **normal**. Colour black was used **forbidden** states, the colour green was used for **terminal** states, yellow for **special** states and blue for start state. The figures also indicate the numbering of coordinates that is used in the program output. The 0.0 utility in green state means that this is terminal state. 

<div align="center" id="put_id"> 
  <img src=images/world1_graph.png width="250" />
  &#xa0;
</div>

## :microscope: Tests ##
For the termination condition, the reduction of all the differences between successive iterations below **0.0001** was taken.

<h2>Test 1</h2>
This test aimed to calculate the solution for the problem shown in the World0 file. Results are identical as presented in the literature, so it can be assumed that the algorithm implementation is correct. 

Number of iterations:23

<div align="center" id="put_id"> 
  <img src=images/test1.png width="500" />
  &#xa0;
</div>

<h2>Test 2</h2>
This test aimed to calculate the solution for the problem shown in the World1 file.

Number of iterations:32
<div align="center" id="put_id"> 
  <img src=images/test2.png width="500" />
  &#xa0;
</div>

<h2>Test 3</h2>
In this test, World1 was still considered but with the normal reward changed from -1 to -5. As expected, both the utilities and the actions have changed locally. Before changed normal reward value (test 2) the special state value was so small with comparison to a normal state so the agent tried to avoid going into this field. After changing the value, this difference is not so great and it is more profitable to go through the special field (11) than to avoid it. This is noticeable in actions on state 3 and 7.

Number of iterations:30
<div align="center" id="put_id"> 
  <img src=images/test3.png width="500" />
  &#xa0;
</div>


<h2>Test 4</h2>
Test 4 concerned a change in the distribution of uncertainty. The original distribution was: P(UP)=0.8, P(LEFT)=0.1 and P(RIGHT)=0.1. The values were changed to: P(UP)=0.1 , P(LEFT)=0.8 and P(RIGHT)=0.1. The policy changed to more reckless. The agent didn't try to avoid special state and she didn't try to reach terminal state. In fact, she waled into the forbidden state what is very counter-intuitive. Also, the algorithm needed more iterations to converge.

Numer of iterations: 43
<div align="center" id="put_id"> 
  <img src=images/test4.png width="500" />
  &#xa0;
</div>


<h2>Test 5</h2>
This test was to change the discounting parameter value for the World 1. The value was changed from 0.99 to 0.6. A smaller discounting parameter has a huge influence on final utilities. Also, the number of iteration is smaller. Actions show that the agent didn't try to avoid the special field. She has no time to learn more (the original case was 32 iteration). 

Numer of iterations: 17

<div align="center" id="put_id"> 
  <img src=images/test5.png width="500" />
  &#xa0;
</div>

## :memo: License ##

This project is under license from MIT.

## :technologist: Author ##

Made with :heart: by <a href="https://github.com/KamilGos" target="_blank">Kamil Goś</a>

&#xa0;

<a href="#top">Back to top</a>