import time
import board
import thingspeak
import adafruit_scd30
i2c = board.I2C() # uses board.SCL and board.SDA
scd = adafruit_scd30.SCD30(i2c)

channel_id = XXXXX # PUT CHANNEL ID HERE
key  = 'XXXXX' # PUT YOUR WRITE KEY HERE

def measure(channel):
        try:
                response = channel.update({'field1': scd.CO2, 'field2': scd.temperature,'field3': scd.relative_humidity}) # POST to api.thingspeak.com
                print("Data Available!")
                print("CO2:", scd.CO2, "PPM")
                print("Temperature:", scd.temperature, "degrees C")
                print("Humidity:", scd.relative_humidity,"%%rH")
                print("")
                print("Waiting for new data...")
                print("")
                print(response)
        except:
                print("upsi, something went wrong.")


if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(60)                                        # Change 60 seconds to x seconds if needed. 
