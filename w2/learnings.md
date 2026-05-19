# Linear Algebra

### Eigenvalues

- When doing a linear transformation, there are certain vectors that are entirely unaffected vector-wise (they are affected by scalar factor), these vectors: eigenvectors
- The scalar factor of these vectors are the corresponding eigenvalues
- Eigenbasis, are when the eigenvectors are basis vectors, using matrix manipulation to translate initial eigenvectors in eigenbasis, makes them easier to calculate

$M^-1\cdot (A) \cdot (M)$

# Calculus

### Core idea

- Helps us mathematically model rate of change in a definitive notation.

- Regular definition: Instantaneous rate of change, but instant and change are contradictory, idea is rather the best approximation of rate of change at a particular moment.

Example would be a 2d graph plotting time and distance covered by a car, at t = 0, the tangent at t=0, would roughly be 0, since car has not moved, but to say that the car is not moving at t = 0 is contradictory, if we take distance travelled by car at t + 0.1s, we can assume that the car has moved slightly:

- Scoping into lower time intervals (t + 0.0000...1s), the car will move less and less (but still moving!), and that approximation is what results to the tangent (rate of change at t = 0), to conclude to the value of 0.
- The concept is that, at t=0 and in the very near future, the car is moving (albeit very little), and the best approximation of the rate of change of that car (speed), can be concluded as 0.


## Ideology on derivative

- Sectioning circles with circular partitions.

### Power Rule

$x^n$ -> $nx^{n-1}$

Idea of square, adding dx of length, and of cube, since dx would be minimal, resulting in those factors omitted from the result.

### Sum Rule

$g(x)+(h(x))$ -> $\frac{d(g(x))}{dx}$ + $\frac{d(h(x))}{dx}$

Idea of graph, sums of graph give an additive result when dx implemented in both charts.

### Product Rule

$g(x)\cdot(h(x))$ -> $\frac{d(g(x))}{dx}\cdot (h(x))$ + $\frac{d(h(x))}{dx}\cdot (g(x))$

Idea similar to square on referred to by the power rule


### Composition Rule

$g(h(x))$ -> $g'(h(x)) \cdot h'(x)$

Number line idea, substituting inside function as another representative variable.

In Leibniz notation, if $y = f(u)$ and $u = g(x)$, the rule is written as:$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$