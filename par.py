from scenario_generation_demo import gen_scenarios, Args, gen_prices, gen_gains
from multiprocessing import Process
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
import multiprocessing as mp

if __name__ == '__main__':

      package_dict = [((94682, 'LST', 1.0, 63.75, 0.00030121810855855924, 1.0, 0.02181150179219391), 2.0), ((94682, 'LST', 2.0, 63.75, 0.00030121810855855924, 1.0, 0.02181150179219391), 2.0)]
      info = [i[0] for i in package_dict]
      print(info)
      start_time = time.time()
      gain = GainScenarioGenerator(relation='Stock_Investments_10',
            base_predicate='')
      result = gain.generate_scenarios(
            seed=1204567,
            no_of_scenarios=1000,
            info=info
      )
      result = [r[0] for r in result]
      print(result)
      print('Time taken to generate 1 million scenarios of gain from 20 thousand tuples:',
            round(time.time() - start_time, 2))

      print("""
            
            
            """)
      print(result)