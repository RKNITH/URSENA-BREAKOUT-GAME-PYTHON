from ursina import *

app = Ursina()

#1 build 4 walls
ceiling = Entity(model='quad', x= 0, y = 4, scale = (16,0.2),  collider='box', color = color.orange)
left_wall = Entity(model='quad', x= -7.2, y = 0, scale = (0.2,10),  collider='box', color = color.orange)
right_wall = Entity(model='quad', x= 7.2, y = 0, scale = (0.2,10),  collider='box', color = color.orange)

#2 create a ball
ball = Entity(model='circle', scale=0.2, collider='box', dx = 0.05, dy = 0.05)

#3 Create a paddle
paddle = Entity(model='quad', x= 0, y = -3.5, scale = (2, 0.2),  collider='box', color = color.orange)

#4 Lay out bricks
bricks = []
for x_pos in range(-65, 75, 10):
    for y_pos in range(3,7):
        brick = Entity(model='quad', x = x_pos/10 , y = y_pos/3, scale = (0.9, 0.3),  collider='box', color = color.red)
        bricks.append(brick)

#5 move the ball so it bounces off the walls
def update():
    ball.x += ball.dx
    ball.y += ball.dy
    paddle.x += (held_keys['right arrow'] - held_keys['left arrow']) * time.dt *5
    hit_info = ball.intersects()
    if hit_info.hit:        
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx
        if hit_info.entity == ceiling:
            ball.dy = -ball.dy
        if hit_info.entity in bricks:
            destroy(hit_info.entity)
            bricks.remove(hit_info.entity)
            ball.dy = -ball.dy
        if hit_info.entity == paddle:
            ball.dy = -ball.dy
            ball.dx = 0.05*(ball.x - paddle.x)
    if ball.y < -5:
        message = Text(text = 'You LOST', scale=2, origin=(0,0), background=True, color=color.blue)
        application.pause()
    if len(bricks) == 0:
        message = Text(text = 'You WON', scale=2, origin=(0,0), background=True, color=color.blue)
        application.pause()
    
            
app.run()