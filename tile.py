import pygame

class Tile:
    def __init__(self, screen):
        """
        Tile 클래스 초기화
        
        Args:
            screen: main.py로부터 전달받은 pygame display surface
        """
        self.screen = screen
        self.load_images()
        # 기본 시작 위치 설정 (화면 중앙 기준)
        screen_width, screen_height = screen.get_size()
        self.base_position = (screen_width // 2, screen_height // 2)
        self.start_pos = (self.base_position[0] + 300, self.base_position[1] + 1100)
        self.tile_positions = []  # 타일들의 위치 정보 (경계를 저장)
        self.background_image = pygame.image.load('./graphics/tiles/overhead_tile.png').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (screen_width,screen_height))
    def load_images(self):
        """트랙에 사용되는 모든 이미지를 로드합니다."""
        self.trackImageST = pygame.image.load('./graphics/tiles/st-h-3-ch.png').convert_alpha()
        self.trackImage6 = pygame.image.load('./graphics/tiles/st-h-3.png').convert_alpha()
        self.trackImage61 = pygame.image.load('./graphics/tiles/st-h-3-k1.png').convert_alpha()
        self.trackImage62 = pygame.image.load('./graphics/tiles/st-h-3-k2.png').convert_alpha()
        self.trackImage63 = pygame.image.load('./graphics/tiles/st-h-3-k3.png').convert_alpha()
        self.trackImage64 = pygame.image.load('./graphics/tiles/st-h-3-k4.png').convert_alpha()
        self.trackImage41 = pygame.image.load('./graphics/tiles/b-4-1.png').convert_alpha()
        self.trackImage31 = pygame.image.load('./graphics/tiles/b-3-1.png').convert_alpha()
        self.trackImage12 = pygame.image.load('./graphics/tiles/b-1-2.png').convert_alpha()
        self.trackImage22 = pygame.image.load('./graphics/tiles/b-2-2.png').convert_alpha()
        self.trackImage34 = pygame.image.load('./graphics/tiles/b-3-4.png').convert_alpha()
        self.trackImage53 = pygame.image.load('./graphics/tiles/st-v-3-k3.png').convert_alpha()
        self.trackImage54 = pygame.image.load('./graphics/tiles/st-v-3-k4.png').convert_alpha()
        self.trackImage21 = pygame.image.load('./graphics/tiles/b-2-1.png').convert_alpha()
        self.trackImage44 = pygame.image.load('./graphics/tiles/b-4-4.png').convert_alpha()
        self.trackImage11 = pygame.image.load('./graphics/tiles/b-1-1.png').convert_alpha()
        self.trackImage14 = pygame.image.load('./graphics/tiles/b-1-4.png').convert_alpha()
        self.trackImage24 = pygame.image.load('./graphics/tiles/b-2-4.png').convert_alpha()

    def draw(self, camera):
        """
        기준 위치에 전체 트랙을 그리고, camera 오프셋을 적용합니다.
        
        Args:
            camera (Camera): 화면에 따라 오프셋을 적용하는 카메라 객체
        """
        position = self.base_position
        background_position = (0, 0)  # 배경 위치 설정
        self.screen.blit(self.background_image, background_position)

        self.screen.blit(self.trackImage62, camera.apply(pygame.Rect(position[0] - 1000, position[1] - 115, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 1000, position[1] - 115, self.trackImage62.get_width(), self.trackImage62.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0] - 700, position[1] - 100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 700, position[1] - 100, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0] - 400, position[1] - 100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 400, position[1] - 100, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0] - 100, position[1] - 100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 100, position[1] - 100, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0], position[1] - 100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0], position[1] - 100, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage64, camera.apply(pygame.Rect(position[0] + 300, position[1] - 100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 300, position[1] - 100, self.trackImage64.get_width(), self.trackImage64.get_height()))

        self.screen.blit(self.trackImage41, camera.apply(pygame.Rect(position[0] + 600, position[1] - 100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 600, position[1] - 100, self.trackImage41.get_width(), self.trackImage41.get_height()))

        self.screen.blit(self.trackImage31, camera.apply(pygame.Rect(position[0] + 600, position[1] + 300, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 600, position[1] + 300, self.trackImage31.get_width(), self.trackImage31.get_height()))

        self.screen.blit(self.trackImage63, camera.apply(pygame.Rect(position[0] + 300, position[1] + 385, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 300, position[1] + 385, self.trackImage63.get_width(), self.trackImage63.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0], position[1] + 400, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0], position[1] + 400, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0] - 300, position[1] + 400, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 300, position[1] + 400, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage61, camera.apply(pygame.Rect(position[0] - 600, position[1] + 400, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 600, position[1] + 400, self.trackImage61.get_width(), self.trackImage61.get_height()))

        self.screen.blit(self.trackImage12, camera.apply(pygame.Rect(position[0] - 1100, position[1] + 400, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 1100, position[1] + 400, self.trackImage12.get_width(), self.trackImage12.get_height()))

        self.screen.blit(self.trackImage22, camera.apply(pygame.Rect(position[0] - 1100, position[1] + 900, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 1100, position[1] + 900, self.trackImage22.get_width(), self.trackImage22.get_height()))

        self.screen.blit(self.trackImage62, camera.apply(pygame.Rect(position[0] - 600, position[1] + 1085, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 600, position[1] + 1085, self.trackImage62.get_width(), self.trackImage62.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0] - 300, position[1] + 1100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 300, position[1] + 1100, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0], position[1] + 1100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0], position[1] + 1100, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImageST, camera.apply(pygame.Rect(*self.start_pos, 0, 0)))
        self.tile_positions.append(pygame.Rect(self.start_pos[0], self.start_pos[1], self.trackImageST.get_width(), self.trackImageST.get_height()))

        self.screen.blit(self.trackImage6, camera.apply(pygame.Rect(position[0] + 600, position[1] + 1100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 600, position[1] + 1100, self.trackImage6.get_width(), self.trackImage6.get_height()))

        self.screen.blit(self.trackImage63, camera.apply(pygame.Rect(position[0] + 900, position[1] + 1085, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 900, position[1] + 1085, self.trackImage63.get_width(), self.trackImage63.get_height()))

        self.screen.blit(self.trackImage34, camera.apply(pygame.Rect(position[0] + 1200, position[1] + 700, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 1200, position[1] + 700, self.trackImage34.get_width(), self.trackImage34.get_height()))

        self.screen.blit(self.trackImage53, camera.apply(pygame.Rect(position[0] + 1585, position[1] + 400, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 1585, position[1] + 400, self.trackImage53.get_width(), self.trackImage53.get_height()))

        self.screen.blit(self.trackImage54, camera.apply(pygame.Rect(position[0] + 1585, position[1] + 100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 1585, position[1] + 100, self.trackImage54.get_width(), self.trackImage54.get_height()))

        self.screen.blit(self.trackImage41, camera.apply(pygame.Rect(position[0] + 1500, position[1] - 300, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 1500, position[1] - 300, self.trackImage41.get_width(), self.trackImage41.get_height()))

        self.screen.blit(self.trackImage21, camera.apply(pygame.Rect(position[0] + 1100, position[1] - 400, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 1100, position[1] - 400, self.trackImage21.get_width(), self.trackImage21.get_height()))

        self.screen.blit(self.trackImage44, camera.apply(pygame.Rect(position[0] + 700, position[1] - 1100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 700, position[1] - 1100, self.trackImage44.get_width(), self.trackImage44.get_height()))

        self.screen.blit(self.trackImage11, camera.apply(pygame.Rect(position[0] + 300, position[1] - 1100, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 300, position[1] - 1100, self.trackImage11.get_width(), self.trackImage11.get_height()))

        self.screen.blit(self.trackImage31, camera.apply(pygame.Rect(position[0] + 200, position[1] - 700, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] + 200, position[1] - 700, self.trackImage31.get_width(), self.trackImage31.get_height()))

        self.screen.blit(self.trackImage63, camera.apply(pygame.Rect(position[0] - 100, position[1] - 615, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 100, position[1] - 615, self.trackImage63.get_width(), self.trackImage63.get_height()))

        self.screen.blit(self.trackImage62, camera.apply(pygame.Rect(position[0] - 100, position[1] - 615, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 100, position[1] - 615, self.trackImage62.get_width(), self.trackImage62.get_height()))

        self.screen.blit(self.trackImage22, camera.apply(pygame.Rect(position[0] - 600, position[1] - 800, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 600, position[1] - 800, self.trackImage22.get_width(), self.trackImage22.get_height()))

        self.screen.blit(self.trackImage41, camera.apply(pygame.Rect(position[0] - 700, position[1] - 1200, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 700, position[1] - 1200, self.trackImage41.get_width(), self.trackImage41.get_height()))

        self.screen.blit(self.trackImage64, camera.apply(pygame.Rect(position[0] - 1000, position[1] - 1200, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 1000, position[1] - 1200, self.trackImage64.get_width(), self.trackImage64.get_height()))

        self.screen.blit(self.trackImage61, camera.apply(pygame.Rect(position[0] - 1000, position[1] - 1200, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 1000, position[1] - 1200, self.trackImage61.get_width(), self.trackImage61.get_height()))

        self.screen.blit(self.trackImage14, camera.apply(pygame.Rect(position[0] - 1700, position[1] - 1200, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 1700, position[1] - 1200, self.trackImage14.get_width(), self.trackImage14.get_height()))

        self.screen.blit(self.trackImage24, camera.apply(pygame.Rect(position[0] - 1700, position[1] - 500, 0, 0)))
        self.tile_positions.append(pygame.Rect(position[0] - 1700, position[1] - 500, self.trackImage24.get_width(), self.trackImage24.get_height()))


    def get_start_position(self):
        """
        시작점 타일(trackImageST)의 위치를 반환합니다.
        
        Returns:
            tuple: 시작점의 (x, y) 좌표
        """
        return self.start_pos
    
    def get_tile_positions(self):
        return self.tile_positions

    