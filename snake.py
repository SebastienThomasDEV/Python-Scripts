import pygame
from random import randint


def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
    bg = pygame.image.load('assets/bg.png')
    ecrantitre = pygame.image.load('assets/ecrantitre.png')
    running = True
    pygame.display.set_caption("Snakezer")
    play = False
    while running:
        if play == False:
            serpent.perdu()
            screen.blit(ecrantitre, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play = True

        if play == True:
            screen.blit(bg, (0, 0))
            screen.blit(food.image, (food.rect.x, food.rect.y))
            screen.blit(serpent.image, serpent.rect)
            screen.blit(serpent2.image,serpent2.rect)

            if serpent.getcoordsX() == food.rect.x and serpent.getcoordsY() == food.rect.y:
                food.rect.x = food.newcoordsX()
                food.rect.y = food.newcoordsY()
                serpent.grailler()
            coordnow = (serpent.rect.x, serpent.rect.y)
            coordsanslatete = serpent.listcoord[:-1]
            if coordnow in coordsanslatete:
                play = False

            goodcoords = (serpent.rect.x, serpent.rect.y)
            if goodcoords not in serpent.listcoord:
                serpent.listcoord.append((serpent.rect.x, serpent.rect.y))
            if len(serpent.listcoord) > serpent.longueur:
                del serpent.listcoord[0]
            if serpent.listcoord[-1][0] in serpent.badcoordx or serpent.listcoord[-1][1] in serpent.badcoordy:
                play = False

            for i in serpent.listcoord:
                screen.blit(serpent.image, (i[0], i[1]))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print("Fermeture du jeu")
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        serpent.move_up()
                        pygame.display.flip()
                    if event.key == pygame.K_DOWN:
                        serpent.move_down()
                        pygame.display.flip()
                    if event.key == pygame.K_LEFT:
                        serpent.move_left()
                        pygame.display.flip()
                    if event.key == pygame.K_RIGHT:
                        serpent.move_right()
                        pygame.display.flip()
                    if event.key == pygame.K_w:
                        serpent2.move_up()
                        pygame.display.flip()
                    if event.key == pygame.K_s:
                        serpent2.move_down()
                        pygame.display.flip()
                    if event.key == pygame.K_a:
                        serpent2.move_left()
                        pygame.display.flip()
                    if event.key == pygame.K_d:
                        serpent2.move_right()
                        pygame.display.flip()
                    if event.key == pygame.K_r:
                        play = False

class snake(pygame.sprite.Sprite):  # définit le classe snake
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets\snake.png')
        self.longueur = 1
        self.velocity = 16
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 240
        self.listcoord = []
        self.badcoordx = [-16, 480]
        self.badcoordy = [-16, 480]

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def getcoordsX(self):
        return self.rect.x

    def getcoordsY(self):
        return self.rect.y

    def grailler(self):
        self.longueur += 1

    def perdu(self):
        self.longueur = 1
        self.listcoord = []
        self.rect.x = 240
        self.rect.y = 240


serpent = snake()
serpent2 = snake()
serpent2.rect.x = 224
serpent2.rect.y = 224

class graille(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/cookie.png')
        self.longueur = 5
        self.velocity = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.newcoordsX()
        self.rect.y = self.newcoordsY()

    def newcoordsX(self):
        listeposition = list(range(0, 481, 16))
        aleatoire1 = randint(0, 29)
        aleatoire2 = randint(0, 29)
        return listeposition[aleatoire1]

    def newcoordsY(self):
        listeposition = list(range(0, 481, 16))
        aleatoire1 = randint(0, 29)
        aleatoire2 = randint(0, 29)
        return listeposition[aleatoire2]


food = graille()

main()
