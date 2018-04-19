# Python

**GaussianSim.ipynb** is the Python version of the Listeria monocytogenes cell-cell spread simulation described in the **Listeria_spread_simulations** repository, reproduced here: "simulation of Listeria spread where the size of the hop is sampled from a Normal distribution with mean = 0 and std = sqrt(2Dt)."

Update on 4/13/18: generation of Normal random numbers was Cythonized. Running the simulation up to 1e6 bacteria was speeded up from ~7 seconds to ~1.7 seconds. The code also measures the area of the convex hull of the bacterial focus.

Update 4/15/18: you can run the simulation more than once by setting N to an integer. The simulation will be run N times and the circularity of the bacterial focus will be averaged. The array bactposData will store the bacterial positions for each of the runs, which allows you to visualize the data for any of the individual runs.

Update 4/18/18: you can now measure the second moment, i.e. the average r^2, of the bacteria as a function of time. The slope of this line should equal 4D, which can be used as a sanity check (to make sure it equals to the original diffusion coefficient). There is also the chance to extract the growth rate from the exponential graph of the number of bacteria, which should equal the original input replicate rate k.
