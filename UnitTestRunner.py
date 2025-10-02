from PgConnection.PgConnectionUnitTest import PgConnectionUnitTest
from OfflinePreprocessing.MeanAbsoluteDistanceUnitTest import MeanAbsoluteDistanceUnitTest
from OfflinePreprocessing.PivotScanUnitTest import PivotScanUnitTest
from ScenarioGenerator.ScenarioGeneratorUnitTest import ScenarioGeneratorUnitTest
from ScenarioGenerator.TpchScenarioGenerators.PriceScenarioGeneratorUnitTest import PriceScenarioGeneratorUnitTest
from ScenarioGenerator.TpchScenarioGenerators.QuantityScenarioGeneratorUnitTest import QuantityScenarioGeneratorUnitTest
from ScenarioGenerator.PorfolioScenarioGenerator.GainScenarioGeneratorUnitTest import GainScenarioGeneratorUnitTest
from StochasticPackageQuery.Constraints.ConstraintUnitTest import ConstraintUnitTest
from StochasticPackageQuery.Constraints.RepeatConstraint.RepeatConstraintUnitTest import RepeatConstraintUnitTest
from StochasticPackageQuery.Constraints.PackageSizeConstraint.PackageSizeConstraintUnitTest import PackageSizeConstraintUnitTest
from StochasticPackageQuery.Constraints.DeterministicConstraint.DeterministicConstraintUnitTest import DeterministicConstraintUnitTest
from StochasticPackageQuery.Constraints.ExpectedSumConstraint.ExpectedSumConstraintUnitTest import ExpectedSumConstraintUnitTest
from StochasticPackageQuery.Constraints.VaRConstraint.VaRConstraintUnitTest import VaRConstraintUnitTest
from StochasticPackageQuery.Constraints.CVaRConstraint.CVaRConstraintUnitTest import CVaRConstraintUnitTest
from StochasticPackageQuery.Objective.ObjectiveUnitTest import ObjectiveUnitTest
from StochasticPackageQuery.QueryUnitTest import QueryUnitTest
from StochasticPackageQuery.Parser.ParserUnitTest import ParserUnitTest
from StochasticPackageQuery.Parser.State.StateUnitTest import StateUnitTest
from StochasticPackageQuery.Parser.Transition.TransitionUnitTest import TransitionUnitTest
from Utils.HeapUnitTest import HeapUnitTest
from Utils.UtilsUnitTest import UtilsUnitTest
from ValueGenerator.ValueGeneratorUnitTest import ValueGeneratorUnitTest


def UnitTestRunner():
    print('Running all unit tests...')
    tests = [
        ('RepeatConstraintUnitTest', RepeatConstraintUnitTest),
        ('PackageSizeConstraintUnitTest', PackageSizeConstraintUnitTest),
        ('DeterministicConstraintUnitTest', DeterministicConstraintUnitTest),
        ('ExpectedSumConstraintUnitTest', ExpectedSumConstraintUnitTest),
        ('VaRConstraintUnitTest', VaRConstraintUnitTest),
        ('CVaRConstraintUnitTest', CVaRConstraintUnitTest),
        ('ObjectiveUnitTest', ObjectiveUnitTest),
        ('ConstraintUnitTest', ConstraintUnitTest),
        ('UtilsUnitTest', UtilsUnitTest),
        ('QueryUnitTest', QueryUnitTest),
        ('TransitionUnitTest', TransitionUnitTest),
        ('StateUnitTest', StateUnitTest),
        ('ParserUnitTest', ParserUnitTest),
        ('PgConnectionUnitTest', PgConnectionUnitTest),
        ('ScenarioGeneratorUnitTest', ScenarioGeneratorUnitTest),
        ('PriceScenarioGeneratorUnitTest', PriceScenarioGeneratorUnitTest),
        ('QuantityScenarioGeneratorUnitTest', QuantityScenarioGeneratorUnitTest),
        ('GainScenarioGeneratorUnitTest', GainScenarioGeneratorUnitTest),
        ('ValueGeneratorUnitTest', ValueGeneratorUnitTest),
        ('MeanAbsoluteDistanceUnitTest', MeanAbsoluteDistanceUnitTest),
        ('PivotScanUnitTest', PivotScanUnitTest),
        ('HeapUnitTest', HeapUnitTest),
    ]
    for idx, (name, test_cls) in enumerate(tests, 1):
        print(f'Running test {idx}/{len(tests)}: {name}...')
        test_cls().main()
        print(f'{name} passed.')
    print('All unit tests passed')

if __name__ == "__main__":
    UnitTestRunner()