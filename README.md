# RiskAndReward

Evolving individuals (in the form of trees) to asses offers.

Main Ideas:

Individual "Brains"
- Individuals are represented as trees
- These trees consist of nodes that refer to functions
- Individuals "think" by running the function in the root node first and following a path to a leaf
- An EA is implemented to generate individuals
- As is, functions will return _True_ or _False_
- The "thought" process will terminate with a negative answer if a function in the path returns False
- If the function referred to by the currently active node returns True, the next node in the path will be evaluated, or the process will end with an affirmative answer if the node is a leaf.

Fitness Evaluation
- The fitness of an individual is evalutated by running a series of trials
- A trial entails an offer being made to the individual, with the relevant information being the cost, potential reward,
and probability of success
- On success, the reward is added to the individuals total
- On failure, the cost is subtracted from the individuals total
- A higher score = better fitness
- Recombination is done by selecting two parents (currently tournament selection), copying parent A, and (potentially) inserting
a branch from parent B at a randomly selected point

Evolving Functions
- Evolving the functions themselves, which effectively means multilayered evolutionary computation whereby functions are evolved
and subsequently used as building blocks for individuals
- The fitness of functions can be evaluated by counting the number of times they bare present in (relatively) fit individuals, and the count can be added to their weight when selecitng functions from the pool for reproduction
