from StochasticPackageQuery.Parser.State.State import State
from StochasticPackageQuery.Query import Query


class AddLogarithmConstraintState(State):

    def process(self, query: Query, char: chr) -> Query:
        query.add_logarithm_constraint()
        return query