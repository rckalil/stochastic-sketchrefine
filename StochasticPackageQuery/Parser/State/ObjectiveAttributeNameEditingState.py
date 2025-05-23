from StochasticPackageQuery.Parser.State.State import State
from StochasticPackageQuery.Query import Query


class ObjectiveAttributeNameEditingState(State):

    def process(self, query: Query, char: chr) -> Query:
        query.add_character_to_objective_attribute(char)
        return query