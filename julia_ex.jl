using Random: MersenneTwister
using SamplingRB

rng = MersenneTwister(1)

# Parameters
d    = 3  # dimension
nsim = 10 # Nb of simulations

B = ones(d)
alpha = 0.90
relative_losses = randn(rng, d, nsim)

status, w = cvar_rbp(B, alpha, relative_losses)

println("Finished")
@assert status == 0
println(w)
@assert isapprox(w, [0.2280, 0.2706, 0.5014]; atol=1e-4)

println(2)