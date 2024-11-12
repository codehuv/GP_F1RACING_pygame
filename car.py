import pygame
import math

class Car(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, speed, tile_positions, max_speed=1000):
        super().__init__()
        self.width = width
        self.height = height
        self.car_x = pos_x
        self.car_y = pos_y
        self.car_speed = speed
        self.car_angle = 0
        self.acceleration = 0
        self.angular_velocity = 0
        self.turn_acceleration = 0.5
        self.max_speed = max_speed
        self.original_image = pygame.image.load("./graphics/Mini Pixel Pack 2/Cars/bike1-1.png").convert_alpha()
        self.image = pygame.transform.rotate(self.original_image, 0)
        self.rect = self.image.get_rect(center=(self.car_x, self.car_y))
        self.tile_positions = tile_positions
        # 사운드 설정
        self.engine_sound = pygame.mixer.Sound('./sounds/go.mp3')  
        # 직진 키를 눌렀을 때 재생할 사운드
        self.curve_sound = pygame.mixer.Sound('./sounds/curve.mp3')  
        # 회전 시 재생할 사운드

        self.engine_sound.set_volume(0.1)  # 기본 볼륨을 50%로 설정
        self.curve_sound.set_volume(1)  # 기본 볼륨을 50%로 설정

        self.engine_playing = False  # 직진 사운드 재생 상태
        self.curve_playing = False  # 회전 사운드 재생 상태
        

    def draw_car(self):
        rotated_image = pygame.transform.rotate(self.image, self.car_angle)
        rotated_rect = rotated_image.get_rect(center=(self.car_x, self.car_y))
        return rotated_image, rotated_rect

    def move(self, time_delta, keys):
        if keys[pygame.K_UP]:
            self.acceleration = 120
            if not self.engine_playing:
                self.engine_sound.play(loops=-1, maxtime=0)  
                # 무한 반복으로 사운드 재생
                self.engine_playing = True
        elif keys[pygame.K_DOWN]:
            self.acceleration = -160
        else:
            self.acceleration = -0.9 * self.car_speed
            if self.engine_playing:
                self.engine_sound.stop()
                self.engine_playing = False
       # 회전 중일 때 사운드 재생
        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and not self.curve_playing:
            if self.engine_playing:
                self.engine_sound.fadeout(500)  # 직진 소리 점차 사라짐
                self.engine_playing = False
            self.curve_sound.play(loops=-1, maxtime=0)  # 회전 소리 무한 반복
            self.curve_playing = True
            # 직진 소리와 회전 소리가 동시에 재생될 때
        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and self.engine_playing:
            # 직진 소리의 볼륨을 줄여줍니다
            self.engine_sound.set_volume(0.3)  # 직진 소리 볼륨 30%로 줄임
        else:
            if self.engine_playing:
                self.engine_sound.set_volume(1.0)  # 직진 소리 볼륨을 원래대로 복구

        # 회전 소리의 fadeout 처리
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and self.curve_playing:
            self.curve_sound.fadeout(500)  # 회전 소리 점차 사라짐
            self.curve_playing = False
                
        self.car_speed += self.acceleration * time_delta
        if self.car_speed > self.max_speed:
            self.car_speed = self.max_speed
        elif self.car_speed < -self.max_speed:
            self.car_speed = -self.max_speed

        self.car_x += (self.car_speed * math.cos(math.radians(self.car_angle)) * time_delta +
                       0.5 * self.acceleration * math.cos(math.radians(self.car_angle)) * (time_delta ** 2))
        self.car_y -= (self.car_speed * math.sin(math.radians(self.car_angle)) * time_delta +
                       0.5 * self.acceleration * math.sin(math.radians(self.car_angle)) * (time_delta ** 2))

        if self.car_speed != 0:
            if keys[pygame.K_RIGHT]:
                if self.angular_velocity > 0:
                    self.angular_velocity = 0
                self.angular_velocity -= self.turn_acceleration * time_delta
            elif keys[pygame.K_LEFT]:
                if self.angular_velocity < 0:
                    self.angular_velocity = 0
                self.angular_velocity += self.turn_acceleration * time_delta
            else:
                self.angular_velocity *= 0.9

        self.car_angle += self.angular_velocity
        self.handle_collision()


    def handle_collision(self):
        rotated_image, rotated_rect = self.draw_car()
        self.rect = rotated_rect

        is_within_any_tile = False
        nearest_tile = None
        nearest_overlap_x = 0
        nearest_overlap_y = 0

        for tile_rect in self.tile_positions:
            if self.rect.colliderect(tile_rect):
                is_within_any_tile = True
                break
            else:
                dx = min(tile_rect.right - self.rect.left, self.rect.right - tile_rect.left)
                dy = min(tile_rect.bottom - self.rect.top, self.rect.bottom - tile_rect.top)
                
                if nearest_tile is None or abs(dx) < abs(nearest_overlap_x) or abs(dy) < abs(nearest_overlap_y):
                    nearest_tile = tile_rect
                    nearest_overlap_x = dx
                    nearest_overlap_y = dy

        if not is_within_any_tile and nearest_tile is not None:
            if abs(nearest_overlap_x) < abs(nearest_overlap_y):
                self.car_x += nearest_overlap_x
                self.car_speed = -self.car_speed * math.cos(math.radians(self.car_angle))
                self.car_angle = 180 - self.car_angle
            else:
                self.car_y += nearest_overlap_y
                self.car_speed = -self.car_speed * math.sin(math.radians(self.car_angle))
                self.car_angle = -self.car_angle

            print("충돌 발생! 트랙 경계에서 반사.")

    def sound_stop(self):
        self.engine_sound.stop()
        self.curve_sound.stop()


