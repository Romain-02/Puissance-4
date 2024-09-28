import pygame
import random
import time
from jeton import Jeton
pygame.init()
mat = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
mat_coord = {'x1' : 46, 'x2' : 174, 'x3': 302, 'x4' : 430, 'x5' : 558, 'x6' : 686, 'x7' : 814
            , 'y1' : 25, 'y2' : 154, 'y3': 281, 'y4' : 409, 'y5' : 537, 'y6' : 665}
image_texte = ''

#creer la fenetre du jeu
screen = pygame.display.set_mode((972, 950))
pygame.display.set_caption("Puissance 4")

background = pygame.image.load('puissance 4.png')
ecran_noir = pygame.image.load('écran noir.jpg')
ecran_noir = pygame.transform.scale(ecran_noir, (1000, 1000))
bouton_image = pygame.image.load('boutton.png')
bouton_image = pygame.transform.scale(bouton_image, (30, 30))
boutons = [bouton_image, bouton_image, bouton_image, bouton_image, bouton_image, bouton_image ,bouton_image]
bouton_rect = []
a = 82
for bouton in boutons:
    rect = bouton.get_rect()
    rect.x = a
    rect.y = 800
    bouton_rect.append(rect)
    a += 129

def poser_pion(mat, l, num):
    for i in range(len(mat)):
        ind = len(mat) - i - 1
        print(ind, l)
        if mat[ind][l] == 0:
            mat[len(mat) - i - 1][l] = num
            return mat
    return 'la colonne est pleine'

def alignement1(matrice):
    #en ligne
    running = True
    for ligne in matrice:
        for i in range(4):
            if ligne[i : i + 4] == [2, 2, 2, 2] or ligne[i : i + 4] == [1, 1, 1, 1]:
                return running
    #en colonne
    mat_col = []
    for i in range(len(matrice[0])):
        mat = []
        for j in range(len(matrice)):
            mat.append(matrice[j][i])
        mat_col.append(mat)
    for ligne in mat_col:
        for i in range(3):
            if ligne[i: i + 4] == [2, 2, 2, 2] or ligne[i: i + 4] == [1, 1, 1, 1]:
                return running
    #en diagonale gauche
    mat_diag_d = []
    i = 5
    b = 0
    for j in range(3, 6):
        mat = []
        b += 1
        j2 = j
        i2 = i
        for x in range(3 + b):
            mat.append(matrice[i2][j2])
            j2 -= 1
            i2 -= 1
        mat_diag_d.append(mat)
    b = 0
    j = 6
    for i in range(3, 6):
        mat = []
        b += 1
        j2 = j
        i2 = i
        for x in range(3 + b):
            mat.append(matrice[i2][j2])
            j2 -= 1
            i2 -= 1
        mat_diag_d.append(mat)
    for mat in mat_diag_d:
        for i in range(len(mat) - 3):
            if mat[i: i + 4] == [2, 2, 2, 2] or mat[i: i + 4] == [1, 1, 1, 1]:
                return running
    #en diagonale droite
    mat_diag_g = []
    i = 5
    b = 0
    for j in range(1, 4):
        mat = []
        b += 1
        j2 = j
        i2 = i
        for x in range(6 - b):
            mat.append(matrice[i2][j2])
            j2 += 1
            i2 -= 1
        mat_diag_g.append(mat)
    b = 0
    j = 0
    for i in range(3, 6):
        mat = []
        b += 1
        j2 = j
        i2 = i
        for x in range(3 + b):
            mat.append(matrice[i2][j2])
            j2 += 1
            i2 -= 1
        mat_diag_g.append(mat)
    for mat in mat_diag_g:
        for i in range(len(mat) - 3):
            if mat[i: i + 4] == [2, 2, 2, 2] or mat[i: i + 4] == [1, 1, 1, 1]:
                return running
    running = False
    return running

def alignement2(matrice):
    if game.bot == 'rouge':
        c = [1, 1, 1]
        f = [2, 2, 2]
    else:
        c = [2, 2, 2]
        f = [1, 1, 1]
    #en ligne
    m1 = []
    m2 = []
    for j in range(6):
        for i in range(5):
            if matrice[j][i : i + 3] == c:
                    m1.append((j, i - 1))
                    m1.append((j, i + 3))
            elif matrice[j][i: i + 3] == f:
                    m2.append((j, i - 1))
                    m2.append((j, i + 3))
    #en colonne
    mat_col = []
    for i in range(len(matrice[0])):
        mat = []
        for j in range(len(matrice)):
            mat.append(matrice[j][i])
        mat_col.append(mat)
    for j  in range(7):
        for i in range(4):
            if mat_col[j][i: i + 3] == c:
                    m1.append((i - 1, j))
                    m1.append((i + 3, j))
            elif mat_col[j][i: i + 3] == f:
                    m2.append((i - 1, j))
                    m2.append((i + 3, j))
    #en diagonale gauche
    mat_diag_d = []
    i = 5
    b = 0
    for j in range(3, 6):
        b += 1
        mat = []
        j2 = j
        i2 = i
        for x in range(3 + b):
            mat.append((matrice[i2][j2], (i2, j2)))
            j2 -= 1
            i2 -= 1
        mat_diag_d.append(mat)
    b = 0
    j = 6
    for i in range(3, 6):
        b += 1
        mat = []
        j2 = j
        i2 = i
        for x in range(3 + b):
            mat.append((matrice[i2][j2], (i2, j2)))
            j2 -= 1
            i2 -= 1
        mat_diag_d.append(mat)
    for mat in mat_diag_d:
        for x in range(len(mat) - 2):
            mat2 = []
            mat3 = []
            for y in range(3):
                mat2.append(mat[x + y][0])
                mat3.append(mat[x + y][1])
            if mat2 == c:
                m1.append((mat3[0][0] + 1, mat3[0][1] + 1))
                m1.append((mat3[-1][0] - 1, mat3[-1][1] - 1))
            elif mat2 == f:
                m2.append((mat3[0][0] + 1, mat3[0][1] + 1))
                m2.append((mat3[-1][0] - 1, mat3[-1][1] - 1))
    #en diagonale droite
    mat_diag_g = []
    i = 5
    b = 0
    for j in range(1, 4):
        mat = []
        j2 = j
        i2 = i
        for x in range(6 - b):
            mat.append((matrice[i2][j2], (i2, j2)))
            j2 += 1
            i2 -= 1
        mat_diag_g.append(mat)
        b += 1
    b = 0
    j = 0
    for i in range(3, 6):
        b += 1
        mat = []
        j2 = j
        i2 = i
        for x in range(3 + b):
            mat.append((matrice[i2][j2], (i2, j2)))
            j2 += 1
            i2 -= 1
        mat_diag_g.append(mat)
    for mat in mat_diag_g:
        for x in range(len(mat) - 2):
            mat2 = []
            mat3 = []
            for y in range(3):
                mat2.append(mat[x + y][0])
                mat3.append(mat[x + y][1])
            if mat2 == c:
                m1.append((mat3[0][0] + 1, mat3[0][1] - 1))
                m1.append((mat3[-1][0] - 1, mat3[-1][1] + 1))
            elif mat2 == f:
                m2.append((mat3[0][0] + 1, mat3[0][1] - 1))
                m2.append((mat3[-1][0] - 1, mat3[-1][1] + 1))
    return (m1, m2)

def placement_possible(matrice):
    tab = []
    col = []
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i!= 0 and str(matrice[i][j]) in '12':
                if j not in col:
                    tab.append((i-1, j))
                    col.append(j)
            elif i == 5:
                tab.append((i, j))
    return tab

def partie_en_cour(matrice):
    course = True
    if not alignement1(matrice):
        for ligne in matrice:
            for col in ligne:
                if col == 0:
                    return course
    course = False
    return course

def savoir_bouton(button):
    g = 82
    for i in range(7):
        if button.x == g:
            l = i
        g += 129
    return l

jetons = []
jeton_col = []

def convert_matrice(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                jetons.append(Jeton('rouge', (mat_coord['x' + str(j + 1)], mat_coord['y' + str(i + 1)])))
                jeton_col.append('rouge')
            elif matrice[i][j] == 2:
                jetons.append(Jeton('jaune', (mat_coord['x' + str(j + 1)], mat_coord['y' + str(i + 1)])))
                jeton_col.append('jaune')
    return matrice

#boucle du jeu
course = True

s = random.randint(1, 2)

class Game:

    def __init__(self, col1 = 'rouge', col2 = 'jaune'):
        self.course = True
        self.player = col1
        self.bot = col2
        self.matrice = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    def jeu_player(self, button):
        if self.player == 'rouge':
            num = 1
        else:
            num = 2
        a = savoir_bouton(button)
        poser_pion(self.matrice, a, num)

    def jeu_bot(self):
        if self.player == 'rouge':
            num = 2
        else:
            num = 1
        place = 0
        print(placement_possible(self.matrice))
        print(alignement2(self.matrice))
        for coord in placement_possible(self.matrice):
            if coord in alignement2(self.matrice)[0] and place == 0:
                place = coord[1]
        for coord in placement_possible(self.matrice):
            if coord in alignement2(self.matrice)[1] and place == 0:
                place = coord[1]
        place_rest = []
        if place == 0:
            for coord in placement_possible(matrice):
                place_rest.append(coord[1])
            print(place_rest)
            random.shuffle(place_rest)
            place = place_rest[0]
        print(place_rest)
        poser_pion(self.matrice, place, num)

police = pygame.font.SysFont("monospace", 25)
texte1 = police.render("à vous de jouer", 1, (255, 0, 0))
texte2 = police.render("cliquer sur ce bouton", 1, (255, 0, 0))

if s == 1:
    game = Game('rouge', 'jaune')
else:
    game = Game('jaune', 'rouge')

while course:
    screen.blit(ecran_noir, (0, 0))
    jetons = []
    jeton_col = []
    matrice = convert_matrice(game.matrice)
    screen.blit(background, (0, 0))
    for jeton in jetons:
        screen.blit(jeton.image, (jeton.coord))
    for button in bouton_rect:
        screen.blit(bouton_image, button)
    if image_texte != '':
        screen.blit(image_texte, (200, 850))
    bouton_image2 = pygame.image.load('boutton.png')
    bouton_image2 = pygame.transform.scale(bouton_image2, (60, 60))
    screen.blit(bouton_image2, (460, 855))
    bouton_image2_rect = bouton_image2.get_rect()
    bouton_image2_rect.x = 460
    bouton_image2_rect.y = 855
    if partie_en_cour(game.matrice):
        if game.player == 'rouge' and len(jetons) % 2 == 0:
            screen.blit(texte1, (540, 875))
        elif game.player == 'jaune' and len(jetons) % 2 == 1:
            screen.blit(texte1, (540, 875))
        elif game.player == 'rouge' and len(jetons) % 2 == 1:
            screen.blit(texte2, (540, 875))
        elif game.player == 'jaune' and len(jetons) % 2 == 0:
            screen.blit(texte2, (540, 875))
        if partie_en_cour(game.matrice):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    course = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_image2_rect.collidepoint(event.pos):
                        if game.player == 'rouge' and len(jeton_col) % 2 == 1:
                            game.jeu_bot()
                            if not partie_en_cour(game.matrice):
                                screen.blit(ecran_noir, (0, 0))
                                screen.blit(background, (0, 0))
                                matrice = convert_matrice(game.matrice)
                                for jeton in jetons:
                                    screen.blit(jeton.image, (jeton.coord))
                                image_texte = police.render("La partie est finie", 1, (255, 0, 0))
                                screen.blit(image_texte, (350, 875))
                                pygame.display.flip()
                        elif game.player == 'jaune' and len(jeton_col) % 2 == 0:
                            game.jeu_bot()
                            if not partie_en_cour(game.matrice):
                                screen.blit(ecran_noir, (0, 0))
                                screen.blit(background, (0, 0))
                                matrice = convert_matrice(game.matrice)
                                for jeton in jetons:
                                    screen.blit(jeton.image, (jeton.coord))
                                image_texte = police.render("La partie est finie", 1, (255, 0, 0))
                                screen.blit(image_texte, (350, 875))
                                pygame.display.flip()
                    else:
                        for button in bouton_rect:
                            if button.collidepoint(event.pos):
                                if game.player == 'rouge' and len(jeton_col) % 2 == 0:
                                    game.jeu_player(button)
                                    if not partie_en_cour(game.matrice):
                                        screen.blit(ecran_noir, (0, 0))
                                        screen.blit(background, (0, 0))
                                        matrice = convert_matrice(game.matrice)
                                        for jeton in jetons:
                                            screen.blit(jeton.image, (jeton.coord))
                                        image_texte = police.render("La partie est finie", 1, (255, 0, 0))
                                        screen.blit(image_texte, (350, 875))
                                        pygame.display.flip()
                                if game.player == 'jaune' and len(jeton_col) % 2 == 1:
                                    game.jeu_player(button)
                                    if not partie_en_cour(game.matrice):
                                        screen.blit(ecran_noir, (0, 0))
                                        screen.blit(background, (0, 0))
                                        matrice = convert_matrice(game.matrice)
                                        for jeton in jetons:
                                            screen.blit(jeton.image, (jeton.coord))
                                        image_texte = police.render("La partie est finie", 1, (255, 0, 0))
                                        screen.blit(image_texte, (350, 875))
                                        pygame.display.flip()
        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                course = False


pygame.quit()






