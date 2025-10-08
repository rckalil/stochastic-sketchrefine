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
                      "FROM %s\n",
                      "SUCH THAT\n",
                      "SUM(Price) <= 500 AND\n",
                      "SUM(Gain) >= 350 WITH PROBABILITY >= 0.97\n",
                      "MAXIMIZE EXPECTED SUM(Gain)"]

    SeedManager.reinitialize_seed()

    tables = [
        'stock_investments_5',
        'stock_investments_1'
    ]


    dbInfo = PortfolioInfo
    # open("partition_times.txt", "w").write(
    #     "table,no_of_partitions,time\n"
    # )

    for table in tables:
        preprocessing_time = 0
        query_time = 0
        times = 10
        for i in range(10):
            print('Partitioning', table)
            start_time = time.time()
            relation = table
            
        
            partitioner = DistPartition(
                dbInfo=dbInfo,
                relation=relation
            )
            
            partitioner.partition_relation()
            partitioner.get_metrics().log_performance()
            end_time = time.time()
            preprocessing_time += end_time - start_time

            print(
                f"O pré-processamento de {table} levou {preprocessing_time}\n"
            )

            print("Running query")

            formatted_query = query_template[1] % str(table)
            query_lines = query_template.copy()
            query_lines[1] = formatted_query

            print("Query: ", query_lines)
            start_time = time.time()
            query = Parser().parse(query_lines)
            # print('Parsed query:', query)
            summarySearch = SummarySearch(
                query=query, linear_relaxation=False,
                dbInfo=PortfolioInfo, init_no_of_scenarios=100,
                init_no_of_summaries=1,
                no_of_validation_scenarios=100,
                approximation_bound=0.02)
            # print("Nabo")
            package, objective_value = summarySearch.solve()
            summarySearch.display_package(package)
            resultado = summarySearch.get_results(package)
            summarySearchMetrics = summarySearch.get_metrics()
            # print('Summary search took', time.time() - start_time, 'secs')
            summarySearchMetrics.log()
            # print('-----------------------------------')
            end_time = time.time()
            # print('Total time for gain threshold', gain_threshold, 'is', end_time - start_time, 'secs')
            # print('===================================')
            query_time += end_time - start_time

        #Quantidade de linhas
        conn = PgConnection()
        conn.Execute(f"SELECT COUNT(*) FROM {table};")
        row_count = conn.Fetch()[0][0]
        print(f"Table {table} has {row_count} rows.")
        
        with open("processamento.txt", "a") as f:
            f.write(f"{table},{preprocessing_time/10},{query_time/10},{(query_time+preprocessing_time)/10},{row_count}\n")





    