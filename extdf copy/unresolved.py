

class UnresolvedExpr:

    def __init__(self, resolver):
        self.resolve = resolver

    @classmethod
    def as_expr(cls, value) -> 'UnresolvedExpr':
        if isinstance(value, UnresolvedExpr):
            return value
  
        def resolve(ctx):
            return value

        return cls(resolve)

    @classmethod
    def from_column_name(cls, name: str) -> 'UnresolvedExpr':
        def resolve(ctx):
            return ctx._resolve_column_name(name)
        return cls(resolve)
    
    def alias(self, name: str) -> 'UnresolvedExpr':
        def resolve(ctx):
            return self.resolve(ctx).alias(name)
        return UnresolvedExpr(resolve)

    def __add__(self, other):
        def resolve(ctx):
            valid_other = self.as_expr(other)
            return self.resolve(ctx) + valid_other.resolve(ctx)
        return UnresolvedExpr(resolve)

    def sum(self):
        def resolve(ctx):
            return self.resolve(ctx).sum()
        return UnresolvedExpr(resolve)

    def union(self, other):
        def resolve(ctx):
            return self.resolve(ctx).union(other.resolve(ctx))
        return UnresolvedExpr(resolve)


def col(name: str) -> UnresolvedExpr:
    """Create an unresolved expression for a column name."""
    return UnresolvedExpr.from_column_name(name)