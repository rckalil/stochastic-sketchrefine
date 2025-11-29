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
    S_t = zeros(d*m_time, n_sim)
    for i in 1:d
        for dt in 1:m_time
            sqrt_dt = sqrt(dt)
            mu_daily = actions[d, 3]
            sigma_daily = actions[d, 4]
            S0 = actions[d, 2]
            line = (i-1)*m_time + dt

            exponent_drift = (mu_daily - 0.5 * sigma_daily^2) * dt
            exponent_noise = sigma_daily * sqrt_dt * Z[line, :]
            loss  = S0 * exp.(exponent_drift .+ exponent_noise)
            S_t[line, :] = S0 .- loss
        end
    end

    return S_t

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
    pack = zeros(0, )
    for choice in 1:d

    end
end


function run()
    rng = MersenneTwister(1)

    println(rng)

    # Parameters
    d    = 3  # dimension
    nsim = 10 # Nb of simulations

    B = ones(d)
    alpha = 0.90
    relative_losses = randn(rng, d, nsim)
    println(length(relative_losses))

    status, w = cvar_rbp(B, alpha, relative_losses)

    println("Finished")
    println(status)
    # @assert status == 0
    println(w)
    # @assert isapprox(w, [0.2280, 0.2706, 0.5014]; atol=1e-4)

    println(2)
end