from Objects.Objects import Particle, Box
import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random as rd
import matplotlib.animation as animation


Lx=70
Ly=40
box = Box(Lx, Ly)

N = 300
for _ in range(N):
    m=1
    r=1
    x=rd.randint(0,Lx-r)
    y=rd.randint(0,Ly-r)
    vx=rd.randint(-15,15)
    vy=rd.randint(-15,15)
    box.add_particle(Particle(m=m, x=x, y=y, vx=vx, vy=vy, r=r))

fig, ax = plt.subplots(figsize=(15, 8))
ax.set_xlim(0, box.Lx)
ax.set_ylim(0, box.Ly)
ax.set_aspect('equal')
ax.grid(False)

particle_artists = []
for p in box.particles:
    circle = plt.Circle((p.x, p.y), p.r, fc='red', alpha=0.6)
    ax.add_patch(circle)
    particle_artists.append(circle)


def animate(frame):
    box.simulate()  
    for i, p in enumerate(box.particles):
        circle = particle_artists[i]
        circle.set_center((p.x, p.y))
    return particle_artists

fps = 30  
duration = 1  
total_frames = fps * duration

ani = FuncAnimation(fig, animate, frames=10000, interval=10, blit=False,cache_frame_data=False)

writer = animation.FFMpegWriter(fps=fps, bitrate=1800)
ani.save('simulacion_2_particulas.mp4', writer=writer)


plt.show()