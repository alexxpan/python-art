boids = ximport("boids")
cornu = ximport("cornu")
colors = ximport("colors")

size(750, 750)
nofill()
speed(100)
background_color = colors.hex("#323333", "charcoal")

palette = [colors.hex("#ff0000", "fire1"),
           colors.hex("#ff8d00", "fire2"),
           colors.hex("#ffb400", "fire3"),
           colors.hex("#ffce00", "fire4")]

    
flock = boids.flock(15, 375, 600, 375, 750)

def draw():
    nofill()
    background(background_color)
    n = random(5,20)
    for i in range(n):
    
        flock.update(shuffled=False)
    
        points = []
        for boid in flock:
            points.append((boid.x, boid.y))
        for i in range(len(points)):
            x, y = points[i]
            x /= 1.0 * 750
            y /= 1.0 * 750
            points[i] = (x,y)
        boid_color = choice(palette)
        boid_color.a = random(0.8,0.1)
        stroke(boid_color)
        cornu.drawpath(points, tweaks=0) 
    