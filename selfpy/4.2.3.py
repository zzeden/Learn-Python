temperature = input('Insert the temperature you would like to convert')
temperature = temperature.lower()
temp_len = len(temperature)
temperature_val = int(temperature[:temp_len-1])
if(temperature.endswith('f')):
    print(str(temperature_val/5),"c")
else:
    print(str(temperature_val*5), "f")
