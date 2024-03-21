from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

env_id = "MsPacman-v0"
num_envs = 4
vec_env = make_vec_env(env_id, n_envs=num_envs)


model = PPO('MlpPolicy', vec_env)
model.learn(total_timesteps=2500)


model.save("ppo_pacman")


