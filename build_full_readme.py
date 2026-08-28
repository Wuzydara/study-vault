#!/usr/bin/env python3
"""
Generates README.md with full VR24 syllabus content AND clickable folder links.
"""

import os

# ---------------------------------------------------------------------
# UNIT_DATA – full unit descriptions per subject (kept intact)
# ---------------------------------------------------------------------
UNIT_DATA = {

    # ---- 1-1 ----
    "MA": [
        {"title": "Matrices", "desc": "Rank of a matrix by Echelon form and Normal form. Inverse of Non-singular matrices by Gauss-Jordan method. System of linear equations: solving Homogeneous and Non-Homogeneous equations by Gauss elimination and Gauss Seidel Iteration Method."},
        {"title": "Eigen values and Eigen vectors", "desc": "Linear Transformation and Orthogonal Transformation. Eigen values, Eigenvectors and their properties. Diagonalization of a matrix. Cayley-Hamilton Theorem (without proof), finding inverse and power of a matrix. Quadratic forms and Nature of the Quadratic Forms, Reduction of Quadratic form to canonical forms by Orthogonal Transformation."},
        {"title": "Calculus", "desc": "Mean value theorems: Rolle's theorem, Lagrange's Mean value theorem with their Geometrical Interpretation and applications, Cauchy's Mean value Theorem, Taylor's Series. Applications of definite integrals to evaluate surface areas and volumes of revolutions of curves (Only in Cartesian coordinates), Definition of Improper Integral: Beta and Gamma functions and their applications."},
        {"title": "Multivariable Calculus (Partial Differentiation and applications)", "desc": "Definitions of Limit and continuity. Partial Differentiation: Euler's Theorem, Total derivative, Jacobian, Functional dependence & independence. Applications: Maxima and minima of functions of two variables and three variables using method of Lagrange multipliers."},
        {"title": "Multivariable Calculus (Integration)", "desc": "Evaluation of Double Integrals (Cartesian and polar coordinates), change of order of integration (only Cartesian form), Evaluation of Triple Integrals: Change of variables (Cartesian to polar) for double and (Cartesian to Spherical and Cylindrical polar coordinates) for triple integrals. Applications: Areas (by double integrals) and volumes (by double integrals and triple integrals)."}
    ],
    "Chemistry": [
        {"title": "Water and its treatment", "desc": "Introduction to hardness of water - Estimation of hardness of water by complex metric method and related numerical problems. Potable water and its specifications - Steps involved in the treatment of potable water - Disinfection of potable water by chlorination and break-point chlorination. Defluoridation - Determination of F- ion by ion-selective electrode method. Boiler troubles: Sludges, Scales and Caustic embrittlement. Internal treatment of Boiler feed water - Calgon conditioning - Phosphate conditioning - Colloidal conditioning, External treatment methods - Softening of water by ion-exchange processes. Desalination of water - Reverse osmosis."},
        {"title": "Battery Chemistry & Corrosion", "desc": "Introduction - Classification of batteries- primary, secondary and reserve batteries with examples. Basic requirements for commercial batteries. Construction, working and applications of: Zn-air and Lithium ion battery, Applications of Li-ion battery to electrical vehicles. Fuel Cells- Differences between battery and a fuel cell, Construction and applications of Methanol Oxygen fuel cell and Solid oxide fuel cell. Solar cells - Introduction and applications of Solar cells. Corrosion: Causes and effects of corrosion - theories of chemical and electrochemical corrosion - mechanism of electrochemical corrosion, Types of corrosion: Galvanic, waterline and pitting corrosion. Factors affecting rate of corrosion, Corrosion control methods- Cathodic protection - Sacrificial anode and impressed current methods."},
        {"title": "Polymeric materials", "desc": "Definition - Classification of polymers with examples - Types of polymerization - addition (free radical addition) and condensation polymerization with examples - Nylon 6:6, Terylene. Plastics: Definition and characteristics- thermoplastic and thermosetting plastics, Preparation, Properties and engineering applications of PVC and Bakelite, Teflon, Fiber reinforced plastics (FRP). Rubbers: Natural rubber and its vulcanization. Elastomers: Characteristics - preparation - properties and applications of Buna-S, Butyl and Thiokol rubber. Conducting polymers: Characteristics and Classification with examples- mechanism of conduction in trans-poly acetylene and applications of conducting polymers. Biodegradable polymers: Concept and advantages - Polylactic acid and poly vinyl alcohol and their applications."},
        {"title": "Energy Sources", "desc": "Introduction, Calorific value of fuel - HCV, LCV- Dulongs formula. Classification- solid fuels: coal - analysis of coal - proximate and ultimate analysis and their significance. Liquid fuels - petroleum and its refining, cracking types - moving bed catalytic cracking. Knocking - octane and cetane rating, synthetic petrol - Fischer-Tropsch's process; Gaseous fuels - composition and uses of natural gas, LPG and CNG, Biodiesel - Transesterification, advantages."},
        {"title": "Engineering Materials", "desc": "Cement: Portland cement, its composition, setting and hardening. Smart materials and their engineering applications. Shape memory materials- Poly L-Lactic acid. Thermo response materials- Polyacryl amides, Poly vinyl amides. Lubricants: Classification of lubricants with examples- characteristics of a good lubricants - mechanism of lubrication (thick film, thin film and extreme pressure)- properties of lubricants: viscosity, cloud point, pour point, flash point and fire point."}
    ],
    "PPS": [
        {"title": "Introduction to Programming", "desc": "Compilers, compiling and executing a program. Representation of Algorithm - Algorithms for finding roots of a quadratic equations, finding minimum and maximum numbers of a given set, finding if a number is prime number Flowchart/Pseudocode with examples, Program design and structured programming. Introduction to C Programming Language: variables (with data types and space requirements), Syntax and Logical Errors in compilation, object and executable code, Operators, expressions and precedence, Expression evaluation, Storage classes (auto, extern, static and register), type conversion, The main method and command line arguments. Bitwise operations: Bitwise AND, OR, XOR and NOT operators. Conditional Branching and Loops: Writing and evaluation of conditionals and consequent branching with if, if-else, switch-case, ternary operator, goto, Iteration with for, while, do-while loops. I/O: Simple input and output with scanf and printf, formatted I/O, Introduction to stdin, stdout and stderr. Command line arguments."},
        {"title": "Arrays, Strings, Structures and Pointers", "desc": "Arrays: one and two dimensional arrays, creating, accessing and manipulating elements of arrays. Strings: Introduction to strings, handling strings as array of characters, basic string functions available in C (strlen, strcat, strcpy, strstr etc.), arrays of strings. Structures: Defining structures, initializing structures, unions, Array of structures. Pointers: Idea of pointers, Defining pointers, Pointers to Arrays and Structures, Use of Pointers in self-referential structures, usage of self-referential structures in linked list (no implementation). Enumeration data type."},
        {"title": "Preprocessor and File handling in C", "desc": "Preprocessor: Commonly used Preprocessor commands like include, define, undef, if, ifdef, ifndef. Files: Text and Binary files, Creating and Reading and writing text and binary files, Appending data to existing files, Writing and reading structures using binary files, Random access using fseek, ftell and rewind functions."},
        {"title": "Function and Dynamic Memory Allocation", "desc": "Functions: Designing structured programs, Declaring a function, Signature of a function, Parameters and return type of a function, passing parameters to functions, call by value, Passing arrays to functions, passing pointers to functions, idea of call by reference, Some C standard functions and libraries. Recursion: Simple programs, such as Finding Factorial, Fibonacci series etc., Limitations of Recursive functions. Dynamic memory allocation: Allocating and freeing memory, Allocating memory for arrays of different data types."},
        {"title": "Searching and Sorting", "desc": "Basic searching in an array of elements (linear and binary search techniques), Basic algorithms to sort array of elements (Bubble, Insertion and Selection sort algorithms), Basic concept of order of complexity through the example programs."}
    ],
    "BEE": [
        {"title": "D.C. Circuits", "desc": "Electrical circuit elements (R, L and C), voltage and current sources, KVL&KCL, analysis of simple circuits with dc excitation. Superposition, Thevenin and Norton Theorems. Time-domain analysis of first-order RL and RC circuits."},
        {"title": "A.C. Circuits", "desc": "Representation of sinusoidal waveforms, peak and rms values, phasor representation, real power, reactive power, apparent power, power factor, Analysis of single-phase ac circuits consisting of R, L, C, RL, RC, RLC combinations (series and parallel), resonance in series R-L-C circuit. Three-phase balanced circuits, voltage and current relations in star and delta connections."},
        {"title": "Transformers", "desc": "Ideal and practical transformer, equivalent circuit, losses in transformers, regulation and efficiency. Auto-transformer and three-phase transformer connections."},
        {"title": "Electrical Machines", "desc": "Construction and working principle of dc machine, performance characteristics of dc shunt machine. Generation of rotating magnetic field, Construction and working of a three-phase induction motor, Significance of torque-slip characteristics. Single-phase induction motor, Construction and working. Construction and working of synchronous generator."},
        {"title": "Electrical Installations", "desc": "Components of LT Switchgear: Switch Fuse Unit (SFU), MCB, ELCB, MCCB, Types of Wires and Cables, Earthing. Types of Batteries, Important Characteristics for Batteries. Elementary calculations for energy consumption, power factor improvement and battery backup."}
    ],
    "CAEG": [
        {"title": "Introduction to Engineering Graphics", "desc": "Principles of Engineering Graphics and their Significance, Scales - Plain & Diagonal, Conic Sections including the Rectangular Hyperbola - General method only. Cycloid, Epicycloid and Hypocycloid, Introduction to Computer aided drafting - views, commands and conics."},
        {"title": "Orthographic Projections", "desc": "Principles of Orthographic Projections - Conventions - Projections of Points and Lines, Projections of Plane regular geometric figures. Auxiliary Planes. Computer aided orthographic projections - points, lines and planes."},
        {"title": "Projections of Regular Solids", "desc": "Auxiliary Views - Sections or Sectional views of Right Regular Solids - Prism, Cylinder, Pyramid, Cone - Auxiliary views, Computer aided projections of solids - sectional views."},
        {"title": "Development of Surfaces", "desc": "Development of Surfaces of Right Regular Solids: Prism, Cylinder, Pyramid and Cone, Development of surfaces using computer aided drafting."},
        {"title": "Isometric Projections", "desc": "Principles of Isometric Projection - Isometric Scale - Isometric Views - Conventions - Isometric Views of Lines, Plane Figures, Simple and Compound Solids - Isometric Projection of objects having non-isometric lines. Isometric Projection of Spherical Parts. Conversion of Isometric Views to Orthographic Views and Vice-versa - Conventions. Conversion of orthographic projection into isometric view using computer aided drafting."}
    ],
    "ECS": [
        {"title": "Basics of a Computer", "desc": "Hardware, Software, Generations of computers. Hardware- functional units, Components of CPU, Memory - hierarchy, types of memory, Input and output devices. Software- systems software, application software, packages, frame works, IDEs."},
        {"title": "Software Development", "desc": "Software development- water fall model, Agile, Types of computer languages- Programming, markup, scripting. Program Development- steps in program development, flowcharts, algorithms, data structures- definition, types of data structures."},
        {"title": "Operating Systems & DBMS", "desc": "Operating systems: Functions of operating systems, types of operating systems, Device & Resource management. Database Management Systems: Data models, RDBMS, SQL, Database Transactions, data centers, cloud services."},
        {"title": "Computer Networks & Web", "desc": "Computer Networks: Advantages of computer networks, LAN, WAN, MAN, internet, WiFi, sensor networks, vehicular networks, 5G communication. World Wide Web- Basics, role of HTML, CSS, XML, Tools for web designing, Social media, Online social networks. Security- information security, cyber security, cyber laws."},
        {"title": "Autonomous Systems", "desc": "Autonomous Systems: IoT, Robotics, Drones, Artificial Intelligence - Learning, Game Development, natural language processing, image and video processing."}
    ],

    # ---- 1-2 ----
    "ODE": [
        {"title": "First Order ODE", "desc": "Exact differential equations, integrating factors, linear equations, Bernoulli's equation."},
        {"title": "Higher Order ODE", "desc": "Homogeneous and non-homogeneous equations. Method of undetermined coefficients, variation of parameters."},
        {"title": "Laplace Transforms", "desc": "Definition, properties, inverse transforms. Applications to ODEs."},
        {"title": "Vector Differentiation", "desc": "Gradient, divergence, curl, vector identities."},
        {"title": "Vector Integration", "desc": "Line, surface, volume integrals. Green's theorem, Gauss divergence theorem, Stokes theorem (without proofs) – applications."}
    ],
    "Physics": [
        {"title": "Quantum Physics and Solids", "desc": "Quantum Mechanics: Introduction to quantum physics, blackbody radiation - Stefan-Boltzmann's law, Wein's and Rayleigh-Jean's law, Planck's radiation law - photoelectric effect - Davisson and Germer experiment - Heisenberg uncertainty principle - Born interpretation of the wave function - time independent Schrodinger wave equation - particle in one dimensional potential box. Solids: Symmetry in solids, free electron theory (Drude & Lorentz, Sommerfeld) - Fermi-Dirac distribution - Bloch's theorem - Kronig-Penney model - E-K diagram- effective mass of electron- origin of energy bands- classification of solids."},
        {"title": "Semiconductors and Devices", "desc": "Intrinsic and extrinsic semiconductors - Hall effect - direct and indirect band gap semiconductors - construction, principle of operation and characteristics of P-N Junction diode, Zener diode and bipolar junction transistor (BJT)- LED, PIN diode, avalanche photo diode (APD) and solar cells, their structure, materials, working principle and characteristics."},
        {"title": "Dielectric, Magnetic and Energy Materials", "desc": "Dielectric Materials: Basic definitions- types of polarizations (qualitative)- ferroelectric, piezoelectric, and pyroelectric materials - applications - liquid crystal displays (LCD) and crystal oscillators. Magnetic Materials: Hysteresis - soft and hard magnetic materials - magnetostriction, magnetoresistance - applications - bubble memory devices, magnetic field sensors and multiferroics. Energy Materials: Conductivity of liquid and solid electrolytes- superionic conductors - materials and electrolytes for super capacitors - rechargeable ion batteries, solid fuel cells."},
        {"title": "Nanotechnology", "desc": "Nanoscale, quantum confinement, surface to volume ratio, bottom-up fabrication: sol-gel, precipitation, combustion methods - top-down fabrication: ball milling - physical vapor deposition (PVD) - chemical vapor deposition (CVD) - characterization techniques - XRD, SEM & TEM - applications of nanomaterials."},
        {"title": "Laser and Fiber Optics", "desc": "Lasers: Laser beam characteristics- three quantum processes- Einstein coefficients and their relations- lasing action - pumping methods- ruby laser, He-Ne laser , CO2 laser, Argon ion Laser, Nd:YAG laser- semiconductor laser- applications of laser. Fiber Optics: Introduction to optical fiber- advantages of optical Fibers - total internal reflection- construction of optical fiber - acceptance angle - numerical aperture- classification of optical fibers- losses in optical fiber - optical fiber for communication system - applications."}
    ],
    "Workshop": [
        {"title": "Introduction to Workshop", "desc": "Study of different hand operated power tools, uses and their demonstration. Gain good basic working knowledge required for production of various engineering products. Hands on experience about use of different engineering materials, tools, equipment's and processes. Develop right attitude, team working, precision and safety at workplace. Construction, function, use and application of different working tools, equipment and machines."},
        {"title": "Carpentry", "desc": "Study commonly used carpentry joints. Trades: T-Lap Joint, Dovetail Joint, Mortise & Tenon Joint."},
        {"title": "Fitting and Tin-Smithy", "desc": "Fitting: V-Fit, Dovetail Fit & Semi-circular fit. Tin-Smithy: Square Tin, Rectangular Tray & Conical Funnel."},
        {"title": "Foundry and Welding", "desc": "Foundry: Preparation of Green Sand Mould using Single Piece and Split Pattern. Welding: Arc Welding & Gas Welding."},
        {"title": "House-wiring and Black Smithy", "desc": "House-wiring: Parallel & Series, Two-way Switch and Tube Light. Black Smithy: Round to Square, Fan Hook and S-Hook. Demonstration: Plumbing, Machine Shop, Metal Cutting (Water Plasma), Power tools in construction and Wood Working."}
    ],
    "English": [
        {"title": "Toasted English – R.K. Narayan", "desc": "Vocabulary: The Concept of Word Formation - The Use of Prefixes and Suffixes - Acquaintance with Prefixes and Suffixes from Foreign Languages to form Derivatives Synonyms and Antonyms. Grammar: Identifying Common Errors in Writing with Reference to Articles and Prepositions. Reading: Reading and Its Importance- Techniques for Effective Reading. Writing: Sentence Structures - Use of Phrases and Clauses in Sentences- Importance of Proper Punctuation- Techniques for Writing precisely - Paragraph Writing - Types, Structures and Features of a Paragraph - Creating Coherence- Organizing Principles of Paragraphs in Documents."},
        {"title": "Appro JR\"D\" – Sudha Murthy", "desc": "Vocabulary: Words Often Misspell - Homophones, Homonyms and Homographs. Grammar: Identifying Common Errors in Writing with Reference to Noun-pronoun Agreement and Subject-verb Agreement. Reading: Sub-Skills of Reading - Skimming and Scanning - Exercises for Practice."},
        {"title": "Lessons from Online Learning", "desc": "Vocabulary: Words Often Confused - Words from Foreign Languages and their Use in English. Grammar: Identifying Common Errors in Writing with Reference to Misplaced Modifiers and Tenses. Reading: Sub-Skills of Reading - Intensive Reading and Extensive Reading - Exercises for Practice. Writing: Format of a Formal Letter- Writing Formal Letters E.g., Letter of Complaint, Letter of Requisition, Email Etiquette, Job Application with CV/Resume."},
        {"title": "Art and Literature – Abdul Kalam", "desc": "Vocabulary: Standard Abbreviations in English. Grammar: Redundancies and Clichés in Oral and Written Communication. Reading: Survey, Question, Read, Recite and Review (SQ3R Method) - Exercises for Practice. Writing: Writing Practices- Essay Writing- Writing Introduction and Conclusion -Precis Writing."},
        {"title": "Go, Kiss the World – Subroto Bagchi", "desc": "Vocabulary: Technical Vocabulary and their Usage. Grammar: Common Errors in English (Covering all the other aspects of grammar which were not covered in the previous units). Reading: Reading Comprehension- Exercises for Practice. Writing: Technical Reports- Introduction - Characteristics of a Report - Categories of Reports Formats - Structure of Reports (Manuscript Format) - Types of Reports - Writing a Report."}
    ],
    "EDC": [
        {"title": "Diodes", "desc": "Diodes - Static and Dynamic resistances, Equivalent circuit, Diffusion and Transition Capacitances, V-I Characteristics, Diode as a switch- switching times."},
        {"title": "Diode Applications", "desc": "Rectifier - Half Wave Rectifier, Full Wave Rectifier, Bridge Rectifier, Rectifiers with Capacitive and Inductive Filters, Clippers- Clipping at two independent levels, Clamper- Clamping Circuit Theorem, Clamping Operation, Types of Clampers."},
        {"title": "Bipolar Junction Transistor (BJT)", "desc": "Principle of Operation, Common Emitter, Common Base and Common Collector Configurations, Transistor as a switch, switching times."},
        {"title": "Junction Field Effect Transistor (FET)", "desc": "Construction, Principle of Operation, Pinch-Off Voltage, Volt-Ampere Characteristic, Comparison of BJT and FET, FET as Voltage Variable Resistor, MOSFET, MOSTET as a capacitor."},
        {"title": "Special Purpose Devices", "desc": "Zener Diode - Characteristics, Zener diode as Voltage Regulator, Principle of Operation - SCR, Tunnel diode, UJT, Varactor Diode, Photo diode, Solar cell, LED, Schottky diode."}
    ],

    # ---- 2-1 ----
    "DE": [
        {"title": "Boolean Algebra and Logic Gates", "desc": "Digital Systems, Binary Numbers, Number base conversions, Octal and Hexadecimal Numbers, complements, Signed binary numbers, Binary codes, Binary Storage and Registers, Binary logic. Basic Definitions, Axiomatic definition of Boolean Algebra, Basic theorems and properties of Boolean algebra, Boolean functions, canonical and standard forms, other logic operations, Digital logic gates."},
        {"title": "Gate-Level Minimization", "desc": "The map method, Four- variable map, Five- Variable map, product of sums simplification Don't-care conditions, NAND and NOR implementation other Two-level implementations, Exclusive - Or function."},
        {"title": "Combinational Logic", "desc": "Combinational Circuits, Analysis procedure Design procedure, Binary Adder- Subtractor Decimal Adder, Binary multiplier, magnitude comparator, Decoders, Encoders, Multiplexers, HDL for combinational circuits."},
        {"title": "Sequential Logic", "desc": "Sequential circuits, latches, Flip-Flops Analysis of clocked sequential circuits, state Reduction and Assignment, Design Procedure. Registers, shift Registers, Ripple counters, synchronous counters, other counters."},
        {"title": "Memories and Asynchronous Sequential Logic", "desc": "Introduction, Random-Access Memory, Memory Decoding, Error Detection and correction. Read-only memory, Programmable logic Array programmable Array logic, Sequential Programmable Devices. Introduction, Analysis Procedure, Circuits with Latches, Design Procedure, Reduction of state and Flow Tables, Race-Free state Assignment Hazards, Design Example."}
    ],
    "DS": [
        {"title": "Introduction to Data Structures", "desc": "Introduction to Data Structures, abstract data types, Linear list - singly linked list implementation, insertion, deletion and searching operations on linear list."},
        {"title": "Stacks and Queues", "desc": "Stacks- Operations, array and linked representations of stacks, stack applications. Queues- operations, array and linked representations."},
        {"title": "Trees", "desc": "Binary Search Trees, Definition, Implementation, Operations- Searching, Insertion and Deletion. AVL Trees, Definition, Height of an AVL Tree, Operations - Insertion, Deletion and Searching. B-Trees, B+ Trees."},
        {"title": "Graphs", "desc": "Graphs: Graph Implementation Methods. Graph Traversal Methods. Sorting: Quick Sort, Heap Sort, External Sorting- Model for external sorting, Merge Sort."},
        {"title": "Hashing and Pattern Matching", "desc": "Hash Table Representation: hash functions, collision resolution- separate chaining, open addressing-linear probing, quadratic probing, double hashing, rehashing, extendible hashing. Pattern Matching: Brute force, Boyer-Moore, Knuth-Morris-Pratt."}
    ],
    "PnS": [
        {"title": "Probability", "desc": "Sample space, events, axioms of probability. Conditional probability, independence. Bayes' theorem."},
        {"title": "Random Variables", "desc": "Discrete and continuous random variables. Probability mass/density functions, cumulative distribution functions. Expectation, variance, moments. Joint distributions, covariance, correlation."},
        {"title": "Probability Distributions", "desc": "Binomial, Poisson, Normal, Exponential distributions – properties, applications. Central limit theorem."},
        {"title": "Statistical Inference", "desc": "Estimation – point and interval estimation. Testing of hypotheses – one-sample and two-sample tests for means and proportions. Chi-square test, F-test."},
        {"title": "Stochastic Processes and Markov Chains", "desc": "Introduction to stochastic processes. Markov process, transition probabilities, transition matrix. n-step transitions, Markov chain, steady state, Markov analysis."}
    ],
    "CO": [
        {"title": "Basic Structure of Computers", "desc": "Computer types, functional units, basic operational concepts. Bus structures, performance measures."},
        {"title": "Instruction Sets and Addressing Modes", "desc": "Machine instructions, instruction formats. Addressing modes – direct, indirect, register, indexed, etc. Program control – conditional branches, subroutines."},
        {"title": "Control Unit Design", "desc": "Hardwired control – design methods. Microprogrammed control – microinstructions, sequencing."},
        {"title": "Memory Organization", "desc": "Memory hierarchy, main memory, cache memory – mapping techniques. Virtual memory – paging, segmentation. Auxiliary memory."},
        {"title": "I/O Organization and Pipelining", "desc": "I/O interface, asynchronous data transfer, modes of transfer, interrupt, DMA. RISC vs CISC. Pipelining – arithmetic, instruction, RISC pipeline. Vector processing, array processors. Multiprocessors – characteristics, interconnection, arbitration, communication, cache coherence."}
    ],
    "Java": [
        {"title": "Introduction to Java", "desc": "History, features, JVM, bytecode. Data types, variables, operators, control statements. Arrays, strings. Classes and objects, constructors, this keyword, garbage collection."},
        {"title": "Inheritance and Polymorphism", "desc": "Inheritance – super, method overriding, final. Abstract classes, interfaces. Packages and access modifiers. Wrapper classes."},
        {"title": "Exception Handling and Multithreading", "desc": "Exception hierarchy, try-catch-finally, throw, throws, custom exceptions. Multithreading – thread lifecycle, creation, synchronization, inter-thread communication. Enumerations, autoboxing, generics, annotations."},
        {"title": "Event Handling and AWT", "desc": "Event delegation model – events, sources, listeners. Mouse/keyboard events, adapter classes. AWT components – labels, buttons, text components, checkboxes, choices, lists, panels, menus. Layout managers – Border, Grid, Flow, Card, GridBag."},
        {"title": "Applets and Swing", "desc": "Applet lifecycle, types, passing parameters. Swing – MVC architecture, components – JApplet, JFrame, JComponent, icons, labels, text fields, buttons, checkboxes, radio buttons, combo boxes, tabbed panes, scroll panes, trees, tables."}
    ],

    # ---- 2-2 ----
    "DM": [
        {"title": "Mathematical Logic", "desc": "Introduction, Statements and Notation, Connectives, Normal Forms, Theory of Inference for the Statement Calculus, The Predicate Calculus, Inference Theory of the Predicate Calculus."},
        {"title": "Set Theory", "desc": "Introduction, Basic Concepts of Set Theory, Representation of Discrete Structures, Relations and Ordering, Functions."},
        {"title": "Algebraic Structures", "desc": "Introduction, Algebraic Systems, Semi groups and Monoids, Lattices as Partially Ordered Sets, Boolean Algebra."},
        {"title": "Elementary Combinatorics", "desc": "Basics of Counting, Combinations and Permutations, Enumeration of Combinations and Permutations, Enumerating Combinations and Permutations with Repetitions, Enumerating Permutation with Constrained Repetitions, Binomial Coefficient, The Binomial and Multinomial Theorems, The Principle of Exclusion."},
        {"title": "Graph Theory", "desc": "Basic Concepts, Isomorphism and Subgraphs, Trees and their Properties, Spanning Trees, Directed Trees, Binary Trees, Planar Graphs, Euler's Formula, Multi-graphs and Euler Circuits, Hamiltonian Graphs, Chromatic Numbers, The Four-Color Problem."}
    ],
    "BEFA": [
        {"title": "Introduction to Business Economics", "desc": "Definition, scope, nature. Economic systems and their impact on business. Basic concepts – utility, value, price, wealth, welfare."},
        {"title": "Demand and Supply Analysis", "desc": "Law of demand, determinants, elasticity. Demand forecasting. Supply – law, determinants, elasticity."},
        {"title": "Production and Cost Analysis", "desc": "Production function, returns to scale. Cost concepts – fixed, variable, total, average, marginal. Break-even analysis."},
        {"title": "Financial Accounting", "desc": "Accounting concepts and conventions. Double-entry system, journal, ledger, trial balance. Financial statements – trading, profit & loss, balance sheet (simple problems)."},
        {"title": "Financial Ratios Analysis", "desc": "Concept, importance, types – liquidity, turnover, profitability, proprietary, solvency, leverage ratios. Analysis and interpretation (simple problems)."}
    ],
    "OS": [
        {"title": "Introduction and Structures", "desc": "Operating System - Introduction, Structures - Simple Batch, Multi-programmed, Time-shared, Personal Computer, Parallel, Distributed Systems, Real-Time Systems, System components, Operating System services, System Calls. Process - Process concepts and scheduling, Operations on processes, Cooperating Processes, Threads."},
        {"title": "CPU Scheduling and Deadlocks", "desc": "CPU Scheduling - Scheduling Criteria, Scheduling Algorithms, Multiple-Processor Scheduling. System call interface for process management- fork, exit, wait, waitpid, exec. Deadlocks - System Model, Deadlocks Characterization, Methods for Handling Deadlocks, Deadlock Prevention, Deadlock Avoidance, Deadlock Detection, and Recovery from Deadlock."},
        {"title": "Process Management and Synchronization", "desc": "Process Management and Synchronization - The Critical Section Problem, Synchronization Hardware, Semaphores, and Classical Problems of Synchronization, Critical Regions, Monitors. Interprocess Communication Mechanisms: IPC between processes on a single computer system, IPC between processes on different systems, using pipes, FIFOs, message queues, shared memory."},
        {"title": "Memory Management and Virtual Memory", "desc": "Memory Management and Virtual Memory - Logical versus Physical Address Space, Swapping, Contiguous Allocation, Paging, Segmentation, Segmentation with Paging, Demand Paging, Page Replacement, Page Replacement Algorithms."},
        {"title": "File System Interface and Operations", "desc": "File System Interface and Operations - Access methods, Directory Structure, Protection, File System Structure, Allocation methods, Free-space Management. Usage of open, create, read, write, close, lseek, stat, ioctl system calls."}
    ],
    "DBMS": [
        {"title": "Introduction to Databases", "desc": "Characteristics, advantages. Data models – hierarchical, network, relational. Database system architecture – three-schema architecture, data independence. Database languages and interfaces."},
        {"title": "Entity-Relationship Model", "desc": "Entities, attributes, relationships, ER diagrams. Constraints, cardinalities, participation. ER to relational mapping."},
        {"title": "Relational Model and SQL", "desc": "Relational algebra, tuple/domain relational calculus. SQL – DDL, DML, queries (nested, correlated), aggregate functions, GROUP BY, HAVING, views. Constraints, triggers, stored procedures."},
        {"title": "Normalization and Transaction Management", "desc": "Functional dependencies, normalization up to BCNF. Transaction concept, ACID properties, states. Concurrency control – locking, timestamp, validation, multiple granularity. Recovery – log-based recovery, checkpoints."},
        {"title": "File Organisation and Indexing", "desc": "Storage, file organisation – heap, sequential, hashing. Indexing – primary, secondary, cluster, B+ trees, hash-based. Comparison of file organisations."}
    ],
    "SE": [
        {"title": "Introduction to Software Engineering", "desc": "Introduction to Software Engineering: The evolving role of software, changing nature of software, software myths. A Generic view of process: Software engineering- a layered technology, a process framework, the capability maturity model integration (CMMI). Process models: The waterfall model, Spiral model and Agile methodology."},
        {"title": "Software Requirements", "desc": "Software Requirements: Functional and non-functional requirements, user requirements, system requirements, interface specification, the software requirements document. Requirements engineering process: Feasibility studies, requirements elicitation and analysis, requirements validation, requirements management."},
        {"title": "Design Engineering", "desc": "Design Engineering: Design process and design quality, design concepts, the design model. Creating an architectural design: software architecture, data design, architectural styles and patterns, architectural design, conceptual model of UML, basic structural modeling, class diagrams, sequence diagrams, collaboration diagrams, use case diagrams, component diagrams."},
        {"title": "Testing Strategies", "desc": "Testing Strategies: A strategic approach to software testing, test strategies for conventional software, black-box and white-box testing, validation testing, system testing, the art of debugging. Metrics for Process and Products: Software measurement, metrics for software quality."},
        {"title": "Risk Management and Quality Management", "desc": "Risk management: Reactive Vs proactive risk strategies, software risks, risk identification, risk projection, risk refinement, RMMM. Quality Management: Quality concepts, software quality assurance, software reviews, formal technical reviews, statistical software quality assurance, software reliability, the ISO 9000 quality standards."}
    ],

    # ---- 3-1 ----
    "DAA": [
        {"title": "Introduction and Divide and Conquer", "desc": "Algorithm definition, performance analysis – time/space complexity, asymptotic notations. Recurrence relations – solving by substitution, master theorem. Divide and conquer – binary search, merge sort, quick sort, strassen's matrix multiplication."},
        {"title": "Greedy Method", "desc": "General method. Applications – knapsack, job sequencing with deadlines, minimum spanning trees (Prim's, Kruskal's), single source shortest path (Dijkstra's)."},
        {"title": "Dynamic Programming", "desc": "General method. Applications – matrix chain multiplication, optimal binary search trees, 0/1 knapsack, all-pairs shortest path (Floyd-Warshall), travelling salesperson."},
        {"title": "Backtracking and Branch and Bound", "desc": "Backtracking – general method, n-queens, sum of subsets, graph coloring, Hamiltonian cycles. Branch and bound – 0/1 knapsack, travelling salesperson."},
        {"title": "NP-Hard and NP-Complete Problems", "desc": "Basic concepts, non-deterministic algorithms. NP-hard and NP-complete classes, Cook's theorem."}
    ],
    "CN": [
        {"title": "Introduction and Physical Layer", "desc": "Network hardware, software, OSI, TCP/IP reference models. Example networks – ARPANET, Internet. Physical layer – guided media (twisted pair, coaxial, fibre), wireless transmission. Data link layer – design issues, framing, error detection/correction."},
        {"title": "Data Link Layer and Medium Access Sublayer", "desc": "Elementary data link protocols: simplex protocol, stop-and-wait, sliding window protocols (one-bit, Go-Back-N, Selective Repeat). Medium Access sublayer: channel allocation, multiple access protocols (ALOHA, CSMA, collision-free), wireless LANs, switching."},
        {"title": "Network Layer", "desc": "Design issues, routing algorithms – shortest path, flooding, hierarchical, broadcast, multicast, distance vector. Congestion control algorithms, quality of service, internetworking. Network layer in the internet."},
        {"title": "Transport Layer", "desc": "Transport services, elements, connection management. TCP and UDP protocols."},
        {"title": "Application Layer", "desc": "Domain name system, SNMP, electronic mail, WWW, HTTP, streaming audio/video."}
    ],
    "DevOps": [
        {"title": "Introduction to DevOps", "desc": "Introduction to DevOps: Introduction, Agile development model, DevOps and ITIL. DevOps process and Continuous Delivery, Release management, Scrum, Kanban, delivery pipeline, identifying bottlenecks."},
        {"title": "Software development models and DevOps", "desc": "Software development models and DevOps: DevOps Lifecycle for Business Agility, DevOps, and Continuous Testing. DevOps influence on Architecture: Introducing software architecture, The monolithic scenario, Architecture rules of thumb, The separation of concerns, Handling database migrations, Micro services and the data tier, DevOps, architecture, and resilience."},
        {"title": "Introduction to project management", "desc": "Introduction to project management: The need for source code control, the history of source code management, Roles and code, source code management system and migrations, shared authentication, Hosted Git servers, Different Git server implementations, Docker intermission, Gerrit, The pull request model, GitLab."},
        {"title": "Integrating the system", "desc": "Integrating the system: Build systems, Jenkins build server, Managing build dependencies, Jenkins plugins, and file system layout, The host server, Build slaves, Software on the host, Triggers, Job chaining and build pipelines, Build servers and infrastructure as code, Building by dependency order, Build phases, Alternative build servers, Collating quality measures."},
        {"title": "Testing Tools and Deployment", "desc": "Testing Tools and Deployment: Various types of testing, Automation of testing Pros and cons, Selenium - Introduction, Selenium features, JavaScript testing, Testing backend integration points, Test-driven development, REPL-driven development. Deployment of the system: Deployment systems, Virtualization stacks, code execution at the client, Puppet master and agents, Ansible, Deployment tools: Chef, Salt Stack and Docker."}
    ],
    "AECS": [
        {"title": "Listening and Reading", "desc": "Active Listening - Development of Listening Skills Through Audio clips - Benefits of Reading - Methods and Techniques of Reading - Basic Steps to Effective Reading - Common Obstacles - Discourse Markers or Linkers - Subskills of reading - Reading for facts, negative facts and Specific Details - Guessing Meanings from Context, Inferring Meaning - Critical Reading - Reading Comprehension - Exercises for Practice."},
        {"title": "Writing Skills", "desc": "Vocabulary for Competitive Examinations - Planning for Writing - Improving Writing Skills - Structure and presentation of different documents."},
        {"title": "Presentation Skills", "desc": "Starting a conversation - responding appropriately and relevantly - using the right language and body language - Role Play in different situations including Seeking Clarification, Making a Request, Asking for and Refusing Permission, Participating in a Small Talk - Oral presentations (individual and group) through JAM sessions- PPTs - Importance of Presentation Skills - Planning, Preparing, Rehearsing and Making a Presentation - Dealing with Glossophobia or Stage Fear - Understanding Nuances of Delivery - Presentations through Posters/Projects/Reports."},
        {"title": "Group Discussion", "desc": "Types of GD and GD as a part of a Selection Procedure - Dynamics of Group Discussion- Myths of GD - Intervention, Summarizing - Modulation of Voice, Body Language, Relevance, Fluency and Organization of Ideas - Do's and Don's - GD Strategies - Exercises for Practice."},
        {"title": "Interview Skills", "desc": "Concept and Process - Interview Preparation Techniques - Types of Interview Questions - Pre-interview Planning, Opening Strategies, Answering Strategies - Interview Through Tele-conference & Video-conference - Mock Interviews."}
    ],
    "DA": [
        {"title": "Data Management", "desc": "Data Management: Design Data Architecture and manage the data for analysis, understand various sources of Data like Sensors/Signals/GPS etc. Data Management, Data Quality(noise, outliers, missing values, duplicate data) and Data Processing & Processing."},
        {"title": "Data Analytics Introduction", "desc": "Data Analytics: Introduction to Analytics, Introduction to Tools and Environment, Application of Modeling in Business, Databases & Types of Data and Variables, Data Modeling Techniques, Missing Imputations etc. Need for Business Modeling."},
        {"title": "Regression", "desc": "Regression - Concepts, Blue property assumptions, Least Square Estimation, Variable Rationalization, and Model Building etc. Logistic Regression: Model Theory, Model fit Statistics, Model Construction, Analytics applications to various Business Domains etc."},
        {"title": "Object Segmentation", "desc": "Object Segmentation: Regression Vs Segmentation - Supervised and Unsupervised Learning, Tree Building - Regression, Classification, Overfitting, Pruning and Complexity, Multiple Decision Trees etc. Time Series Methods: Arima, Measures of Forecast Accuracy, STL approach, Extract features from generated model as Height, Average Energy etc and Analyze for prediction."},
        {"title": "Data Visualization", "desc": "Data Visualization: Pixel-Oriented Visualization Techniques, Geometric Projection Visualization Techniques, Icon-Based Visualization Techniques, Hierarchical."}
    ],
    "NLP": [
        {"title": "Structure of Words and Documents", "desc": "Finding the Structure of Words: Words and Their Components, Issues and Challenges, Morphological Models. Finding the Structure of Documents: Introduction, Methods, Complexity of the Approaches, Performances of the Approaches, Features."},
        {"title": "Syntax I", "desc": "Syntax I: Parsing Natural Language, Treebanks: A Data-Driven Approach to Syntax, Representation of Syntactic Structure, Parsing Algorithms."},
        {"title": "Syntax II and Semantic Parsing I", "desc": "Syntax II: Models for Ambiguity Resolution in Parsing, Multilingual Issues. Semantic Parsing I: Introduction, Semantic Interpretation, System Paradigms, Word Sense."},
        {"title": "Semantic Parsing II", "desc": "Semantic Parsing II: Predicate-Argument Structure, Meaning Representation Systems."},
        {"title": "Language Modeling", "desc": "Language Modeling: Introduction, N-Gram Models, Language Model Evaluation, Bayesian parameter estimation, Language Model Adaptation, Language Models- class based, variable length, Bayesian topic based, Multilingual and Cross Lingual Language Modeling."}
    ],

    # ---- 3-2 ----
    "ML": [
        {"title": "Introduction", "desc": "Learning - Types of Machine Learning - Supervised Learning - The Brain and the Neuron - Design a Learning System - Perspectives and Issues in Machine Learning - Concept Learning Task - Concept Learning as Search - Finding a Maximally Specific Hypothesis - Version Spaces and the Candidate Elimination Algorithm - Linear Discriminants: - Perceptron - Linear Separability - Linear Regression."},
        {"title": "Multi-layer Perceptron", "desc": "Multi-layer Perceptron - Going Forwards - Going Backwards: Back Propagation Error - Multi-layer Perceptron in Practice - Examples of using the MLP - Overview - Deriving Back-Propagation - Radial Basis Functions and Splines - Concepts - RBF Network - Curse of Dimensionality - Interpolations and Basis Functions - Support Vector Machines."},
        {"title": "Decision Trees and Ensemble", "desc": "Learning with Trees - Decision Trees - Constructing Decision Trees - Classification and Regression Trees - Ensemble Learning - Boosting - Bagging - Different ways to Combine Classifiers - Basic Statistics - Gaussian Mixture Models - Nearest Neighbor Methods - Unsupervised Learning - K means Algorithms."},
        {"title": "Dimensionality Reduction", "desc": "Dimensionality Reduction - Linear Discriminant Analysis - Principal Component Analysis - Factor Analysis - Independent Component Analysis - Locally Linear Embedding - Isomap - Least Squares Optimization. Evolutionary Learning - Genetic algorithms - Genetic Offspring: - Genetic Operators - Using Genetic Algorithms."},
        {"title": "Reinforcement Learning", "desc": "Reinforcement Learning - Overview - Getting Lost Example. Markov Chain Monte Carlo Methods - Sampling - Proposal Distribution - Markov Chain Monte Carlo - Graphical Models - Bayesian Networks - Markov Random Fields - Hidden Markov Models - Tracking Methods."}
    ],
    "FLAT": [
        {"title": "Finite Automata", "desc": "Introduction to Finite Automata: Structural Representations, Automata and Complexity, the Central Concepts of Automata Theory - Alphabets, Strings, Languages, Problems. Nondeterministic Finite Automata: Formal Definition, an application, Text Search, Finite Automata with Epsilon-Transitions. Deterministic Finite Automata: Definition of DFA, How A DFA Process Strings, The language of DFA, Conversion of NFA with ε-transitions to NFA without ε-transitions. Conversion of NFA to DFA, Moore and Melay machines."},
        {"title": "Regular Expressions", "desc": "Regular Expressions: Finite Automata and Regular Expressions, Applications of Regular Expressions, Algebraic Laws for Regular Expressions, Conversion of Finite Automata to Regular Expressions. Pumping Lemma for Regular Languages, Statement of the pumping lemma, Applications of the Pumping Lemma. Closure Properties of Regular Languages: Closure properties of Regular languages, Decision Properties of Regular Languages, Equivalence and Minimization of Automata."},
        {"title": "Context-Free Grammars", "desc": "Context-Free Grammars: Definition of Context-Free Grammars, Derivations Using a Grammar, Leftmost and Rightmost Derivations, the Language of a Grammar, Sentential Forms, Parse Trees, Applications of Context-Free Grammars, Ambiguity in Grammars and Languages. Push Down Automata: Definition of the Pushdown Automaton, the Languages of a PDA, Equivalence of PDA's and CFG's, Acceptance by final state, Acceptance by empty stack, Deterministic Pushdown Automata. From CFG to PDA, From PDA to CFG."},
        {"title": "Normal Forms and Turing Machines", "desc": "Normal Forms for Context-Free Grammars: Eliminating useless symbols, Eliminating ε-Productions. Chomsky Normal form Greibach Normal form. Pumping Lemma for Context-Free Languages: Statement of pumping lemma, Applications. Closure Properties of Context-Free Languages: Closure properties of CFL's, Decision Properties of CFL's Turing Machines: Introduction to Turing Machine, Formal Description, Instantaneous description, The language of a Turing machine."},
        {"title": "Turing Machine Types and Undecidability", "desc": "Types of Turing machine: Turing machines and halting. Undecidability: Undecidability, A Language that is Not Recursively Enumerable, An Undecidable Problem That is RE, Undecidable Problems about Turing Machines, Recursive languages, Properties of recursive languages, Post's Correspondence Problem, Modified Post Correspondence problem, Other Undecidable Problems, Counter machines."}
    ],
    "AI": [
        {"title": "Introduction and Search", "desc": "Introduction to AI, Intelligent Agents, problem-Solving Agents, Searching for Solutions, Uninformed Search Strategies: Breadth-first search, Uniform cost search, Depth-first search, Iterative deepening Depth-first search, Bidirectional search, Informed (Heuristic) Search Strategies: Greedy best-first search, A* search, Heuristic Functions, Beyond Classical Search: Hill-climbing search, Simulated annealing search, Local Search in Continuous Spaces."},
        {"title": "Adversarial Search and Logic", "desc": "Problem Solving by Search-II and Propositional Logic. Adversarial Search: Games, Optimal Decisions in Games, Alpha-Beta Pruning, Imperfect Real-Time Decisions. Constraint Satisfaction Problems: Defining Constraint Satisfaction Problems, Constraint Propagation, Backtracking Search for CSPs, Local Search for CSPs, The Structure of Problems. Propositional Logic: Knowledge-Based Agents, The Wumpus World, Logic, Propositional Logic, Propositional Theorem Proving: Inference and proofs, Proof by resolution, Horn clauses and definite clauses, Forward and backward chaining, Effective Propositional Model Checking, Agents Based on Propositional Logic."},
        {"title": "Logic and Knowledge Representation", "desc": "Logic and Knowledge Representation. First-Order Logic: Representation, Syntax and Semantics of First-Order Logic, Using First-Order Logic, Knowledge Engineering in First-Order Logic. Inference in First-Order Logic: Propositional vs. First-Order Inference, Unification and Lifting, Forward Chaining, Backward Chaining, Resolution."},
        {"title": "Planning", "desc": "Knowledge Representation: Ontological Engineering, Categories and Objects, Events. Mental Events and Mental Objects, Reasoning Systems for Categories, Reasoning with Default Information. Classical Planning: Definition of Classical Planning, Algorithms for Planning with State-Space Search, Planning Graphs, other Classical Planning Approaches, Analysis of Planning approaches."},
        {"title": "Uncertainty", "desc": "Uncertain knowledge and Learning Uncertainty: Acting under Uncertainty, Basic Probability Notation, Inference Using Full Joint Distributions, Independence, Bayes' Rule and Its Use. Probabilistic Reasoning: Representing Knowledge in an Uncertain Domain, The Semantics of Bayesian Networks, Efficient Representation of Conditional Distributions, Approximate Inference in Bayesian Networks, Relational and First-Order Probability, Other Approaches to Uncertain Reasoning; Dempster-Shafer theory."}
    ],

    # ---- 4-1 ----
    "CNS": [
        {"title": "Introduction to Cyber Security", "desc": "Introduction to Cyber Security: Basic Cyber Security Concepts, layers of security, Vulnerability, threat, Harmful acts, Internet Governance - Challenges and Constraints, Computer Criminals, CIA Triad, Assets and Threat, motive of attackers, active attacks, passive attacks, Software attacks, hardware attacks, Cyber Threats- Cyber Warfare, Cyber Crime, Cyber terrorism, Cyber Espionage, etc., Comprehensive Cyber Security Policy."},
        {"title": "Cyberspace Law and Cyber Forensics", "desc": "Cyberspace and the Law & Cyber Forensics: Introduction, Cyber Security Regulations, Roles of International Law. The INDIAN Cyberspace, National Cyber Security Policy. Introduction, Historical background of Cyber forensics, Digital Forensics Science, The Need for Computer Forensics, Cyber Forensics and Digital evidence, Forensics Analysis of Email, Digital Forensics Lifecycle, Forensics Investigation, Challenges in Computer Forensics."},
        {"title": "Cybercrime: Mobile and Wireless Devices", "desc": "Cybercrime: Mobile and Wireless Devices: Introduction, Proliferation of Mobile and Wireless Devices, Trends in Mobility, Credit card Frauds in Mobile and Wireless Computing Era, Security Challenges Posed by Mobile Devices, Registry Settings for Mobile Devices, Authentication service Security, Attacks on Mobile/Cell Phones, Organizational security Policies and Measures in Mobile Computing Era, Laptops."},
        {"title": "Organizational Implications", "desc": "Cyber Security: Organizational Implications: Introduction, cost of cybercrimes and IPR issues, web threats for organizations, security and privacy implications, social media marketing: security risks and perils for organizations, social computing and the associated challenges for organizations."},
        {"title": "Privacy Issues", "desc": "Privacy Issues: Basic Data Privacy Concepts: Fundamental Concepts, Data Privacy Attacks, Data linking and profiling, privacy policies and their specifications, privacy policy languages, privacy in different domains- medical, financial, etc. Cybercrime: Examples and Mini-Cases."}
    ],
    "CD": [
        {"title": "Introduction and Lexical Analysis", "desc": "Introduction: The structure of a compiler, the science of building a compiler, programming language basics. Lexical Analysis: The Role of the Lexical Analyzer, Input Buffering, Recognition of Tokens, The Lexical-Analyzer Generator Lex, Finite Automata, From Regular Expressions to Automata, Design of a Lexical-Analyzer Generator, Optimization of DFA-Based Pattern Matchers."},
        {"title": "Syntax Analysis", "desc": "Syntax Analysis: Introduction, Context-Free Grammars, Writing a Grammar, Top-Down Parsing, Bottom-Up Parsing, Introduction to LR Parsing: Simple LR, More Powerful LR Parsers, Using Ambiguous Grammars and Parser Generators."},
        {"title": "Syntax Directed Translation and Intermediate Code", "desc": "Syntax-Directed Translation: Syntax-Directed Definitions, Evaluation Orders for SDD's, Applications of Syntax-Directed Translation, Syntax-Directed Translation Schemes, Implementing L-Attributed SDD's. Intermediate-Code Generation: Variants of Syntax Trees, Three-Address Code, Types and Declarations, Type Checking, Control Flow, Switch-Statements, Intermediate Code for Procedures."},
        {"title": "Run-Time Environments and Code Generation", "desc": "Run-Time Environments: Stack Allocation of Space, Access to Nonlocal Data on the Stack, Heap Management, Introduction to Garbage Collection, Introduction to Trace Based Collection. Code Generation: Issues in the Design of a Code Generator, The Target Language, Addresses in the Target Code, Basic Blocks and Flow Graphs, Optimization of Basic Blocks, A Simple Code Generator, Peephole Optimization, Register Allocation and Assignment, Dynamic Programming Code-Generation."},
        {"title": "Machine-Independent Optimization", "desc": "Machine-Independent Optimization: The Principal Sources of Optimization, Introduction to Data-Flow Analysis, Foundations of Data-Flow Analysis, Constant Propagation, Partial-Redundancy Elimination, Loops in Flow Graphs."}
    ],

    # ---- 4-2 ----
    "OB": [
        {"title": "Organizational Behaviour", "desc": "Organizational Behaviour: Definition, need and importance of organizational behaviour - Nature and scope - Frame work - Organizational behaviour models."},
        {"title": "Individual Behaviour", "desc": "Individual Behaviour: Personality - types - Factors influencing personality - Theories - Learning - Types of learners - The learning process - Learning theories - Organizational behaviour modification, Misbehavior - Types - Management Intervention. Emotions - Emotional Labour - Emotional Intelligence - Theories. Attitudes - Characteristics - Components - Formation - Measurement - Values. Perceptions - Importance - Factors influencing perception - Interpersonal perception - Impression Management. Motivation - importance - Types - Effects on work behavior."},
        {"title": "Group Behaviour", "desc": "Group Behaviour: Organization structure - Formation - Groups in organizations - Influence - Group dynamics - Emergence of informal leaders and working norms - Group decision making techniques - Team building - Interpersonal relations - Communication - Control."},
        {"title": "Leadership and Power", "desc": "Leadership and Power: Meaning - Importance - Leadership styles - Theories of leadership - Leaders Vs Managers - Sources of power - Power centers - Power and Politics."},
        {"title": "Dynamics of Organizational Behaviour", "desc": "Dynamics of Organizational Behaviour: Organizational culture and climate - Factors affecting organizational climate - Importance. Job satisfaction - Determinants - Measurements - Influence on behavior. Organizational change - Importance - Stability Vs Change - Proactive Vs Reaction change - the change process - Resistance to change - Managing change. Stress - Work Stressors - Prevention and Management of stress - Balancing work and Life. Organizational development - Characteristics - objectives - Organizational effectiveness."}
    ]
}

# ---------------------------------------------------------------------
# Semester -> subject mapping
# ---------------------------------------------------------------------
SEMESTER_MAP = {
    "1-1": ["MA", "Chemistry", "PPS", "BEE", "CAEG", "ECS"],
    "1-2": ["ODE", "Physics", "Workshop", "English", "EDC"],
    "2-1": ["DE", "DS", "PnS", "CO", "Java"],
    "2-2": ["DM", "BEFA", "OS", "DBMS", "SE"],
    "3-1": ["DAA", "CN", "DevOps", "AECS", "DA", "NLP"],
    "3-2": ["ML", "FLAT", "AI"],
    "4-1": ["CNS", "CD"],
    "4-2": ["OB"],
}

SEMESTER_NAMES = {
    "1-1": "I B.Tech. I Semester",
    "1-2": "I B.Tech. II Semester",
    "2-1": "II B.Tech. I Semester",
    "2-2": "II B.Tech. II Semester",
    "3-1": "III B.Tech. I Semester",
    "3-2": "III B.Tech. II Semester",
    "4-1": "IV B.Tech. I Semester",
    "4-2": "IV B.Tech. II Semester",
}

# ---------------------------------------------------------------------
# Build README with links
# ---------------------------------------------------------------------
def build():
    lines = []
    lines.append("# VR24 B.Tech. Computer Science & Engineering – Complete Syllabus")
    lines.append("")
    lines.append("> **Autonomous Institution** – Vignan's Institute of Management and Technology for Women")
    lines.append("> **Regulations:** VR24 (2024–2028)")
    lines.append("> **Program:** B.Tech. in Computer Science & Engineering (CSE)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ---- Navigation Table (folder links) ----
    lines.append("## 📂 Repository Navigation")
    lines.append("")
    lines.append("| Semester | Folder Link |")
    lines.append("|----------|-------------|")
    for sem in SEMESTER_MAP:
        lines.append(f"| {SEMESTER_NAMES[sem]} | [`/{sem}`](/{sem}) |")
    lines.append("| DSA (Data Structures & Algorithms) | [`/DSA`](/DSA) |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ---- Table of Contents (syllabus sections) ----
    lines.append("## Table of Contents")
    for sem in SEMESTER_MAP:
        lines.append(f"- [{SEMESTER_NAMES[sem]}](#{sem.lower().replace(' ', '-')})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ---- Syllabus content per semester ----
    for sem, subjects in SEMESTER_MAP.items():
        sem_name = SEMESTER_NAMES[sem]
        anchor = sem.lower().replace(" ", "-")
        lines.append(f"## {sem_name}  `[{sem}](/{sem})`")
        lines.append("")
        lines.append(f"**Folder:** [`/{sem}`](/{sem})")
        lines.append("")
        lines.append("| Subject | Folder |")
        lines.append("|---------|--------|")
        for sub in subjects:
            lines.append(f"| {sub} | [`/{sem}/{sub}`](/{sem}/{sub}) |")
        lines.append("")
        lines.append("---")
        lines.append("")

        # subject details
        for sub in subjects:
            data = UNIT_DATA.get(sub)
            if not data:
                continue
            lines.append(f"### {sub}  `[/{sem}/{sub}](/{sem}/{sub})`")
            lines.append("")
            lines.append("**Course Objectives:** (Refer to the official syllabus document.)")
            lines.append("")
            lines.append("**Course Outcomes:** (Refer to the official syllabus document.)")
            lines.append("")
            for i, unit in enumerate(data, 1):
                unit_link = f"/{sem}/{sub}/Unit-{i}"
                lines.append(f"**Unit-{i}: {unit['title']}**  [`[Unit-{i}]`]({unit_link})")
                lines.append("")
                lines.append(f"{unit['desc']}")
                lines.append("")
            lines.append("**Text Books:** (Refer to the official syllabus document.)")
            lines.append("**Reference Books:** (Refer to the official syllabus document.)")
            lines.append("")
            lines.append("---")
            lines.append("")

    # ---- DSA section ----
    lines.append("## DSA (Data Structures & Algorithms)  `[/DSA](/DSA)`")
    lines.append("")
    lines.append("**Folder:** [`/DSA`](/DSA)")
    lines.append("")
    for i in range(1, 6):
        lines.append(f"- [Unit-{i}](/DSA/Unit-{i})")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("*This document was automatically generated from the VR24 syllabus structure.*")

    return "\n".join(lines)


if __name__ == "__main__":
    content = build()
    with open("README.md", "w") as f:
        f.write(content)
    print("README.md generated successfully with folder links.")
    