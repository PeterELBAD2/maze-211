namespace SpriteKind {
    export const Npc = SpriteKind.create()
}
info.onCountdownEnd(function () {
    info.changeLifeBy(-1)
    info.startCountdown(65)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level2`)
    myEnemy.destroy()
    mySprite3 = sprites.create(assets.image`npc`, SpriteKind.Npc)
    mySprite3.sayText("Hello.")
    tiles.placeOnRandomTile(mySprite3, assets.tile`myTile1`)
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile0`)
})
info.onLifeZero(function () {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.over(false, effects.smiles)
})
let mySprite3: Sprite = null
let myEnemy: Sprite = null
let mySprite: Sprite = null
console.log("PETERDEV GAMES C2018-2022")
console.log("MAZE GAME 2.1.1")
game.splash("WELCOME TO MAZE GAME 2.1.1")
game.splash("YOU WAKE UP IN A MAZE AND YOU TRY TO GET OUT OF THERE.")
info.setLife(3)
info.startCountdown(65)
mySprite = sprites.create(assets.image`player1`, SpriteKind.Player)
let mySprite2 = sprites.create(assets.image`player2`, SpriteKind.Player)
myEnemy = sprites.create(assets.image`badguy`, SpriteKind.Enemy)
mySprite.sayText("I Need to get out of here.", 1000, false)
myEnemy.sayText("COME OVER HERE", 1000, false)
scene.cameraFollowSprite(mySprite)
controller.moveSprite(mySprite)
controller.player2.moveSprite(mySprite2, 100, 100)
tiles.setCurrentTilemap(tilemap`level1`)
tiles.placeOnRandomTile(mySprite, assets.tile`myTile0`)
tiles.placeOnRandomTile(mySprite2, assets.tile`myTile0`)
music.playMelody("C5 B F C5 B F C5 B ", 120)
myEnemy.follow(mySprite)
