import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constante de gravedad (puede ajustarse para simular otros planetas)
g = 9.81  # m/s^2

# Entradas del usuario
peso = float(input("Introduce el peso de la bola (kg): "))
angulo = float(input("Introduce el ángulo de lanzamiento (grados): "))
velocidad_inicial = float(input("Introduce la velocidad inicial (m/s): "))
altura_inicial = float(input("Introduce la altura inicial (m): "))

# Conversiones y cálculos
angulo_rad = np.radians(angulo)  # Convertir ángulo a radianes
vx = velocidad_inicial * np.cos(angulo_rad)  # Componente horizontal de la velocidad
vy = velocidad_inicial * np.sin(angulo_rad)  # Componente vertical de la velocidad

# Tiempo total de vuelo (resolviendo la ecuación cuadrática de y = 0)
t_total = (vy + np.sqrt(vy**2 + 2 * g * altura_inicial)) / g

# Tiempo y puntos de trayectoria
t = np.linspace(0, t_total, num=500)
x = vx * t
y = altura_inicial + vy * t - 0.5 * g * t**2

# Alcance máximo y altura máxima
alcance = max(x)
altura_maxima = altura_inicial + (vy**2) / (2 * g)

# Imprimir resultados
print("\nResultados del Tiro Parabólico:")
print(f"Alcance máximo: {alcance:.2f} m")
print(f"Altura máxima: {altura_maxima:.2f} m")
print(f"Tiempo total en el aire: {t_total:.2f} s")

# Configurar la animación
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, alcance + 5)
ax.set_ylim(0, altura_maxima + 5)
ax.set_title("Simulación de Tiro Parabólico")
ax.set_xlabel("Distancia horizontal (m)")
ax.set_ylabel("Altura (m)")

# Dibujar lanzador y ángulo
lanzador = ax.plot(0, altura_inicial, 's', color='brown', markersize=20, label="Lanzador")[0]
angle_arrow = ax.arrow(0, altura_inicial, 
                       np.cos(angulo_rad) * 5, 
                       np.sin(angulo_rad) * 5, 
                       head_width=1, head_length=2, fc='green', ec='green', label="Ángulo")

trajectory, = ax.plot([], [], 'b-', lw=2, label="Trayectoria")
ball, = ax.plot([], [], 'ro', markersize=8, label="Bola")
impact_point, = ax.plot([], [], 'gx', markersize=10, label="Impacto")
result_text = ax.text(0.5, 0.95, "", transform=ax.transAxes, fontsize=12, va='top')

# Función de actualización para la animación
def update(frame):
    # Actualizar trayectoria y pelota
    trajectory.set_data(x[:frame], y[:frame])
    ball.set_data([x[frame]], [y[frame]])  # Asegurar que se pase como lista
    
    # Mostrar el punto de impacto y resultados cuando llegue al final
    if frame == len(t) - 1:
        impact_point.set_data([alcance], [0])
        result_text.set_text(
            f"Alcance: {alcance:.2f} m\nAltura Máxima: {altura_maxima:.2f} m\nTiempo Total: {t_total:.2f} s"
        )
    return trajectory, ball, impact_point, result_text

# Crear animación
ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

# Mostrar la animación
plt.legend()
plt.tight_layout()
plt.show()
