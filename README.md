
# Game Of Life

## Major Learning Points

This project helped reinforce some important software development concepts:

* **How to structure large programs**: Learn how to break down a complex program into smaller, manageable parts, keeping the code modular and easier to maintain.
* **How to break down projects into manageable chunks and milestones**: Gain experience with planning and dividing a project into well-defined tasks, making progress predictable and manageable.
* **How to write automated tests**: Implement unit tests and automated checks to ensure that your code works correctly and that future changes don't introduce bugs.

## Introduction to Life

The **Game of Life**, created by John Conway in 1970, is a cellular automaton — a grid of cells that evolve over time based on a set of simple rules. It's important to note that **Life** isn't really a "game" in the traditional sense; there are no winners or losers. Instead, it simulates the evolution of cells on a grid.

### How It Works

Life operates on a 2D grid where each cell is either **alive** or **dead**. Each cell has **8 neighbors** (the cells surrounding it). The next state of each cell depends on its current state and the number of live neighbors it has. The rules are as follows:

* **A live cell with fewer than two live neighbors dies** (underpopulation).
* **A live cell with two or three live neighbors stays alive** (stable population).
* **A live cell with more than three live neighbors dies** (overpopulation).
* **A dead cell with exactly three live neighbors becomes alive** (reproduction).

The evolution of cells is determined by these rules. Even though the rules themselves are simple, they give rise to very complex patterns, which makes Life an interesting study for emergent behavior.

### Rules of the Game

1. **Initialization**: The grid starts with an initial configuration, where each cell can be either alive or dead.
2. **Evolution**: The state of the grid is updated at each step according to the rules.
3. **Loop**: The game runs indefinitely unless manually stopped.

### Visual Representation

The board can be printed in the terminal, where live cells are represented by a specific character (e.g., `#` or `*`), and dead cells are represented by a space or another character. This gives a dynamic, visual representation of how the grid evolves over time.

## Milestones

This project was divided into several important milestones. Each of these steps builds on the previous one to gradually evolve the program into a fully working implementation of Conway's Game of Life.

### Core Features

1. **Build a Data Structure to Store the Board State**:
   The first step is creating a data structure that will hold the current state of the grid. A list of lists is commonly used to represent the 2D grid, where each element can be 1 (alive) or 0 (dead).

2. **"Pretty-print" the Board to the Terminal**:
   Once the board state is defined, the next task is to visualize it. We print the board to the terminal, representing live cells with one character (e.g., `#`), and dead cells with a blank space or another character.

3. **Calculate the Next State**:
   The next step is to implement the logic that calculates the next board state based on the current state and the number of neighbors each cell has. This is where Conway’s rules come into play.

4. **Run the Game Forever**:
   After the basic game loop is implemented, the program should keep running indefinitely, updating the grid at each step and rendering it in the terminal.

### Extensions and Improvements

Once the basic functionality is in place, several enhancements and new features can be added to make the game more powerful and user-friendly.

1. **Save and Load Game States**:
   Add functionality to save interesting starting positions to a file and reload them later. This allows users to replay specific scenarios or share configurations.

2. **Improve the User Interface**:
   The initial terminal UI is functional but minimal. We could enhance it by adding menus, options for customizing the grid size, the number of cycles, or the characters used to represent live and dead cells.

3. **Change the Rules of Life**:
   While Conway's original rules are widely known and studied, the system can be extended. You can experiment with alternative sets of rules, such as changing the number of neighbors required for a cell to survive or reproduce.

4. **Optimize Performance**:
   For larger grids, performance might become an issue. Optimizing how the state is stored and updated (e.g., using more advanced data structures like numpy arrays) could help with scalability.

5. **Visualize the Game**:
   Moving beyond the terminal, one could build a graphical user interface (GUI) for a more intuitive way to visualize the evolving grid. This could also allow users to interactively create and modify initial patterns.

## Requirements

To run this project, you will need **Python 3.12** or later. The recommended approach is to set up a **virtual environment** to manage dependencies.

1. **Set up a Virtual Environment**:

   Create a virtual environment using `venv`:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```

2. **Install Dependencies**:

   After activating the virtual environment, install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Game**:

   To run the game, execute the following command:

   ```bash
   python -m src.main
   ```

   This will launch the interactive menu, from which you can start the Game of Life and adjust settings.

### Alternative Installation (Using `.toml` File)

If you prefer, you can install the project as a package and run it through the `game-of-life` command directly:

1. Install the package:

   ```bash
   pip install .
   ```

2. Run the game:

   After installing the package, you can run the game with the command:

   ```bash
   game-of-life
   ```

## Project Structure

Here’s an overview of the project's directory structure:

```
gameoflife/
├── src/
│   ├── utils/
│   │   ├── render.py
│   │   ├── config.py
│   │   ├── menu.py
│   │   ├── pretty_title.py
│   ├── main.py
│   └── __init__.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── LICENSE
```

* `src/`: Contains all the source code files for the project.
* `utils/`: Utility files for rendering, configuration, and user menu.
* `main.py`: The entry point for running the game loop.
* `requirements.txt`: Lists the Python dependencies needed for the project.
* `pyproject.toml`: Defines the package configuration, including dependencies and entry points.
* `README.md`: This file, providing documentation for the project.
* `LICENSE`: The project's license file (e.g., MIT License).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This expanded README provides additional details on the goals, setup instructions, project structure, and possible extensions, giving users and developers more context about the project and how to run or contribute to it.

Let me know if you need any other adjustments or additions!
