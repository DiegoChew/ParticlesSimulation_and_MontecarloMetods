from Objects.Objects import Particle, Box
import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

box = Box(Lx=15, Ly=15)


box.add_particle(Particle(m=1.0, x=10.0, y=10.0, vx=-40, vy=20, r=1.5))
box.add_particle(Particle(m=1.0, x=5.0, y=5.0, vx=10, vy=-50, r=1.5))

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, box.Lx)
ax.set_ylim(0, box.Ly)
ax.set_aspect('equal')
ax.grid(False)

particle_artists = []
for p in box.particles:
    circle = plt.Circle((p.x, p.y), p.r, fc='green', alpha=0.6)
    ax.add_patch(circle)
    particle_artists.append(circle)


def animate(frame):
    box.simulate()  
    for i, p in enumerate(box.particles):
        circle = particle_artists[i]
        circle.set_center((p.x, p.y))
    return particle_artists

# fps = 30  
# duration = 10  
# total_frames = fps * duration

ani = FuncAnimation(fig, animate, frames=10000, interval=10, blit=False,cache_frame_data=False)

# writer = animation.FFMpegWriter(fps=fps, bitrate=1800)
# ani.save('simulacion_2_particulas.mp4', writer=writer)

plt.show()
 