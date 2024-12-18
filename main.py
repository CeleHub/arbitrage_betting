# from fetch_data import fetch_odds_from_site
# from arbitrage_calculator import detect_arbitrage, calculate_stakes

# def main():
#     url = "https://example.com/sports"  # Replace with betting platform URL
#     class_name = "odds-class"          # Replace with the class name for odds
#     total_investment = 100             # Total amount to bet

#     # Fetch odds
#     odds = fetch_odds_from_site(url, class_name)
#     if not odds:
#         print("No odds fetched. Exiting.")
#         return

#     # Detect arbitrage
#     is_arb, arb_sum = detect_arbitrage(odds)
#     if is_arb:
#         print(f"Arbitrage opportunity detected! Arbitrage Sum: {arb_sum:.2f}")
#         stakes = calculate_stakes(total_investment, odds)
#         print("Recommended Stakes:", stakes)
#     else:
#         print("No arbitrage opportunities found.")

# if __name__ == "__main__":
#     main()

import arbitrage_calculator
print(arbitrage_calculator.__file__)
import arbitrage_calculator
print(dir(arbitrage_calculator))

from fetch_data import fetch_odds
from arbitrage_calculator import detect_arbitrage, calculate_stakes
from utils import format_odds, log_results

def main():
    total_investment = 100  # Total amount to bet

    # Fetch odds from betting platforms
    print("Fetching odds...")
    odds = fetch_odds()

    if not odds:
        print("No odds fetched. Exiting.")
        return

    # Format and display the fetched odds
    formatted_odds = format_odds(odds)
    print("Fetched Odds:", formatted_odds)

    # Check for arbitrage opportunities
    is_arb, arb_sum = detect_arbitrage(odds)
    if is_arb:
        print(f"Arbitrage opportunity found! Arbitrage sum: {arb_sum:.2f}")

        # Calculate optimal stakes
        stakes = calculate_stakes(total_investment, odds)
        print("Optimal stakes for each outcome:", stakes)

        # Log results
        log_results("results_log.txt", f"Arbitrage found! Odds: {formatted_odds}, Stakes: {stakes}")
    else:
        print("No arbitrage opportunities found.")
        log_results("results_log.txt", "No arbitrage opportunities detected.")

if __name__ == "__main__":
    main()
