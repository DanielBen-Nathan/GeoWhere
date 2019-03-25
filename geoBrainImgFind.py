import google_streetview.api
import requests
import random
import json

#google_streetview -s key= AIzaSyDz4GOxotujjxVF3eLx5dtnf6QgyWs55ug
#x=str(round(random.uniform(54,55),7))#europe 36-30x-10,20
#y=str(round(random.uniform(-1,-2),7))
#x2=str(round(random.uniform(60,61),6))
#y2=str(round(random.uniform(24,25),7))
iterations=2000
picCount=0
reqSize=90
latCoordinates=[37,65]#europe
longCoordinates=[-10,25]

latCoordinates=[-85,85]#world
longCoordinates=[-180,180]

for i in range(0,iterations):
   
    lats=[]
    longs=[]

    for i2 in range(0, reqSize):
        lats.append(str(round(random.uniform(latCoordinates[0],latCoordinates[1]),7)))
        longs.append(str(round(random.uniform(longCoordinates[0],longCoordinates[1]),7)))
    stringLocs=''
    for location in range(0, reqSize):
        stringLocs=stringLocs+lats[location]+','+longs[location]
        if (location!=reqSize-1):
            stringLocs=stringLocs+'|'
    #print(stringLocs)
    url ='https://roads.googleapis.com/v1/nearestRoads?points='+stringLocs+'&key=AIzaSyDz4GOxotujjxVF3eLx5dtnf6QgyWs55ug'
    #print(url)
    r = requests.get(url)
    data=json.loads(r.text)
    #print(data)
    #print("\n")
    found=True
    try:
        #print(data['snappedPoints'][0]['location'])
        #print (content)
        lat=str(round(data['snappedPoints'][0]['location']['latitude'],7))
        long=str(round(data['snappedPoints'][0]['location']['longitude'],7))
    except Exception:
        found=False

    if(found):
        
        params = [{
          'size': '300x300', 
          'location': lat+','+long,
          'heading': '0',
          'pitch': '0',
          'key': 'AIzaSyDz4GOxotujjxVF3eLx5dtnf6QgyWs55ug'
        }]
        #print(lat,",",long)

        results = google_streetview.api.results(params)
        
        if(results.metadata[0]['status']!='ZERO_RESULTS'):
            print("output pic")
            picCount+=1
            results.download_links('data_set\\'+lat+','+long)
        #else:
            #print("no streetview")
    #else:
       # pass
        #print("no road near")

print("percentage found: ",(picCount/iterations)*100,"\npictures found: ",picCount)
