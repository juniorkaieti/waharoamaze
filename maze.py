import pygame

#window screen
WIDTH, HEIGHT, FPS = 800, 600, 60
NAVY = (9, 24, 43)
WHITE = (255, 255, 255)
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Waharoa Maze")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 70)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(NAVY)
        title = font.render("Waharoa Maze", True, WHITE)
        screen.blit(title, (250, 250))
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    run_game()
