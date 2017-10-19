import machine

adc = machine.ADC(0)
adcVal = adc.read()
print(adcVal)