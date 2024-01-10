# Simple Calculator

## Overview

This is a simple command-line calculator implemented in Python. It supports basic arithmetic operations such as addition, subtraction, multiplication, and division. Users can input the operation they want to perform and two numbers to execute the selected operation.

## Usage

1. Run the `calculator.py` script in a Python environment.
2. Follow the on-screen prompts to select the operation (1/2/3/4) and enter two numbers.
3. The result of the operation will be displayed.

## Operations

- **1. Addition:** Adds two numbers.
- **2. Subtraction:** Subtracts the second number from the first.
- **3. Multiplication:** Multiplies two numbers.
- **4. Division:** Divides the first number by the second. Handles division by zero.

## Error Handling

- The program validates user inputs to ensure they are valid numbers and a valid operation.
- Division by zero is handled, and an error message is displayed in case of an attempt to divide by zero.

## File Structure

- `calculator.py`: Main Python script containing the calculator implementation.
- `README.md`: Documentation file providing information about the calculator and how to use it.

## Requirements

- Python 3.x

## Run the Calculator

```bash
python calculator.py
```

## Example

```plaintext
Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter the Operation (1/2/3/4): 1
Enter the first number: 5
Enter the second number: 3

Addition Result: 8.0
```

## Notes

- Ensure Python is installed on your system.
- For division, avoid entering zero as the second number to prevent division by zero errors.

