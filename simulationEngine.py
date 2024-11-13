import numpy as np 

class Particle:
  def __init__(self, mass, position, velocity):
    self.mass = mass
    self.position = np.array(position)
    self.velocity = np.array(velocity)
    self.force = np.zeros_like(position)

class ParticleSystem:
  def __init__(self, particles):
    self.particles = particles 

  def calculate_forces(self):
    for particle in self.particles:
      particle.force = np.zeros_like(particle.position)

  def update_positions(self, dt):
    for particle in self.particles:
      acceleration = particle.force / particle.mass 
      particle.velocity += acceleration * dt
      particle.position += particle.velocity * dt 

  def simulate(self, dt, num_steps):
    for _ in range(num_steps):
      self.calculate_forces()
      self.update_positions(dt)

# example usage
particles = [
  Particle(1.0, [0, 0], [1, 0]),
  Particle(2,0, [1, 1], [-1, -1])
]

system = ParticleSystem(particles)
system.simulate(0.1, 100) 
