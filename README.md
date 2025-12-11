# Algebra Equation Solver

An interactive algebra equation solver built with Pygame that solves single-variable linear equations and displays step-by-step solutions. 
Features a graphical interface for inputting equations and automatically generates detailed solving steps.

## ✨ Features

- **Interactive GUI** - Click buttons or use keyboard to input equations
- **Step-by-Step Solutions** - Generates clear, educational solving steps
- **Multiple Operations** - Supports addition, subtraction, multiplication, division, exponents, and parentheses
- **Real-Time Display** - Shows equation as you build it
- **Algebraic Operations**:
  - Combining like terms
  - Isolating variables
  - Handling negative coefficients
  - Working with fractions
  - Solving equations with parentheses
  - Exponent operations

## 🎯 Supported Equation Types

The solver handles equations in the form: **expression = expression**

Examples:
- `2x + 5 = 13` → Solution with 2 steps
- `3x - 7 = 2x + 8` → Combines like terms
- `-4x + 10 = 6` → Handles negative coefficients
- `(2x + 4) / 2 = 10` → Processes parentheses
- `x^2 = 16` → Takes square root of both sides

## 📋 Installation

### Prerequisites
- Python 3.7 or higher
- Pygame library

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Eli-Weiss/algebra-equation-solver.git
cd algebra-equation-solver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the solver:
```bash
python algebra_solver.py
```

## 💻 Usage

### Building an Equation

**Mouse Input:**
- Click number buttons (0-9) to enter digits
- Click operation buttons (+, -, *, /, ^)
- Click parentheses buttons to group terms
- Click **x** to add the variable
- Click **=** to move to the right side of equation
- Press **Enter (Numpad)** to solve

**Keyboard Input:**
- Type numbers 0-9
- Type **x** for the variable
- Press **↓** to close exponents
- Press **Enter (Numpad)** to calculate solution
- Press **R** to restart/clear

### Example Workflow

1. Input left side: `2 * x + 5`
2. Click `=` to move to right side
3. Input right side: `13`
4. Press **Enter** to solve
5. View step-by-step solution on new screen

## 🏗️ How It Works

### Solution Algorithm

1. **Parse Input** - Separates equation into left and right expressions
2. **Identify Operations** - Tracks addition, subtraction, multiplication, division, exponents
3. **Combine Like Terms** - If variable appears on both sides, combines coefficients
4. **Isolate Variable** - Applies inverse operations in order:
   - Addition/Subtraction (undo constants)
   - Handle negatives
   - Multiplication/Division (undo coefficients)
   - Exponents (apply roots)
5. **Generate Steps** - Creates human-readable explanation for each operation
6. **Display Solution** - Shows final answer with step-by-step work

### Key Components

**State Management:**
- Tracks current operation (adding, subtracting, multiplying, etc.)
- Maintains separate lists for different operation types
- Handles nested operations within parentheses

**Step Generation:**
- Dynamically creates solution steps based on operations performed
- Combines related operations (e.g., multiply by -3 instead of separate negative and multiply steps)
- Rounds decimal answers to 3 decimal places

## 🛠️ Technical Details

- **Language:** Python 3.x
- **GUI Framework:** Pygame
- **Math Operations:** Built-in Python math library, fractions module
- **Display:** Fullscreen 1800x1000 resolution
- **Fonts:** FreeType-based rendering

## 🎨 Interface

**Input Screen:**
- Number pad (0-9)
- Operation buttons (+, -, *, /)
- Exponent button (^)
- Parentheses buttons
- Variable button (x)
- Equation display at bottom

**Solution Screen:**
- Initial equation display
- Numbered step-by-step solution
- Final answer highlighted in orange

## 📝 Code Structure

```python
# Main components:
- Number/operation button functions
- Mouse click event handlers
- Keyboard input handlers
- Expression parsing logic
- Step calculation engine
- Display rendering functions
```

## 🚧 Known Limitations

- Only solves for single variable (x)
- Limited to linear equations and simple polynomials
- Cannot handle systems of equations
- Exponents limited to whole numbers
- GUI fixed at fullscreen resolution

## 📚 Educational Use

This solver is designed to help students:
- Understand the order of operations in solving equations
- See the logical progression from problem to solution
- Learn algebraic manipulation techniques
- Verify their own work

## 👤 Author

**Eli Weiss**
- GitHub: https://github.com/EliWeiss1
- LinkedIn: https://www.linkedin.com/in/eli-weiss-40803a330/
- Email: eliisaweiss@gmail.com

