# Hue
**make sure you have python3 installed and your preffered IDE**


for **"ip"** change "bridge ip" to the ip of your hue light bridge , this can be found in your router settings under DHCP search for "Philips hue" and copy the ip into the script.



To find your hue **bridge username** go to https://your_bridge_ip_address/debug/clip.html and type  	
```{"devicetype":"my_hue_app#iphone peter"}```     into the message body 
Go and press the button on the bridge and then press the POST button and this should return an authorized user , simply copy this username into the script where it asks for "hue light username" now all we need left is to find our **light number** for the light we want the script to apply to , this can be found by running the 
Find_light_number.py and search throught the list untill you find your light and copy the light number
Now we should have everything you need to sun the light controll scripts !

