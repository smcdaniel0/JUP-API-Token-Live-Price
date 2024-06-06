from functions.coin_data import get_coin_ticker, get_coin_price
from datetime import datetime
import time

DELAY = 20  # constant variable for delay: 10 = ~5 seconds
count = 0
retries = 2

coin = input("WARNING: Some pump.fun tokens may not be available for monitoring."
             "\nEnter CA: ")  # user enters the contract address
ticker = get_coin_ticker(coin)  # get ticker of the provided (coin) EX: SOL, ETH, etc.
start_price = get_coin_price(coin)  # get price
last_price = start_price  # this will update over time
temp_price = start_price  # temporary price holder
start_time = datetime.now()  # getting the start time

# start program
while True:
    current_time = datetime.now()
    try:
        current_price = get_coin_price(coin)

        # calculating percentage change in price
        # by taking difference in start and current price
        # and dividing the difference by the current price * 100
        dif_in_price = current_price - start_price
        percent_change = (dif_in_price / current_price) * 100

        # display information to console
        print(f"Time: {current_time.hour}:{current_time.minute}:{current_time.second}"
              f"\n${ticker} ||| Start Price: ${start_price}"
              f"\nCurrent Price:  ${current_price} | Last Price (~10 sec): ${last_price}"
              f"\nChange since {start_time.hour}:{start_time.minute}:{start_time.second} : {round(percent_change, 3)}%"
              f"\n")

        # setting a price change by time using a delay
        if count > DELAY:
            last_price = temp_price
            temp_price = current_price
            count = -1

    except TypeError:
        print("Could not load coin information."
              f"\nSleeping for 5 seconds, retrying {retries} more time(s)."
              f"\n")
        time.sleep(5)
        retries -= 1
        if retries == 0:
            print(f"Could not load token information."
                  f"\nPlease check https://price.jup.ag/v6/price?ids={coin}. "
                  "\nIf data is empty(data: {}), it is not available/trusted in Jupiter at this time."
                  "\nTry entering a different token CA.")
            break

    except KeyboardInterrupt:
        break

    count += 1

##########################################################################################
# ##### VARIABLE TESTING #################################################################
# ## print(f"Last: {last_price} - Current: {current_price} = Difference: {-dif_in_price}")
# ## print(f"{dif_in_price} / {current_price} * 100 = {percent_change}")
##########################################################################################
