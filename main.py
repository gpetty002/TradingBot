import tkinter as tk 
import logging

from connectors.binance import BinanceClient

from interface.root_component import Root

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceClient("6e434363c1df9cc2667832d9adfa98ba54f37184a1389ca96d3882cdc808b4e2",
    "fa6ca2c31e3a199841ecf351f50faed356c577275dd3fa965cc005ed989cc20e", True)    

    root = Root(binance)
    root.mainloop()
