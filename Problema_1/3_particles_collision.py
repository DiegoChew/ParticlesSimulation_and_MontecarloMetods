from Objects.Objects import Particle, Box
import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
            
box = Box(Lx=20, Ly=20)


box.add_particle(Particle(m=1.0, x=15.0, y=3.0, vx=50, vy=30, r=1))
box.add_particle(Particle(m=1.0, x=2.0, y=10.0, vx=-40, vy=20, r=1))
box.add_particle(Particle(m=1.0, x=10.0, y=15.0, vx=10, vy=-50, r=1))

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, box.Lx)
ax.set_ylim(0, box.Ly)
ax.set_aspect('equal')
ax.grid(False)

particle_artists = []
for p in box.particles:
    circle = plt.Circle((p.x, p.y), p.r, fc='blue', alpha=0.6)
    ax.add_patch(circle)
    particle_artists.append(circle)


def animate(frame):
    box.simulate()  
    for i, p in enumerate(box.particles):
        circle = particle_artists[i]
        circle.set_center((p.x, p.y))
    return particle_artists

ani = FuncAnimation(fig, animate, frames=10000, interval=10, blit=False,cache_frame_data=False)
plt.show()
 