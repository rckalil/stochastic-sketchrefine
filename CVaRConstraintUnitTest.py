import unittest
from StochasticPackageQuery.Constraints.ExpectedSumConstraint.ExpectedSumConstraint import ExpectedSumConstraint
from StochasticPackageQuery.Constraints.CVaRConstraint.CVaRConstraint import CVaRConstraint
from Utils.TailType import TailType
import sys

# Função auxiliar para prints formatados
def print_separator(title):
    print("\n" + "="*50)
    print(f"--- {title} ---")
    print("="*50)

class CVaRConstraintUnitTest(unittest.TestCase):
    
    def test_initial_conditions(self):
        print_separator("TEST 1: Condições Iniciais da CVaRConstraint")
        cvar_constraint = CVaRConstraint()
        self.assertTrue(cvar_constraint.is_risk_constraint())
        self.assertTrue(cvar_constraint.is_cvar_constraint())
        print("Status: Nova CVaRConstraint inicializada.")
        print(f"É restrição de risco (True): {cvar_constraint.is_risk_constraint()}")
        print(f"Limite de soma (V) configurado (False): {cvar_constraint.is_sum_limit_set()}")
        self.assertFalse(cvar_constraint.is_sum_limit_set())
        self.assertFalse(cvar_constraint.is_inequality_sign_set())
        self.assertFalse(cvar_constraint.is_percentage_of_scenarios_set())
        self.assertFalse(cvar_constraint.is_tail_type_set())
        print("TEST 1 CONCLUÍDO: Todos os sinalizadores iniciais estão False.")
    
    def test_initial_conditions_from_expected_sum_constraint(self):
        print_separator("TEST 2: Inicialização a partir de ExpectedSumConstraint")
        expected_sum_constraint = ExpectedSumConstraint()
        expected_sum_constraint.set_attribute_name('Expected_Gain_Attr')
        expected_sum_constraint.set_inequality_sign('>')
        expected_sum_constraint.set_sum_limit(-50)
        print(f"Origem (ExpectedSumConstraint) configurada: Atributo='{expected_sum_constraint.get_attribute_name()}', Limite={expected_sum_constraint.get_sum_limit()}")
        
        cvar_constraint = CVaRConstraint()
        cvar_constraint.initialize_from_expected_sum_constraint(
            expected_sum_constraint)
        
        print("\nCVaRConstraint após a inicialização:")
        self.assertEqual(cvar_constraint.get_attribute_name(),
                          expected_sum_constraint.get_attribute_name())
        self.assertEqual(cvar_constraint.get_inequality_sign(),
                          expected_sum_constraint.get_inequality_sign())
        self.assertEqual(cvar_constraint.get_sum_limit(),
                          expected_sum_constraint.get_sum_limit())
        print(f" -> Atributo Copiado: {cvar_constraint.get_attribute_name()}")
        print(f" -> Sinal Copiado: {cvar_constraint.get_inequality_sign()}")
        print(f" -> Limite (V) Copiado: {cvar_constraint.get_sum_limit()}")
        
        self.assertFalse(cvar_constraint.is_percentage_of_scenarios_set())
        self.assertFalse(cvar_constraint.is_tail_type_set())
        print("TEST 2 CONCLUÍDO: Atributos e Limites foram copiados corretamente.")
    
    def test_percentage_of_scenarios_consistency(self):
        print_separator("TEST 3: Consistência do Percentual de Cenários")
        
        # Teste de sucesso
        cvar_constraint = CVaRConstraint()
        cvar_constraint.set_percentage_of_scenarios(95)
        print(f"Status: Percentual de 95% setado com sucesso.")
        self.assertEqual(cvar_constraint.get_percentage_of_scenarios(), 95)

        # Testes de falha (limites)
        print("Verificando se valores inválidos (0, <0, >100) levantam exceção...")
        with self.assertRaises(Exception):
            cvar_constraint.set_percentage_of_scenarios(0)
        with self.assertRaises(Exception):
            cvar_constraint.set_percentage_of_scenarios(-5)
        with self.assertRaises(Exception):
            cvar_constraint.set_percentage_of_scenarios(105)
        print("TEST 3 CONCLUÍDO: Limites de 0 a 100% estão sendo validados.")
    
    def test_setting_percentage_of_scenarios_digit_by_digit(self):
        print_separator("TEST 4: Configuração Digito por Digito (Parser)")
        cvar_constraint = CVaRConstraint()
        
        cvar_constraint.add_character_to_percentage_of_scenarios('9')
        cvar_constraint.add_character_to_percentage_of_scenarios('.')
        cvar_constraint.add_character_to_percentage_of_scenarios('5')
        
        self.assertTrue(cvar_constraint.is_percentage_of_scenarios_set())
        self.assertAlmostEqual(cvar_constraint.get_percentage_of_scenarios(), 9.5)
        print(f"Percentual reconstruído com sucesso: 9.5")

        # Testes de falha de construção (e.g., caracter inválido)
        print("Verificando falhas de construção (ex: sinal negativo, valor grande)...")
        with self.assertRaises(Exception):
            cvar_constraint = CVaRConstraint()
            cvar_constraint.add_character_to_percentage_of_scenarios('-')
            cvar_constraint.add_character_to_percentage_of_scenarios('5')
        with self.assertRaises(Exception):
            cvar_constraint = CVaRConstraint()
            cvar_constraint.add_character_to_percentage_of_scenarios('1')
            cvar_constraint.add_character_to_percentage_of_scenarios('1')
            cvar_constraint.add_character_to_percentage_of_scenarios('1')
        print("TEST 4 CONCLUÍDO: A construção digito a digito funciona e falha corretamente.")
    
    def test_get_percentage_of_scenarios_before_setting_it(self):
        print_separator("TEST 5: Tentativa de Acesso Antes da Configuração")
        cvar_constraint = CVaRConstraint()
        with self.assertRaises(Exception):
            cvar_constraint.get_percentage_of_scenarios()
        print("TEST 5 CONCLUÍDO: Leitura antes da configuração levanta exceção esperada.")
    
    def test_tail_type_consistency(self):
        print_separator("TEST 6: Consistência do Tipo de Cauda (Tail Type)")
        
        cvar_constraint = CVaRConstraint()
        cvar_constraint.set_tail_type('h')
        self.assertEqual(cvar_constraint.get_tail_type(), TailType.HIGHEST)
        print("Cauda configurada: 'h' -> TailType.HIGHEST")

        cvar_constraint = CVaRConstraint()
        cvar_constraint.set_tail_type('l')
        self.assertEqual(cvar_constraint.get_tail_type(), TailType.LOWEST)
        print("Cauda configurada: 'l' -> TailType.LOWEST")

        with self.assertRaises(Exception):
            cvar_constraint = CVaRConstraint()
            cvar_constraint.set_tail_type('a')
        print("TEST 6 CONCLUÍDO: Tipos de cauda ('h', 'l') são validados.")
        
    def test_get_tail_type_before_setting_it(self):
        print_separator("TEST 7: Tentativa de Leitura da Cauda Antes da Configuração")
        cvar_constraint = CVaRConstraint()
        with self.assertRaises(Exception):
            cvar_constraint.get_tail_type()
        print("TEST 7 CONCLUÍDO: Leitura do tipo de cauda antes da configuração levanta exceção esperada.")


    def main(self):
        # Para evitar problemas com o ambiente unittest, use unittest.main() ou execute diretamente.
        # Se for rodar main(), comente as linhas 'with self.assertRaises(Exception):' para evitar parar o script.
        # No entanto, a forma padrão é rodar o script diretamente via linha de comando ou VS Code.
        print("Iniciando testes de unidade para CVaRConstraint...")
        self.test_initial_conditions()
        self.test_initial_conditions_from_expected_sum_constraint()
        self.test_percentage_of_scenarios_consistency()
        self.test_setting_percentage_of_scenarios_digit_by_digit()
        self.test_get_percentage_of_scenarios_before_setting_it()
        self.test_tail_type_consistency()
        self.test_get_tail_type_before_setting_it()

# Para rodar fora do ambiente unittest padrão:
if __name__ == '__main__':
    CVaRConstraintUnitTest().main()