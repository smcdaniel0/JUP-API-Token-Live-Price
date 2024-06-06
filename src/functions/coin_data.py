import time
import requests


def get_coin_data(coin):
    """
    utilize the Jupiter api endpoint for coin information
    format the response into JSON data
    return the JSON data provided in from the "coin" arg
    """
    try:
        # sending a get request to Jupiter public endpoint, verifying local SSL cert
        coin_info = requests.get(f'https://price.jup.ag/v6/price?ids={coin}',
                                 verify="PATH_TO_YOUR_CERT") # verify can be removed or changed to False
        data = coin_info.json()  # converting get-call result to JSON
        return data  # return JSON data

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}"  # display the exception that was caught
              f"\nSleeping..."
              f"\n")
        return time.sleep(2)  # wait to retry


def get_coin_price(coin):
    """
    calls the get_coin_data function to get JSON data
    returns coin price from the data
    """
    price = get_coin_data(coin)
    try:
        return price['data'][coin]['price']
    except KeyError:
        return f"Could not find the requested data for: {coin}"


def get_coin_ticker(coin):
    """
    calls the get_coin_data function to get JSON data
    returns coin ticker from the data
    """
    ticker = get_coin_data(coin)
    try:
        return ticker['data'][coin]['mintSymbol']
    except KeyError:
        return f"Could not find the requested data for: {coin}"


################################################
# ########### TESTING ##########################
# user_coin = input("Enter CA: ")
# coin_p = get_coin_price(user_coin)
# coin_t = get_coin_ticker(user_coin)
#
# print(coin_p, coin_t)
