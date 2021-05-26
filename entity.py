import pygame

class Entity:
    def __init__(self, filename_image, filename_data):
        self.image_data = pygame.image.load(filename_image).convert_alpha()
        self.size = 1.0
        self.direction = "DIREITA"
        self.compute_sprite_data(filename_data)

    def set_size(self, size):
        self.size = size
        self.image_data = pygame.transform.scale(self.image_data, (int(self.image_data.get_width() * size), int(self.image_data.get_height() * size)))

    def set_direction(self, direction):
        self.direction = direction

    def compute_sprite_data(self, filename_data):
        txt_sprite_data_lines = open(filename_data, "r").readlines()
        self.animations = {}

        for line in txt_sprite_data_lines:
            animation_name = line.split()[0]
            data_pos_frames = line.split()[1:]
            #print(data_pos_frames)
            self.animations[animation_name] = data_pos_frames

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def get_frame(self, state, frame_number):
        return (int(self.animations[state][frame_number * 4]) * self.size,
            int(self.animations[state][frame_number * 4 + 1]) * self.size,
            int(self.animations[state][frame_number * 4 + 2]) * self.size,
            int(self.animations[state][frame_number * 4 + 3]) * self.size)
