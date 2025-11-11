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

    query_template = ["SELECT PACKAGE(*) AS P\n",
                      "FROM Stock_Investments_10\n",
                      "SUCH THAT\n",
                      "SUM(Price) <= 500 AND\n",
                      "SUM(Gain) >= %s WITH PROBABILITY >= 0.97\n",
                      "MAXIMIZE EXPECTED SUM(Gain)"]

    SeedManager.reinitialize_seed()
    # print("Arroz")

    for gain_threshold in range(-100, 650, 100):
        print("Berinjela")
        print('Gain threshold:', gain_threshold)
        formatted_query = query_template[4] % str(gain_threshold)
        print('Formatted query:', formatted_query)
        query_lines = query_template.copy()
        query_lines[4] = formatted_query
        query = Parser().parse(query_lines)
        print('Parsed query:', query)

        start_time = time.time()
        rclsolve = RCLSolve(
            query=query, linear_relaxation=False,
            dbInfo=PortfolioInfo, init_no_of_scenarios=100,
            no_of_validation_scenarios=100,
            approximation_bound=0.02,
            sampling_tolerance=0.01,
            bisection_threshold=0.01)
        
        package, objective_value = rclsolve.solve()
        rclsolve.display_package(package)
        package_dict = rclsolve.get_results(package) # each asset option has id, ticker, sell_after?, gain, ...
        rclsolveMetrics = rclsolve.get_metrics()
        rclsolveMetrics.log()
        # info = [i[0] for i in package_dict]
        # print(info)
        # gain = GainScenarioGenerator(relation='Stock_Investments_10',
        #         base_predicate='')
        # result = gain.generate_scenarios(
        #         seed=1204567,
        #         no_of_scenarios=1000,
        #         info=info
        #     )
        # result = [r[0] for r in result]
        end_time = time.time()
        # print(len(result))
        with open("tr_rcl.txt", "a") as f:
            f.write(f"{gain_threshold},{end_time - start_time}\n")
            for line in package_dict: f.write(f"{line}\n")
            f.write(f"Objective value: {objective_value}\n")
        