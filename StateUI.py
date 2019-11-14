import cv2
import numpy as np

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
card_width = 40
card_height = 60
card_font_color_black = (0, 0, 0)
card_font_color_red = (0, 0, 255)
card_text_x_offset = 5
card_text_y_offset = 5
card_font_scale = 0.5
clubs_img = cv2.resize(cv2.imread('res\\clubs.jpg'), (20, 25))
spades_img = cv2.resize(cv2.imread('res\\spades.jpg'), (20, 25))
hearts_img = cv2.resize(cv2.imread('res\\hearts.jpg'), (20, 25))
diamonds_img = cv2.resize(cv2.imread('res\\diamonds.jpg'), (20, 25))


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


def draw_total(img, px_center, ty2, player_no, player_totals):
    total = player_totals[player_no]
    if total < 10:
        cv2.putText(img, str(total), (px_center - 10, ty2 - 10), font, 1, font_color, line_type)
    else:
        cv2.putText(img, str(total), (px_center - 20, ty2 - 10), font, 1, font_color, line_type)


def draw_players(img, table_x, table_y, player_totals, num_players, current_player):
    player_x_margin = 40
    py_center = table_y + player_table_offset + player_radius
    for i in range(max_num_players):
        px_center = int((i * (player_radius * 2 + player_x_margin)) + int(table_x + player_radius))
        if i < num_players:
            if i == current_player:
                cv2.circle(img, (px_center, py_center), player_radius, player_color_current_turn, -1)
            else:
                cv2.circle(img, (px_center, py_center), player_radius, player_color, -1)
        else:
            cv2.circle(img, (px_center, py_center), player_radius, player_color_inactive, -1)
        cv2.putText(img, str(i), (px_center - 10, py_center + 10), font, 1, font_color, line_type)
        draw_total(img, px_center, table_y, i, player_totals)


def get_card_value_string(code):
    if code == 1:
        return 'A'
    elif code == 10:
        return 'T'
    elif code == 11:
        return 'J'
    elif code == 12:
        return 'Q'
    elif code == 13:
        return 'K'
    elif code == 255:
        return '?'
    else:
        return str(code)


def draw_card(img, x, y, value, suit):
    cv2.rectangle(img, (x, y), (x + card_width, y + card_height), (255, 255, 255), -1)
    if suit == 1:
        cv2.putText(img, get_card_value_string(value), (x + card_text_x_offset, y + card_height - card_text_y_offset), font, 1, (0, 0, 0), line_type)
        img[y+3:y+3+spades_img.shape[0], x+17:x+17+spades_img.shape[1]] = spades_img
    elif suit == 2:
        cv2.putText(img, get_card_value_string(value), (x + card_text_x_offset, y + card_height - card_text_y_offset), font, 1, (0, 0, 255), line_type)
        img[y + 3:y + 3 + hearts_img.shape[0], x + 17:x + 17 + hearts_img.shape[1]] = hearts_img
    elif suit == 3:
        cv2.putText(img, get_card_value_string(value), (x + card_text_x_offset, y + card_height - card_text_y_offset), font, 1, (0, 0, 255), line_type)
        img[y + 3:y + 3 + diamonds_img.shape[0], x + 17:x + 17 + diamonds_img.shape[1]] = diamonds_img
    elif suit == 4:
        cv2.putText(img, get_card_value_string(value), (x + card_text_x_offset, y + card_height - card_text_y_offset), font, 1, (0, 0, 0), line_type)
        img[y + 3:y + 3 + clubs_img.shape[0], x + 17:x + 17 + clubs_img.shape[1]] = clubs_img
    elif suit == 255:
        cv2.putText(img, get_card_value_string(value), (x + card_text_x_offset, y + card_height - card_text_y_offset), font, 1, (0, 0, 0), line_type)


def draw_cards(image, table_x, table_y, num_players):
    player_x_margin = 40
    py_center = table_y + player_table_offset + player_radius
    for i in range(num_players):
        px_center = int((i * (player_radius * 2 + player_x_margin)) + int(table_x + player_radius))
        draw_card(image, int(px_center - card_width / 2), py_center - 150, np.random.randint(1, 14), np.random.randint(1, 5))


def draw_game_state(num_players, current_player, player_total_values):
    image = blank_image()
    tx, ty = draw_table(image)
    draw_players(image, tx, ty, player_total_values, num_players, current_player)
    # Draw all player cards in loop
    draw_cards(image, tx, ty, num_players)
    cv2.imshow('BlackJack', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


draw_game_state(6, 3, np.random.randint(0, 100, 10))
