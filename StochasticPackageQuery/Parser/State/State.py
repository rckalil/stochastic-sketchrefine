from StochasticPackageQuery.Query import Query
from StochasticPackageQuery.Parser.Transition.Transition import Transition


class State:

    def __init__(self) -> None:
        self.__transitions = []

    def process(self, query: Query, char: chr) -> Query:
        return query
    
    def get_transitions(self) -> list[Transition]:
        return self.__transitions
    
    def add_transition(self, transition: Transition):
        for existing_transition in self.__transitions:
            if existing_transition.get_trigger() == transition.get_trigger()\
                and existing_transition.fires(transition.get_trigger())\
                and transition.fires(transition.get_trigger()):
                raise Exception
        self.__transitions.append(transition)

    def get_next_state(self, char: chr):
        # print("Getting next state for char:", char)
        # print("Current transitions:")
        # print(self.__transitions)
        trans = [t.get_trigger() for t in self.__transitions]
        # print("Firing transitions for char:", trans)
        for transition in self.__transitions:
            # print(transition.get_trigger(), transition.fires(char), char)
            if transition.fires(char):
                return transition.get_next_state()
        raise Exception
