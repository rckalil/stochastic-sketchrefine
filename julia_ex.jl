using Random: MersenneTwister
using SamplingRB
using CSV
using DataFrames

function get_actions(path)
    println("Getting source")
    data = CSV.read(path, DataFrame)
    return data
end

function simulate(actions, n_sim, m_time)
    println("Actions")
    d = size(actions, 1)
    rng = MersenneTwister(123)
    Z = randn(rng, d*m_time, n_sim)
    loss = zeros(d*m_time, n_sim)
    for i in 1:d
        for dt in 1:m_time
            sqrt_dt = sqrt(dt)
            mu_daily = actions[d, 3]
            sigma_daily = actions[d, 4]
            S0 = actions[d, 2]
            line = (i-1)*m_time + dt

            exponent_drift = (mu_daily - 0.5 * sigma_daily^2) * dt
            exponent_noise = sigma_daily * sqrt_dt * Z[line, :]
            S_t  = S0 * exp.(exponent_drift .+ exponent_noise)
            loss[line, :] = S0 .- S_t
        end
    end

    return loss

end

function call_optimizer(relative_losses, alpha=0.9)
    println("Optimize")
    d = size(relative_losses, 1)
    B = ones(d)
    status, w = cvar_rbp(B, alpha, relative_losses)
    # println("Status")
    # println(status)
    # println("W")
    # println(w)
    return status, w
end

function get_int(w, factor)
    d = size(w, 1)
    w .*= factor
    q = zeros(d)
    for i in 1:d
        q[i] = floor(w[i])
    end
    return q
end

function package(q, actions, m_time)
    # println("Arroz")
    d = size(q, 1)
    pack = zeros(0, 8)
    # println("Botão")
    for choice in 1:d
        if q[choice] > 0
            # println("Cavalo")
            act = floor(Int, choice/m_time)
            time = choice - act*m_time + 1
            act += 1
            # println("Dia")

            # println(actions)
            # println(act, choice)
            identifier = actions[act, 5]
            ticker = actions[act, 1]
            # println("Estanho")
            sell_after = time
            price = actions[act, 2]
            volatility = actions[act, 4]
            volatility_coef = 1.0
            drift = actions[act, 3]
            quantity = q[choice]
            # println("Família")

            addition = [identifier, ticker, sell_after, price, volatility, volatility_coef, drift, quantity]
            addition = reshape(addition, 1, 8)
            pack = cat(pack, addition; dims=1)
            # println("Gerânio")
        end
    end
    return pack
end

function top(package, num)
    if num > size(package, 1)
        num = size(package, 1)
    end
    # print("Assadura")
    sorted_indices = sortperm(package[:, 4], rev=true)
    # println("Bocarra")
    sorted_package = package[sorted_indices, :]
    # println("Centeio")
    # println(sorted_package)
    top = sorted_package[1:num, :]
    # println("Doido")
    # println("Top ", num, " items sorted by column 4:")
    # println(top)
    return top
end


function run()
    start = time()
    path = "Data/portfolio.csv"
    n_sim = 10
    m_time = 7
    factor = 2831*m_time
    num = 10

    actions = get_actions(path)
    # actions = actions[1:10, :]
    relative_losses = simulate(actions, n_sim, m_time)
    println("Starting optimization")
    status, w = call_optimizer(relative_losses)
    if !status
        q = get_int(w, factor)
        pack = package(q, actions, m_time)
        final = top(pack, num)
        println("The package to be chosen is ")
        println(final)
    end
    finish = time()
    println("Total time: ")
    println(finish-start)
end

function time_exp()
    
    path = "Data/portfolio.csv"
    n_sim = 1000
    m_time = 7
    num = 10

    actions = get_actions(path)
    # actions = actions[1:10, :]
    assets = size(actions, 1)
    time_results = DataFrame(m_time = Int[], run_time = Float64[])
    package_cols = [
        "identifier", "ticker", "sell_after", "price", 
        "volatility", "volatility_coef", "drift", "quantity"
    ]
    package_results = DataFrame()
    factor = assets*m_time

    
    clock = []

    for i in 1:6
        m_time = i*5
        factor = assets*m_time
        relative_losses = simulate(actions, n_sim, m_time)
        println("Starting optimization")
        start = time()
        status, w = call_optimizer(relative_losses)
        finish = time()
        run_time = finish-start
        # println(run_time)
        push!(time_results, (m_time, run_time))
        if !status
            q = get_int(w, factor)
            pack = package(q, actions, m_time)
            final = top(pack, num)
            # println("The package to be chosen is ")
            # println(final)
            final_df = DataFrame(final, package_cols)
            insertcols!(final_df, 1, :m_time => m_time)
            
            if isempty(package_results)
                package_results = final_df
            else
                append!(package_results, final_df)
            end
        end
        # finish = time()
        
        # println("Total time: ")
        # println(run_time)
        clock = append!(clock, run_time)

        # --- Salvamento Final ---
    
        # 1. Salvar os tempos de execução
        time_output_path = "julia_times.csv"
        CSV.write(time_output_path, time_results)
        println("\nTempo de execução salvo em: $time_output_path")

        # 2. Salvar os pacotes escolhidos
        package_output_path = "julia_packages.csv"
        CSV.write(package_output_path, package_results)
        println("Pacotes escolhidos salvo em: $package_output_path")
    end
    # --- Salvamento Final ---
    
    # 1. Salvar os tempos de execução
    time_output_path = "julia_times.csv"
    CSV.write(time_output_path, time_results)
    println("\nTempo de execução salvo em: $time_output_path")

    # 2. Salvar os pacotes escolhidos
    package_output_path = "julia_packages.csv"
    CSV.write(package_output_path, package_results)
    println("Pacotes escolhidos salvo em: $package_output_path")
    
    println(clock)
    return time_results, package_results
end