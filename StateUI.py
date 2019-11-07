import cv2
import numpy as np

# Settings
max_num_players = 10
num_players = 3
player_current_turn = 2

height = 600
width = 1200

table_width = width * 0.8
table_height = height * 0.7
table_y_offset = 5
table_color = (41, 145, 0)

player_radius = 30
player_table_offset = 10
player_color = (255, 102, 3)
player_color_inactive = (209, 209, 209)
player_color_current_turn = (0, 100, 255)

# Text settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (255, 255, 255)
line_type = 2

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
player_x_margin = 40
py_center = ty2 + player_table_offset + player_radius
players_width = max_num_players * 2 * player_radius
for i in range(max_num_players):
    px_center = int((i * (player_radius * 2 + player_x_margin)) + int(tx1 + player_radius))
    if i < num_players:
        if i == (player_current_turn - 1):
            cv2.circle(img, (px_center, py_center), player_radius, player_color_current_turn, -1)
        else:
            cv2.circle(img, (px_center, py_center), player_radius, player_color, -1)
    else:
        cv2.circle(img, (px_center, py_center), player_radius, player_color_inactive, -1)

# Draw text
cv2.putText(img, 'Hello World!', (tx1, ty2), font, 0.5, font_color, line_type)


cv2.imshow('BlackJack', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

