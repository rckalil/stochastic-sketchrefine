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
import pandas as pd

def reform(data_list: list, days, sc, filepath: str = "results"):
    # print(data_list)
    # Colunas para os detalhes (7 colunas) + o peso final (1 coluna)
    cols = ["ID", "Ticker", "Sell_After", "Price", "Volatility", "Vol_Coeff", "Drift", "Objective_Value"]

    # 2. Achatar e extrair dados
    # Achatamos a estrutura (detalhes_tuple, valor) em uma única lista de listas/tuplas
    flat_data = []
    for details_tuple, value in data_list:
        # Cria uma linha única: [ID, Ticker, ..., Drift, Objective_Value]
        row = list(details_tuple) + [value]
        flat_data.append(row)

    # 3. Criar o DataFrame
    df = pd.DataFrame(flat_data, columns=cols)


    # Manipular
    total_sum = df['Objective_Value'].sum()
    df['Objective_Value'] = df['Objective_Value'] / total_sum
    df['Objective_Value'] = df['Objective_Value'] * 50
    df = df.sort_values(by=['Objective_Value'], ascending=False)

    # print(df)
    df = df.head(10)

    # 4. Salvar em CSV
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    filename = os.path.join(filepath, f'spaql_{days}_{sc}.csv')
    df.to_csv(filename, index=False)
    
    print("\n--- Exportação Concluída ---")
    print(f"DataFrame criado com {len(df)} linhas.")
    print(f"Salvo em: {filename}")
    
    return df

if __name__ == '__main__':

    query_template = ["SELECT PACKAGE(*) AS P\n",
                      "FROM Stock_Investments_%s\n",
                      "SUCH THAT\n",
                    #   "SUM(Price) <= 500 AND\n",
                      "LOG RISK BUDGET\n",
                      "MAXIMIZE CVAR SUM(Gain)"]
                    #   "MAXIMIZE EXPECTED SUM(Gain)"

    SeedManager.reinitialize_seed()

    for days in range(5, 11, 5):
        for sc in range(1000, 2001, 1000):
            # print("Berinjela")
            print('Hold assets up to ', days, " days.")
            formatted_query = query_template[1] % str(days)
            # print('Formatted query:', formatted_query)
            query_lines = query_template.copy()
            query_lines[1] = formatted_query
            query = Parser().parse(query_lines)
            # print('Parsed query:', query)
            print(query.get_objective())
            print(query.get_constraints())
            # sc = 500 * days  # number of scenarios
            # break
            # package_dict, objective_value = SketchRefine(query, PortfolioInfo).solve()
            # print('Sketch package:', package_dict,
            #             'Objective value:', objective_value)

            start_time = time.time()
            rclsolve = RCLSolve(
                query=query, linear_relaxation=True,
                dbInfo=PortfolioInfo, init_no_of_scenarios=sc,
                no_of_validation_scenarios=5000,
                approximation_bound=0.02,
                sampling_tolerance=0.001,
                bisection_threshold=0.001)
            
            # rclsolve.__add_constraints_to_model
            # query.add_con
            
            package, objective_value = rclsolve.solve()
            # rclsolve.display_package(package)
            package_dict = rclsolve.get_results(package)
            rclsolveMetrics = rclsolve.get_metrics()
            rclsolveMetrics.log()
            end_time = time.time()

            top = reform(package_dict, days, sc)
            
            if package_dict == None:
                with open("spaql_times.txt", "a") as f:
                    f.write(f"{days},{end_time - start_time},{sc}\n")
                    # f.write(f"Objective value: None\n")
                break
            print("Done with: ", days)
            with open("spaql_times.txt", "a") as f:
                f.write(f"{days},{end_time - start_time},{sc}\n")
                # for line in package_dict: f.write(f"{line}\n")
                # f.write(f"Objective value: {objective_value}\n")
