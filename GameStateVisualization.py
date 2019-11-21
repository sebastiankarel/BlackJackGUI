import cv2
import numpy as np


class Visualizer:
    __max_num_players = 10

    __height = 600
    __width = 1200

    __table_width = __width * 0.8
    __table_height = __height * 0.7
    __table_y_offset = 5
    __table_color = (41, 145, 0)

    __player_radius = 30
    __player_table_offset = 10
    __player_color = (255, 102, 3)
    __player_color_inactive = (209, 209, 209)
    __player_color_current_turn = (0, 100, 255)
    __dealer_color = (0, 0, 0)

    __font = cv2.FONT_HERSHEY_SIMPLEX
    __font_color = (255, 255, 255)
    __line_type = 2

    __card_width = 40
    __card_height = 60
    __card_font_color_black = (0, 0, 0)
    __card_font_color_red = (0, 0, 255)
    __card_text_x_offset = 5
    __card_text_y_offset = 5
    __card_font_scale = 0.5
    __clubs_img = cv2.resize(cv2.imread('res\\clubs.jpg'), (20, 25))
    __spades_img = cv2.resize(cv2.imread('res\\spades.jpg'), (20, 25))
    __hearts_img = cv2.resize(cv2.imread('res\\hearts.jpg'), (20, 25))
    __diamonds_img = cv2.resize(cv2.imread('res\\diamonds.jpg'), (20, 25))

    def __blank_image(self):
        img = np.ones((self.__height, self.__width, 3), np.uint8)
        img *= 255
        return img

    def __draw_table(self, img):
        tx1 = int((self.__width / 2) - (self.__table_width / 2))
        ty1 = self.__table_y_offset
        tx2 = int(tx1 + self.__table_width)
        ty2 = int(ty1 + self.__table_height)
        cv2.rectangle(img, (0, ty1), (self.__width, ty2), self.__table_color, -1)
        cv2.rectangle(img, (tx1, ty1), (tx2, ty2), self.__table_color, -1)
        return tx1, ty2

    def __draw_total(self, img, px_center, ty2, player_no, player_totals):
        total = player_totals[player_no]
        if total < 10:
            cv2.putText(img, str(total), (px_center - 10, ty2 - 10), self.__font, 1, self.__font_color, self.__line_type)
        else:
            cv2.putText(img, str(total), (px_center - 20, ty2 - 10), self.__font, 1, self.__font_color, self.__line_type)

    def __draw_players(self, img, table_x, table_y, player_totals, num_players, current_player):
        player_x_margin = 40
        py_center = table_y + self.__player_table_offset + self.__player_radius
        for i in range(self.__max_num_players):
            px_center = int((i * (self.__player_radius * 2 + player_x_margin)) + int(table_x + self.__player_radius))
            if i < num_players:
                if i == current_player:
                    cv2.circle(img, (px_center, py_center), self.__player_radius, self.__player_color_current_turn, -1)
                else:
                    cv2.circle(img, (px_center, py_center), self.__player_radius, self.__player_color, -1)
            else:
                cv2.circle(img, (px_center, py_center), self.__player_radius, self.__player_color_inactive, -1)
            cv2.putText(img, str(i), (px_center - 10, py_center + 10), self.__font, 1, self.__font_color, self.__line_type)
            self.__draw_total(img, px_center, table_y, i, player_totals)

    def __draw_dealer(self, img, table_x, dealer_total, dealer_cards):
        py_center = self.__player_radius + 20
        px_center = int(table_x + self.__table_width / 2 - self.__player_radius / 2)
        cv2.circle(img, (px_center, py_center), self.__player_radius, self.__dealer_color, -1)
        cv2.putText(img, "D", (px_center - 10, py_center + 10), self.__font, 1, self.__font_color, self.__line_type)
        cv2.putText(img, str(dealer_total), (px_center - 80, py_center + 10), self.__font, 1, self.__font_color, self.__line_type)
        card_x = px_center + 20
        for i in range(len(dealer_cards)):
            if dealer_cards[i][0] > 0:
                self.__draw_card(img, card_x + i * (self.__card_width + 5), py_center,
                             dealer_cards[i][0], dealer_cards[i][1])

    @staticmethod
    def __get_card_value_string(code):
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

    def __draw_card(self, img, x, y, value, suit):
        cv2.rectangle(img, (x, y), (x + self.__card_width, y + self.__card_height), (255, 255, 255), -1)
        if suit == 1:
            cv2.putText(img, self.__get_card_value_string(value),
                        (x + self.__card_text_x_offset, y + self.__card_height - self.__card_text_y_offset),
                        self.__font, 1, (0, 0, 0), self.__line_type)
            img[y + 3:y + 3 + self.__spades_img.shape[0], x + 17:x + 17 + self.__spades_img.shape[1]] = self.__spades_img
        elif suit == 2:
            cv2.putText(img, self.__get_card_value_string(value),
                        (x + self.__card_text_x_offset, y + self.__card_height - self.__card_text_y_offset),
                        self.__font, 1, (0, 0, 255), self.__line_type)
            img[y + 3:y + 3 + self.__hearts_img.shape[0], x + 17:x + 17 + self.__hearts_img.shape[1]] = self.__hearts_img
        elif suit == 3:
            cv2.putText(img, self.__get_card_value_string(value),
                        (x + self.__card_text_x_offset, y + self.__card_height - self.__card_text_y_offset),
                        self.__font, 1, (0, 0, 255), self.__line_type)
            img[y + 3:y + 3 + self.__diamonds_img.shape[0],
            x + 17:x + 17 + self.__diamonds_img.shape[1]] = self.__diamonds_img
        elif suit == 4:
            cv2.putText(img, self.__get_card_value_string(value),
                        (x + self.__card_text_x_offset, y + self.__card_height - self.__card_text_y_offset),
                        self.__font, 1, (0, 0, 0), self.__line_type)
            img[y + 3:y + 3 + self.__clubs_img.shape[0], x + 17:x + 17 + self.__clubs_img.shape[1]] = self.__clubs_img
        elif suit == 255:
            cv2.putText(img, self.__get_card_value_string(value),
                        (x + self.__card_text_x_offset, y + self.__card_height - self.__card_text_y_offset),
                        self.__font, 1, (0, 0, 0), self.__line_type)

    def __draw_player_cards(self, image, table_x, table_y, num_players, player_cards):
        player_x_margin = 40
        py_center = table_y + self.__player_table_offset + self.__player_radius
        for i in range(num_players):
            px_center = int((i * (self.__player_radius * 2 + player_x_margin)) + int(table_x + self.__player_radius))
            for j in range(len(player_cards[i])):
                if player_cards[i][j][0] > 0 and j < 8:
                    self.__draw_card(image, int(px_center - self.__card_width / 2) - j * 20, py_center - 150 - j * 30,
                                     player_cards[i][j][0], player_cards[i][j][1])

    def draw_game_state(self, num_players, current_player, player_total_values, player_cards, dealer_total, dealer_cards):
        image = self.__blank_image()
        tx, ty = self.__draw_table(image)
        self.__draw_players(image, tx, ty, player_total_values, num_players, current_player)
        self.__draw_player_cards(image, tx, ty, num_players, player_cards)
        self.__draw_dealer(image, tx, dealer_total, dealer_cards)
        cv2.imshow('BlackJack', image)
        cv2.waitKey(5000)

    @staticmethod
    def end():
        cv2.destroyAllWindows()
