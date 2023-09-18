import requests
import json
import gtts
import playsound

city = input("enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=78737490e93a4a31b9b155845231307&q={city}"

r = requests.get(url)
#print (r.text)
wdict = json.loads(r.text)
var = {wdict["current"]["temp_c"]}
var1 = {wdict["current"]["temp_f"]}

text = f"the current weather in {city} is {var} "
sound = gtts.gTTS(text, lang ="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")


# print(f"the wheter in celsicus is :{var}C")
# # print(wdict["current"]["temp_c"])
# print(f"the wheter in fer is :{var1}F")
# # print(wdict["current"]["temp_f"])

