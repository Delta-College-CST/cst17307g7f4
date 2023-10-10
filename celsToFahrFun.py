# CST 173 - Delta College
# This program prompts for a temperature in Celsius and
# returns the equivalent in Fahrenheit.

# Input
def getCelsiusTemp():
    cTemp = float(input("Enter Celsius temperature: "))
    return cTemp

# Processing
def convertToFahr(celsTemp):
    fahrTemp = 9.0 / 5.0 * celsTemp + 32.0
    return fahrTemp

# Output
def writeTempData(cels,fahr):
    print (cels,"degrees C =",fahr,"degrees F")

# ----- Main Routine -----
degC = getCelsiusTemp()
degF = convertToFahr(degC)
writeTempData(degC,degF)
