#!/usr/bin/env python3
"""
Generate detailed README.md files for all Unit-* and *-Experiment folders
based on the VR24 B.Tech CSE syllabus.
"""

import os
import re

# ---------------------------------------------------------------------
# Unit titles and brief descriptions for each subject (VR24 syllabus)
# Keys = subject folder names (exactly as created)
# Values = list of 5 dicts (one per unit) with 'title' and 'description'
# ---------------------------------------------------------------------
UNIT_DATA = {

    # ---- 1-1 ----
    "MA": [
        {"title": "Matrices", "desc": "Rank of a matrix by Echelon form and Normal form. Inverse of Non-singular matrices by Gauss-Jordan method. System of linear equations: solving homogeneous and non-homogeneous equations by Gauss elimination and Gauss Seidel Iteration Method."},
        {"title": "Eigen values and Eigen vectors", "desc": "Linear Transformation and Orthogonal Transformation. Eigen values, Eigenvectors and their properties. Diagonalization of a matrix. Cayley-Hamilton Theorem. Quadratic forms – nature and reduction to canonical forms by Orthogonal Transformation."},
        {"title": "Calculus", "desc": "Mean value theorems: Rolle's, Lagrange's, Cauchy's – geometrical interpretation and applications. Taylor's Series. Applications of definite integrals to surface areas and volumes of revolutions. Improper Integral – Beta and Gamma functions."},
        {"title": "Multivariable Calculus (Partial Differentiation)", "desc": "Limits and continuity. Partial Differentiation – Euler's Theorem, Total derivative, Jacobian, Functional dependence & independence. Maxima and minima of functions of two and three variables using Lagrange multipliers."},
        {"title": "Multivariable Calculus (Integration)", "desc": "Evaluation of Double Integrals (Cartesian and polar), change of order of integration. Evaluation of Triple Integrals – change of variables. Applications – Areas and volumes."}
    ],
    "Chemistry": [
        {"title": "Water and its treatment", "desc": "Hardness of water – estimation by complexometric method. Potable water – specifications, treatment steps, disinfection. Boiler troubles – sludges, scales, caustic embrittlement. Internal and external treatment. Desalination – Reverse osmosis."},
        {"title": "Battery Chemistry & Corrosion", "desc": "Classification of batteries – primary, secondary, reserve. Zn-air and Lithium-ion batteries – construction, working, applications. Fuel cells. Solar cells. Corrosion – causes, effects, theories, types, factors, control methods."},
        {"title": "Polymeric materials", "desc": "Polymers – classification, polymerization (addition and condensation). Nylon 6:6, Terylene. Plastics – thermoplastics and thermosetting, PVC, Bakelite, Teflon, FRP. Rubbers – natural rubber, vulcanization. Elastomers. Conducting polymers. Biodegradable polymers."},
        {"title": "Energy Sources", "desc": "Calorific value – HCV, LCV, Dulong's formula. Solid fuels – coal, proximate and ultimate analysis. Liquid fuels – petroleum refining, cracking. Knocking – octane and cetane rating. Synthetic petrol – Fischer-Tropsch process. Gaseous fuels – natural gas, LPG, CNG. Biodiesel."},
        {"title": "Engineering Materials", "desc": "Cement – Portland cement, composition, setting and hardening. Smart materials – shape memory, thermo-response. Lubricants – classification, characteristics, mechanisms, properties."}
    ],
    "PPS": [
        {"title": "Introduction to Programming", "desc": "Compilers, compiling and executing. Algorithms, Flowcharts. C basics – variables, data types, operators, expressions, storage classes, type conversion. Bitwise operations. Conditional branching and loops. I/O – scanf, printf. Command line arguments."},
        {"title": "Arrays, Strings, Structures and Pointers", "desc": "Arrays – one and two dimensional. Strings – handling as character arrays, string functions. Structures – defining, initializing, unions, array of structures. Pointers – definition, pointers to arrays and structures, self-referential structures."},
        {"title": "Preprocessor and File handling in C", "desc": "Preprocessor commands – include, define, undef, if, ifdef, ifndef. Files – text and binary, creating, reading, writing, appending. Reading/writing structures using binary files. Random access – fseek, ftell, rewind."},
        {"title": "Function and Dynamic Memory Allocation", "desc": "Functions – declaration, signature, parameters, return type, call by value, passing arrays/pointers, call by reference. Recursion – factorial, Fibonacci, limitations. Dynamic memory allocation – malloc, calloc, free, realloc."},
        {"title": "Searching and Sorting", "desc": "Linear and binary search. Bubble, Insertion and Selection sort. Concept of order of complexity."}
    ],
    "BEE": [
        {"title": "D.C. Circuits", "desc": "Electrical circuit elements (R, L, C), voltage and current sources, KVL & KCL. Analysis of simple DC circuits. Superposition, Thevenin and Norton theorems. Time-domain analysis of first-order RL and RC circuits."},
        {"title": "A.C. Circuits", "desc": "Sinusoidal waveforms – peak and rms values, phasor representation, real/reactive/apparent power, power factor. Analysis of single-phase AC circuits. Resonance in series RLC. Three-phase balanced circuits – star and delta connections."},
        {"title": "Transformers", "desc": "Ideal and practical transformer, equivalent circuit, losses, regulation and efficiency. Auto-transformer and three-phase transformer connections."},
        {"title": "Electrical Machines", "desc": "DC machine – construction, working, performance of shunt machine. Rotating magnetic field, three-phase induction motor – construction, working, torque-slip characteristics. Single-phase induction motor. Synchronous generator."},
        {"title": "Electrical Installations", "desc": "LT Switchgear – SFU, MCB, ELCB, MCCB. Wires and cables, earthing. Batteries – types and characteristics. Calculations for energy consumption, power factor improvement, battery backup."}
    ],
    "CAEG": [
        {"title": "Introduction to Engineering Graphics", "desc": "Principles, Scales (Plain & Diagonal). Conic sections – Rectangular Hyperbola. Cycloid, Epicycloid, Hypocycloid. Introduction to CAD – views, commands, conics."},
        {"title": "Orthographic Projections", "desc": "Principles, conventions, projections of points, lines and plane regular geometric figures. Auxiliary planes. CAD for orthographic projections."},
        {"title": "Projections of Regular Solids", "desc": "Auxiliary views, sections or sectional views of right regular solids – prism, cylinder, pyramid, cone. CAD for projections and sectional views."},
        {"title": "Development of Surfaces", "desc": "Development of surfaces of right regular solids – prism, cylinder, pyramid, cone. CAD for development."},
        {"title": "Isometric Projections", "desc": "Principles, Isometric Scale, Isometric views – lines, plane figures, simple and compound solids, objects with non-isometric lines, spherical parts. Conversion between isometric and orthographic views."}
    ],
    "ECS": [
        {"title": "Basics of a Computer", "desc": "Hardware – functional units, CPU components, memory hierarchy, I/O devices. Software – systems software, application software, packages, frameworks, IDEs. Generations of computers."},
        {"title": "Software Development", "desc": "Waterfall model, Agile. Types of languages – programming, markup, scripting. Program development – steps, flowcharts, algorithms. Data structures – definition and types."},
        {"title": "Operating Systems & DBMS", "desc": "OS functions, types, device & resource management. DBMS – data models, RDBMS, SQL, transactions, data centers, cloud services."},
        {"title": "Computer Networks & Web", "desc": "Advantages, LAN, WAN, MAN, internet, WiFi, sensor networks, vehicular networks, 5G. WWW – HTML, CSS, XML, web designing tools, social media. Security – information security, cyber security, cyber laws."},
        {"title": "Autonomous Systems", "desc": "IoT, Robotics, Drones, Artificial Intelligence – learning, game development, NLP, image/video processing."}
    ],

    # ---- 1-2 ----
    "ODE": [
        {"title": "First Order ODE", "desc": "Exact differential equations, integrating factors, linear equations, Bernoulli's equation, applications."},
        {"title": "Higher Order ODE", "desc": "Homogeneous and non-homogeneous linear ODEs with constant coefficients. Method of undetermined coefficients, variation of parameters."},
        {"title": "Laplace Transforms", "desc": "Definition, properties, inverse transforms, transforms of derivatives and integrals, solving ODEs with initial conditions."},
        {"title": "Vector Differentiation", "desc": "Scalar and vector fields, gradient, divergence and curl – definitions, physical interpretation, vector identities."},
        {"title": "Vector Integration", "desc": "Line, surface and volume integrals. Green's theorem, Gauss divergence theorem, Stokes theorem – statements and applications."}
    ],
    "Physics": [
        {"title": "Quantum Physics and Solids", "desc": "Blackbody radiation – Stefan-Boltzmann, Wien's, Rayleigh-Jeans, Planck's law. Photoelectric effect, Davisson-Germer experiment. Heisenberg uncertainty principle, Born interpretation, Schrodinger wave equation, particle in a 1-D box. Solids – free electron theory, Fermi-Dirac distribution, Bloch's theorem, Kronig-Penney model, energy bands."},
        {"title": "Semiconductors and Devices", "desc": "Intrinsic and extrinsic semiconductors, Hall effect, direct and indirect band gap. PN junction diode, Zener diode, BJT – construction, principle, characteristics. LED, PIN diode, APD, solar cells – structure, materials, working."},
        {"title": "Dielectric, Magnetic and Energy Materials", "desc": "Dielectric – polarization types, ferroelectric, piezoelectric, pyroelectric, LCD, crystal oscillators. Magnetic – hysteresis, soft/hard magnetic materials, magnetostriction, magnetoresistance, bubble memory, sensors. Energy materials – liquid/solid electrolytes, superionic conductors, supercapacitors, rechargeable batteries, fuel cells."},
        {"title": "Nanotechnology", "desc": "Nanoscale, quantum confinement, surface-to-volume ratio. Bottom-up fabrication – sol-gel, precipitation, combustion. Top-down – ball milling, PVD, CVD. Characterization – XRD, SEM, TEM. Applications."},
        {"title": "Laser and Fiber Optics", "desc": "Lasers – characteristics, three quantum processes, Einstein coefficients, lasing action, pumping. Ruby, He-Ne, CO2, Argon ion, Nd:YAG, semiconductor lasers – applications. Fiber optics – advantages, TIR, construction, acceptance angle, NA, classification, losses, communication system."}
    ],
    "Workshop": [
        {"title": "Introduction to Workshop Practices", "desc": "Study of hand operated power tools. Safety, precision, teamwork. Overview of trades – carpentry, fitting, smithy, foundry, welding, house-wiring."},
        {"title": "Carpentry and Fitting", "desc": "Carpentry joints – T-Lap, Dovetail, Mortise & Tenon. Fitting – V-fit, Dovetail fit, Semi-circular fit. Use of measuring tools, marking tools."},
        {"title": "Smithy and Foundry", "desc": "Black Smithy – Round to Square, Fan Hook, S-Hook. Foundry – Preparation of Green Sand Mould (Single Piece and Split Pattern)."},
        {"title": "Welding and Sheet Metal", "desc": "Welding – Arc Welding & Gas Welding. Tin-Smithy – Square Tin, Rectangular Tray, Conical Funnel."},
        {"title": "House-wiring and Machine Shop", "desc": "House-wiring – Parallel & Series, Two-way Switch, Tube Light. Machine Shop exposure – drilling, turning, grinding. Plumbing and power tools."}
    ],
    "English": [
        {"title": "Toasted English – R.K. Narayan", "desc": "Vocabulary – word formation, prefixes/suffixes, synonyms/antonyms. Grammar – common errors with articles and prepositions. Reading – importance, techniques. Writing – sentence structures, phrases/clauses, punctuation, paragraph writing."},
        {"title": "Appro JR\"D\" – Sudha Murthy", "desc": "Vocabulary – words often misspelt, homophones, homonyms, homographs. Grammar – noun-pronoun agreement, subject-verb agreement. Reading – skimming and scanning."},
        {"title": "Lessons from Online Learning", "desc": "Vocabulary – words often confused, foreign words. Grammar – misplaced modifiers, tenses. Reading – intensive and extensive reading. Writing – formal letters, email etiquette, job application with CV/Resume."},
        {"title": "Art and Literature – Abdul Kalam", "desc": "Vocabulary – standard abbreviations. Grammar – redundancies and clichés. Reading – SQ3R method. Writing – essay writing, précis writing."},
        {"title": "Go, Kiss the World – Subroto Bagchi", "desc": "Vocabulary – technical vocabulary. Grammar – common errors. Reading – comprehension exercises. Writing – technical reports – introduction, characteristics, categories, formats, structure."}
    ],
    "EDC": [
        {"title": "Diodes", "desc": "Static and Dynamic resistances, Equivalent circuit, Diffusion and Transition Capacitances, V-I Characteristics, Diode as a switch – switching times."},
        {"title": "Diode Applications", "desc": "Rectifiers – Half Wave, Full Wave, Bridge, with capacitive/inductive filters. Clippers – clipping at two independent levels. Clampers – clamping circuit theorem, operation, types."},
        {"title": "Bipolar Junction Transistor (BJT)", "desc": "Principle of operation, CE, CB, CC configurations. Transistor as a switch, switching times."},
        {"title": "Junction Field Effect Transistor (FET)", "desc": "Construction, principle, Pinch-Off Voltage, Volt-Ampere characteristics. Comparison of BJT and FET. FET as Voltage Variable Resistor, MOSFET, MOSFET as capacitor."},
        {"title": "Special Purpose Devices", "desc": "Zener diode – characteristics, voltage regulator. SCR, Tunnel diode, UJT, Varactor diode, Photo diode, Solar cell, LED, Schottky diode – principle of operation."}
    ],

    # ---- 2-1 ----
    "DE": [
        {"title": "Boolean Algebra and Logic Gates", "desc": "Digital systems, binary numbers, base conversions, complements, signed binary, codes, registers, binary logic. Boolean algebra – axioms, theorems, properties, functions, canonical/standard forms, logic operations, digital logic gates."},
        {"title": "Gate-Level Minimization", "desc": "K-map method – 4-variable, 5-variable, product of sums simplification, don't-care conditions. NAND and NOR implementation, other two-level implementations, Exclusive-OR function."},
        {"title": "Combinational Logic", "desc": "Analysis and design procedures. Binary adder-subtractor, decimal adder, binary multiplier, magnitude comparator. Decoders, encoders, multiplexers. HDL for combinational circuits."},
        {"title": "Sequential Logic", "desc": "Sequential circuits, latches, flip-flops. Analysis of clocked sequential circuits, state reduction/assignment, design procedure. Registers, shift registers, ripple counters, synchronous counters, other counters."},
        {"title": "Memories and Asynchronous Sequential Logic", "desc": "Random-access memory, memory decoding, error detection/correction. Read-only memory, programmable logic arrays, programmable array logic, sequential programmable devices. Asynchronous sequential logic – analysis, circuits with latches, design, reduction, race-free state assignment, hazards."}
    ],
    "DS": [
        {"title": "Introduction to Data Structures", "desc": "Abstract data types. Arrays – representation, operations. Linked lists – singly, doubly, circular – insertion, deletion, traversal."},
        {"title": "Stacks and Queues", "desc": "Stack – operations, array and linked representations, applications – infix/postfix/prefix, recursion. Queue – operations, array and linked representations, circular queues, dequeues."},
        {"title": "Trees", "desc": "Binary trees – properties, representation, traversals. Binary search trees – operations (search, insert, delete). AVL trees – rotations, insertion, deletion. Heaps – operations, heap sort."},
        {"title": "Graphs", "desc": "Definitions, representations – adjacency matrix, adjacency list. Graph traversals – BFS, DFS. Shortest path – Dijkstra's algorithm. Minimum spanning trees – Prim's and Kruskal's."},
        {"title": "Searching, Sorting and Hashing", "desc": "Linear and binary search. Sorting – Bubble, Insertion, Selection, Quick, Merge, Heap. Hashing – hash functions, collision resolution – chaining, open addressing, rehashing."}
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
        {"title": "Mathematical Logic", "desc": "Statements, connectives, normal forms. Theory of inference for statement calculus. Predicate calculus, inference theory."},
        {"title": "Set Theory", "desc": "Basic concepts, representation of discrete structures. Relations and ordering, functions."},
        {"title": "Algebraic Structures", "desc": "Algebraic systems, semigroups, monoids. Lattices as partially ordered sets, Boolean algebra."},
        {"title": "Elementary Combinatorics", "desc": "Basics of counting, combinations, permutations (with/without repetitions). Binomial and multinomial theorems. Principle of inclusion-exclusion."},
        {"title": "Graph Theory", "desc": "Basic concepts, isomorphism, subgraphs. Trees and their properties, spanning trees, directed trees, binary trees. Planar graphs, Euler's formula, multigraphs, Euler circuits. Hamiltonian graphs, chromatic numbers, four-color problem."}
    ],
    "BEFA": [
        {"title": "Introduction to Business Economics", "desc": "Definition, scope, nature. Economic systems and their impact on business. Basic concepts – utility, value, price, wealth, welfare."},
        {"title": "Demand and Supply Analysis", "desc": "Law of demand, determinants, elasticity. Demand forecasting. Supply – law, determinants, elasticity."},
        {"title": "Production and Cost Analysis", "desc": "Production function, returns to scale. Cost concepts – fixed, variable, total, average, marginal. Break-even analysis."},
        {"title": "Financial Accounting", "desc": "Accounting concepts and conventions. Double-entry system, journal, ledger, trial balance. Financial statements – trading, profit & loss, balance sheet (simple problems)."},
        {"title": "Financial Ratios Analysis", "desc": "Concept, importance, types – liquidity, turnover, profitability, proprietary, solvency, leverage ratios. Analysis and interpretation (simple problems)."}
    ],
    "OS": [
        {"title": "Introduction and Structures", "desc": "Simple batch, multiprogrammed, time-shared, PC, parallel, distributed, real-time systems. System components, OS services, system calls. Process – concepts, scheduling, operations, cooperating processes, threads."},
        {"title": "CPU Scheduling and Deadlocks", "desc": "Scheduling criteria, algorithms, multiple-processor scheduling. System calls for process management – fork, exit, wait, waitpid, exec. Deadlocks – system model, characterisation, methods (prevention, avoidance, detection, recovery)."},
        {"title": "Process Management and Synchronization", "desc": "Critical section problem, synchronisation hardware, semaphores, classical problems, monitors. IPC mechanisms – pipes, FIFOs, message queues, shared memory."},
        {"title": "Memory Management and Virtual Memory", "desc": "Logical vs physical address space, swapping, contiguous allocation, paging, segmentation, segmentation with paging. Demand paging, page replacement algorithms."},
        {"title": "File System Interface and Operations", "desc": "Access methods, directory structure, protection. File system structure, allocation methods, free-space management. System calls – open, create, read, write, close, lseek, stat, ioctl."}
    ],
    "DBMS": [
        {"title": "Introduction to Databases", "desc": "Characteristics, advantages. Data models – hierarchical, network, relational. Database system architecture – three-schema architecture, data independence. Database languages and interfaces."},
        {"title": "Entity-Relationship Model", "desc": "Entities, attributes, relationships, ER diagrams. Constraints, cardinalities, participation. ER to relational mapping."},
        {"title": "Relational Model and SQL", "desc": "Relational algebra, tuple/domain relational calculus. SQL – DDL, DML, queries (nested, correlated), aggregate functions, GROUP BY, HAVING, views. Constraints, triggers, stored procedures."},
        {"title": "Normalization and Transaction Management", "desc": "Functional dependencies, normalisation up to BCNF. Transaction concept, ACID properties, states. Concurrency control – locking, timestamp, validation, multiple granularity. Recovery – log-based recovery, checkpoints."},
        {"title": "File Organisation and Indexing", "desc": "Storage, file organisation – heap, sequential, hashing. Indexing – primary, secondary, cluster, B+ trees, hash-based. Comparison of file organisations."}
    ],
    "SE": [
        {"title": "Introduction to Software Engineering", "desc": "Evolving role, changing nature, software myths. Generic view – layered technology, process framework, CMMI. Process models – Waterfall, Spiral, Agile."},
        {"title": "Software Requirements", "desc": "Functional and non-functional requirements, user/system requirements, interface specification. Requirements document. Requirements engineering process – feasibility, elicitation, analysis, validation, management."},
        {"title": "Design Engineering", "desc": "Design process and quality, design concepts, design model. Architectural design – software architecture, data design, architectural styles/patterns. UML – conceptual model, class, sequence, collaboration, use case, component diagrams."},
        {"title": "Testing Strategies", "desc": "Strategic approach, test strategies for conventional software, black-box/white-box testing. Validation testing, system testing, debugging. Metrics for process and products – software measurement, quality metrics."},
        {"title": "Risk Management and Quality Management", "desc": "Reactive vs proactive risk strategies, software risks, identification, projection, refinement, RMMM. Quality concepts, SQA, software reviews, formal technical reviews, statistical SQA, software reliability, ISO 9000."}
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
        {"title": "Data Link Layer and Medium Access Sublayer", "desc": "Elementary protocols – simplex, stop-and-wait. Sliding window protocols – one-bit, Go-Back-N, Selective Repeat. Medium access – channel allocation, multiple access protocols (ALOHA, CSMA, collision-free), wireless LANs, switching."},
        {"title": "Network Layer", "desc": "Design issues, routing algorithms – shortest path, flooding, hierarchical, broadcast, multicast, distance vector. Congestion control algorithms, quality of service, internetworking. Network layer in the internet."},
        {"title": "Transport Layer", "desc": "Transport services, elements, connection management. TCP and UDP protocols."},
        {"title": "Application Layer", "desc": "Domain name system, SNMP, electronic mail, WWW, HTTP, streaming audio/video."}
    ],
    "DevOps": [
        {"title": "Introduction to DevOps", "desc": "Agile development model, DevOps and ITIL. DevOps process, continuous delivery, release management. Scrum, Kanban, delivery pipeline, identifying bottlenecks."},
        {"title": "Software Development Models and DevOps", "desc": "DevOps lifecycle for business agility, continuous testing. Impact on architecture – monolithic, separation of concerns, database migrations, microservices, resilience."},
        {"title": "Project Management and Source Code Control", "desc": "Need for source code control, history, roles, migrations. Git, Gerrit, pull request model, GitLab."},
        {"title": "Integrating the System", "desc": "Build systems, Jenkins, build dependencies, plugins, file system layout, build slaves, triggers, job chaining, pipeline, infrastructure as code, build by dependency order, build phases."},
        {"title": "Testing Tools and Deployment", "desc": "Types of testing, automation – pros/cons, Selenium, JavaScript testing, backend integration, TDD, REPL-driven development. Deployment systems, virtualization, Puppet, Ansible, Chef, Salt Stack, Docker."}
    ],
    "AECS": [
        {"title": "Listening and Reading", "desc": "Active listening, audio clips, reading methods, discourse markers, subskills, critical reading."},
        {"title": "Writing Skills", "desc": "Vocabulary for competitive exams, planning, structure, presentation."},
        {"title": "Presentation Skills", "desc": "Starting conversations, role plays, JAM sessions, PPTs, handling stage fear, delivery nuances, poster/project presentations."},
        {"title": "Group Discussion", "desc": "Types, dynamics, myths, intervention, summarising, voice modulation, body language, do's/don'ts."},
        {"title": "Interview Skills", "desc": "Concept, preparation, types of questions, pre-planning, strategies, tele/video-conference, mock interviews."}
    ],
    "DA": [
        {"title": "Data Management", "desc": "Design architecture, data sources (sensors/GPS), data quality (noise, outliers, missing values), processing."},
        {"title": "Data Analytics Introduction", "desc": "Introduction, tools, business modeling, databases, variables, imputations."},
        {"title": "Regression", "desc": "Concept, least square estimation, model building. Logistic regression – model theory, fit statistics, applications."},
        {"title": "Object Segmentation", "desc": "Regression vs segmentation, supervised/unsupervised learning, tree building (regression, classification), overfitting, pruning, multiple decision trees. Time series – ARIMA, STL, feature extraction."},
        {"title": "Data Visualization", "desc": "Pixel-oriented, geometric projection, icon-based, hierarchical visualization techniques."}
    ],
    "NLP": [
        {"title": "Structure of Words and Documents", "desc": "Morphology, models, issues, challenges, document analysis methods, performance, features."},
        {"title": "Syntax I", "desc": "Parsing natural language, treebanks, representation, parsing algorithms."},
        {"title": "Syntax II and Semantic Parsing I", "desc": "Ambiguity resolution, multilingual issues. Semantic parsing – introduction, interpretation, paradigms, word sense."},
        {"title": "Semantic Parsing II", "desc": "Predicate-argument structures, meaning representation systems."},
        {"title": "Language Modeling", "desc": "N-gram models, evaluation, Bayesian parameter estimation, adaptation, class-based, variable length, topic-based, multilingual/cross-lingual."}
    ],

    # ---- 3-2 ----
    "ML": [
        {"title": "Introduction", "desc": "Types of ML, supervised learning, brain/neuron, design a learning system, concept learning, version spaces, candidate elimination. Linear discriminants – perceptron, linear separability, linear regression."},
        {"title": "Multi-layer Perceptron", "desc": "Backpropagation, RBF, support vector machines."},
        {"title": "Decision Trees and Ensemble", "desc": "Decision trees – classification/regression, ensemble learning – boosting, bagging, basic statistics, Gaussian mixture models, nearest neighbour, unsupervised K-means."},
        {"title": "Dimensionality Reduction and Evolutionary Learning", "desc": "Dimensionality reduction – LDA, PCA, factor analysis, ICA, LLE, Isomap. Evolutionary learning – genetic algorithms, operators, applications."},
        {"title": "Reinforcement Learning and Graphical Models", "desc": "Reinforcement learning, Markov chain Monte Carlo, graphical models – Bayesian networks, Markov random fields, HMMs."}
    ],
    "FLAT": [
        {"title": "Finite Automata", "desc": "Structural representations, automata and complexity, alphabets, strings, languages, problems. NFA – formal definition, application, epsilon transitions. DFA – definition, processing, language, conversion NFA-DFA, Moore/Mealy machines."},
        {"title": "Regular Expressions", "desc": "Finite automata to RE, applications, algebraic laws, pumping lemma, closure properties, decision properties, equivalence/minimisation."},
        {"title": "Context-Free Grammars", "desc": "Definition, derivations, leftmost/rightmost, language, sentential forms, parse trees, ambiguity. PDA – definition, languages, equivalence with CFG, acceptance by final state/empty stack, deterministic PDA."},
        {"title": "Normal Forms and Turing Machines", "desc": "Eliminating useless symbols, epsilon productions, Chomsky and Greibach normal forms. Pumping lemma for CFLs, closure/decision properties. Turing Machines – introduction, formal description, instantaneous description, language."},
        {"title": "Turing Machine Types and Undecidability", "desc": "Turing machine types – halting, undecidability, recursively enumerable languages, recursive languages, Post's Correspondence Problem, counter machines."}
    ],
    "AI": [
        {"title": "Introduction and Search", "desc": "Introduction to AI, intelligent agents, problem-solving agents, uninformed search (BFS, uniform cost, DFS, iterative deepening, bidirectional), informed search (greedy best-first, A*), heuristic functions, local search (hill-climbing, simulated annealing, continuous spaces)."},
        {"title": "Adversarial Search and Logic", "desc": "Adversarial search – games, minimax, alpha-beta pruning. CSP – definition, propagation, backtracking, local search, structure. Propositional logic – knowledge-based agents, Wumpus world, inference, resolution, Horn clauses, forward/backward chaining."},
        {"title": "Logic and Knowledge Representation", "desc": "First-order logic – representation, syntax/semantics, knowledge engineering. Inference – unification, lifting, forward/backward chaining, resolution. Knowledge representation – ontological engineering, categories, objects, events."},
        {"title": "Planning", "desc": "Classical planning – definition, state-space search, planning graphs. Reasoning systems, default reasoning."},
        {"title": "Uncertainty", "desc": "Probability, Bayes' rule, Bayesian networks, approximate inference, Dempster-Shafer theory."}
    ],

    # ---- 4-1 ----
    "CNS": [
        {"title": "Introduction to Cyber Security", "desc": "Basic concepts, layers of security, vulnerability, threat, harmful acts, Internet Governance, CIA Triad, assets and threat, active/passive attacks, software/hardware attacks, Cyber Warfare, Cyber Crime, Cyber terrorism, Cyber Espionage, Comprehensive Cyber Security Policy."},
        {"title": "Cyberspace Law and Cyber Forensics", "desc": "Cyber Security Regulations, Roles of International Law. The INDIAN Cyberspace, National Cyber Security Policy. Historical background of Cyber forensics, Digital Forensics Science, The Need for Computer Forensics, Cyber Forensics and Digital evidence, Forensics Analysis of Email, Digital Forensics Lifecycle, Forensics Investigation, Challenges."},
        {"title": "Cybercrime: Mobile and Wireless Devices", "desc": "Proliferation of Mobile and Wireless Devices, Trends in Mobility, Credit card Frauds, Security Challenges Posed by Mobile Devices, Registry Settings, Authentication service Security, Attacks on Mobile/Cell Phones, Organizational security Policies and Measures, Laptops."},
        {"title": "Organizational Implications", "desc": "Cost of cybercrimes and IPR issues, web threats for organizations, security and privacy implications, social media marketing risks, social computing challenges."},
        {"title": "Privacy Issues", "desc": "Basic Data Privacy Concepts, Data Privacy Attacks, Data linking and profiling, privacy policies and their specifications, privacy policy languages, privacy in different domains (medical, financial)."}
    ],
    "CD": [
        {"title": "Introduction and Lexical Analysis", "desc": "The structure of a compiler, the science of building a compiler, programming language basics. The Role of the Lexical Analyzer, Input Buffering, Recognition of Tokens, The Lexical-Analyzer Generator Lex, Finite Automata, From Regular Expressions to Automata, Design of a Lexical-Analyzer Generator, Optimization of DFA-Based Pattern Matchers."},
        {"title": "Syntax Analysis", "desc": "Introduction, Context-Free Grammars, Writing a Grammar, Top-Down Parsing, Bottom-Up Parsing, Introduction to LR Parsing: Simple LR, More Powerful LR Parsers, Using Ambiguous Grammars and Parser Generators."},
        {"title": "Syntax Directed Translation and Intermediate Code", "desc": "Syntax-Directed Definitions, Evaluation Orders for SDD's, Applications, Syntax-Directed Translation Schemes, Implementing L-Attributed SDD's. Intermediate-Code Generation – Variants of Syntax Trees, Three-Address Code, Types and Declarations, Type Checking, Control Flow, Switch-Statements, Intermediate Code for Procedures."},
        {"title": "Run-Time Environments and Code Generation", "desc": "Stack Allocation of Space, Access to Nonlocal Data on the Stack, Heap Management, Introduction to Garbage Collection, Trace-Based Collection. Code Generation – Issues, Target Language, Addresses in the Target Code, Basic Blocks and Flow Graphs, Optimization of Basic Blocks, A Simple Code Generator, Peephole Optimization, Register Allocation and Assignment, Dynamic Programming Code-Generation."},
        {"title": "Machine-Independent Optimization", "desc": "The Principal Sources of Optimization, Introduction to Data-Flow Analysis, Foundations of Data-Flow Analysis, Constant Propagation, Partial-Redundancy Elimination, Loops in Flow Graphs."}
    ],

    # ---- 4-2 ----
    "OB": [
        {"title": "Organizational Behaviour", "desc": "Definition, need and importance of organizational behaviour. Nature and scope. Framework. Organizational behaviour models."},
        {"title": "Individual Behaviour", "desc": "Personality – types, factors influencing, theories. Learning – types, process, theories, OB modification. Emotions – Emotional Labour, Emotional Intelligence. Attitudes – characteristics, components, formation, measurement, values. Perceptions – importance, factors influencing, interpersonal perception, Impression Management. Motivation – importance, types, effects on work behavior."},
        {"title": "Group Behaviour", "desc": "Organization structure. Groups in organizations – influence, dynamics, informal leaders, working norms. Group decision making techniques. Team building. Interpersonal relations, communication, control."},
        {"title": "Leadership and Power", "desc": "Meaning, importance, leadership styles, theories of leadership. Leaders vs Managers. Sources of power, power centers, power and politics."},
        {"title": "Dynamics of Organizational Behaviour", "desc": "Organizational culture and climate – factors, importance. Job satisfaction – determinants, measurements, influence on behavior. Organizational change – importance, stability vs change, proactive vs reaction change, change process, resistance to change, managing change. Stress – work stressors, prevention and management, balancing work and life. Organizational development – characteristics, objectives, organizational effectiveness."}
    ]
}

# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------

def write_readme(path, content):
    """Write content to README.md if it doesn't exist or is empty."""
    readme_path = os.path.join(path, "README.md")
    if os.path.exists(readme_path):
        # If it's not empty, skip to preserve user content
        if os.path.getsize(readme_path) > 0:
            print(f"Skipping (exists): {readme_path}")
            return
    with open(readme_path, "w") as f:
        f.write(content)
    print(f"Created: {readme_path}")

def generate_unit_readme(subject, unit_num):
    """Generate README content for a Unit-X folder."""
    unit_num = int(unit_num)
    idx = unit_num - 1
    data = UNIT_DATA.get(subject)
    if data and idx < len(data):
        title = data[idx]["title"]
        desc = data[idx]["desc"]
    else:
        title = f"Unit {unit_num}"
        desc = "Topics covered as per the VR24 syllabus. Please refer to the course textbook for detailed content."

    return f"""# {subject} – {title}

## Overview

{desc}

## Topics Covered

Refer to the detailed unit outline in your course textbook or lecture notes. This unit is part of the VR24 B.Tech CSE curriculum.

## Expected Outcomes

Upon completing this unit, you should be able to:
- Understand the core concepts and principles covered.
- Apply the knowledge to solve related problems.
- Analyse and evaluate case studies / examples relevant to the topic.

---

*This README was automatically generated from the VR24 syllabus structure.*
"""

def generate_experiment_readme(exp_num):
    """Generate README content for an Experiment folder."""
    return f"""# Experiment {exp_num}

## Aim

*Describe the objective of this experiment.*

## Theory

*Provide the theoretical background, formulas, and concepts required for this experiment.*

## Procedure

*List the step-by-step procedure to perform the experiment.*

## Observations

*Record your observations, readings, and data here.*

## Result

*State the conclusion or result obtained from the experiment.*

---

*This README is a template. Fill in the details as you perform the experiment.*
"""

# ---------------------------------------------------------------------
# Main walk
# ---------------------------------------------------------------------

def main():
    root = "."
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden directories and .git
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if os.path.basename(dirpath) in [".git", "__pycache__"]:
            continue

        # Check for Unit-X folders
        if re.match(r"^Unit-[1-5]$", os.path.basename(dirpath)):
            parent = os.path.basename(os.path.dirname(dirpath))
            # If parent is a lab folder, skip (labs shouldn't have units)
            if "Lab" in parent or "Experiment" in parent:
                continue
            unit_num = os.path.basename(dirpath).split("-")[1]
            content = generate_unit_readme(parent, unit_num)
            write_readme(dirpath, content)

        # Check for Experiment folders
        if re.match(r"^[0-9][0-9]-Experiment$", os.path.basename(dirpath)):
            exp_num = os.path.basename(dirpath).split("-")[0]
            content = generate_experiment_readme(exp_num)
            write_readme(dirpath, content)

if __name__ == "__main__":
    main()