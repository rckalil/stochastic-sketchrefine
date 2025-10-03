from scenario_generation_demo import gen_scenarios
from CVaRification.CVaRification import CVaRification
from CVaRification.StaircaseCVaRification import StaircaseCVaRification
from CVaRification.RCLSolve import RCLSolve
from DbInfo.PortfolioInfo import PortfolioInfo
from DbInfo.TpchInfo import TpchInfo
from Hyperparameters.Hyperparameters import Hyperparameters
from Naive.Naive import Naive
from SummarySearch.SummarySearch import SummarySearch
from OfflinePreprocessing.DistPartition import DistPartition
from PgConnection.PgConnection import PgConnection
from QueryHardness.HardnessEvaluator import HardnessEvaluator
from QueryHardness.RCLSolveBasedHardness import RCLSolveBasedHardness
from ScenarioGenerator.PorfolioScenarioGenerator.GainScenarioGenerator import GainScenarioGenerator
from ScenarioGenerator.RepresentativeScenarioGenerator.RepresentativeScenarioGenerator import RepresentativeScenarioGenerator
from ScenarioGenerator.RepresentativeScenarioGenerator.RepresentativeScenarioGeneratorWithoutCorrelation import RepresentativeScenarioGeneratorWithoutCorrelation
from ScenarioGenerator.TpchScenarioGenerators.PriceScenarioGenerator import PriceScenarioGenerator
from SeedManager.SeedManager import SeedManager
from SketchRefine.Sketch import Sketch
from SketchRefine.SketchRefine import SketchRefine
from OfflinePreprocessing.MonotonicDequeUnitTest import MonotonicDequeUnitTest
from OfflinePreprocessing.OptimalPartitioningUnitTest import OptimalPartitioningUnitTest
from StochasticPackageQuery.Parser.Parser import Parser
from Utils.Stochasticity import Stochasticity
from Utils.Relation_Prefixes import Relation_Prefixes
from UnitTestRunner import UnitTestRunner
from ValueGenerator.ValueGenerator import ValueGenerator
from Validator.Validator import Validator
import warnings
import time
import os
import numpy as np

if __name__ == '__main__':

    query = """
        SELECT PACKAGE(*) AS P
        FROM Stock_Investments_Half
        SUCH THAT
        SUM(Price) <= 500 AND
        SUM(Gain) >= %s WITH PROBABILITY >= 0.95
        MAXIMIZE EXPECTED SUM(Gain)
    """

    for gain_threshold in [300, 325, 350, 375, 400]:
        print('Gain threshold:', gain_threshold)
        query = query % gain_threshold
        print(query)


    # SeedManager.reinitialize_seed()
    # start_time = time.time()
    # summarySearch = SummarySearch(
    #     query=query, linear_relaxation=False,
    #     dbInfo=PortfolioInfo, init_no_of_scenarios=100,
    #     init_no_of_summaries=1,
    #     no_of_validation_scenarios=1000000,
    #     approximation_bound=0.02)
    # package, objective_value = summarySearch.solve()
    # summarySearch.display_package(package)
    # summarySearchMetrics = summarySearch.get_metrics()
    # print('Summary search took', time.time() - start_time, 'secs')
    # summarySearchMetrics.log()