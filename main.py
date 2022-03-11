@namespace
class SpriteKind:
    Npc = SpriteKind.create()

def on_countdown_end():
    info.change_life_by(-1)
    info.start_countdown(65)
info.on_countdown_end(on_countdown_end)

def on_overlap_tile(sprite, location):
    global mySprite3
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    myEnemy.destroy()
    mySprite3 = sprites.create(assets.image("""
        npc
    """), SpriteKind.Npc)
    mySprite3.say_text("Hello.")
    tiles.place_on_random_tile(mySprite3, assets.tile("""
        myTile1
    """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile0
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile)

def on_life_zero():
    game.over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap(sprite2, otherSprite):
    game.over(False, effects.smiles)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

mySprite3: Sprite = None
myEnemy: Sprite = None
mySprite: Sprite = None
print("PETERDEV GAMES C2018-2022")
print("MAZE GAME 2.1.1")
game.splash("WELCOME TO MAZE GAME 2.1.1")
game.splash("YOU WAKE UP IN A MAZE AND YOU TRY TO GET OUT OF THERE.")
info.set_life(3)
info.start_countdown(65)
mySprite = sprites.create(assets.image("""
    player1
"""), SpriteKind.player)
mySprite2 = sprites.create(assets.image("""
    player2
"""), SpriteKind.player)
myEnemy = sprites.create(assets.image("""
    badguy
"""), SpriteKind.enemy)
mySprite.say_text("I Need to get out of here.", 1000, False)
myEnemy.say_text("COME OVER HERE", 1000, False)
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite)
controller.player2.move_sprite(mySprite2, 100, 100)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile0
"""))
tiles.place_on_random_tile(mySprite2, assets.tile("""
    myTile0
"""))
music.play_melody("C5 B F C5 B F C5 B ", 120)
myEnemy.follow(mySprite)