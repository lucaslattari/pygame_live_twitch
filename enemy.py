import pygame

class Enemy:
    def __init__(self, nome_inimigo, nome_arquivo):
        self.nome_inimigo = nome_inimigo
        self.image_data = pygame.image.load(nome_arquivo)
        self.position = {}

    def set_position(self, x, y):
        self.position["x"] = x
        self.position["y"] = y

    def set_position_x(self, x):
        self.position["x"] = x

    def set_position_y(self, y):
        self.position["y"] = y

    def add_position(self, x, y):
        self.position["x"] += x
        self.position["y"] += y

    def add_position_x(self, x):
        self.position["x"] += x

    def add_position_y(self, y):
        self.position["y"] += y

    def get_position(self):
        return (self.position["x"], self.position["y"])
