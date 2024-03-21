from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import gymnasium as gym

vec_env = make_vec_env("CartPole-v1")

model = PPO.load("ppo_cartpole")
obs = vec_env.reset()

done = False
scores = 0
while not done:
    action, _states = model.predict(obs)
    obs, rewards, done, info = vec_env.step(action)
    scores += rewards
    vec_env.render("human")
print('Score: {}'.format(scores[0]))