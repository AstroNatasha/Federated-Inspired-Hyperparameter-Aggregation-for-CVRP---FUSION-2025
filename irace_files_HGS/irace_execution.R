# Start R and load irace
library(irace)

# Define the scenario with the suggested changes
scenario <- list(
  targetRunner = "target-runner.sh",    # The script that runs your C++ program
  targetEvaluator = NULL,               # No custom evaluator script
  maxExperiments = 100,                 # Total budget for experiments
  instances = readLines("instances.txt"),  # Read instances from the file
  logFile = "irace.log",                # Log file to record irace activity
  seed = 1234,                          # Seed for reproducibility
  parameterFile = "parameters.txt",     # File defining parameters to tune
  #digits = 3,                           # Precision for numerical parameters
  firstTest = 5,                        # Number of evaluations in the first iteration
  minNbSurvival = 1                     # Allow irace to proceed with fewer configurations
  # nbIterations = 5,                   # Optional: Set the number of iterations
  # parallel = 4,                       # Number of parallel runs
)

# Confirm 'scenario' is defined
print(scenario)

# Run irace
irace(scenario = scenario)

# # Load the irace results
# load("irace.Rdata")

# # Get the best configurations
# best_configs <- iraceResults$allConfigurations[iraceResults$allConfigurations$eliminated == 0, ]

# # Print the best configurations
# print(best_configs)

