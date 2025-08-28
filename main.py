""" Main:
    The purpose of this program is to execute the black_scholes program given a set of user entered values via a menu."""

from black_scholes import black_scholes_prices, black_scholes_greeks
from visualise import plot_greeks_vs_strikes, plot_option_vs_strike_price

# provide a menu for the user to make a selection from the engine

def pricing_engine_menu():
    """ The purpose of this function is to provide the user with a pricing engine menu, with different options to access different functionalities.
    """

    # store user inputs
    inputs = None


    while True:

        print("===================================================")
        print("Welcome to the Option Pricing Engine!")
        print("Enter your choice: ")
        print("1. Calculate option price.")
        print("2. Calculate option Greeks.")
        print("3. Provide option and Greeks visualisations.")
        print("0. Exit program.")
        print("===================================================")

        user_input = input().strip()
        if not user_input.isdigit():
            continue

        user_option = int(user_input)

        if user_option == 1:
            inputs = run_option_pricing_engine()

        if user_option == 2:
            if inputs:
                run_option_greek_calculation(*inputs)                           # *inputs -> utilise the user inputs for the calculation of Greeks and for visualisation
            else:
                print("Please calculate the option price first.")

        if user_option == 3:
            if inputs:
                run_option_visualisation(*inputs)
            else:
                print("Please calculate the option price first.")

        if user_option == 0:
            exit_program()


def run_option_pricing_engine():
    """ The purpose of this function is to run the option pricing engine, taking model inputs from the user, and print the option price.
    """

    # prompt the user for input values -> Loop until valid input

    while True:
        try:
            S = float(input("Enter the current stock price (S): "))

            K = float(input("Enter the strike price (K): "))

            T = float(input("Enter the time to maturity in years (T): "))

            r = float(input("Enter the risk-free interest rate (as a decimal; 5% as 0.05): "))

            sigma = float(input("Enter the option volatility (as a decimal; 20% as 0.2): "))

            option_type = input("Enter the option type ('call' or 'put'): ").strip().lower()


            # validate option type

            if option_type not in ['call', 'put']:
                raise ValueError("Invalid option type. Please enter 'call' or 'put'.")


            # calculate option price

            price = black_scholes_prices(S, K, T, r, sigma, option_type)

            # display result

            print(f"\nEuropean {option_type.capitalize()} Option Price: ${price:.2f}\n")

            # return variables to pass through to option Greeks and visualisation functions

            return S, K, T, r, sigma, option_type
        
        except ValueError as inv_input:
            print(f"\nInvalid input: {inv_input}\n")



def run_option_greek_calculation(S, K, T, r, sigma, option_type):
    """ The purpose of this function is to run the greek calculations based upon the user input and present this to the user."""
            
    greeks = black_scholes_greeks(S, K, T, r, sigma, option_type)

    print(f"Option Greeks: \n")
    for greek, value in greeks.items():
        print(f"    {greek}: {value:.4f}\n")




def run_option_visualisation(S, K, T, r, sigma, option_type):
    """ The purpose of this function is to run the graphs for plotting the option v the strike price and the Greeks across strike prices, saving the graphs for user reference."""

    plot_option_vs_strike_price(S, T, r, sigma, option_type)
    plot_greeks_vs_strikes(S, T, r, sigma, option_type)



def exit_program():
        """ The purpose of this function is to double check the user wishes to exit the program, and if so, exit the program."""

        # confirm exit of program -> if so, exit

        confirm_exit = input("\nConfirm you would like to exit the program? (yes/no): ")

        if confirm_exit == 'yes':
            print("Exiting program.")
            exit()



# call menu

if __name__ == "__main__":
    pricing_engine_menu()
