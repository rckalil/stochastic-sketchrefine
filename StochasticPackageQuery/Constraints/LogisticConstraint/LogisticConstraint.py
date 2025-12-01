from StochasticPackageQuery.Constraints.Constraint import Constraint
from Utils.RelationalOperators import RelationalOperators


class LogisticConstraint(Constraint):
    """
    Representa a restrição logarítmica do problema Risk Budgeting Portfolio (RBP),
    formulada como: SUM(B_i * log(v_i)) >= 0.

    Esta restrição é determinística e tem o limite (sum_limit) e o operador
    relacional fixos (GREATER_THAN_OR_EQUAL_TO e 0.0, respectivamente).
    """

    def __init__(self):
        # A restrição RBP é considerada determinística, pois as variáveis de 
        # risco (B_i) são pré-determinadas (o RBP é resolvido em um problema de otimização convexo
        # após a simulação).
        self.__is_inequality_sign_set = True
        self.__inequality_sign = RelationalOperators.GREATER_THAN_OR_EQUAL_TO
        self.__is_sum_limit_set = True
        self.__sum_limit = 1.0 
        
        # O nome do atributo é o keyword completo (LOG RISK BUDGET) ou a função.
        self.__attribute_name = 'price'

    def is_logistic_constraint(self) -> bool:
        """Indica que esta é uma restrição do tipo determinística (para o parser)."""
        return True

    def is_deterministic_constraint(self) -> bool:
        """Indica que esta é uma restrição do tipo determinística (para o parser)."""
        return True

    def is_inequality_sign_set(self) -> bool:
        """O sinal é fixo (>=), então é sempre True."""
        return self.__is_inequality_sign_set

    def is_sum_limit_set(self) -> bool:
        """O limite é fixo (0.0), então é sempre True."""
        return self.__is_sum_limit_set

    def get_inequality_sign(self) -> RelationalOperators:
        """Retorna o sinal fixo: >=."""
        return self.__inequality_sign

    def get_sum_limit(self) -> float:
        """Retorna o limite fixo: 0.0."""
        return self.__sum_limit

    # Os métodos abaixo não são necessários para a Lógica RBP (pois o sinal e o limite são fixos),
    # mas são definidos para compatibilidade:
    
    def set_inequality_sign(self, char: chr):
        raise NotImplementedError("Inequality sign for LogisticConstraint is fixed (>=) and cannot be changed.")

    def set_sum_limit(self, sum_limit: float):
        raise NotImplementedError("Sum limit for LogisticConstraint is fixed (0.0) and cannot be changed.")

    def add_character_to_sum_limit(self, char: chr):
        raise NotImplementedError("Sum limit for LogisticConstraint is fixed (0.0) and cannot be built iteratively.")

    def set_attribute_name(self, attribute_name: str):
        """Permite a redefinição do nome, se necessário."""
        self.__attribute_name = attribute_name

    def add_character_to_attribute_name(self, char: chr):
        """Permite construir o nome do atributo, se necessário."""
        self.__attribute_name += char
        
    def get_attribute_name(self) -> str:
        """Retorna o nome simbólico da restrição."""
        return self.__attribute_name