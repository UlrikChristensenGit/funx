class UnresolvedExpression:

    def resolve():
        pass

    def __add__(self, other: "UnresolvedExpression") -> "UnresolvedExpression":
        def resolve():
            return self.resolve() + other.resolve()
