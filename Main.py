from GameStateVisualization import Visualizer
import numpy as np

gsv = Visualizer()
gsv.draw_game_state(7, 2, np.zeros(10, dtype=int), np.ones((7, 7, 2)))

