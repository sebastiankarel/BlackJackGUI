import cv2
import numpy as np

# Values from game state
num_players = 3
player_current_turn = 2
player_totals = np.random.randint(0, 100, 10)

# Settings
max_num_players = 10

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

# General text settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (255, 255, 255)
line_type = 2

# Cards
card_width = 10
card_height = 20
card_font_color_black = (0, 0, 0)
card_font_color_red = (0, 0, 255)
card_text_x_offset = 5
card_text_y_offset = 5
card_font_scale = 0.5


def blank_image():
    img = np.ones((height, width, 3), np.uint8)
    img *= 255
    return img


def draw_table(img):
    tx1 = int((width / 2) - (table_width / 2))
    ty1 = table_y_offset
    tx2 = int(tx1 + table_width)
    ty2 = int(ty1 + table_height)
    cv2.rectangle(img, (tx1, ty1), (tx2, ty2), table_color, -1)
    return tx1, ty2


def draw_total(img, px_center, ty2, player_no):
    total = player_totals[player_no]
    if total < 10:
        cv2.putText(img, str(total), (px_center - 10, ty2 - 10), font, 1, font_color, line_type)
    else:
        cv2.putText(img, str(total), (px_center - 20, ty2 - 10), font, 1, font_color, line_type)


def draw_players(img, tx1, ty2):
    player_x_margin = 40
    py_center = ty2 + player_table_offset + player_radius
    for i in range(max_num_players):
        px_center = int((i * (player_radius * 2 + player_x_margin)) + int(tx1 + player_radius))
        if i < num_players:
            if i == player_current_turn:
                cv2.circle(img, (px_center, py_center), player_radius, player_color_current_turn, -1)
            else:
                cv2.circle(img, (px_center, py_center), player_radius, player_color, -1)
        else:
            cv2.circle(img, (px_center, py_center), player_radius, player_color_inactive, -1)
        cv2.putText(img, str(i), (px_center - 10, py_center + 10), font, 1, font_color, line_type)
        draw_total(img, px_center, ty2, i)


image = blank_image()
table_x, table_y = draw_table(image)
draw_players(image, table_x, table_y)

cv2.imshow('BlackJack', image)
cv2.waitKey(0)

cv2.destroyAllWindows()

