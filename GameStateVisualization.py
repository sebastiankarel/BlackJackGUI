import cv2
import numpy as np


class Visualizer:
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

    def blank_image(self):
        img = np.ones((self.height, self.width, 3), np.uint8)
        img *= 255
        return img

    def draw_table(self, img):
        tx1 = int((self.width / 2) - (self.table_width / 2))
        ty1 = self.table_y_offset
        tx2 = int(tx1 + self.table_width)
        ty2 = int(ty1 + self.table_height)
        cv2.rectangle(img, (0, ty1), (self.width, ty2), self.table_color, -1)
        cv2.rectangle(img, (tx1, ty1), (tx2, ty2), self.table_color, -1)
        return tx1, ty2

    def draw_total(self, img, px_center, ty2, player_no, player_totals):
        total = player_totals[player_no]
        if total < 10:
            cv2.putText(img, str(total), (px_center - 10, ty2 - 10), self.font, 1, self.font_color, self.line_type)
        else:
            cv2.putText(img, str(total), (px_center - 20, ty2 - 10), self.font, 1, self.font_color, self.line_type)

    def draw_players(self, img, table_x, table_y, player_totals, num_players, current_player):
        player_x_margin = 40
        py_center = table_y + self.player_table_offset + self.player_radius
        for i in range(self.max_num_players):
            px_center = int((i * (self.player_radius * 2 + player_x_margin)) + int(table_x + self.player_radius))
            if i < num_players:
                if i == current_player:
                    cv2.circle(img, (px_center, py_center), self.player_radius, self.player_color_current_turn, -1)
                else:
                    cv2.circle(img, (px_center, py_center), self.player_radius, self.player_color, -1)
            else:
                cv2.circle(img, (px_center, py_center), self.player_radius, self.player_color_inactive, -1)
            cv2.putText(img, str(i), (px_center - 10, py_center + 10), self.font, 1, self.font_color, self.line_type)
            self.draw_total(img, px_center, table_y, i, player_totals)

    @staticmethod
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

    def draw_card(self, img, x, y, value, suit):
        cv2.rectangle(img, (x, y), (x + self.card_width, y + self.card_height), (255, 255, 255), -1)
        if suit == 1:
            cv2.putText(img, self.get_card_value_string(value),
                        (x + self.card_text_x_offset, y + self.card_height - self.card_text_y_offset),
                        self.font, 1, (0, 0, 0), self.line_type)
            img[y + 3:y + 3 + self.spades_img.shape[0], x + 17:x + 17 + self.spades_img.shape[1]] = self.spades_img
        elif suit == 2:
            cv2.putText(img, self.get_card_value_string(value),
                        (x + self.card_text_x_offset, y + self.card_height - self.card_text_y_offset),
                        self.font, 1, (0, 0, 255), self.line_type)
            img[y + 3:y + 3 + self.hearts_img.shape[0], x + 17:x + 17 + self.hearts_img.shape[1]] = self.hearts_img
        elif suit == 3:
            cv2.putText(img, self.get_card_value_string(value),
                        (x + self.card_text_x_offset, y + self.card_height - self.card_text_y_offset),
                        self.font, 1, (0, 0, 255), self.line_type)
            img[y + 3:y + 3 + self.diamonds_img.shape[0],
            x + 17:x + 17 + self.diamonds_img.shape[1]] = self.diamonds_img
        elif suit == 4:
            cv2.putText(img, self.get_card_value_string(value),
                        (x + self.card_text_x_offset, y + self.card_height - self.card_text_y_offset),
                        self.font, 1, (0, 0, 0), self.line_type)
            img[y + 3:y + 3 + self.clubs_img.shape[0], x + 17:x + 17 + self.clubs_img.shape[1]] = self.clubs_img
        elif suit == 255:
            cv2.putText(img, self.get_card_value_string(value),
                        (x + self.card_text_x_offset, y + self.card_height - self.card_text_y_offset),
                        self.font, 1, (0, 0, 0), self.line_type)

    def draw_cards(self, image, table_x, table_y, num_players, player_cards):
        player_x_margin = 40
        py_center = table_y + self.player_table_offset + self.player_radius
        for i in range(num_players):
            px_center = int((i * (self.player_radius * 2 + player_x_margin)) + int(table_x + self.player_radius))
            for j in range(len(player_cards[i])):
                if player_cards[i][j][0] > 0 and j < 8:
                    self.draw_card(image, int(px_center - self.card_width / 2) - j * 20, py_center - 150 - j * 30,
                                   player_cards[i][j][0], player_cards[i][j][1])

    def draw_game_state(self, num_players, current_player, player_total_values, player_cards):
        image = self.blank_image()
        tx, ty = self.draw_table(image)
        self.draw_players(image, tx, ty, player_total_values, num_players, current_player)
        self.draw_cards(image, tx, ty, num_players, player_cards)
        cv2.imshow('BlackJack', image)
        cv2.waitKey(0)

    @staticmethod
    def end():
        cv2.destroyAllWindows()
