class Particle():
  def __init__(self,m, x, y, vx, vy, r):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.m = m
    self.dt = 0.01
    self.r = r

  def momentum(self):
    return self.m*self.vx, self.m*self.vy

  def move(self):
      self.x += self.vx * self.dt
      self.y += self.vy * self.dt
  
  def particle_box_collision(self, box):
      
    if self.x - self.r <= 0:
      self.x = self.r  
      self.vx *= -1
    elif self.x + self.r >= box.Lx:
        self.x = box.Lx - self.r
        self.vx *= -1

    if self.y - self.r <= 0:
        self.y = self.r
        self.vy *= -1
    elif self.y + self.r >= box.Ly:
        self.y = box.Ly - self.r
        self.vy *= -1

  def particle_particle_collision(self, other):
      dx = self.x - other.x
      dy = self.y - other.y
      distance = (dx**2 + dy**2)**0.5
      min_distance = self.r+other.r
      if distance < min_distance:

        nx = dx / (distance +1e-50)
        ny = dy / (distance +1e-50)

        overlap = min_distance - distance
        self.x += nx * (overlap / 2)
        self.y += ny * (overlap / 2)
        other.x -= nx * (overlap / 2)
        other.y -= ny * (overlap / 2)

        m1, m2 = self.m, other.m
        v1x, v1y = self.vx, self.vy
        v2x, v2y = other.vx, other.vy

        self.vx = (v1x*(m1 - m2) + 2*m2*v2x) / (m1 + m2)
        self.vy = (v1y*(m1 - m2) + 2*m2*v2y) / (m1 + m2)
        other.vx = (v2x*(m2 - m1) + 2*m1*v1x) / (m1 + m2)
        other.vy = (v2y*(m2 - m1) + 2*m1*v1y) / (m1 + m2)

class Box():
    def __init__(self, Lx, Ly):
      self.Lx = Lx
      self.Ly = Ly
      self.particles = []

    def add_particle(self, particle):
      self.particles.append(particle)

    def simulate(self):
      for p in self.particles:
          p.move()
          p.particle_box_collision(self)  
            
      for i in range(len(self.particles)):
          for j in range(i + 1, len(self.particles)):
             self.particles[i].particle_particle_collision(self.particles[j])

