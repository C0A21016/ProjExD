import pygame as pg
import sys
import random

class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()              # Rect
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)


class Bird:
    def __init__(self,image:str,size:float,xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
    
    def update(self,scr:Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self,color,size,vxy,scr):
        self.sfc = pg.Surface((2*size,2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size,size),size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr):
         # 練習6
        self.rct.move_ip(self.vx,self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)

class enemy:  #新たにもう一つの敵を追加
    def __init__(self,color,size,vxy,scr):
        self.sfc = pg.Surface((4*size,4*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size,size),size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = 100
        self.rct.centery = 450
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr):
        self.rct.move_ip(self.vx,self.vy)
        self.vx+=0.1
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
    
class end: #hpが０になった時にゲームおーばーとなる
    def __init__(self,hp,txt):
        hp=0

    def hhh(self,tk,bkd,scr):

        if self.rct.colliderect(self.rct)and kkt.rct.colliderect(bkd.rct):
                scr.sfc.blit(tk.sfc,tk.rct)
                life -= 1 #life point を減らす
                scr.sfc.blit(tk.sfc,tk.rct)
                life -= 1
                if life <=0:
                    return


class bullet(pg.sprite.Sprite):  #スペースキーを押したら弾が発射される

    speed = -11
    images = []

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0: #弾が画面外に行くと消える
            self.kill()


def main():
    clock = pg.time.Clock()

    
    scr=Screen("負けるな！こうかとん",(1600,900),"ex03/fig/pg_bg.jpg")

    
    kkt=Bird("ex03/fig/6.png",2.0,(900,400))

    
    bkd=Bomb((255,0,0),10,(+1,+1),scr)
    en=end(3,"ゲームオバー")
    tk = enemy((255,255,0),30,(+3,0),scr)
    bullets = pg.sprite.Group()
    bullet.containers = bullets, all
    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        kkt.update(scr)

        
        bkd.update(scr)
        tk.update(scr)
        keystate = pg.key.get_pressed()
        firing = keystate[pg.K_SPACE]
        if not kkt.reloading and firing and len(bullets) < 3:
            bullet(kkt.gunpos())
          
        if kkt.rct.colliderect(bkd.rct):
            return 
        if kkt.rct.colliderect(tk.rct):
            return 

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()