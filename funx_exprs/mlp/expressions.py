import polars as pl


class FunctionExpression:

    pass

class Constant(Expression):

    def __init__(self, pl_expr: pl.Expr):
        self.pl_expr = pl_expr




class MLPExpression(Expression):

    def __init__(self, pl_expr: pl.Expr, dims: dict[str, str]):
        self.pl_expr = pl_expr
        self.dims = dims

    def sum(self) -> "MLPExpression":
        

        """
        (a + bx + cy + dxy)
        
        """