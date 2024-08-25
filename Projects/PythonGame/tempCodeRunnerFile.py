img_list = []
#it will iterate 21 times (amount of tiles)
for x in range(TILE_TYPES):
    img = pygame.image.load(f"img/tile/{x}.png") # we iterate over all tile images
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE)) # img and x, y -> qwe are scaling the size of the img
    img_list.append(list) #by end of the iteration, we will append each image to the lisdt

