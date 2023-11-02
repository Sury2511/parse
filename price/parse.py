import paho.mqtt.client as mqtt
import price_pb2


symbol = 'AAA'
def on_connect(client, userdata, flags, rc):
    client.subscribe(f"quotes/stock/TP/{symbol}", qos=0)
   

def on_message(client, userdata, message):
    try:
        decoded_payload = message.payload.decode('utf-8')
        print(decoded_payload)
    except UnicodeDecodeError:
        print(str(message.payload))
        
    
    stock_info= price_pb2.StockInfo()
    stock_info.ParseFromString(message.payload)
    print(stock_info)




client = mqtt.Client(client_id="064C246644", transport="websockets")
client.tls_set()  # Set TLS. Adjust this if you have specific SSL settings or certificates
client.on_connect = on_connect
client.on_message = on_message

# If the server requires authentication:
# client.username_pw_set("username", "password")

client.ws_set_options(path="/wss")  # Set WebSocket path

client.connect("datafeed.dnse.com.vn", 443, 60)

client.loop_forever()
