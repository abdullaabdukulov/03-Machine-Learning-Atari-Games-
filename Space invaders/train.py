import gym
from stable_baselines3 import PPO
from stable_baselines3.common.atari_wrappers import FireResetEnv
from gym.wrappers import AtariPreprocessing, FrameStack

env = gym.make('SpaceInvadersNoFrameskip-v4')

env = FireResetEnv(env)
env = AtariPreprocessing(env)
env = FrameStack(env, num_stack=4)

model = PPO('CnnPolicy', env)
model.learn(total_timesteps=2500)

model.save("ppo_space_invaders")
