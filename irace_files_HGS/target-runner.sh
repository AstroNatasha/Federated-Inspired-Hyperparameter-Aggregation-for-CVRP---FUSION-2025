#!/bin/sh

# Check that we have at least 4 arguments
if [ "$#" -lt 4 ]; then
  echo "Error: Not enough arguments" >&2
  exit 1
fi

# Extract the instance path from the arguments
INSTANCE="$4"

# Shift the first 4 arguments (the ones irace uses for internal purposes)
shift 4

# The remaining arguments are the parameters
PARAMS="$@"

# For debugging purposes (optional)
# echo "INSTANCE: $INSTANCE" >&2
# echo "PARAMS: $PARAMS" >&2

# Run your program with the given parameters
#COMMAND="./bin/main "$INSTANCE" $PARAMS"
COMMAND="../build/hgs "$INSTANCE" mySolution.sol -log 0 -t 20 $PARAMS"

# # Construct the command to run your C++ program
# COMMAND="./bin/main Instances/ $maxIterILS $maxStart $maxPertubation $maxEliteSetSize $deltaPct"
# COMMAND="./target-runner.sh $INSTANCE --max_iter_ils $maxIterILS --max_start $maxStart --max_perturb $maxPertubation --max_elite $maxEliteSetSize --delta_pct $deltaPct"

# Run the command and capture the output
OUTPUT=$($COMMAND)

# Extract the performance measure from the output
# Assuming your program outputs a single numeric value
PERFORMANCE=$OUTPUT

# Print the performance measure (irace expects a single numeric value)
echo "$PERFORMANCE"
