
'''
CPT
@ Dahab, Youssef
@ Dominic, Ryan
@ 2016 / 06 / 16
@ ICS3U1
'''
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
 
Font/Text:
 
http://programarcadegames.com/python_examples/f.php?file=move_game_controller.py
"""
 
import pygame
import random
import time

# Define beginning colours and values.
PI = 3.141592654
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)

''' Subprogram for point system.'''
def point_System(player_1_score, player_2_score):
     player_1_score = player_1_score
     player_2_score = player_2_score
     
     # Check if player 2 scored a goal.
     if(ball.rect.x <= 40 and ball.rect.y >= 310 and ball.rect.y <= 490):
          player_2_score = player_2_score + 1
          
     # Check if player 1 scored a goal.
     elif (ball.rect.x >= 1240 and ball.rect.y >= 310 and ball.rect.y <= 490):
          player_1_score = player_1_score + 1
     
     return (player_1_score, player_2_score)

''' Subprogram to draw the soccer field.''' 
def draw_soccer_field():
     
     # Draw the soccer field.
     pygame.draw.rect(screen, GREEN, [0, 0, 1300, 800], 0)
     pygame.draw.rect(screen, WHITE, [50, 20, 1200, 760], 5)
     pygame.draw.line(screen, WHITE, [650, 20], [650, 780], 5)
     pygame.draw.circle(screen, WHITE, [650, 400], 100, 5)
   
     # Draw the nets.
     pygame.draw.rect(screen, RED, [0, 300, 50, 200], 5)
     pygame.draw.rect(screen, BLUE, [1250, 300, 50, 200], 5)
 
# Create class for soccer players.
class Player(pygame.sprite.Sprite):
     def __init__(self, colour, collision_list):
 
          # Call the parent class (Sprite) constructor.
          pygame.sprite.Sprite.__init__(self)
       
          # Attributes for Player class.
          self.collide_list = collision_list
          self.radius = 0
          self.change_of_x = 0
          self.change_of_y = 0
          self.colour = colour
          self.width = 40
          self.height = 40
          self.image = pygame.Surface([self.width,self.height])
          self.image.fill(WHITE)
          self.image.set_colorkey(WHITE)
 
          # Draw the players.
          pygame.draw.ellipse(self.image, self.colour, [0, 0, self.width, self.height])
          self.rect = self.image.get_rect()
          self.rect.x = 0
          self.rect.y = 0
         
 
     # Method to move the player.
     def move(self):
          self.rect.x += self.change_of_x
          self.rect.y += self.change_of_y
 
          # Setting boundries for the players.
          if(self.rect.x <=0 or self.rect.x >=1260):
               self.change_of_x = 0
 
          elif(self.rect.y <=0 or self.rect.y >=760):
               self.change_of_y = 0
 
     # Method to check for colliding.
     def check_colliding(self):
          collide_list = pygame.sprite.spritecollide(self, self.collide_list, False)

          # If player collides with other player, they bounce off each other.
          if collide_list:
               self.change_of_x = self.change_of_x * -1
               self.change_of_y = self.change_of_y * -1
               
     # Method to update the players.
     def update(self):
          self.check_colliding()
          self.move()
          
# Inheritance of Player class.
class Soccer_ball(Player):
     def __init__(self, collision_list):
 
          # Call the parent class (Sprite) constructor.
          Player.__init__(self, BLACK, collision_list)

          # Attributes for Soccer ball class.
          self.ball_x = 640
          self.ball_y = 400
          self.ball_change_x = 15
          self.ball_change_y = 5
          self.collide_list = collision_list
          self.width = 20
          self.height = 20
          self.image = pygame.Surface([self.width,self.height])
          self.image.fill(WHITE)
          self.image.set_colorkey(WHITE)

          # Draw the soccer ball.
          pygame.draw.ellipse(self.image, self.colour, [0, 0, self.width, self.height])
          self.rect = self.image.get_rect()
          self.rect.x = 630
          self.rect.y = 380
         
 
     # Method to move the ball
     def move(self):
          self.rect.x += self.ball_change_x
          self.rect.y += self.ball_change_y

          # Boundries for soccer ball.
          if(self.rect.x <=0 and self.rect.y >= 490):
               self.ball_change_x = self.ball_change_x * -1

          elif(self.rect.x <= 0 and self.rect.y <= 310):
               self.ball_change_x = self.ball_change_x * -1

          elif(self.rect.x >=1280 and self.rect.y >= 490):
               self.ball_change_x = self.ball_change_x * -1

          elif(self.rect.x >=1280 and self.rect.y <= 310):
               self.ball_change_x = self.ball_change_x * -1

          elif(self.rect.x >=0 and self.rect.y <=0):
               self.ball_change_y = self.ball_change_y * -1

          elif(self.rect.x >=0 and self.rect.y >= 780):
               self.ball_change_y = self.ball_change_y * -1
               
             
     # Method to check for collision with soccer ball.
     def check_colliding(self):
          collide_list = pygame.sprite.spritecollide(self, self.collide_list, False)

          # If ball collides with a player, it bounces off the player.     
          if collide_list:
               self.ball_change_x = self.ball_change_x * -1
               self.ball_change_y = random.randrange(-3, 3)

     # Method to update the soccer ball.
     def update(self):
          self.check_colliding()
          self.move()
     
# Creating lists for collisions.
ball_collision_list = pygame.sprite.Group()
player1_collision_list = pygame.sprite.Group()
player2_collision_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
# Creating players.
player_1 = Player(RED, player1_collision_list)
player_2 = Player(BLUE, player2_collision_list) 
 
# Creating stats for Player 1.
player_1.rect.x = 50
player_1.rect.y = 400
player_1.radius = 20
player_1.change_of_x = 0
player_1.change_of_y = 0
 
# Creating stats for Player 2.
player_2.rect.x = 1200
player_2.rect.y = 400
player_2.radius = 20
player_2.change_of_x = 0
player_2.change_of_y = 0

# Creating soccer ball.
ball = Soccer_ball(ball_collision_list)
 
# Creating lists to check for collisions.
all_sprites_list.add(player_1)
all_sprites_list.add(player_2)
all_sprites_list.add(ball)
player1_collision_list.add(player_2)
player2_collision_list.add(player_1)
ball_collision_list.add(player_1)
ball_collision_list.add(player_2)

# Initializing pygame. 
pygame.init()
 
# Set the width and height of the screen.
size = (1300, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("SOCCER BATTLE!")
 
# Select the font to use, size, bold, italics.
font = pygame.font.SysFont('Calibri', 50, True, False)
 
# Initial score for point system.
player_1_score = 0
player_2_score = 0
 
# Create an empty list for sparks.
spark_list = []
spark_color = [YELLOW, RED, ORANGE, YELLOW, ORANGE]
 
# Loop to create random sparks and add them to a list.
for i in range(100):
     x = random.randrange(0, 1300)
     y = random.randrange(0, 800)
     spark_list.append([x, y])

# Background image.
screen.fill(WHITE)
 
# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Loops until user(s) click close button.
done = False

# Help with displaying instructions.
instructions_read = False
 
# Main program loop.
while not done:
 
     # Main event loop.
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               done = True
 
          # Player 1 and player 2 pressing down keys.
          elif event.type == pygame.KEYDOWN: 
 
               # Player 2 pressing down arrow keys.
               if event.key == pygame.K_UP:
                    player_2.change_of_y = -3
 
               if event.key == pygame.K_DOWN:
                    player_2.change_of_y = 3
 
               if event.key == pygame.K_RIGHT:
                    player_2.change_of_x = 3
 
               if event.key == pygame.K_LEFT:
                    player_2.change_of_x = -3
 
               # Player 1 pressing down WASD keys.
               if event.key == pygame.K_w:
                    player_1.change_of_y = -3
 
               if event.key == pygame.K_s:
                    player_1.change_of_y = 3
 
               if event.key == pygame.K_d:
                    player_1.change_of_x = 3
 
               if event.key == pygame.K_a:
                    player_1.change_of_x = -3
           
 
          # Player 1 and player 2 lets go of keys.
          elif event.type == pygame.KEYUP:
 
               # Player 2 lets go of arrow keys.
               if event.key == pygame.K_UP:
                    player_2.change_of_y = 0
 
               if event.key == pygame.K_DOWN:
                    player_2.change_of_y = 0
 
               if event.key == pygame.K_RIGHT:
                    player_2.change_of_x = 0
 
               if event.key == pygame.K_LEFT:
                    player_2.change_of_x = 0
           
            # Player 1 lets go of WASD keys.
               if event.key == pygame.K_w:
                    player_1.change_of_y = 0
 
               if event.key == pygame.K_s:
                    player_1.change_of_y = 0
 
               if event.key == pygame.K_d:
                    player_1.change_of_x = 0
 
               if event.key == pygame.K_a:
                    player_1.change_of_x = 0
     
     # Generate the soccer field.          
     draw_soccer_field()
 
     # Displaying initial score of soccer game.
     text = font.render(str(player_1_score) + "-" + str(player_2_score), True, BLACK)
     screen.blit(text, [620, 25])
 
     # Check if player 1 or player 2 scored a goal.
     if(ball.rect.x <= 40 and ball.rect.y >= 310 and ball.rect.y <= 490 or ball.rect.x >= 1240 and ball.rect.y >= 310 and ball.rect.y <= 490):
          (player_1_score, player_2_score) = point_System(player_1_score, player_2_score)
          text = font.render(str(player_1_score) + "-" + str(player_2_score), True, BLACK)

          # Display score on screen.
          screen.blit(text, [620, 25])

          # Reset soccer ball and players.
          ball.rect.x = 650
          ball.rect.y = 400
          player_1.rect.x = 50
          player_1.rect.y = 400
          player_2.rect.x = 1200
          player_2.rect.y = 400
          ball.change_x = 0
          ball.change_y = 0
          all_sprites_list.update()
          all_sprites_list.draw(screen)

          # Continue soccer game.
          time.sleep(1)
          ball.change_x = random.randint(-15, 15)
          ball.change_y = random.randint(-3, 3)
          
     elif(player_1_score >= 3 or player_2_score >= 3):

          # Reset soccer ball and players to end game.
          ball.rect.x = 650
          ball.rect.y = 400
          player_1.rect.x = 50
          player_1.rect.y = 400
          player_2.rect.x = 1200
          player_2.rect.y = 400
          ball.change_x = 0
          ball.change_y = 0
          

     # Check if player 1 won the game.
     if(player_1_score >= 3):
          text = font.render("Congrats Player 1, YOU WIN!!!", True, RED)
          screen.blit(text, [400, 400])

          # Process each spark in the list
          for i in range(len(spark_list)):
             
               # Draw the spark
               pygame.draw.arc(screen,spark_color[random.randint(0,len(spark_color)-1)],[spark_list[i][0],spark_list[i][1], 50, 50], PI/2, PI, 5)
               pygame.draw.arc(screen,spark_color[random.randint(0,len(spark_color)-1)],[spark_list[i][0],spark_list[i][1], 50, 50], 3*PI/2, 2*PI, 5)
                           
               # Move the sparks down 1 pixel.
               spark_list[i][1] += 1

     # Check if player 2 won the game.
     elif(player_2_score >= 3):
          text = font.render("Congrats Player 2, YOU WIN!!!", True, BLUE)
          screen.blit(text, [400, 400])

           # Process each spark in the list
          for i in range(len(spark_list)):
             
               # Draw the spark
               pygame.draw.arc(screen,spark_color[random.randint(0,len(spark_color)-1)],[spark_list[i][0],spark_list[i][1], 50, 50], PI/2, PI, 5)
               pygame.draw.arc(screen,spark_color[random.randint(0,len(spark_color)-1)],[spark_list[i][0],spark_list[i][1], 50, 50], 3*PI/2, 2*PI, 5)
                           
               # Move the sparks down 1 pixel.
               spark_list[i][1] += 1

     # Displays instructions long enough for players to read them.
     while not instructions_read:
          text = font.render("First to 3 is the winner.", True, BLACK)
          screen.blit(text, [500, 400])
          pygame.display.flip()
          time.sleep(3)
          instructions_read = True
          
     # Generating players in game.
     all_sprites_list.update()
     all_sprites_list.draw(screen)
 
     
     # Update the screen with what we've drawn.
     pygame.display.flip()
 
     # Limit to 60 frames per second.
     clock.tick(60)

# Close the window and quit.
pygame.quit()
 
