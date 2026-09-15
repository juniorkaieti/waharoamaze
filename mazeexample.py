import pygame

# window screen
WIDTH, HEIGHT, FPS = 800, 600, 60

NAVY = (9, 24, 43)
WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)
GREEN = (50, 200, 100)
BLACK = (0, 0, 0)

def run_game():
    pygame.init()

    # screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Waharoa Maze")
    clock = pygame.time.Clock()

    # fonts
    title_font = pygame.font.Font(None, 80)
    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 30)

    # -------------------------
    # 5 MAZE LEVELS
    # -------------------------

    levels = [

        # LEVEL 1
        [
            pygame.Rect(0, 0, 800, 20),
            pygame.Rect(0, 580, 800, 20),
            pygame.Rect(0, 0, 20, 600),
            pygame.Rect(780, 0, 20, 600),

            pygame.Rect(150, 20, 20, 400),
            pygame.Rect(150, 480, 20, 100),

            pygame.Rect(300, 100, 20, 400),
            pygame.Rect(300, 100, 200, 20),

            pygame.Rect(450, 200, 20, 300),
            pygame.Rect(450, 200, 200, 20),

            pygame.Rect(600, 300, 20, 280),
        ],

        # LEVEL 2
        [
            pygame.Rect(0, 0, 800, 20),
            pygame.Rect(0, 580, 800, 20),
            pygame.Rect(0, 0, 20, 600),
            pygame.Rect(780, 0, 20, 600),

            pygame.Rect(100, 20, 20, 350),
            pygame.Rect(100, 450, 20, 130),

            pygame.Rect(200, 100, 20, 480),
            pygame.Rect(300, 20, 20, 350),
            pygame.Rect(300, 450, 20, 130),

            pygame.Rect(400, 100, 20, 400),
            pygame.Rect(500, 20, 20, 350),
            pygame.Rect(500, 450, 20, 130),

            pygame.Rect(600, 100, 20, 400),
            pygame.Rect(700, 20, 20, 350),
        ],

        # LEVEL 3
        [
            pygame.Rect(0, 0, 800, 20),
            pygame.Rect(0, 580, 800, 20),
            pygame.Rect(0, 0, 20, 600),
            pygame.Rect(780, 0, 20, 600),

            pygame.Rect(100, 20, 20, 450),
            pygame.Rect(100, 520, 20, 60),

            pygame.Rect(200, 100, 20, 480),
            pygame.Rect(300, 20, 20, 450),
            pygame.Rect(300, 520, 20, 60),

            pygame.Rect(400, 100, 20, 480),
            pygame.Rect(500, 20, 20, 450),
            pygame.Rect(500, 520, 20, 60),

            pygame.Rect(600, 100, 20, 480),
            pygame.Rect(700, 20, 20, 450),
        ],

        # LEVEL 4
        [
            pygame.Rect(0, 0, 800, 20),
            pygame.Rect(0, 580, 800, 20),
            pygame.Rect(0, 0, 20, 600),
            pygame.Rect(780, 0, 20, 600),

            pygame.Rect(100, 20, 20, 250),
            pygame.Rect(100, 330, 20, 250),

            pygame.Rect(200, 20, 20, 400),
            pygame.Rect(200, 480, 20, 100),

            pygame.Rect(300, 100, 20, 480),

            pygame.Rect(400, 20, 20, 400),
            pygame.Rect(400, 480, 20, 100),

            pygame.Rect(500, 20, 20, 250),
            pygame.Rect(500, 330, 20, 250),

            pygame.Rect(600, 100, 20, 400),
            pygame.Rect(700, 20, 20, 250),
            pygame.Rect(700, 330, 20, 250),
        ],

        # LEVEL 5
        [
            pygame.Rect(0, 0, 800, 20),
            pygame.Rect(0, 580, 800, 20),
            pygame.Rect(0, 0, 20, 600),
            pygame.Rect(780, 0, 20, 600),

            pygame.Rect(80, 20, 20, 400),
            pygame.Rect(80, 480, 20, 100),

            pygame.Rect(180, 100, 20, 480),
            pygame.Rect(280, 20, 20, 400),
            pygame.Rect(280, 480, 20, 100),

            pygame.Rect(380, 100, 20, 480),
            pygame.Rect(480, 20, 20, 400),
            pygame.Rect(480, 480, 20, 100),

            pygame.Rect(580, 100, 20, 480),
            pygame.Rect(680, 20, 20, 400),
            pygame.Rect(680, 480, 20, 100),
        ]
    ]

    # -------------------------
    # INFORMATION FOR LEVELS
    # -------------------------

    information = [
        "A waharoa is a traditional Maori gateway.",
        "Waharoa can represent identity, history and culture.",
        "Carvings can tell stories about ancestors and traditions.",
        "Kaitiakitanga means caring for and protecting the environment.",
        "Learning about culture helps keep traditions strong for future generations."
    ]

    # player
    player = pygame.Rect(40, 40, 25, 25)
    player_speed = 4

    # finish
    finish = pygame.Rect(730, 520, 40, 40)

    # game states
    welcome = True
    won = False
    info_box = False

    level = 0

    running = True
    start_time = pygame.time.get_ticks()

    while running:
        clock.tick(FPS)

        # -------------------------
        # EVENTS
        # -------------------------

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # Start game
                if welcome and event.key == pygame.K_RETURN:
                    welcome = False
                    start_time = pygame.time.get_ticks()

                # Restart
                if event.key == pygame.K_r:
                    welcome = True
                    won = False
                    info_box = False
                    level = 0
                    player.x = 40
                    player.y = 40

            # Click to close information box
            if event.type == pygame.MOUSEBUTTONDOWN:

                if info_box:

                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Continue button
                    if 330 <= mouse_x <= 470 and 430 <= mouse_y <= 480:

                        info_box = False

                        level += 1

                        if level >= 5:
                            won = True
                        else:
                            player.x = 40
                            player.y = 40

                    # X button
                    if 700 <= mouse_x <= 750 and 150 <= mouse_y <= 200:

                        info_box = False

                        level += 1

                        if level >= 5:
                            won = True
                        else:
                            player.x = 40
                            player.y = 40

        # -------------------------
        # GAMEPLAY
        # -------------------------

        if not welcome and not won and not info_box:

            keys = pygame.key.get_pressed()

            old_x = player.x
            old_y = player.y

            # movement
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.x -= player_speed

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.x += player_speed

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player.y -= player_speed

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player.y += player_speed

            # wall collision
            for wall in levels[level]:

                if player.colliderect(wall):
                    player.x = old_x
                    player.y = old_y

            # reach finish
            if player.colliderect(finish):

                # show information box
                info_box = True

        # -------------------------
        # DRAW SCREEN
        # -------------------------

        screen.fill(NAVY)

        # -------------------------
        # WELCOME SCREEN
        # -------------------------

        if welcome:

            title = title_font.render(
                "Waharoa Maze", True, WHITE
            )

            start = font.render(
                "Press ENTER to Start", True, ORANGE
            )

            controls = small_font.render(
                "Use WASD or Arrow Keys to move",
                True,
                WHITE
            )

            screen.blit(title, (220, 180))
            screen.blit(start, (235, 300))
            screen.blit(controls, (260, 360))

        # -------------------------
        # GAME SCREEN
        # -------------------------

        elif not won:

            # maze walls
            for wall in levels[level]:
                pygame.draw.rect(screen, WHITE, wall)

            # finish
            pygame.draw.rect(screen, GREEN, finish)

            # player
            pygame.draw.rect(screen, ORANGE, player)

            # level
            level_text = small_font.render(
                "Level: " + str(level + 1) + " / 5",
                True,
                WHITE
            )

            screen.blit(level_text, (30, 30))

            # timer
            time = (pygame.time.get_ticks() - start_time) // 1000

            timer_text = small_font.render(
                "Time: " + str(time) + "s",
                True,
                WHITE
            )

            screen.blit(timer_text, (680, 30))

            # -------------------------
            # INFORMATION BOX
            # -------------------------

            if info_box:

                # dark overlay
                overlay = pygame.Surface((WIDTH, HEIGHT))
                overlay.set_alpha(180)
                overlay.fill(BLACK)
                screen.blit(overlay, (0, 0))

                # information box
                box = pygame.Rect(150, 150, 500, 350)
                pygame.draw.rect(screen, WHITE, box)

                # heading
                heading = font.render(
                    "Level Complete!",
                    True,
                    NAVY
                )

                screen.blit(heading, (260, 190))

                # information
                info_text = information[level]

                # split text into lines
                words = info_text.split()
                lines = []
                current_line = ""

                for word in words:

                    test_line = current_line + word + " "

                    if small_font.size(test_line)[0] < 400:
                        current_line = test_line

                    else:
                        lines.append(current_line)
                        current_line = word + " "

                lines.append(current_line)

                y = 270

                for line in lines:

                    text = small_font.render(
                        line,
                        True,
                        NAVY
                    )

                    screen.blit(text, (200, y))
                    y += 35

                # continue button
                button = pygame.Rect(330, 430, 140, 50)

                pygame.draw.rect(
                    screen,
                    ORANGE,
                    button
                )

                button_text = small_font.render(
                    "Continue",
                    True,
                    WHITE
                )

                screen.blit(
                    button_text,
                    (350, 445)
                )

                # X button
                x_button = pygame.Rect(700, 150, 50, 50)

                pygame.draw.rect(
                    screen,
                    ORANGE,
                    x_button
                )

                x_text = font.render(
                    "X",
                    True,
                    WHITE
                )

                screen.blit(
                    x_text,
                    (712, 155)
                )

        # -------------------------
        # FINAL WIN SCREEN
        # -------------------------

        if won:

            win_text = title_font.render(
                "YOU WIN!",
                True,
                GREEN
            )

            completed = font.render(
                "You completed all 5 levels!",
                True,
                WHITE
            )

            restart = small_font.render(
                "Press R to play again",
                True,
                ORANGE
            )

            screen.blit(win_text, (275, 180))
            screen.blit(completed, (190, 290))
            screen.blit(restart, (290, 360))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run_game()