from StochasticPackageQuery.Parser.State.State import State
from StochasticPackageQuery.Query import Query


class AddLogisticConstraintState(State):

    def process(self, query: Query, char: chr) -> Query:
        query.add_logistic_constraint()
        return query