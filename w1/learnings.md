## W1 Learnings

### Linear Alg.

- Basis vectors: min set of linearly independent vectors whose combinations span the entire vector space
- Matrix multipliaction: Transformations, where each matrix col represents the new coordinates for each basis vector

$$
\begin{bmatrix}
1 & 2 \\
4 & 5\\
\end{bmatrix}
$$


means that the i vector, will be at co-ordinates (1,4) and j basis vector will be at co-ordinates (2,5) post matrix transformation.

- Transformations are applied left to right: meaning if we have an existing vector V, and is transformed with Matrix A and B successively, the mathematical representation is as follows where V' is the new matrix:

```
V' = B * A * V
```

- The value of a determinant represents how much the area covered by a vector will scale based after a matrix transformation.

Given matrix M:

$$
\begin{bmatrix}
3 & 0 \\
0 & 3\\
\end{bmatrix}
$$

```
det(M) = 9
```
Given an original vector at
$$
\begin{bmatrix}
2 & 0 \\
0 & 2\\
\end{bmatrix}
$$

Where the original area is 4 (2*2), this will transform the new matrix into:

$$
\begin{bmatrix}
6 & 0 \\
0 & 6\\
\end{bmatrix}
$$

And as described above, the area increases from 4 to 36, scaling the area by a factor of 9, and reflects the statement provided above.


## Broadcasting

- Prepend 1 to fit shape dimensions
- Stretch all 1 dimensions to fit the shape of 1st matrix in a given 2 matrix op.

## Axis reduction

- When there are reduction operations (e.g. sum), and axis is specified, this means shape transforms to one where the axis is removed from the original shape e.g. 

```
(3, 4, 4) --> reduce axis 1 --> (3, 4) 
```

