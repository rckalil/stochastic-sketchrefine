using Random: MersenneTwister
using SamplingRB
using CSV
using DataFrames

function get_actions(path)
    println("Getting source")
    data = CSV.read(path, DataFrame)
    return data
end

function simulate(actions, n_sim)
    println("Actions")

end

function call_optimizer(relative_losses, alpha=0.9)
    println("Optimize")
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