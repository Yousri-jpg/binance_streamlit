import streamlit as st 
import time
import config
#from binance.client import Client
from streamlit_option_menu import option_menu
import ccxt
import streamlit as st
#import pandas as pd


##########
global api_key
global api_secret


#########


st.title('AbuFahaad Trading Station')
### Hide Hamburger Menu
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

#################

##################

api_key = st.text_input('your api key')
api_secret = st.text_input('your api_secret')
##############



option = st.multiselect(
'Choose Your Coin',
(config.usdt_coin_list),
('ADAUSDT','ETHUSDT'))



st.text_area('You selected:', option)



usdt_amount = st.number_input('Amount in USDT to trade for each Pair')




#api_key = config.api_key
#api_secret = config.api_secret

exchange=ccxt.binance ({
'apiKey': api_key,
'secret': api_secret,
# 'timeout': 30000,
'enableRateLimit': True,
'set_sandbox_mode':True


})
params = {
'test': True,  # test if it's valid, but don't actually place it
}

#######
for coin in option:

 symbol_ticker = exchange.fetch_ticker(coin)
 symbol_price=float(symbol_ticker['last'])


if symbol_price == 0 :



  st.warning (f"Please Remove {coin}")

else:
 amount = (usdt_amount*1) / (symbol_price*1)



execute = st.button("Execute all Orders")

if(execute):

  st.write('Please wait , Executing Your orders......',)

	
  for coin in option :
   opened_orders = exchange.fetch_open_orders(coin)
   if coin not in opened_orders:

    try:

     exchange.create_market_order(symbol=coin, side='BUY', amount=amount)

     st.success('Orders are Sucessful')
     time.sleep(0.5)

    except Exception as e:
       st.write("an exception occured - {}".format(e))
