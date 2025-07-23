
class GroupBy:

    def __init__(self, df: DataFrame, by: list[UnresolvedExpr]):
        self.df = df
        self.by = by

    def agg(self, exprs: list[UnresolvedExpr]) -> DataFrame:
        schema = {expr.name: expr.dtype for expr in exprs}
        pl_by = [expr.pl_expr for expr in self.by]
        pl_df = self.df.pl_df.group_by(pl_by).agg([expr.pl_expr for expr in exprs])
        return DataFrame(pl_df, schema)