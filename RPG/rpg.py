class Role:
  def __init__(self,name: str,level: int,hit_point:int,mana_point:int):
      self.name = name             #角色名稱
      self.level = level           #角色等級
      self.hit_point = hit_point   #生命力
      self.mana_point = mana_point #魔力點數

  def __str__(self):
    return "('{name}',{level},{blood})".format(**vars(self))

  def __repr__(self):
    return self.__str__()


class SwordsMan(Role):
  def fight(self):
    print('揮劍攻擊')

class Magician(Role):
  def fight(self):
    print('魔法攻擊')
  
  def cure(self):
    print('魔法治療')
    
