boids = ximport("boids")
colors = ximport("colors")

size(1280,800)
rect(0, 0, 1280, 800, fill=(0, 0, 0))

palette = [colors.hex("#FAFAD2", "light yellow"),
           colors.hex("#EEE8AA", "pale yellow"),
           colors.hex("#F0E68C", "khaki"),
           colors.hex("#FFD700", "gold"),
           colors.hex("#DAA520", "goldenrod")]

num_boids = random(100,140)
nostroke()

flock = boids.flock(num_boids, 0, 0, 1350, 850)

for boid in flock:
    boid_color = choice(palette)
    boid_color.a = random(0.4,0.8)
    fill(boid_color)
    dimension = random(60,110)
    oval(boid.x, boid.y, dimension, dimension, draw=True)
