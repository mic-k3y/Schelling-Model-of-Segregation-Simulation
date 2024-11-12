---

## Repo Overview

### Title
**Implementation of Schelling's Model of Racial Segregation Using Python**

### Abstract
This project aims to simulate Thomas Schelling’s model of racial segregation using Python, demonstrating how individual preferences and tendencies can lead to residential segregation. Schelling’s model is an agent-based approach that showcases the emergence of segregation based solely on neighborhood preferences, with agents representing individuals who relocate within a city. The project comprises two Python files:
1. **Object Classes File**: Contains all class objects necessary for the program and serves as a reusable library.
2. **Main File**: Executes the simulation, handles user input, and visualizes the results.

The simulation begins by taking user input for initial parameters and generating a randomized grid of agents. The agents' satisfaction levels are calculated based on a threshold of similar neighbors, and dissatisfied agents relocate to compatible spaces. The program also plots the population's overall satisfaction over multiple simulation rounds and saves the data as a CSV file.

---

## Project Design

### Key Components
- **Grid Representation**: A 32x32 grid where each cell can contain a red agent, a blue agent, or be empty.
- **Data Storage**: Utilizes Python's dictionary (hash map) to store and manage grid data efficiently, with keys representing cell positions.
- **Agent Behavior**: Agents' satisfaction is determined by the proportion of neighboring agents of the same type, compared to a user-defined threshold.
- **Simulation Process**: Unsatisfied agents relocate to compatible spaces until overall satisfaction is maximized.

---

## Functional Details

### Functions
- **Home Scene**: Collects user input for simulation parameters.
- **Initialize**: Generates initial population distribution and data structures.
- **Check Happiness**: Determines agent satisfaction based on neighbors.
- **Simulate Once**: Moves unsatisfied agents to new positions.
- **Simulate**: Repeats the simulation process, updates agent positions, and plots satisfaction data.
- **Save Data**: Saves the simulation results to a CSV file.

---

## Critical Evaluation

### Strengths
- Efficient use of dictionaries reduces runtime complexity, enhancing performance.
- Object-oriented structure with classes and inheritance improves code organization and maintainability.

### Weaknesses
- Dependency on Python’s built-in dictionary, which may not be optimized for all program-specific needs.
- Main file complexity could be reduced by splitting interrelated functions into separate files.

---

## Limitations and Potential Biases

- **Model Limitations**: Simplifies real-world factors, focusing solely on agent preference for similar neighbors.
- **Program Constraints**: Limited to a 32x32 grid.

### Recommended Input Values
- **Number of Simulations**: 10-16 for effective results.
- **Red Population Percentage**: 0.3-0.7 for balanced simulations.
- **Free Space Percentage**: 0.01-0.3 for better representation.
- **Intolerance Thresholds**: Values above ⅓ typically lead to noticeable segregation.

---
