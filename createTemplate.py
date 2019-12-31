import os, sys

# Set up enviornment
path="/Users/belser/python/configs"
if not os.path.exists(path):
    print("Creating %s" % path)
    os.mkdir(path)
os.chdir(path)

# Create device data structure
devices = {
    "routers": [

        {
            "hostname": "router1",
            "netID": 11,
            "interfaceID": 0
        },
        {
            "hostname": "router2",
            "netID": 22,
            "interfaceID": 1
        },
        {
            "hostname": "router3",
            "netID": 33,
            "interfaceID": 2
        },
    ]
    
}

# Loop through routers in dictionary and grab values 
for router in devices["routers"]:
    configFileName=f"""{path}/{router["hostname"]}.txt"""
    
    # Example of static config inline using string expansion to edit 
    config=f"""conft
!
hostname {router["hostname"]} 
!
192.168.{router["netID"]}.0
!
intetface gi0/{router["interfaceID"]}"""
    
    # Write it out to commandLine
    print(config)
    
    # Open File
    file = os.open(configFileName, os.O_RDWR|os.O_CREAT)
    # Encode string to bytes
    configInBytes = str.encode(config)
    # Write bytes to file
    os.write(file, configInBytes)
    # Close the file
    os.close(file)
