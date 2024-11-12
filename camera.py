class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, target_x, target_y):
        # 타겟(예: 자동차)의 위치를 중앙에 유지하도록 오프셋 설정
        self.offset_x = self.screen_width // 2 - target_x
        self.offset_y = self.screen_height // 2 - target_y

    def apply(self, rect):
        # 오프셋을 적용한 새로운 위치 반환
        return rect.move(self.offset_x, self.offset_y)
