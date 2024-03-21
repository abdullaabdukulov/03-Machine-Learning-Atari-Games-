# 03-Machine-Learning-Atari-Games

### Task
<p>Let's play Atari games, but with deep learning :)</p>
<p>It's time to dive in and learn about neural networks and deep learning! This is a significant but fun project that contributes value to your technical portolio and software development experience.</p>
<p><em>My Mission</em> 
<br>
Your mission is to build an AI that "plays" Atari video games. You will build 3 diffeent models that solve three different Atari games.</p>

### Description
I will do this steps instead:
<ul>
<li>a model that plays Cart Pole</li>
<li>a model that plays Space invaders</li>
<li>a model that plays Pacman</li>
<li>A blog post explaining your approach</li>
</ul>

### Installation
For working with this project you need to install required libraries wich mentioned in `requirements.txt`. Just write this command in your teminal:
```pip install -r requirements.txt```

### Usage
This project has some steps for using correctly. \
First step choose the game:
1. CartPole
2. Pacman
3. Space invaders

- Next step open a folder which has a same name like game names.
There two files inside:
  - train.py
  - test.py

- If you want to train the model you should run the `train.py` file.

  - ```python train.py```

    **Important !!!** \
    You can change the learning steps(default is 2500 steps) \
    Just change the value of `total_timesteps` parameter to number that you want to train. 


-  Then you can test it by running `test.py` file.
    - ```python test.py```

pip install gym==0.26.2 
pip install stable-baselines3==2.2.1