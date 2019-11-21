from GameStateVisualization import Visualizer
import numpy as np

gsv = Visualizer()

num_players = 3
max_num_cards = 8

player_cards = np.zeros((num_players, max_num_cards, 2), dtype=int)
player_cards[0][0] = (1, 2)
player_cards[0][1] = (4, 3)
player_cards[0][2] = (10, 4)

player_cards[1][0] = (12, 1)
player_cards[1][1] = (8, 2)

gsv.draw_game_state(num_players, 2, np.zeros(10, dtype=int), player_cards)

