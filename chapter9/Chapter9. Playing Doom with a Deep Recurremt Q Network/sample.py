from vizdoom import *
import random
import time

game = DoomGame()

game.load_config("/home/sohee/openai/ViZDoom/scenarios/basic.cfg") 


game.init()

shoot = [0, 0, 1]
left = [1, 0, 0]
right = [0, 1, 0]
actions = [shoot, left, right]

no_of_episodes = 10

for i in range(no_of_episodes):
    
    game.new_episode()
    
    while not game.is_episode_finished():
        state = game.get_state()
        img = state.screen_buffer
        
        misc = state.game_variables
        
        reward = game.make_action(random.choice(actions))
        
        print(reward)
        
    time.sleep(2)
    