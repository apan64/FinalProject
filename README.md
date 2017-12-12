# Using the Quine-McCluskey Algorithm to Algorithmically Generate Combinational Logic Circuits
Andrew Pan, Jonah Spear

### Background
The Quine-McCluskey Algorithm is a deterministic method for creating boolean functions for arbitrary combinational nets. We created an implementation of the Quine-McCluskey Algorithm and used it to generate circuits for modules we have have previously designed by hand, specifically the 4-bit ALU. We then present comparison data on our algorithmically generated design with the hand-generated designs, specifically comparing them based on metrics of latency and area. 

### Implementation
The Quine-McCluskey Algorithm has two major parts. The first finding the prime implicants of a given logical function, and the second is finding the minimum amount of these prime implicants needed to cover all output conditions. The code for these lives in src/findPrimeImplicants.py and src/tabulation.py respectively. These were both hefty chunks of code and getting them to work correctly took a vast majority of our time. We also had to extend this code to work for circuits with multiple outputs, which added an additional layer of complexity to the codebase.

### Results
Ultimately we were successful in creating an architecture that could synthesize combinational circuits given a description of the input. The comparison charts for our circuits is shown below:

# insert comparison chart here.

# insert discussion of results here
