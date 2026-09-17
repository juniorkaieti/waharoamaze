import pygame

#window screen
WIDTH, HEIGHT, FPS = 800, 600, 60

NAVY = (9, 24, 43)
WHITE = (255, 255, 255)
ORANGE = (255, 149, 0)
GREEN = (50, 200, 100)
BLACK = (0, 0, 0)

def run_game():
    pygame.init()
    #small part of this area was also helped by ai
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Waharoa Maze")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 70)
    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 30)

    #5 maze levels 

    level = [
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

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(NAVY)
        #screen title use by the help of ai
        title = font.render("Waharoa Maze", True, WHITE)
        screen.blit(title, (250, 250))
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    run_game()
