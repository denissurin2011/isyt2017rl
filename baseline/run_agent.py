#!/usr/bin/env python
import gym
import random
import matplotlib.pyplot as plt
from pathenv.agent import BaseAgent

episodes_number = 90
max_steps = 1000

if __name__ == '__main__':
    env = gym.make('PathFindingByPixelWithDistanceMapEnv-v1')
    env._configure()
    
    agent = BaseAgent(input_shape=env.observation_space.shape, number_of_actions=env.action_space.n)
    train_step = []
    for episode_i in xrange(1, episodes_number + 1):
        
        observation = env.reset()
        agent.new_episode(env.finish)
        reward, done = 0, False
        train_step.append(max_steps + 1)
        for step_i in range(max_steps):
            action = agent.act(observation)
            next_observation, reward, done, _ = env.step(action)
            agent.update_memory(observation, action, reward, next_observation, done)
            observation = next_observation
            if done:
                train_step.append(step_i + 1)
                break

    agent.train_on_memory()
plt.plot(train_step)
plt.savefig('train'+'.png', format='png', dpi=100)
plt.clf()
ans = []
for num_test in range(10):
    observation = env.reset()
    cur_ans = 0
        for step_i in range(max_steps):
            cur_ans = cur_ans + 1
            name = ''.join(str(v) for v in observation)
            cur_max = 0
            action = -1
            for i in range(8):
                if name not in agent.memory:
                    continue
                if agent.memory[name][i] > cur_max:
                    action = i
                    cur_max = agent.memory[name][i]
            if action == -1:
                action = random.randint(0, 7);
            next_observation, reward, done, _ = env.step(action)
            observation = next_observation
            if done:
                break
    ans.append(cur_ans)
plt.plot(ans)
plt.savefig('result'+'.png', format='png', dpi=100)
plt.clf()

