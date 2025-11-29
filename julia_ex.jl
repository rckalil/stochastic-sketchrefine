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
    println("Status")
    println(status)
    println("W")
    println(w)
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
    d = size(q, 1)
    pack = zeros(0, 8)
    for choice in 1:d
        if q[choice] > 0
            act = floor(Int, choice/m_time)
            time = choice - act*m_time + 1

            # println(actions)
            identifier = actions[act, 5]
            ticker = actions[act, 1]
            sell_after = time
            price = actions[act, 2]
            volatility = actions[act, 4]
            volatility_coef = 1.0
            drift = actions[act, 3]
            quantity = q[choice]

            addition = [identifier, ticker, sell_after, price, volatility, volatility_coef, drift, quantity]
            addition = reshape(addition, 1, 8)
            pack = cat(pack, addition; dims=1)
        end
    end
    return pack
end

function top(package, num)
    sorted_indices = sortperm(package[:, 4], rev=true)
    sorted_package = package[sorted_indices, :]
    top = sorted_package[1:num, :]
    println("Top ", num, " items sorted by column 4:")
    println(top)
    return top
end


function run()
    path = "Data/portfolio.csv"
    n_sim = 10
    m_time = 7
    factor = 2831*m_time
    num = 20

    actions = get_actions(path)
    relative_losses = simulate(actions, n_sim, m_time)
    status, w = call_optimizer(relative_losses)
    if !status
        q = get_int(w, factor)
        package = package(q, actions, m_time)
        top = top(package, num)
        println("The package to be chosen is ")
        println(top)
    end
end