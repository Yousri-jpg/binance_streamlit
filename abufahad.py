import streamlit as st 
#import datetime 
#import time
import config
#from binance.client import Client
import ccxt
import streamlit as st
#import pandas as pd


##########
global api_key
global api_secret


#########


st.title('AbuFahaad Trading Station')
### Hide Hamburger Menu
# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)

#################

##################

##############


option = st.multiselect(
'Choose Your Coin',
(config.usdt_coin_list),
('ADAUSDT','ETHUSDT'))
  
st.text_area('You selected:', option)



amount = st.number_input('Amount in USDT to trade for each Pair',min_value=50)




api_key = config.api_key
api_secret = config.api_secret

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

#print (option)
#######
amount = amount

execute = st.button("Execute all Orders")
if(execute):
    st.write('Please wait , Executing Your orders......',)

        
    for coin in option :
        opened_orders = exchange.fetch_open_orders(coin)
        if coin not in opened_orders:
           
            try:
                exchange.create_market_order(symbol=coin, side='BUY', amount=amount,params=params)

                st.success('Orders are Sucessful')

            except Exception as e:
                st.write("an exception occured - {}".format(e))



        else: 
                st.warning('There is already open order for',coin)
             
