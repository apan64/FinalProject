# Using the Quine-McCluskey Algorithm to Algorithmically Generate Combinational Logic Circuits
Andrew Pan, Jonah Spear

### Background
The Quine-McCluskey Algorithm is a deterministic method for creating boolean functions for arbitrary combinational nets. We created an implementation of the Quine-McCluskey Algorithm and used it to generate circuits for modules we have have previously designed by hand, specifically an adder and ALU. We then present comparison data on our algorithmically generated design with the hand-generated designs, specifically comparing them based on metrics of latency and area. 

### Project Goals
We chose to explore the area of logic synthesis because the subject seemed both challenging and useful as a whole.  Many of the circuits we had experience designing were created without any particular desire for optimization, instead focusing on whether or not the end result would simply be correct.  Additionally, both of us were very interested in the ability to computationally solve nontrivial problems across various fields with the ability to optimize solutions for certain parameters.  We hoped to create a program that would be able to synthesize a circuit layout based solely on the inputs and outputs of a module and analyze the effectiveness of our generated circuit in comparison to the circuits we spent significant portions of time designing in class and for projects.  

### Implementation
The Quine-McCluskey Algorithm has two major parts. The first finding the prime implicants of a given logical function, and the second is finding the minimum amount of these prime implicants needed to cover all output conditions. The code for these lives in src/findPrimeImplicants.py and src/tabulation.py respectively. These were both hefty chunks of code and getting them to work correctly took the vast majority of our time. We also had to extend this code to work for circuits with multiple outputs, which added an additional layer of complexity to the codebase.

### Results
Ultimately we were successful in creating an architecture that could synthesize combinational circuits given a description of the input. The comparison charts for our circuits is shown below:

1-Bit Adder(Computer Generated): Area: 33, Latency: 5

1-Bit Adder(Hand Generated): Area: 29, Latency 7

1-Bit ALU (Computer Generated): 

1-Bit ALU (Hand Generated): Area: 146, Latency 21


Suprisingly, the algorithmically generated ALU was much faster than the hand-drawn one. 

### Documentation
Our synthesis code can be run from the synthesizeMultipleOutput() function in the file src/synthesize.py.  The function takes two arguments, a list containing lists of the minimum terms for each output based on the inputs, and the number of total inputs.  Throughout our code, we use data structures and functions from the collections and itertools libraries.  

A major difficulty for our project was properly understanding and translating the Quine-McCluskey Algorithm into a program because some of the decisions that had to be made across the various steps of the algorithm were difficult to reach conclusions on without iterating through all possible combinations.  We also had to spend time debugging our program because the segments of the Quine-McCluskey Algorithm were large to begin with and difficult to split into reasonably sized unit tests.  

Overall, we were very satisfied with the scope of the work that we accomplished, and our ability to mostly stick to our work plan.  Our work plan ensured that we had properly planned out various components of our project before even beginning to write any code, and our time estimates for the various sections of the project were not too far off from the actual alloted time spent.

Looking forward, we would like to further optimize the efficiency and run-time of our code so that we are properly able to synthesize a complex circuit within a reasonable amount of time, and possibly introduce clock-based components into our logic synthesis as well.