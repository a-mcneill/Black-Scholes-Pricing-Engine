# Black-Scholes European Option Pricing Tool

To build upon my foundational understanding of Python learnt during my postgraduate studies, and with the assistance of a provided template (AI), I have developed an European Options pricing engine, with functionality that allows for the calculation of option Greeks, and the visualisation of their behaviour across strike prices.

The purpose of this project was to continue my learning and development in Python programming, while also applying my professional experience and interest in financial markets to a Python project.

While the original functionality was supported by a template, I have continued to build upon this in the model, applying my own knowledge and learnings to change and adapt the model in alignment with my previous exposure and to add greater functionality.

The project implements a Black-Scholes pricing engine for European call and put options.
The program also includes support for the calculation of the option Greeks, as well as visualising their behaviour across strike prices.

--------------------------

# Features

- Program provides interactive CLI menu for user input and analysis.
- Calculates European call and put option prices using the Black-Scholes formula.
- Calculates the key Greeks: Delta, Gamma, Vega, Theta, Rho.
- Allows option for user to receive visualisations of option price and Greeks versus the strike prices using Matplotlib.

--------------------------

# Technology

- Python 3.10+
- 'scipy' for statistical functions.
- 'matplotlib' for plotting/graphing.
- 'math' for calulcations.

--------------------------

# Run the program

- python main.py

--------------------------

# Requirements

- scipy>=1.10.0
- matplotlib>=3.7.0

--------------------------

# Project Structure

- Black-Scholes-Pricing-Tool:
    - black_scholes.py              # Core pricing and Greeks logic
    - visualise.py                  # Graphing function for price and Greeks 
    - main.py                       # CLI for user interaction
    - README.md                     # Project Documentation

--------------------------