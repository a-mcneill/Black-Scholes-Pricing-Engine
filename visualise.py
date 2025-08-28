"""" Visualise:
    The purpose of this file is to provide documentation for the production of graphs for the black_scholes and main files"""

import matplotlib.pyplot as plt
from black_scholes import black_scholes_prices, black_scholes_greeks

def plot_option_vs_strike_price(S, T, r, sigma, option_type):
    """ The purpose of this function is to produce a graph plotting the option versus strike price
    
    Parameters:
    S: Current stock price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility
    option_type: 'call' or 'put'
    """

    # calculate the strike prices and option prices

    # create a range of strike prices around the current stock price
    strikes = [K for K in range(int(S * 0.5), int(S * 1.5))]
    
    # calculate the option price for each strike
    prices = [black_scholes_prices(S, K, T, r, sigma, option_type) for K in strikes]

    # plot the graph

    plt.figure(figsize=(10, 6))
    plt.plot(strikes, prices, label=f'{option_type.capitalize()} Option Price')
    plt.xlabel('Strike Price (K)')
    plt.ylabel('Option Price')
    plt.title(f'Black-Scholes {option_type.capitalize()} Price v Strike')
    plt.grid(True)
    plt.legend()
    plt.savefig("option_vs_strike.png")


def plot_greeks_vs_strikes(S, T, r, sigma, option_type):
    """ The purpose of this function is to produce a graph plotting the greeks versus the strike price
    
    Parameters:
    S: Current stock price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility
    option_type: 'call' or 'put'
    """

    # calculate the strike prices versus the greeks
    
    # create a range of strike prices around the current stock price
    strikes = [K for K in range(int(S * 0.5), int(S * 1.5))]
    
    # create a dictionary to store Greek values
    greeks_data = {greek: [] for greek in ['Delta', 'Gamma', 'Vega', 'Theta', 'Rho']}

    # calculate the Greeks for each strike price
    for K in strikes:
        greeks = black_scholes_greeks(S, K, T, r, sigma, option_type)

        for greek in greeks_data:
            greeks_data[greek].append(greeks[greek])
 
    # plot the graph

    plt.figure(figsize=(12, 8))

    for i, greek in enumerate(greeks_data, 1):
        plt.subplot(3, 2, i)
        plt.plot(strikes, greeks_data[greek], label=greek)
        plt.xlabel('Strike Price (K)')
        plt.ylabel(greek)
        plt.title(f'{greek} vs Strike Price')
        plt.grid(True)
        plt.legend()

    plt.tight_layout()
    plt.savefig("greeks_vs_strike.png")