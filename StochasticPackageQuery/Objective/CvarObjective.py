from Utils.ObjectiveType import ObjectiveType
from Utils.Stochasticity import Stochasticity
from Utils.TailType import TailType
from StochasticPackageQuery.Objective.Objective import Objective


class CvarObjective(Objective):

    def __init__(self):
        # self.__is_objective_type_set = False
        # self.__objective_type = ObjectiveType.MAXIMIZATION
        # self.__attribute_name = ''
        # self.__is_stochasticity_set = False
        # self.__stochasticity = Stochasticity.STOCHASTIC
        super().__init__()
        self.__is_tail_type_set = False
        self.__tail_type = TailType.LOWEST
        self.__is_percentage_of_scenarios_set = False
        self.__percentage_of_scenarios = 0.0
        self.__cached_percentage_string = ''

    def set_stochasticity(self, is_stochastic: bool):
        self.__is_stochasticity_set = True
        self.__stochasticity = Stochasticity.CVAR
    
    def is_risk_objective(self) -> bool:
        return True
    
    def is_cvar_objective(self) -> bool:
        return True