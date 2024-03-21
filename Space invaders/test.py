from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.env_util import make_atari_env

model = PPO.load("ppo_space_invaders")
env_id = "SpaceInvadersNoFrameskip-v4"
env = make_atari_env(env_id)

env = VecFrameStack(env, n_stack=4)

obs = env.reset()

done = False
scores = 0
while not done:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    scores += rewards
    env.render("human")
print('Score: {}'.format(scores[0]))