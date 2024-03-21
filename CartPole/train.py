from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

vec_env = make_vec_env("CartPole-v1")
model = PPO("MlpPolicy", vec_env, verbose=1)
model.learn(total_timesteps=2500)
model.save("ppo_cartpole")