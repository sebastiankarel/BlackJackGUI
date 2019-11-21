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

player_totals = np.zeros(10, dtype=int)
player_totals[0] = 15
player_totals[1] = 18

dealer_cards = np.zeros((5, 2), dtype=int)
dealer_cards[0] = (1, 2)
dealer_cards[1] = (4, 3)
dealer_cards[2] = (10, 4)

gsv.draw_game_state(num_players, 0, player_totals, player_cards, 10, dealer_cards)
gsv.draw_game_state(num_players, 1, player_totals, player_cards, 10, dealer_cards)
gsv.draw_game_state(num_players, 2, player_totals, player_cards, 10, dealer_cards)

gsv.end()

