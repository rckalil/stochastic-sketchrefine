from scenario_generation_demo import gen_scenarios
from CVaRification.RCLSolve import RCLSolve
from DbInfo.PortfolioInfo import PortfolioInfo
from SeedManager.SeedManager import SeedManager
from SketchRefine.SketchRefine import SketchRefine
from StochasticPackageQuery.Parser.Parser import Parser
from UnitTestRunner import UnitTestRunner
import time
import os
import numpy as np

if __name__ == '__main__':

    query_template = ["SELECT PACKAGE(*) AS P\n",
                      "FROM Stock_Quarterly\n",
                      "SUCH THAT\n",
                      "SUM(Price) <= 500 AND\n",
                      "LOG RISK BUDGET\n",
                      "MAXIMIZE EXPECTED SUM(Gain)"]
                    #   "LOG RISK BUDGET >= 0\n",

    SeedManager.reinitialize_seed()

    for gain_threshold in range(300, 350, 100):
        print("Berinjela")
        print('Gain threshold:', gain_threshold)
        # formatted_query = query_template[4] % str(gain_threshold)
        # print('Formatted query:', formatted_query)
        query_lines = query_template.copy()
        # query_lines[4] = formatted_query
        query = Parser().parse(query_lines)
        print('Parsed query:', query)
        print(query.get_objective())
        print(query.get_constraints())
        # break
        # package_dict, objective_value = SketchRefine(query, PortfolioInfo).solve()
        # print('Sketch package:', package_dict,
        #             'Objective value:', objective_value)

        start_time = time.time()
        rclsolve = RCLSolve(
            query=query, linear_relaxation=False,
            dbInfo=PortfolioInfo, init_no_of_scenarios=100,
            no_of_validation_scenarios=100,
            approximation_bound=0.02,
            sampling_tolerance=0.01,
            bisection_threshold=0.01)
        
        # rclsolve.__add_constraints_to_model
        # query.add_con
        
        package, objective_value = rclsolve.solve()
        # rclsolve.display_package(package)
        package_dict = rclsolve.get_results(package)
        rclsolveMetrics = rclsolve.get_metrics()
        rclsolveMetrics.log()
        end_time = time.time()
        
        if package_dict == None: break
        print("Done with: ", gain_threshold)
        with open("tr_rcl.txt", "a") as f:
            f.write(f"{gain_threshold},{end_time - start_time}\n")
            for line in package_dict: f.write(f"{line}\n")
            f.write(f"Objective value: {objective_value}\n")
        