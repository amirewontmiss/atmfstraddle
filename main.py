import math
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

def atmf_straddle_price(S, T, r, sigma):
    """
    Parameters:
        S (float): Current stock price (and forward price, assuming no dividends)
        T (float): Time to maturity in years
        r (float): Risk-free interest rate (annualized)
        sigma (float): Volatility (annualized)

    Returns:
        float: ATMF straddle price
    """
    call_price = black_scholes_price(S, S, T, r, sigma, option_type="call")
    put_price = black_scholes_price(S, S, T, r, sigma, option_type="put")
    return call_price + put_price

if __name__ == "__main__":
    # Inputs
    S = 100  # Current stock price
    T = 0.5  # Time to maturity in years
    r = 0.05  # Risk-free interest rate (5%)
    sigma = 0.2  # Volatility (20%)

    # Calculate ATMF straddle price
    straddle_price = atmf_straddle_price(S, T, r, sigma)
    print(f"The approximate price of the ATMF straddle is: {straddle_price:.2f}")
