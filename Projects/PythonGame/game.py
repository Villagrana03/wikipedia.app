import pygame
import os # this will import the function that helped me determine which animatio to use, such as idle run or jump 
import random
import csv
import button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * .8) # 80% of the screen width, and we put it inside of int, so it can be a full value

#screen window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Title
pygame.display.set_caption('Shooter')

#set framerate
#we created this clock that acts like a timer and will limit how quick the game runs

clock = pygame.time.Clock()
FPS = 60

#Game variables
GRAVITY = 0.75 #changing this can affect how quick it goes down

#scroll function
SCROLL_THRESH = 200 #IS the distance the player can get to he end of the screen before screen starts to scroll (left and right)
screen_scroll = 0 # this will always be equal to the player speed
bg_scroll = 0 #this is a accumulate value 

#Game settings
ROWS = 16
COLS = 150
#level of the game
level = 1
TILE_SIZE = SCREEN_HEIGHT // ROWS
#tile types means the amount of tile types i will have
TILE_TYPES =  21

start_game = False

#Define player action variables
moving_left = False
moving_right = False
shoot = False # -> here we will make the bullet False, everytime the user press SPACE it wil become True and it will shoot
grenade = False #its false, everytime we press g, it will become True and action will occur 
grenade_thrown = False #if its True the grenade has been thrown this will only happen when we press "g"

#load button images
start_img = pygame.image.load("projects\\PythonGame\\start_btn.png").convert_alpha()
exit_img = pygame.image.load("projects\\PythonGame\\exit_btn.png").convert_alpha()
restart_img = pygame.image.load("projects\\PythonGame\\restart_btn.png").convert_alpha()

#load images background
pine1_img = pygame.image.load("projects\\PythonGame\\img\\background\\pine1.png").convert_alpha()
pine2_img = pygame.image.load("projects\\PythonGame\\img\\background\\pine2.png").convert_alpha()
mountain_img = pygame.image.load("projects\\PythonGame\\img\\background\\mountain.png").convert_alpha()
sky_img = pygame.image.load("projects\\PythonGame\\img\\background\\sky_cloud.png").convert_alpha()


#HARE UN ARCHIVO DE PYTHON APARTE EXPLICANDOLO (PYTHON DESCARGAR IMAGENES)
#store tiles in a list (tiles = pictures of the tiles)
img_list = []
#it will iterate 21 times (amount of tiles)
for x in range(TILE_TYPES):
    img = pygame.image.load(f"projects\\PythonGame\\img/tile/{x}.png") # we iterate over all tile images
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE)) # img and x, y -> qwe are scaling the size of the img
    img_list.append(img) #by end of the iteration, we will append each image to the lisdt


#load images
grenade_img = pygame.image.load("projects\\PythonGame\\img\\icons\\grenade.png").convert_alpha()  #In Pygame, the convert_alpha() method is used to optimize the performance of surfaces that have per-pixel transparency (i.e., an alpha channel). When you load an image or create a surface, it may not be optimized for quick blitting (copying pixels to another surface), especially if it has transparency.
#bullet
bullet_img = pygame.image.load("projects\\PythonGame\\img\\icons\\bullet.png").convert_alpha()  #In Pygame, the convert_alpha() method is used to optimize the performance of surfaces that have per-pixel transparency (i.e., an alpha channel). When you load an image or create a surface, it may not be optimized for quick blitting (copying pixels to another surface), especially if it has transparency.

#pick up boxes
health_box_img = pygame.image.load("projects\\PythonGame\\img\\icons\\health_box.png").convert_alpha()
ammo_box_img = pygame.image.load("projects\\PythonGame\\img\\icons\\ammo_box.png").convert_alpha()
grenade_box_img = pygame.image.load("projects\\PythonGame\\img\\icons\\grenade_box.png").convert_alpha()


item_boxes = {
    "Health": health_box_img,
    "Ammo": ammo_box_img,
    "Grenade": grenade_box_img
}

#define colors
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
#define font
font = pygame.font.SysFont("Futura", 30)

#will display (Player: health, Ammo and Grenades )
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col) #This method is used to create an image (surface) of the text that can be drawn onto the screen.
    screen.blit(img, (x,y)) #In Python, particularly when using the Pygame library, the blit method is used to draw one image onto another. This is typically done to display an image or surface onto the screen or another surface



#create a function that will refresh the brackground every iteration. (function = draw_background)
def draw_bg():
    #Here we will fill the background with a particular color
    screen.fill(BG)
    #The game has like a effect of tyhe images are moving one faster then the other and that is because of the .6, .7, .8 it scales at different size
    width = sky_img.get_width() #got the width of the sky
    for x in range(5):
        screen.blit(sky_img, ((x * width) - bg_scroll * .5,0)) #i display the background
        screen.blit(mountain_img, ((x * width) - bg_scroll *.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, ((x * width) - bg_scroll *.7,SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, ((x * width) - bg_scroll *.8,SCREEN_HEIGHT - pine2_img.get_height()))
    #Coordinates                   x   y 
    #pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300)) #just drawing the botton line


#Here we will create the main charecter
#Sprite class is a base class for visible game objects. Sprites are often used to represent characters, enemies, bullets, and other objects that can move or interact in the game world. !!!!Soldier is a subclass of Sprite!!!!
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, health, grenades):
        #with this function i am inhereting some of the function from sprite and adds some built in code
        pygame.sprite.Sprite.__init__(self)
        self.alive = True

    #All this self, are variables that each Soldier will have
        #Here we will determine if its a player or a enemy with the char_type
        self.char_type = char_type

        #a soldier will move with the speed (by pixels) with each iteration
        self.speed = speed

        #How much ammo does the soldier have, so everytime i shoot i will be reducing this self variable like a counter, so everytime we reset the game it will be reset to self.start_ammo
        self.ammo = ammo

        #here we are setting with how much ammo the player is starting
        self.start_ammo = ammo

        # this will start at 0 and everytime i shoot i will set it to a higher number and slowly bring the number down...
        self.shoot_cooldown = 0

        #grenades capacity
        self.grenades = grenades # all of tyhe instances will have grenades
        #live of the player
        self.health = health

        #is going going to be useful once we create the health bars
        self.max_health = self.health

        #if the number is positive it will be facing to the right, if its facing to the left will be -1, so at 1, is looking to the right. due to the x-axis
        self.direction = 1

        # we have this variable because because we are giving a vertical velocity and gravity will drag him down.
        self.vel_y = 0

        #i am going to make a jump thing, because i want to check once the user lands to the floor, if not, the player can just spam (space) and go up
        self.jump = False #we started at false because player is not jumping

        #The idea here is to i am assuming the player is in the air until it lands to something and we will set it false, and everytime it jumps it will be True
        self.in_air = True
        
        #self.flip is how the image of thecharecter behaves, if its False nothing will happen but once its True it will flip
        self.flip = False


        #Animation List
        self.animation_list = []
        #this index will just point where the animation is at
        self.frame_index = 0

        #same as frame_index but while running, if i want the player to run, it will change to 1 
        self.action = 0

        #upddate time is just going to be used to track the time of the animationn when was last updated
        self.update_time = pygame.time.get_ticks() # <- we will use this one as base to get the next animation sequence

        #create AI variables
        self.move_counter = 0 #as soon as it will the end of the tile it will flip to the other side

        self.idling = False  #i will set this method so the enemy can idle 
        self.idling_counter = 0 #this will be a counter, to idle
        self.vision = pygame.Rect(0,0,150,20) #py game rect takes 4 parameters (x, y, width and height) in this case 150 would be the width so 150 means how far can the enemy look

    #load all image foir players
        animation_types = ['idle','run', 'Jump', "Death"]
        for animation in animation_types:
            #reset tempory list of images
            #we will create a temporary empty list., we will add idle img to the temp_list instead of animation list, ONCE they are on temp_list we will move to animation_list
            temp_list = []
            #Here i will be looping through all the images (animations) (((The Varible img is indented inside of  the for loop)))
            #count number of files in the folder
            num_of_frames = len(os.listdir(f"projects\\PythonGame\\img/{self.char_type}/{animation}")) #-> os means the module we imported list dir creates a list  within the directory SO what it is doing is will make a list depending on the folder of the directory
            for i in range(num_of_frames):
            #charecter image
            #index 0 Running
            #we declare a variable inside the class
            #we set it now to curly braces, and now everytime we create an object we can specify if its a player or the enemy. {char_type}
                img = pygame.image.load(f"projects\\PythonGame\\img/{self.char_type}/{animation}/{i}.png").convert_alpha()
            #Here we will make the charcter bigger, we are multypling, we close it with int() so we dont get decimals.
            #the image we want this instance to have, self.image is an attribute of the Soldier
            #we set it to self, because we will be inserting images depedning on the charecter (useer, enemy) -> The self keyword is used to define instance attributes, meaning each instance of the Soldier class (or any other class) will have its own separate image and rect attributes. This allows each sprite to have its own unique image and position, making it possible to have multiple characters or enemies with different appearances and positions.
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                #the for loop will move into the next one,, (the for loop with just iterate 5 times), so what we want is to store the img somewhere, and that location will be animation.list[] -> The list starts empty but after each iteration, e add a new image and load it, after the loop ends.
                temp_list.append(img) #-> i am putting each iteration of the img into the new list 
            self.animation_list.append(temp_list) ##ASK CHATGPT TO EXPLAIN

#Here i think i made a mistake, everything now works as it should but all of the time i have 2 for loops, i will check the code later
        #     temp_list = []
        #     #Same thing as other loop, but here i will be updating over 6 images while running
        #     #index 1 Running
        #     for i in range(num_of_frames):
        #         img = pygame.image.load(f"img/player/{animation}/{i}.png")
        #         img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        #         temp_list.append(img) 
        #     self.animation_list.append(temp_list)
        # # the next action iy load in will be number 2

        #ask CHATGPT 
        #i upload this, after adding [self.action] here depending on which action we are currently in, it will call the frame_index of that particular index, for insatnce, if we are idle, it should call all of idle images
        self.image = self.animation_list[self.action][self.frame_index] # -> we have 5 images... each one by index, self.index started at 0 so that will be the starting position
        #takes the size of the image, "user image" and creates a boundary box around it, and it will help controlling the position and as well doing collisions, and the image will just be drawn in the rectangle
        self.rect = self.image.get_rect()
        #we will position the rectangle base on the position of x and y
        #object is used to get or set the center position of the rectangle. It takes a tuple with two values, which represent the x and y coordinates.
        self.rect.center = (x, y)
        self.width = self.image.get_width() #just getting thr width of the player
        self.height =  self.image.get_height() #just getting thr height of the player


    def update(self):
        self.update_animation()
        self.check_alive()
        #update cooldown
        if self.shoot_cooldown > 0: #so here what is happening first shoot_cooldown starts at 0, once we shoot it will now be 20 because we set it at the shoot method, and in thisline, if shoot coldown is greater than 0, which it will be, we will rest it by 1
            self.shoot_cooldown -= 1


    #a method for the class.
    #we have the move method first because we want to update the charecter position first
    def move(self, moving_left, moving_right):
        #reset movement variables.
        #SCROLLING
        #since all the scrilling will be done by player movement, it will done at move method
        screen_scroll = 0 #local variable 


        #d stands for delta, whcih means the change of the x and change of the x
        #dx serves as a temporary variable to store the change in the x-coordinate for the player's position based on the movement direction and speed. 
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if(moving_left == True):
            #f moving_left is True, dx is set to -self.speed, indicating movement to the left. which makes -5, so now dx = -5, so NOW self.rect.x = self.rect + (-dx) whixh means that it is self.rect.x = 200 - 5, and it is afecting the x coord
            dx = -self.speed
            self.flip = True

            
            self.direction = -1
        if(moving_right == True):
            dx = self.speed
            self.flip = False
            self.direction = 1

            
            # moving_right is True, moving_left is False, and self.speed is 5.
            # dx is set to 5.
            # self.rect.x += dx results in self.rect.x = 200 + 5 = 205.

        #jump
        #so everytime i press "w" it will set self.jump = True and for instance it will call this if
        if(self.jump == True and self.in_air == False):
            self.vel_y = -11 # is negative because the top of the screen is 0, and when you go down you go on the negative side, (this is gravity)
            self.jump = False #after jumping i want to set the self.jump back to False
            self.in_air = True

        #apply gravity
        self.vel_y += GRAVITY # positive down, and gravity isd pulling down
        #increasing deltaY by velocity
        if self.vel_y > 10: #if it pass more than 11 it will reset back to 10
            self.vel_y
        dy += self.vel_y #ask chatgpt

        #check collision with floor ASK CHAT GPT

        #check for collsion
        #will check collion x - coord (left and right) and y-coord (up and right)
        #since all the images from 0 to 8 in proccess_data are blocks, we stored them in a list called obstacle list 
        for tile in world.obstacle_list: #checking collsion x direction x -coord (right and left)
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height): #.colliderect() = we are thecking the rect for EACH TILE, and we are comparing for the player or enemy rect  ALSO index 0 is the image and index 1 is the tect of each tile REMEMBER 0=8 are blocks
                #if i  detect a collsion between the player and the tile this code weill happen
                dx = 0 # this means player wont be able to move
                #if AI hits a wall
                if self.char_type == "enemy":
                    self.direction *= -1
                    #self.move_counter = 0
            #check collsion y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): #.colliderect() = we are thecking the rect for EACH TILE, and we are comparing for the player or enemy rect  ALSO index 0 is the image and index 1 is the tect of each tile REMEMBER 0=8 are blocks
                #if i  detect a collsion between the player and the tile this code weill happen
                #check below the ground
                if self.vel_y < 0: #this mean the player is moving up
                    self.vel_y = 0
                    self.in_air = False #this helps me jump
                    dy = tile[1].bottom - self.rect.top # we are resting the bottom of the tile when ever the user jumps and hits the bottom part of the tile over the top of self.rect.top
                #check iff above the ground falling
                elif self.vel_y >= 0:
                    #when player is falling down
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom #this is when the player lands over a tile, we subtract the top of the tiles minus the feet of the player
           
        #check going of the edge of the screen to player
        if self.char_type == "player":
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0


        #updating rectangle position
        self.rect.x += dx
        self.rect.y += dy   

        
        #check collision with water
        if pygame.sprite.spritecollide(self, water_group, False): #we used srpite collide because it works with grouos / if its true it will kill the self (player) but we will handle that
            self.health = 0
            
        #check if player fell of the map
        if self.rect.bottom > SCREEN_HEIGHT: #if player goes beyond the screen
            self.health = 0

        #SCROLLING
        #since all the scrilling will be done by player movement, it will done at move method
        if self.char_type == "player": #checkng that only the player (us) can scroll the game
            #                                                       # i am checking whenever bg scroll is less than the lengtht, following code will occurr (level_length is 128)
            #so at the end of the map once i hit the legth of levels, the game_scroll wont occur due to the checks we put
            if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and bg_scroll < world.level_length * TILE_SIZE) - SCREEN_WIDTH  or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)): #the width is 600, minus 200, = 400, so when ever the player gets at 400 on the right side, the following code will occur
                self.rect.x -= dx #once the player gets at 200 it will stopj moving, anf just the game (background) will move, and thats gonna make the ilsuion of scrolling
                screen_scroll = -dx

        return screen_scroll #this screen_scroll was a local variable we ued return to make it global

#we created a method to the Player class so the enemies can shoot to, because we just set if the player can shoot
    def shoot(self):#                    x-cord                                                y-coord                coords oif the player location underneath we are creating the location of the bullet everytimewe press SPACE
        if self.shoot_cooldown == 0 and self.ammo > 0: #at the beggining it is 0 so the first bullet will shoot and we are checking if we have ammo
            self.shoot_cooldown = 20 #here we set the coldown to 20 it has to go down to 0 so the condition can be met again for instance shoot again
            bullet = Bullet(self.rect.centerx + (.75 * self.rect.size[0] * self.direction), self.rect.centery, self.direction) # we set the coordinates depending where is the player and we are accesing player rect, ALSO player direction means if its negative -1 will be facing left, if its +1 will be facing right, that is set at player method /// .6 * player.rect.size[0] what i am doing here, i got the size of the dith of the player and multiplied by .6 and thats were the bullet will appear in the x-axis and we also will be multiplying be player.direction, since its +1 and -1, when its facing to the left side it fill be multiplied to -1 so the bullet will face to th left
            #we will add tbhis bullte to the bullet_group (Group)
            bullet_group.add(bullet) # we are adding bullet to the group
            self.ammo -= 1 #everytime we press SPACE we will shoot and if we have ammo it will shoot and reduce our ammo minus 1

    
    def ai(self): #who ever we are calling this method, will have this function, since we are calling enemy.ai(), each self, apply to the enemy
        #ai() method is only for the enemies
        #we will call this method on each enemy.
        if self.alive == True and player.alive == True : # (AS LONG AS THERE ALIVE the check will occur)i am checking if the player is alive (if this conditions are met the next if will occur)
            if self.idling == False and random.randint(1, 200) == 1: #what isd happening here, it will randomize a number from 1 to 200 and when ever 1 ios chosen the following code will occur and self.idling = True
                self.idling = True
                self.idling_counter = 50 #this is the counter of how long would be idle the enemy
                self.update_action(0) # idle
            #Check if the AI is near the player
            if self.vision.colliderect(player.rect): #if the sight_rect of the enemy collides with the rect of the pllayer it will shoot
                #AI should stop whenever the ee the player
                self.update_action(0)
                self.idling = True # we will set idling to True so the enemy stop and shoots the player
                self.shoot() 

            if self.idling == False: #when ever the enemy is not moving the folowwing code will occur if its True it will not occur for instance, the will stop
              
                if self.direction == 1: # when the enemy is facing to the right
                    ai_moving_right = True #once the ai is facing right this will occur 
                else:
                    ai_moving_right = False #if self.direction = -1 (facing left) moving right will be false
                ai_moving_left = not ai_moving_right #this line happens when ai_moving_right is false, so when is false, moving left = True
                self.move(ai_moving_left, ai_moving_right) #here i am calling the method move from soldier, so depending where the enemy  is facing, its hwere the enmy will move
                self.update_action(1) #(RUN) 1 is running from the list of actions.
                self.move_counter += 1 #this will start at 0 it will increase by each iteation  of the game -> 

                #update AI vision as the enemy moves
                self.vision.center = (self.rect.centerx +  75 * self.direction, self.rect.centery) #what i am doing here, i am setting the rect i created for the vision, to each enemy rect, so when ever they are facion they will have a sight of vision of 150
                pygame.draw.rect(screen, RED, self.vision) #the representation of how the sight of th enemy works

                if self.move_counter > TILE_SIZE: #so since the counter woulb be increasing, when ever it reaches the size of the tile 
                    self.direction *= -1 #flipping the other side
                    self.move_counter *= -1 # we could have set it to 0 again, buty it will bring the enemy to the starting point, so if we multiply by -1 it will just move to the other side.
            else:
                self.idling_counter -= 1 #so when ever the enemy idles we will have the counter set to 50, so we will subtract 1 each iteration
                if self.idling_counter <= 0: #when the counter reaches to 0  self.idling will be false again and the enemy will start moving again
                    self.idling = False

    #scroll
    #just like this the enemies will stay at their position
        self.rect.x += screen_scroll


    #ASK chapt to ensure few things
    def update_animation(self):
        #i will make a timer and when that timer completes, i want to iterate over the next image, (i have to make the timer quick enough so it looks like a timer.)
        #Update timer. defining the timer (put it in all caps because is a constant)

        ANIMATION_COOLDOWN = 100 # -> controlling this number will help me to change the speed of the animation.
        #to see the time that passed we need to first check what time was at the beginning

        #update image depending on current frame.

        self.image = self.animation_list[self.action][self.frame_index] ### EXPLICAR ESTO

        #Here we will measure the time and we compare it to the last update time, !!!SO we are going to check if enough time has passed since the last update.
        if  pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks() #This resets the timer...
            self.frame_index += 1 
        #If the animation has run out, reset back to the start, what i am going to do is to check how many images are in the list, and then see if my frame_index going to be beyond it. and we will check the number of images through the len()
        if self.frame_index >= len(self.animation_list[self.action]): #what i am doing here, if the actual index (frame_index = each image "each image its called 0,1,2,3,4,5"), and since frame_index is adding 1 each iteration, at some point it will be greater then 5, and we dont have more than 6 images, so here we will reset it bck to the beggining.
           if self.action == 3:
              self.frame_index = len(self.animation_list[self.action]) -1 # here we will determine how long the Death animation is and finish
           else:
             self.frame_index = 0 # and this ir like our loop, we set it back to 0


    def update_action(self, new_action):
        # whats new_action for? = we want they type of action, and update from it
        # #check if new action is different from the previous one
        if (new_action != self.action): # -> meaning if new_action is not equal to 0, if its 1, it will run
            self.action = new_action
            #if animation is around img 3 or 4, i dont want when run switch to idle or viceversa, to be 3 or 4, so i will reset it here
            #update animation settings, 
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()     

    def check_alive(self): #we called this method in the update() method of the Player class
        if self.health <= 0:
            self.health = 0 # if the enemy have less than 0 live, we will set it to 0
            self.speed = 0 #so once they die they will stop there
            self.alive = False 
            self.update_action(3) #we are updating the action (its a method) #so ONCE it dies it will start the animation list at index 3 which is "death"

    def draw(self):
        #We weill appear the charecter in the game
        #The blit function in Pygame is used to draw one image (surface) onto another. It is a method of the Surface class, which represents images and the screen in Pygame.
        #                                              x-axis   y-axis
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        #^^^How to flip the image. we flip it trough the x or y axis, WHEN SELF.FLIP IS True, i want the image to flip, and when is false it wont flip.
        #How will the image flip, self.flip is the x-axis normally it will be false, because it will be facing right, thanks to the move method, anytime we click on "a" it will move to the left and self.flip will become True and will transfrom the image over the x-axis

class World():
    def __init__(self):
        #we created this list becuase it means that the first 9 values of TILE_TYPES are blocks and we wil sotre them in the list underneath,
        self.obstacle_list = []

#HARE UN ARCHIVO DE PYTHON APARTE EXPLICANDOLO (PYTHON DESCARGAR IMAGENES)
    #the data will be the csv file i loaded, we will convert the data
    #this method what is going to do, grab all the images frtom 0 to 20, and give them an attribute, from 0 to 8 are just blocks, some of them are just decorations, etc
    #so we looped trough the esxcel sheet and the game indetified if the number = num (depedning on num) that will be the result
    def process_data(self, data):
        #we are going to check the length of the game
        self.level_length = len(data[0]) #since this is a bidimensional game there is list over list, so we want to get the length of the first row (they are all the same length)

        #ASK CHATGHPT FOR THE COORD HOW THEY WORK
        #iterate over each value in the data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    
                    #what we did here just create the tile size of all tile types
                    img = img_list[tile] #dpepding on the number greater than 0 it will be an image
                    
                    img_rect = img.get_rect() #creating a rect from each image

                    #print(type(img_list[tile]))
                    #after creating the rect of each individual image we will get the rect in the x coord by multypling by the tile size x position
                    #base on their position of the gid, that where the tile will be
                    img_rect.x = x * TILE_SIZE 
                    img_rect.y = y * TILE_SIZE 
                    #after having and img and ther respective rect of the image, we will have it as tuple inside of the tupple i have everything of th eparticular tile
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8: #checking only the dirt blocks Those will have rect
                        self.obstacle_list.append(tile_data) #so all the tiles that are between the index of 0 and 8 will be appended to the list we created above
                    elif tile >= 9 and tile <= 10:
                        water = Water(img, x * TILE_SIZE, y * TILE_SIZE) #img is loaded for the list from the img from 11, 14 "which are all deocrations" will be here
                        water_group.add(water)
                    elif tile >= 11 and tile <= 14:
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE) #img is loaded for the list from the img from 11, 14 "which are all deocrations" will be here
                        decoration_group.add(decoration)
                        
                        pass
                    elif tile == 15: #create a player
                        #__init__(self, char_type, x, y, scale, speed, ammo, health, grenades)
                        player = Soldier('player', x * TILE_SIZE, y * TILE_SIZE, 1.65, 5, 20, 100, 3)
                        health_bar = HealthBar(10,10, player.health, player.health)
                    elif tile == 16: #create enemy
                        enemy = Soldier('enemy', x * TILE_SIZE, y * TILE_SIZE, 1.65, 1.5, 1000, 100, 0)
                        #group of enemy (since we will have many enemies)
                        enemy_group.add(enemy)
                    elif tile == 17: #Ammo box
                        item_box = ItemBox("Ammo", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 18: #grenades
                        item_box = ItemBox("Grenade", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 19: #health
                        item_box = ItemBox("Health", 400, 260)
                        item_box_group.add(item_box)
                    elif tile == 20: #exit
                        exit = Exit(img, x * TILE_SIZE, y * TILE_SIZE) #img is loaded for the list from the img from 11, 14 "which are all deocrations" will be here
                        exit_group.add(exit)

    #reutrn those variables because they are local not global so now i can use it outside the method
        return player, health_bar

#will draw the tiles
    def draw(self):
        for tile in self.obstacle_list: #this is the list i made where all the 21 images are of the tiles
            tile[1][0] += screen_scroll #tile[1] = tile rect tile[1][0] is the x-coord
            screen.blit(tile[0], tile[1]) #tile[0] is the image tiler[1] is therect all fromthe tupple tile_data 

#THE REASON WHY I HAD DECORATIONS, EXIT, AND WATER IN DIFFERENT CLASSES IS BECAUSE THEY WILL BE HANLDED DIFFERENT AND DIFFERENT ACTIONS
class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y): #i saved img as parameter becasue we can haver, enemy, boxes all depends on the item
        pygame.sprite.Sprite.__init__(self) #i added this line so i can inheritenance the methods of pygames
        self.image = img # im going to get each img
        self.rect = self.image.get_rect() #for each imae it wil have arect
       #                    x-coord           y-coord
        self.rect.midtop = (x + TILE_SIZE //2,y + (TILE_SIZE - self.image.get_height()) ) # ASK CHATGPTx = i divided by half because its the middle of the square

    def update(self):
        self.rect.x += screen_scroll

class Water(pygame.sprite.Sprite):
    def __init__(self, img, x, y): #i saved img as parameter becasue we can haver, enemy, boxes all depends on the item
        pygame.sprite.Sprite.__init__(self) #i added this line so i can inheritenance the methods of pygames
        self.image = img # im going to get each img
        self.rect = self.image.get_rect() #for each imae it wil have arect
       #                    x-coord           y-coord
        self.rect.midtop = (x + TILE_SIZE //2,y + (TILE_SIZE - self.image.get_height())) # ASK CHATGPTx = i divided by half because its the middle of the square

    def update(self):
        self.rect.x += screen_scroll

class Exit(pygame.sprite.Sprite):
    def __init__(self, img, x, y): #i saved img as parameter becasue we can haver, enemy, boxes all depends on the item
        pygame.sprite.Sprite.__init__(self) #i added this line so i can inheritenance the methods of pygames
        self.image = img # im going to get each img
        self.rect = self.image.get_rect() #for each imae it wil have arect
       #                    x-coord           y-coord
        self.rect.midtop = (x + TILE_SIZE //2,y + (TILE_SIZE - self.image.get_height())) # ASK CHATGPTx = i divided by half because its the middle of the square

#items drops
class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self) #i added this line so i can inheritenance the methods of pygames
        self.item_type = item_type #so each item in the parameter will be determine each object
        self.image = item_boxes[self.item_type] #so inside of item_boxes list we will have all the images and we will access each one by self.item_type, so we made a dicc, depending on the item_type // i am accesing the dictionary with self.image
        self.rect = self.image.get_rect()       
        self.rect.midtop = (x + TILE_SIZE //2, y + (TILE_SIZE - self.image.get_height())) #x-coord center, y-coord top of the rect

    
        

    def update(self):
        #check if player has picked up any box
        self.rect.x += screen_scroll

        if pygame.sprite.collide_rect(self, player): #when the player collides with a box the following line of code will occur
            #check type of box
            if self.item_type == "Health":
                player.health += 25
                self.kill()
                if player.health >= player.max_health:
                    player.health = player.max_health
              #  print(player.health)
            elif self.item_type == "Ammo":
                player.ammo += 5
                self.kill()
            elif self.item_type == "Grenade":
                player.grenades += 1
                self.kill()

class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health #starting health, starts at 100
        self.max_health = max_health

    def draw(self, health):
        #update new health
        self.health = health #this is update with new player health 

        #calculate health ratio
        ratio = self.health / self.max_health
        #Border around health bar
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y- 2, 154, 24))

        #Here GREEN is the colo that is above it
        pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20)) #self.x and self.y are the x and y coord of the bar and 150 and 20 are height and width
        pygame.draw.rect(screen, GREEN, (self.x, self.y, (150 * ratio), 20)) #whats ratio? ratio = health divided by max_health

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self) #i added this line so i can inheritenance the methods of pygames
        self.speed = 10 # i did not declared bullet as a parameter because i dont want he speed of the bullet to change.
        self.image = bullet_img #image of the bullet
        self.rect = self.image.get_rect() #here we will get a rectangle for the grenade, and it link to the grenade by self.image and in this line i iam getting self.image.get_rect() ??
        self.rect.center = (x, y) #object is used to get or set the center position of the rectangle. It takes a tuple with two values, which represent the x and y coordinates.
        #^^^ i dont have to create an self for x or y because we control their position with the rect_center()
        self.direction = direction #and we crated this one becasue some bullets will go left and some will go right.

    def update(self):
        #move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll #moving the rect of the bullet, depeding where is facing the player and the bullet will have a speed of 10 ------- We add screen_scroll wheneevr the player is at 400, the end of the screen - 200 we are going to update
        #check if bullet has gone of screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH: #if the bullet goes beyond the screen width or less than zero we will dissapear it
            self.kill() #the bullet will dissapear 

        #check for condition in level 
        #we are iterating over all the list tile
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect): #when ever a bullet hits a tile it will dissapear, ??? and there is self.rect because each react of wach bullet  
                self.kill() #since we are in the bullet class, self applies to all the bullets 
        #check collision with charecters
        #here we are going to use a pygame method
        if pygame.sprite.spritecollide(player, bullet_group, False): #here we are going to check the player collide to the bullet (Group) !!! so in Other words -> allow you to specify which sprites should be checked for collisions and how the collisions should be handled.
                                                             #This last argument wheter or not i want the item to be deleted or not, once the collision is detected and its supposed to be True because we do want to dissapear but not at the moment, we will make it True later in the code
           if player.alive == True: #we have this to check if there alive due to their rect, once the enemy dies, it will do the motion but the rectangle weill dissapear.
                player.health -= 5 #if the collision is checked (if it hit the player or enemy) it will reduce the health
                self.kill() #if the enmy fires the bullet at me and hit me the bullet will dissapear


        #Same thing but with the enemy
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False): #here we are going to check the player collide to the bullet (Group) !!! so in Other words -> allow you to specify which sprites should be checked for collisions and how the collisions should be handled.
                                                                #This last argument wheter or not i want the item to be deleted or not, once the collision is detected and its supposed to be True because we do want to dissapear but not at the moment, we will make it True later in the code
                if enemy.alive == True: #we have this to check if there alive due to their rect, once the enemy dies, it will do the motion but the rectangle weill dissapear.
                        enemy.health -= 20 #if the collision is checked (if it hit the player or enemy) it will reduce the health
                        print(enemy.health)
                        self.kill() #if the enmy fires the bullet at me and hit me the bullet will dissapear
               


class Grenade(pygame.sprite.Sprite): #ASK CHATGPT
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self) #i added this line so i can inheritenance the methods of pygames
        self.timer = 100 # the timer of the grenade that takes to explode, i did not have as a argument becasue all the grenades will have the same timer
        self.vel_y = -11#this is the speed in the vertical way / -11 because 0 is at the top 
        self.speed = 7 #horizontal speed (speed of the grenade), i did not declared grenade as a parameter because i dont want he speed of the grenade  to change.
        self.image = grenade_img #image of the bullet
        self.rect = self.image.get_rect() #here we will get a rectangle for the bullet, and it link to the grenade by self.image and in this line i iam getting self.image.get_rect()
        self.rect.center = (x, y) #object is used to get or set the center position of the rectangle. It takes a tuple with two values, which represent the x and y coordinates.
        #^^^ i dont have to create an self for x or y because we control their position with the rect_center()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction #and we crated this one becasue some bullets will go left and some will go right.

    def update(self): #this update will make the function of the grenade
        #here i will control the "y" velocity that work with gravity and the speed horizontsly
        self.vel_y += GRAVITY #we will adjust the "y" velocity base on gravity, we start at -11 that will shoot up 11 pixels so we are going to make like a peak, that goes down.
        dx = self.direction * self.speed #this is the change in the x-coord so thi is defined by multipling the direction which would be -1 or 1 and multyplied by speed
        dy = self.vel_y

        #check for collision in the floor
        #and again we will loop trough every single tile
        for tile in world.obstacle_list:
            #checking collision for walls
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height): #tile[1] means everysingle rect of each tile #we get self from this specific class which is the greande, if self.bottom (the bottom of the rect of the grenade) plus dy, (which is the change in the y-coord) if that exceeds the floor
                #all this is happening once the grenade touches the floor or wall 
                self.direction *= -1 
                dx = self.direction * self.speed 
                #self.speed = 0#once it hits the ground, the speed becomes 0, so the self spped of the grenade will be 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): #.colliderect() = we are thecking the rect for EACH TILE, and we are comparing for the player or enemy rect  ALSO index 0 is the image and index 1 is the tect of each tile REMEMBER 0=8 are blocks
                    #when it does kit something. veertically i want it to stop 
                    self.speed = 0
                    #check below the ground
                    if self.vel_y < 0: #this mean the player is throw up
                        self.vel_y = 0
                        dy = tile[1].bottom - self.rect.top # we are resting the bottom of the tile when ever the user jumps and hits the bottom part of the tile over the top of self.rect.top
                    #check iff above the ground falling
                    elif self.vel_y >= 0:
                        #when player is falling down
                        self.vel_y = 0
                        dy = tile[1].top - self.rect.bottom #this is when the player lands over a tile, we subtract the top of the tiles minus the feet of the player


           #check collsion off the walls
        # if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH: #in the first check (self.rect.left + dx) we are checking if grenade go off screen left side or (self.rect.right + dx > SCREEN_WIDTH:) goes beyond the screen i the right side
        #     self.direction *= -1 #will bounce the grnade
        #     #this line (dx = self.direction * self.speed) was not necesary, same jhob was perfomed without that line
        #     dx = self.direction * self.speed # i declared this here because we declared this exact line above, (10 lines) (so what is this doing is if i have change the direction i have to change th dx acordinly) 
         
    #update grenade position
        #this is still in the Grenade.update() method
        self.rect.x += dx + screen_scroll#which is the rect of the grenade, (where we set it to appear, above  our player) and which is increase by the change of the x-cord
        self.rect.y += dy #which is increased by thw y-coord
        ### i called this method with this code -> grenade_group.draw(screen)


    #countdime timer
        #once the grenade reach certain time i want to make an explosion from it
        self.timer -= 1
        if self.timer <= 0:
            self.kill() #this self grenade will die (dissapear)
            explosion = Explosion(self.rect.x,self.rect.y, 1 ) #we create a variable as of instance of the explosion class which takes (x, y, scale) same as their parameters
            explosion_group.add(explosion) #here we added the explosion as a group, so every grande thrown will have a explosion
            #do damage 
            #   center of grenade
            if abs(self.rect.centerx - player.rect.centerx) < (TILE_SIZE * 2) and abs(self.rect.centery - player.rect.centery) < (TILE_SIZE * 2): #abs = absolute value so we are getting the position of each grenade and compared to our player, if the difference is less than 100 i want to make damage
                player.health -= 50
            for enemy in enemy_group: #instead of checking each individual enemy i will iterate over all enemies 
                if abs(self.rect.centerx - enemy.rect.centerx) < 100 and abs(self.rect.centery - enemy.rect.centery) < 100: #abs = absolute value so we are getting the position of each grenade and compared to our player, if the difference is less than 100 i want to make damage
                    enemy.health -= 100
        
        


class Explosion(pygame.sprite.Sprite): #ASK CHATGPT why we made another Class for explosion
         #X and Yis required because thats where the explosion will happen
         #since i will have many grenade for instance many explosion we will need Groups also.
        def __init__(self, x, y, scale):
           #we will make the same as the plasyer animation
            self.images = [] #we made this list and we will load all the images here, and would run one after another
            for num in range(1,6): #we are going to loop through all the images
                img = pygame.image.load(f"img/explosion/exp{num}.png").convert_alpha() #Here i loaded all the explosion images there 5 of them
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) #transform.cale takes 2 arguments, The first argument is the image that you want to scale, which in this case is img. The second argument is a tuple representing the new size of the image. This tuple contains the new width and height of the image. 
                self.images.append(img) # all this immages will be stored in this self list
            self.frame_index = 0 #this index represewnts which index of the list im at 
            self.image = self.images[self.frame_index]
            pygame.sprite.Sprite.__init__(self)
            #self.image = grenade_img 
            self.rect = self.image.get_rect() 
            self.rect.center = (x, y) 
            self.counter = 0 #this is what is going to control the animation like a colddown
            
        #proccess explosion (make explosion animation)
        def update(self):
            self.rect.x += screen_scroll #by not doing this  the explosion will move with the screen if the player moves left or right, so we are updating the explosing with the screen_scroll
            #since we have Groups, each greande and each explosion will handle independlty
            EXPLOSION_SPEED = 4 #this speed is how fast will the animation run
            #update explosion animation
            self.counter += 1

            if self.counter >= EXPLOSION_SPEED: #so after 4, next image will occur, 
                self.counter = 0 #we reset the counter
                self.frame_index += 1 # this is what control the animation, so we add 1 so it can move to the next one
                #if animation is completed delete explosion
                if self.frame_index >= len(self.images): #this is basically if we exceed thew number of explosion images
                    self.kill() #we will kill the animation
                else:
                    self.image= self.images[self.frame_index] #self.image becomes the next frame_index

#create button
        #we declared a new variable called start_button (x,y img, scale)
start_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT //2 -150, start_img, 1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT //2 + 50, exit_img, 1)
restart_button = button.Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT //2 - 50, restart_img, 2)
                            
#create sprite groups
#sprite group is like a python list it allows me to group all the bullets togetherand creating depending when is a shooting and we dont deal with them individually
bullet_group = pygame.sprite.Group() #In Pygame, the Group class is part of the pygame.sprite module and is used to manage and organize multiple Sprite objects. A Group acts like a container that holds and controls a collection of sprites, making it easier to manage them as a single unit. This is especially useful in games where you have multiple objects (like enemies, bullets, or players) that need to be updated and drawn together.
grenade_group = pygame.sprite.Group() #In Pygame, the Group class is part of the pygame.sprite module and is used to manage and organize multiple Sprite objects. A Group acts like a container that holds and controls a collection of sprites, making it easier to manage them as a single unit. This is especially useful in games where you have multiple objects (like enemies, bullets, or players) that need to be updated and drawn together.
explosion_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()



#Decoration, water and exit group
decoration_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()







#Here i will explain how each level is developed, first there are 16 rows, and on each row there wil be a tile type, for example when ever the tile is empty, there is ground or an enemy or evcen a box it will be -1
#so on each row there will be a list, for insance it will be a list of list
#Create empty tile list

world_data = []

#so here i am iterating 16 times and on each time i will create all negative -1, so an empty map and we will h
for row in range(ROWS):
    r = [-1] * COLS #this will create a list with 160 entries of minus one
    world_data.append(r)

#HARE UN ARCHIVO DE PYTHON APARTE EXPLICANDOLO (PYTHON DESCARGAR IMAGENES)
#load in level data and create world
with open(f"projects\\PythonGame\\level{level}_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter= ",") #delimeter is what separates each value from other so when ever the computer opens the file since there are many "-1" it will see that each value is separated by a comma
   #Here i am getting each individul row x will be the value because since row will be the first value, and row is going down 
    for x, row in enumerate(reader):
        #Here i am getting each value of each row and y is the second value because each value of the row is going to the right
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)

#print(world_data)

#we are going to proccess the world

world = World()
#i am returning the value (player and health_bar)
player, health_bar = world.process_data(world_data) #it took a data argument, and that is going to be thw world that i opened


#timer = 100
#We created this variable to keep the screen on, the reason the screen is not displaying, is because once we run the code the computer reads all the lines and then it finish, once it finish the screen dissapears, thats why we will have the code inside a while loop
run = True
while run:
    
    clock.tick(FPS)

    #starting game
    if start_game == False:

        #means game havent start and i am in th emain menu
        screen.fill(BG)
        #draw buttons
        if start_button.draw(screen) == True: #in the class button whenever is being clicked, will return True
            start_game = True
        elif exit_button.draw(screen) == True:
            run = False

    #once game starts, the following code will hapenn
    else:
        
        #update background
        draw_bg()

    #draw world map
        world.draw()
        #show playe health
        health_bar.draw(player.health)

    #def draw_text(text, font, text_col, x, y):
    #we are placing the images using the x and y
        #show ammo
        draw_text("Ammo: ", font, WHITE, 10, 35)
        for x in range(player.ammo):
            screen.blit(bullet_img, (90 + (x * 10), 40)) #depeding on how many bullets i have, (i am looping through player.ammo) the first bullet will appear at 90 ad after each one, will be added 10, and y-coord will be 40
        #show grenades
        draw_text("Grenades: ", font, WHITE, 10, 60)
        for x in range(player.grenades):
            screen.blit(grenade_img, (135 + (x * 15), 60)) #depeding on how many grenades i have, (i am looping through player.ammo) the first bullet will appear at 90 ad after each one, will be added 10, and y-coord will be 40
    
        #  #show health
        # draw_text("Health: ", font, WHITE, 10, 85)
        # for x in range(player.grenades):
        #     screen.blit(grenade_img, (135 + (x * 15), 60)) #depeding on how many grenades i have, (i am looping through player.ammo) the first bullet will appear at 90 ad after each one, will be added 10, and y-coord will be 40

        

        #Soldier function
        # we called update() method, which calls the animation and check_alive()
        #player.ai() i just set this method to prove that all the method are for everyone, i dont have a subclass, onyl enemies will have ai method
        player.update()
        #Here we are calling the draw method from soldier, which what it does is to display the soldier to the screen
        player.draw() 

        
        
    #This how i was checking my ammo, health and grenades before using blit
        # timer -=1
        # if timer <= 0:
        #     print(f" Health: {player.health}")
        #     print(f"Ammo: {player.ammo}")
        #     print(f"Grenades: {player.grenades}")
        #     timer = 1000
    
    
        for enemy in enemy_group:
            enemy.ai()
            enemy.update()
            enemy.draw()


                #update and draw Groups -> Bullets
                #this is what creates and dispay the bullet images
        bullet_group.update()
        bullet_group.draw(screen)

        grenade_group.update()
        grenade_group.draw(screen)

        explosion_group.update()
        explosion_group.draw(screen)

        item_box_group.update()
        item_box_group.draw(screen)

        decoration_group.update()
        water_group.update()
        exit_group.update()

        decoration_group.draw(screen)
        water_group.draw(screen)
        exit_group.draw(screen)


        #this going to be run if player.alive is True
        if player.alive == True:
            #shooting bullets
            #it will be True everytime we click SPACE button
            if shoot == True: 
                player.shoot()
            #Throw grenade
            elif grenade == True and shoot == False and grenade_thrown == False and player.grenades > 0: # i dont want to throw another grenade until i release the "g" button
                #  in the first parameter i am getting another size of the width of the player [0] is width divided by .5 and depending where the player is facing, i will multiply by 1 or -1
                grenade = Grenade(player.rect.centerx + (.5 * player.rect.size[0] * player.direction), player.rect.centery + (-.5 * player.rect.size[0]), player.direction)#i did not created a method because only player will throw graneade, and for exame i did created a method for bullets becasue player and enemys could shoot
                #Also Grenade() will be an instance
                grenade_group.add(grenade)
                #reduce grenades
                player.grenades -= 1 #so everytime we press "g" grenade will happen and above method will occur, (tha ones that makes the grenade appear) and we will subtract graned minus 1
                grenade_thrown = True
                

            if player.in_air == True:
                player.update_action(2) # 2 means Jump ,,,,,,,,,,,,,,,,, at 1, it goes to update_action metohd
            #check if player running or walking
            #update player action
            elif moving_left or moving_right:
                player.update_action(1) # 1 means run ,,,,,,,,,,,,,,,,, at 1, it goes to update_action metohd
            else:
                player.update_action(0) # when user is not moving left of right action will be 0 so it will be idle    

        else: #if player not alive 
            screen_scroll = 0
            if restart_button.draw(screen):
                bg_scroll = 0
    

        #same as normal function, the move() method took 2 parameters wich are moving_left and moving_right
        #once we press "d" which is right, it willk add to the positive x-axis
        screen_scroll = player.move(moving_left, moving_right) #one of the reasons why i have this is because permantely move the rects
        bg_scroll -= screen_scroll #and this will re position the imges

        
    
    #we will create an exit for the loop, and that would be an event handler or clicking something, thats going to give all the events that are happeing
    for event in pygame.event.get():
        #quit game
        # In Pygame, (((events))) are actions or occurrences that happen during the game, such as key presses, mouse movements, or quitting the game
        #event.type is an attribute of the event object that specifies the type of the event. It tells you what kind of event has occurred.
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        #so event.type checks the type of event is happening, if its pressing a key the if will occur, so the next if will happen.
        if(event.type == pygame.KEYDOWN): #KEYDOWN means if user pressed any key of the keyboard
            #event.key is an attribute of the event object that specifies which key was pressed or released
            if(event.key == pygame.K_a): #pygame.K_a: Represents the 'A' key on the keyboard.
                moving_left = True
            if(event.key == pygame.K_d): #pygame.K_a: Represents the 'd' key on the keyboard.
                moving_right = True
            if(event.key == pygame.K_SPACE):
                shoot = True # Everytime we press SPACE shoot variable will be True so the player.shoot() method will occur
            if(event.key == pygame.K_w and player.alive): #pygame.K_a: Represents the 'w' key on the keyboard.
                player.jump = True   #whats the difference between calling player.jump and making an method of player.jump() 
            if(event.key == pygame.K_ESCAPE):
                run = False  
            if(event.key == pygame.K_g):
                grenade = True
           


    #Keyboard Button release
        if(event.type == pygame.KEYUP): #pygame.KEYUP: This event type is triggered when a key on the keyboard is released.
            #event.key is an attribute of the event object that specifies which key was pressed or released
            if(event.key == pygame.K_a): #pygame.K_a: Represents the 'A' key on the keyboard.
                moving_left = False
            if(event.key == pygame.K_d): #pygame.K_a: Represents the 'd' key on the keyboard.
                moving_right = False
            if(event.key == pygame.K_SPACE):
                shoot = False
            if(event.key == pygame.K_g):
                grenade = False
                grenade_thrown = False
    pygame.display.update()

pygame.quit()