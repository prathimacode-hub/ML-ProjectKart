---
Deep Q Networks
---

## Goal
In this repository, we will tackle 2 major problems, namely **Cartpole Balancing** and **Mountain Climbing**. We will discuss each one of the problem statements in brief. 

## Cartpole Balancing
CartPole problem is the problem of balancing the CartPole. CartPole is the structure where a pole is attached to the cart and the cart is free to slide across the frictionless surface. By sliding the cart left or right, the CartPole is balanced.

So, the objective of the CartPole is to keep it from falling or moving out of the range. Therefore, the failure conditions are:

- Magnitude of the angle of the pole with respect to the vertical exceeding some threshold.

![Angle](https://github.com/Sidhved/ML-ProjectKart/blob/main/DeepQNetworks/resource/Angle.PNG)

- Distance of the CartPole from the center exceeding some threshold.

![Distance](https://github.com/Sidhved/ML-ProjectKart/blob/main/DeepQNetworks/resource/Distance.png)

#### DQN Agent for Cartpole Balancing
- DQN stands for [Deep Q-Network](https://deepmind.com/research/open-source/dqn). In this project, we have created our own Q-Network instead of Tensorflow distribution.
- The Q-Network has a sequential model with 3 Dense layers.
- The Agent runs in an environment. Here, we define the environement using CartPole-v0 from the [gym](https://gym.openai.com/) library.
- After setting the hyperparameters with number of episodes = 1000, we will start training the network by remembering a tuple (state, action, reward, next_state, done).
- The updated weights are saved into [cp_model folder](https://github.com/Sidhved/ML-ProjectKart/tree/main/DeepQNetworks/cp_model) after every 50 episodes.

## Mountain Climbing
A car is on a one-dimensional track, positioned between two mountains. The goal is to drive up the mountain on the right (reaching the flag). 

The car’s engine is not strong enough to climb the mountain in a single pass. Therefore, the only way to succeed is to drive back and forth to build up momentum. Thus we create a reward system in such a way that the car runs back and forth to generate enough momentum to reach the flag.

![Success](https://github.com/Sidhved/ML-ProjectKart/blob/main/DeepQNetworks/resource/mountain_car.gif)

#### DQN Agent and Reward System for Mountain Climbing
- DQN stands for [Deep Q-Network](https://deepmind.com/research/open-source/dqn). In this project, we have created our own Q-Network instead of Tensorflow distribution.
- The Q-Network has a sequential model with 3 Dense layers.
- The Agent runs in an environment. Here, we define the environement using MountainCar-v0 from the [gym](https://gym.openai.com/) library.
- After setting the hyperparameters with number of episodes = 100, we will start training the network by remembering a tuple (state, action, reward, next_state, done).
- After each episode, a score is calculated on basis of loss incurred. The score determines the next action of the agent. It helps with the feedback mechanism constructed on basis of coordinates on the environment plane.

## Terminology
- **Episode**: An episode is an instance of a game (or life of a game). If the game ends or life decreases, the episode ends.
- **Step**: Step is the time or some discrete value which increases monotonically in an episode. With each change in the state of the game, the value of step increases until the game ends.
- **Environment**: The environment is the surrounding or setting on which the agent performs actions.

## Libraries
- [gym](https://gym.openai.com/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [collections](https://docs.python.org/3/library/collections.html)
- [keras.models, keras.layers, keras.optimizers](https://keras.io/)
- [random](https://docs.python.org/3/library/random.html)

## Results
**Cartpole Balancing**
- The agent achieved a stable high score of 199 with 0.01 Exploration Rate.
**Mountain Climbing**
## Results
- The car was able to reach the goal multiple times (episode 60, 71, 74, 79)
- It can be also observed as peaking values in the score plot as show below

![Peak Score](https://github.com/Sidhved/ML-ProjectKart/blob/main/DeepQNetworks/resource/mc.png)

#### Contributor
Project Submitted by [Sidhved](https://github.com/Sidhved).
Connect with me on [LinkedIn](https://www.linkedin.com/in/sidhved-warik-b05aab173/) or [Twitter](https://twitter.com/Sid9051)
