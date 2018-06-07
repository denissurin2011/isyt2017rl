import collections
import random
import pandas as pd
import numpy as np

MemoryRecord = collections.namedtuple('MemoryRecord',
                                      'observation action reward next_observation done')


class BaseAgent(object):
    def __init__(self,
                 input_shape=None,
                 number_of_actions=8,
                 max_memory_size=250):
        self.input_shape = input_shape
        self.number_of_actions = number_of_actions
        self.max_memory_size = max_memory_size
        self.memory = {}
        size = 20
        self.rows_init = np.zeros(8)
        self.goal = None
        self.gamma = 0.9
        self.LF = 0.8
        self._build_model()
    
    def __repr__(self):
        return self.__class__.__name__
    
    def _build_model(self):
        pass
    
    def new_episode(self, goal):
        self.goal = goal
    
    def act(self, observation):
        action = np.random.choice(self.number_of_actions)
        return action
    
    def train_on_memory(self):
        pass
    def init_q(self, name):
        self.memory[name] = {}
        for i in range(0, 8):
            self.memory[name][i] = 0
    def update_memory(self, observation, action, reward, next_observation, done):
        next_state_name = ''.join(str(v) for v in next_observation)
        state_name = ''.join(str(v) for v in observation)
        if not(next_state_name in self.memory):
            self.init_q(next_state_name)
        if not(state_name in self.memory):
            self.init_q(state_name)
        max_value = max(self.memory[next_state_name])
        old = self.memory[state_name][action]
        new = self.memory[next_state_name][action]
        self.memory[state_name][action] = old + self.LF * (reward + self.gamma * max_value - new)



