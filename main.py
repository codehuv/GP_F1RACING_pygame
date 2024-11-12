import pygame
import sys
from car import Car
from camera import Camera
from tile import Tile  # Tile 임포트

# 게임 화면 크기
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800

# 초기화
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

logo_sound = pygame.mixer.Sound('./sounds/max.mp3')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 게임 설정 (여기서는 예시로만 설정)
tile_map = Tile(screen)  # 타일맵 객체는 이미 만들어져 있다고 가정

# 타이머 변수 초기화
start_time = 0
lap_times = []
is_running = False
total_start_time = 0
menu_active = True

#로고 이미지
logo_image = pygame.image.load('./graphics/main_logo.jpeg').convert_alpha()

# 순위표
leaderboard = []

# 플레이어 이름을 받는 함수 (게임 시작 전)
def get_player_name():
    font = pygame.font.Font(None, 36)
    name_text = font.render("Enter Player Name: (Press ENTER to confirm)", True, (255, 255, 255))
    name_input = ""
    input_active = True
    while input_active:
        screen.fill((0, 0, 0))  # 화면 초기화 (배경 색은 검정으로 설정)
        screen.blit(name_text, (SCREEN_WIDTH // 2 - name_text.get_width() // 2, SCREEN_HEIGHT // 3))
        
        name_display = font.render(name_input, True, (255, 255, 255))
        screen.blit(name_display, (SCREEN_WIDTH // 2 - name_display.get_width() // 2, SCREEN_HEIGHT // 2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name_input = name_input[:-1]
                else:
                    name_input += event.unicode

        pygame.display.flip()
        clock.tick(60)
    return name_input

# 메뉴 항목 선택
menu_options = ["Start", "Quit"]
current_option = 0

#Sound loop
sound_played = False
# 게임 루프
running = True
while running:
    time_delta = clock.get_time() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 상태 가져오기
    keys = pygame.key.get_pressed()

    # 메뉴 화면
    if menu_active:
        if not sound_played:
            logo_sound.play()
            sound_played=True
        screen.fill((30, 30, 30))  # 메뉴 화면 배경 색상 (어두운 회색)

        font = pygame.font.Font(None, 36)
        #로고 표시
        logo_image = pygame.transform.scale(logo_image, (SCREEN_WIDTH+200,SCREEN_HEIGHT))
        logo_rect = logo_image.get_rect()
        logo_rect.centerx = SCREEN_WIDTH // 2 - 100
        screen.blit(logo_image, logo_rect)

        # 리더보드 표시
        if leaderboard:
            title_text = font.render("Leaderboard:", True, (255, 255, 255))
            screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
            
            for i, player in enumerate(leaderboard):
                score_text = font.render(
                    f"{i+1}. {player['name']} - Best Lap: {player['best_lap']:.2f} - Total Time: {player['total_time']:.2f}",
                    True, (255, 255, 255)
                )
                screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 150 + i * 40))

        # 메뉴 옵션 (리더보드 아래에 표시)
        menu_y_offset = 400  # 리더보드와 메뉴 옵션 사이 간격 확보
        for i, option in enumerate(menu_options):
            color = (255, 0, 0) if i == current_option else (255, 255, 255)
            option_text = font.render(option, True, color)
            screen.blit(option_text, (SCREEN_WIDTH // 2 - option_text.get_width() // 2, menu_y_offset + i * 40))

        # 메뉴에서 UP, DOWN, ENTER 키로 선택
        if keys[pygame.K_UP]:
            pygame.time.delay(100)
            current_option = (current_option - 1) % len(menu_options)
        if keys[pygame.K_DOWN]:
            pygame.time.delay(100)
            current_option = (current_option + 1) % len(menu_options)
        if keys[pygame.K_RETURN]:
            if current_option == 0:  # Start 선택
                player_name = get_player_name()  # 이름 받기
                menu_active = False  # 메뉴 종료
                is_running = False  # 게임 시작 플래그 설정
                start_x, start_y = tile_map.get_start_position()
                start_x -= 30
                start_y += 150
                car = Car(start_x, start_y, 50, 100, 0, tile_map.get_tile_positions())
                camera = Camera(SCREEN_WIDTH,SCREEN_HEIGHT)
            elif current_option == 1:  # Quit 선택
                running = False

    else:  # 게임 화면
        # W 키로 게임 시작
        if not is_running and keys[pygame.K_UP]:
            is_running = True
            start_time = pygame.time.get_ticks()
            total_start_time = pygame.time.get_ticks()

        # 자동차 이동 업데이트
        if is_running:  # 게임이 시작되었을 때만 자동차 이동
            car.move(time_delta, keys)

        # 카메라 업데이트
        camera.update(car.car_x, car.car_y)

        # 시작점을 기준으로 자동차가 지나갔는지 체크
        if (start_x - 5 < car.car_x < start_x + 5 and
            start_y - 100 < car.car_y < start_y + 100):
            if is_running and pygame.time.get_ticks() - start_time > 1000:  # 일정 시간이 지난 후만 랩 기록
                lap_time = (pygame.time.get_ticks() - start_time) / 1000  # 시간 초 단위로 변환
                lap_times.append(lap_time)  # 랩 타임 기록
                start_time = pygame.time.get_ticks()  # 타이머 리셋

        # 배경색 설정
        screen.fill((30, 30, 30))

        # 타일맵 그리기
        tile_map.draw(camera)

        # 자동차 그리기 (카메라 오프셋 적용)
        r_img, r_rect = car.draw_car()
        screen.blit(r_img, camera.apply(r_rect))
        
        # 랩 타이머
        if is_running:
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            time_text = font.render(f"Time: {elapsed_time:.2f}", True, (255, 255, 255))
        else:
            time_text = font.render("Press UP to Start", True, (255, 255, 255))  # 게임 시작 안내 메시지
        screen.blit(time_text, (10, 50))

        # 랩타임 그리기
        lap_text = font.render(f"Lap: {len(lap_times)}", True, (255, 255, 255))
        screen.blit(lap_text, (10, 90))

        if lap_times:
            best_lap_text = font.render(f"Best Lap: {min(lap_times):.2f}", True, (255, 255, 255))
            screen.blit(best_lap_text, (10, 130))

        # 9번의 랩을 완료한 후 종료
        if len(lap_times) >= 3:  # 3바퀴로 설정되어 있네요
            # 전체 경과 시간 계산
            total_elapsed_time = (pygame.time.get_ticks() - total_start_time) / 1000
            
            # 게임 오버 메시지
            game_over_text = font.render("Game Over! 3 Laps Completed!", True, (255, 255, 255))
            best_lap_text = font.render(f"Best Lap: {min(lap_times):.2f}", True, (255, 255, 255))
            total_time_text = font.render(f"Total Time: {total_elapsed_time:.2f}", True, (255, 255, 255))
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 60))
            screen.blit(best_lap_text, (SCREEN_WIDTH // 2 - best_lap_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
            screen.blit(total_time_text, (SCREEN_WIDTH // 2 - total_time_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

            # 순위표에 기록 추가
            leaderboard.append({
                "name": player_name,
                "best_lap": min(lap_times),
                "total_time": total_elapsed_time
            })
            # Best Lap 기준으로 정렬
            leaderboard.sort(key=lambda x: x['best_lap'])
            # 상위 5명만 유지
            leaderboard = leaderboard[:5]

            pygame.display.flip()
            pygame.time.delay(3000)  # 3초 대기
            
            # 메인 메뉴로 돌아가기
            menu_active = True
            lap_times.clear()  # 랩 타임만 초기화
            is_running = False
            sound_played=False
            car.sound_stop()
            del car

    pygame.display.flip()
    clock.tick(144)

# 종료
pygame.quit()
sys.exit()
