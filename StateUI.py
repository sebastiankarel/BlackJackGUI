import cv2
import numpy as np

# Settings
num_players = 1

height = 600
width = 800

table_width = width * 0.7
table_height = height * 0.7
table_y_offset = 5
table_color = (41, 145, 0)

player_radius = 30
player_table_offset = 10
player_color = (252, 186, 3)

# init image
img = np.ones((height, width, 3), np.uint8)
img *= 255

# draw table
tx1 = int((width / 2) - (table_width / 2))
ty1 = table_y_offset
tx2 = int(tx1 + table_width)
ty2 = int(ty1 + table_height)
cv2.rectangle(img, (tx1, ty1), (tx2, ty2), table_color, -1)

# draw players
center_players = int((width / 2) - (player_radius / 2))
py_center = ty2 + player_table_offset + player_radius
players_width = num_players * 2 * player_radius
for i in range(num_players):
    px_center = int(tx1 + (players_width / 2) / 2 + (table_width - players_width) / 2)
    cv2.circle(img, (px_center, py_center), player_radius, player_color, -1)

cv2.imshow('BlackJack', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

