import rpg

benny=rpg.SwordsMan('Benny',2,3770)
print('name:',benny.name)
print('level:', benny.level)
print('HP:', benny.blood)

def draw_fight(role):
    print(role,end='')
    role.fight()


swordsman=rpg.SwordsMan('JJ',1,200)
draw_fight(swordsman)
