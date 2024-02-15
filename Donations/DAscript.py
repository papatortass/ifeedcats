from currency_converter import CurrencyConverter
import socketio
import json
import serial
import time

TOKEN = "You-DonationAlert-Token"

sio = socketio.Client()

ser = serial.Serial('COM3', 9600)

def dispense_portion():
    ser.write(b'd')
    time.sleep(5)
ser.open()

moneyspent = 0
foodportions = 0

@sio.on('donation')
def on_message(data):
    data_dict = json.loads(data)
    datata = float(data_dict['amount'])
    c = CurrencyConverter()
    datata = c.convert(datata,data_dict['currency'],'USD')
    global moneyspent, foodportions
    moneyspent += datata
    foodportions = moneyspent//1.00
    moneyspent = moneyspent%1.00
    if foodportions > 0:
        for i in range(foodportions):
            dispense_portion()


sio.connect('wss://socket.donationalerts.ru:443')
sio.emit('add-user', {"token": TOKEN, "type": "alert_widget"})