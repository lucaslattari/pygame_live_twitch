import pygame

class SpriteSheet:
    def __init__(self, filename_image, filename_data):
        self.image_data = pygame.image.load(filename_image).convert_alpha()
        self.compute_sprite_data(filename_data)

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

    def get_frame(self, state, frame_number):
        return (int(self.animations[state][frame_number * 4]),
            int(self.animations[state][frame_number * 4 + 1]),
            int(self.animations[state][frame_number * 4 + 2]),
            int(self.animations[state][frame_number * 4 + 3]))
