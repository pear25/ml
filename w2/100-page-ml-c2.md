S' <-- {x2 | x œ S, x > 3}

Set creator notaion, means create a new set S':

1. For all elements in x, 
2. Such that element x is greater than 3,
3. Square the element
4. Add to set S'


e.g:

S = {1,2,5,6}
S'= {25, 36}

In TS:

```typescript

let s = [1,2,5,6]
let s_prime = s.filter((el) => el > 3).map((el) => el ** 2)

```

|S| --> No of elements in S.

Op on Vectors

v1 + v2 = each element in a vector array is added

v1 -> [1,2]
v2 -> [4,6]

v1 + v2 -> [5,8]

Same with subtraction

with scalar multiplication, each element is multiplied by the scalar

c * v -> [c * v1, c * v2, ...., c * vn]

i.e: 1 * v === v

Dot-product between 2 vectors is a scalar:

If you have two vectors, you pair them up index by index:Index 0 times Index 0Index 1 times Index 1Index 2 times Index 2You multiply each pair, sum them up, and you are done.

Example:

1. Define the vectorsLet's choose two three-dimensional vectors for this example:\(\vec{a} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}\)\(\vec{b} = \begin{bmatrix} 5 \\ 6 \\ 7 \end{bmatrix}\)2. Multiply matching componentsMultiply the corresponding components from each vector together:\(x\)-components: \(2 \times 5 = 10\)\(y\)-components: \(3 \times 6 = 18\)\(z\)-components: \(4 \times 7 = 28\)3. Sum the productsAdd all the resulting products together to get the final scalar value:\(\text{Dot\ Product}=10+18+28=56\)

Partial derivatives:

Taking std derative w.r.t. a specific param (ignoring other param) --> hill example from Gemini


AI Mode conversation: Gradient is the generalization of derivative for functions that take several inputs (or one input in the form of a vector or some other complex structure). A gradient of a function is a vector of partial derivatives. You can look at finding a partial derivative of a function as the process of finding the derivative by focusing on one of the function’s inputs and by considering all other inputs as constant values.You said: Gradient is the generalization of derivative for functions that take several inputs (or one input in the form of a vector or some other complex structure). A gradient of a function is a vector of partial derivatives. You can look at finding a partial derivative of a function as the process of finding the derivative by focusing on one of the function’s inputs and by considering all other inputs as constant values.Gradient is the generalization of derivative for functions that take several inputs (or one input in the form of a vector or some other complex structure). A gradient of a function is a vector of partial derivatives. You can look at finding a partial derivative of a function as the process of finding the derivative by focusing on one of the function’s inputs and by considering all other inputs as constant values.You accurately described the foundational mechanics of a gradient. A gradient is a powerful multidimensional extension of the single-variable derivative, packing all of a function's partial derivatives into a neat vector.Key Characteristics of the GradientVector of Partial Derivatives: For a scalar-valued function with inputs \(x_1, x_2, \dots, x_n\), the gradient \(\nabla f\) (read as "del f") is represented as:\(\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}\)Direction of Steepest Ascent: Geometrically, if you are standing at a specific point on a multivariable surface, the gradient vector points in the exact direction where the function's value increases the fastest.Orthogonal to Contour Lines: The gradient vector at any point is always perpendicular to the level curves (contours) of the function.Practical Application: Gradient DescentThis concept is highly valuable in machine learning and optimization algorithms. In Gradient Descent, instead of maximizing a function, algorithms minimize a cost or loss function. By computing the gradient of the error and stepping in the opposite direction of the gradient, models efficiently find the parameter settings that yield the lowest possible error.Would you like to explore how to calculate the gradient of a specific function, or are you interested in learning about how gradients apply to neural network backpropagation? Let me know how you'd like to proceed!9 sitesGradient descent - WikipediaIt is a first-order iterative algorithm for minimizing a differentiable multivariate function. The idea is to take repeated steps ...WikipediaGradients of Scalar Functions | Multivariable Calculus ...hey everyone Katrina here and today I'm going to tell you all about how to find gradients of scalar functions. so to start off wit...6mYouTube·Math Unlocked With KatrinaApplications of Derivatives in Machine LearningGradient descent is an optimization algorithm used to minimize the loss function of a machine learning model. The loss function qu...GeeksforGeeksShow allYou said: I do not understand this at all,, could you go step by step explaining this for meA gradient is just a tool that tells you which way is "steepest uphill" and how steep it is.If you understand a standard derivative, you are already halfway there. Let us break this down step-by-step using a real-world hill analogy.Step 1: Remember Single-Variable DerivativesImagine you are walking on a 2D line graph. You can only move forward or backward.The derivative tells you your slope.A positive derivative means you are walking uphill.A negative derivative means you are walking downhill.Step 2: Move into the 3D WorldNow, imagine you are standing on a physical mountain. You are no longer trapped on a 1D line. You can walk North, South, East, or West.Because you can move in multiple directions, a single number cannot describe your slope anymore. You need to look at your steepness in individual directions. This is where partial derivatives come in.Step 3: Freeze Time with Partial DerivativesTo find a partial derivative, you pretend only one direction matters and freeze the others.Partial Derivative with respect to \(x\) (East/West): You look only to your East and West. You ignore North and South completely. How steep is the hill if you only walk East?Partial Derivative with respect to \(y\) (North/South): You look only to your North and South. You ignore East and West. How steep is the hill if you only walk North?By looking at just one direction at a time, a complex 3D hill becomes as simple as a 2D line.Step 4: Combine Them into the GradientThe gradient is simply a package (a vector) that holds both of those directional answers together.If your East/West slope is \(3\) and your North/South slope is \(4\), your gradient vector is:\(\nabla f=\left[\begin{matrix}3\\ 4\end{matrix}\right]\)Step 5: What does this package actually tell you?This gradient vector gives you two magical pieces of information:The Direction of Steepest Ascent: If you turn your body and walk in the exact direction of the vector (3 steps East, 4 steps North), you will be climbing the hill via the absolute steepest route possible.The Magnitude (Steepness): The length of that vector tells you exactly how steep that steepest route is.
