




class Expr:



class PiecewiseMultilinearPolynomialDataFunction:
    """Data function representing a piecewise multilinear polynomial function.
    I.e. an n-variate function defined on non-overlapping n-rectangles, with
    the function being a multilinear polynomial on each n-rectangle.

    The dimensions are thus represented by intervals and the variables
    by their coefficient matrix. Fx

    - Dimensions:
        - x: [0, 10]
        - y: [50, 100]
    - Variables:
        - s: [[1, 2], [3, 4]] (representing 1 + 3*x + 2*y + 4*x*y)
        - t: [[5, 6], [7, 8]] (representing 5 + 7*x + 6*y + 8*x*y)
    
    """

    def __init__(
        self,
        df,
        dims: list[str],
        vars: list[str]
    ):
        self.df = df
        self.dims = dims
        self.vars = vars
