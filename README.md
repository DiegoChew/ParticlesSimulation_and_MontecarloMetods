# Hoja de Trabajo 1

## Problema 1: Partículas encerradas en una caja

Cuando tenemos un choque elastico se va a conservar el momento, por lo que nos valemos de esto para realizar la simulación.

La creación de los objetos tipo partícula y tipo caja están en la carpeta: [Objects](Problema_1/Objects/Objects.py).

Ya que se usó POO lo que diferencia cada inciso es la cantidad de cuerpos tipo partícula instanciadas.

### Inciso 1

> Dos partículas [Codigo](Problema_1/2_particles_collision.py) | [Video](Problema_1/Videos/2_Particles.mp4).

### Inciso 2

> Tres partículas [Codigo](Problema_1/3_particles_collision.py) |  [Video](Problema_1/Videos/3_Particles.mp4).

### Inciso 3

> N partículas [Codigo](Problema_1/N_particles_collision.py) | [Video](Problema_1/Videos/N_Particles.mp4).

## Problema 2: Métodos de Montecarlo

### Area de un triangulo equilatero inscrito en un circulo unitario.

Inicialmente se creó de forma aleatoria coordenadas polares con $r$ entre $[0,1]$ y $\theta $ entre $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$, ya que el marco de referencia lo tenemos en el centro del circulo se optó por moverlo a uno de sus lados y tomar
un vertice del triangulo en ese punto. Unicamente calcularemos la mitad de la figura y se multiplicará por dos al final.

Por ello pasamos a coordenadas cartesianas y a la coordenada $y$ le sumamos $1$ para trasladar los puntos haciendo que el vertice del triangulo quede en $(0,0)$.

Definimos que los puntos que cumplen ser mayores a la recta $y=\sqrt(3) x$ y menores a $y=1.5$ son los puntos que caen dentro del triangulo inscrito. Esto es ya que por geometría la base del triangulo se hubica en $y=1.5$ y el uno de sus lados forma la recta $y=\sqrt(3)x$ donde $\sqrt(3)$ es la pendiente encontrada por el angulo formado entre la horizontal y el lado del triangulo $60^{\circ}$.

El area del triangulo se define como:

$$A_{t}\approx 2*\frac{\text{cantidad de puntos dentro}}{\text{cantidad de puntos totales}}A_{c}$$

Donde $A_{c} = \frac{\pi}{2}$ la mitad del circulo unitario.

> [Codigo](Problema_2/Area_Triangle_MontecarloMetod.py)

> [Imagen](Problema_2/Images/Area_triangle.png)


Importante: ya que estamos generando números aleatorios en polares, para tener una distribución uniforme debemos aplicar raiz cuadrada a r, para compensar la acumulación de puntos en el centro.


### Algoritmo Metropolis-Hastings para minimizar una función 

Con el algoritmo tomamos un valor inicial y vamos variandolo con una distribución, el objetivo es llegar a un valor mínimo por lo que vamos variando y nos vamos quedando con el valor que va minimizando la función, a esto se le agrega un punto de aleatoriedad que nos permite salirnos de minimos locales.

En varias iteraciones, al final tomamos la media en un rango de los ultimos valores tomados de $x$ y este será nuestro mínimo.

> [Codigo](Problema_2/Minimize_Function_Metropolis-Hastings.py)

### Metodo de montecarlo para hacer integrales

Usamos la aproximación de integrales por sumatorias, donde los valores a valuar serán generados aleatoriamente con el objetivo de encontrar una aproximación uniforme en el intervalo pedido

> [Codigo](Problema_2/Integral_MotecarloMetod.py)

> [Imagen](Problema_2/Images/Functions.png)
