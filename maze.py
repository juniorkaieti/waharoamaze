import pygame

#window screen
WIDTH, HEIGHT, FPS = 800, 600, 60

NAVY = (9, 24, 43)
WHITE = (255, 255, 255)
ORANGE = (255, 149, 0)
GREEN = (50, 200, 100)
BLACK = (0, 0, 0)
DARKGREEN = (34, 139, 34)
RED = (255, 0, 0)

def run_game():
    pygame.init()
    #small part of this area was also helped by ai
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Waharoa Maze")
    clock = pygame.time.Clock()

    title_font = pygame.font.Font(None, 70)
    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 30)

    #5 maze levels 

    levels = [
        #Coldstream
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

        #Uttley
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

        #Deaker
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

        #Pearce
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

        #Grant
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

    information = [
        "Hi"
        "Mauri"
        "Kia ora"
        "Malo"
        "Bula"
    ]

    #adding players
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
    start_time = pygame.time.get_ticks

    while running:
        clock.tick(FPS)

        #Events
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
        #Player controlss
        if not welcome and not won and not info_box:
            keys = pygame.key.get_pressed()
            old_x = player.x
            old_y = player.y
            #player being able to move
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.x -= player_speed

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.x += player_speed

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player.y -= player_speed

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player.y += player_speed
            #wall
            for wall in levels[level]:
                if player.colliderect(wall):
                    player.x = old_x
                    player.y = old_y
            #finish line
            if player.colliderect(finish):
                #showing the information box
                info_box = True
        #Screen color    
        screen.fill(NAVY)

        #Welcome Screen
        if welcome:

        #screen title use by the help of ai
            title = font.render("Waharoa Maze", True, WHITE)
            start = title_font.render("Press ENTER to Play", True, RED)
            controls = small_font.render("Use WASD or Arrow Keys to move", True, WHITE)

            screen.blit(title, (250, 250))
            screen.blit(start, (235, 300))
            screen.blit(controls, (260, 360))

        #Game screen
        elif not won:

            #maze walls
             for wall in levels[level]:
                pygame.draw.rect(screen, DARKGREEN, wall)
            #finish line
                pygame.draw.rect(screen, GREEN, finish)
            #level
                level_text = small_font.render(
                    "Level" + str(level + 1) + " / 5", True, WHITE
                )
            #Information box

                if info_box:
                #dark overlay
                    overlay = pygame.Surface((WIDTH, HEIGHT))
                    overlay.set_alpha(180)
                    overlay.fill(BLACK)
                    screen.blit(overlay, (0, 0))


        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    run_game()
