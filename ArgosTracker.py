#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: Wilderson Medina (wam27@duke.edu)
# Created on: Fall 2019
#--------------------------------------------------------------

# Create a variable pointing to the file with no header
fileName = "Data/raw/SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineStrings = fileObj.readlines()
print ("There are {} records in the file".format(len(lineStrings)))
 
# Close the file object
fileObj.close()

# Create empty dictionaries
dateDict= {}
locationDict= {}

# Use a for loop to read each line, one at a time, until the list is exhausted
for lineString in lineStrings:

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

 #Filter our records
    if obsLC in ('1','2','3'):
    # Add values to dictionary 
        dateDict[recordID]=obsDate
        locationDict[recordID]=(obsLat,obsLon) 
        
# Indicate script is complete
print ("Finished")

#Ask user for date
userDate= "7/3/2003"  #input("Enter a date (M/D/YYYY):")

#Collect keys matching user date
keylist=[]
for k,v in dateDict.items():
    if v == userDate:
        keylist.append(k)
    #print (k,v)