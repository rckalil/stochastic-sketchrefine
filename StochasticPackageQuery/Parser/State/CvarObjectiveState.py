from StochasticPackageQuery.Parser.State.State import State
from StochasticPackageQuery.Query import Query
from StochasticPackageQuery.Objective.CvarObjective import CvarObjective


class CvarObjectiveState(State):

    def process(self, query: Query, char: chr) -> Query:
        """
        Instancia a CvarObjective, define o objetivo da Query,
        e configura a estocasticidade.
        """
        
        # 1. Cria a instância do CvarObjective (que já tem a estocasticidade setada como CVAR)
        cvar_objective = CvarObjective()
        
        # 2. Substitui o objeto Objective padrao pelo CvarObjective
        #    (O Query precisa ter um metodo set_objective que aceite o novo objeto)
        query.set_objective(cvar_objective)
        
        # 3. Define a estocasticidade (Opcional, se ja estiver no construtor de CvarObjective)
        #    A estocasticidade deve ser setada para CVAR, nao apenas TRUE/FALSE.
        #    Se CvarObjective ja seta internamente, essa linha pode ser removida:
        query.set_objective_stochasticity(is_stochastic=True) 

        return query