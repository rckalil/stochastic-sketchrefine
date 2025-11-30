from Utils.ObjectiveType import ObjectiveType
from Utils.Stochasticity import Stochasticity
from Utils.TailType import TailType
from StochasticPackageQuery.Objective.Objective import Objective


class CvarObjective(Objective):

    def __init__(self):
        self.__is_objective_type_set = True
        self.__objective_type = ObjectiveType.MAXIMIZATION
        self.__attribute_name = ''
        self.__is_stochasticity_set = True
        self.__stochasticity = Stochasticity.STOCHASTIC
        self.__is_tail_type_set = True
        self.__tail_type = TailType.LOWEST
        self.__is_percentage_of_scenarios_set = False
        self.__percentage_of_scenarios = 0.0
        self.__cached_percentage_string = ''
    
    def is_objective_type_set(self) -> bool:
        return self.__is_objective_type_set

    def is_stochasticity_set(self) -> bool:
        return self.__is_stochasticity_set

    def get_objective_type(self) -> int:
        if not self.__is_objective_type_set:
            raise Exception
        return self.__objective_type

    def get_attribute_name(self) -> str:
        return self.__attribute_name

    def set_stochasticity(self, is_stochastic: bool):
        print("ah")
        # raise
        self.__is_stochasticity_set = True
        self.__stochasticity = Stochasticity.CVAR
    
    def get_stochasticity(self) -> str:
        if not self.__is_stochasticity_set:
            raise Exception
        return self.__stochasticity
    
    def is_risk_objective(self) -> bool:
        return True
    
    def is_cvar_objective(self) -> bool:
        return True
    
    def get_percentage_of_scenarios(self):
        return 95.0
    
    def get_tail_type(self):
        return TailType.HIGHEST

    def set_attribute_name(self, attribute_name: str):
        self.__attribute_name = attribute_name
    
    def set_objective_type(self, is_maximization: bool):
        self.__is_objective_type_set = True
        if is_maximization:
            self.__objective_type = ObjectiveType.MAXIMIZATION
        else:
            self.__objective_type = ObjectiveType.MINIMIZATION
    
    def add_character_to_attribute_name(self, char: chr):
        self.__attribute_name += char