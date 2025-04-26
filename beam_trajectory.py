# Kritesh Silwal
# 1002163716

import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 1.602e-19       # charge in Coulumb
me = 9.11e-31       # mass in kg

# parameters
Ek_eV = 20
Ek = Ek_eV * e
v0 = np.sqrt(2 * Ek / me)
dt = 1e-11
steps = 5000

def simulate_trajectory(v0, q, m, Bz):
    pos = np.array([0.0, 0.0])
    vel = np.array([v0, 0.0])
    x_traj = []
    y_traj = []
    for _ in range(steps):
        F = q * np.cross(vel, [0, 0, Bz])[:2]
        a = F / m
        vel += a * dt
        pos += vel * dt
        x_traj.append(pos[0] * 100)
        y_traj.append(pos[1] * 100)
        if abs(pos[1]) > 10:
            break
    return x_traj, y_traj


fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Parameter Dependence of Beam Trajectory', fontsize=16)

# 1. Magnetic Field Dependence
for Bz in [1e-3, 2e-3, 5e-3]:
    x, y = simulate_trajectory(v0, e, me, Bz)
    axs[0, 0].plot(x, y, label=f'B = {Bz*1e3:.1f} mT')
axs[0, 0].set_title('Varying Magnetic Field')
axs[0, 0].set_xlabel('x (cm)')
axs[0, 0].set_ylabel('y (cm)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# 2. Kinetic Energy Dependence
for Ek_eV in [10, 20, 40]:
    Ek = Ek_eV * e
    v0 = np.sqrt(2 * Ek / me)
    x, y = simulate_trajectory(v0, e, me, 2e-3)
    axs[0, 1].plot(x, y, label=f'E = {Ek_eV} eV')
axs[0, 1].set_title('Varying Kinetic Energy')
axs[0, 1].set_xlabel('x (cm)')
axs[0, 1].set_ylabel('y (cm)')
axs[0, 1].legend()
axs[0, 1].grid(True)

# 3. Mass Dependence
for m in [me, 2*me, 4*me]:
    v0 = np.sqrt(2 * 20 * e / m)
    x, y = simulate_trajectory(v0, e, m, 2e-3)
    axs[1, 0].plot(x, y, label=f'm = {m/me:.0f} mₑ')
axs[1, 0].set_title('Varying Particle Mass')
axs[1, 0].set_xlabel('x (cm)')
axs[1, 0].set_ylabel('y (cm)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# 4. Charge Sign Dependence
x1, y1 = simulate_trajectory(v0, e, me, 2e-3)
x2, y2 = simulate_trajectory(v0, -e, me, 2e-3)
axs[1, 1].plot(x1, y1, label='Positron (+q)')
axs[1, 1].plot(x2, y2, label='Electron (-q)')
axs[1, 1].set_title('Effect of Charge Sign')
axs[1, 1].set_xlabel('x (cm)')
axs[1, 1].set_ylabel('y (cm)')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
