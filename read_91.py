import requests
import time
import rospy
import std_msgs.msg
headers = {
    'Authorization': 'Bearer 948b6cd86bb29150b3e375f2a03386fc69778ff8',
}
id=0
pub = rospy.Publisher('sensor_data', std_msgs.msg.String, queue_size=10)
rospy.init_node('sensor_pub', anonymous=True)
to_publish=''

try:
    while not rospy.is_shutdown():
        to_print=''
        response = requests.get('https://api.nrfcloud.com/v1/messages', headers=headers)
        time.sleep(0.5)
        id=id+1
        if id==len(response.json()['items'])-1:
            id=0

        to_publish=response.json()['items'][id]['message']['appId']+' '+response.json()['items'][id]['message']['data']
        
        # print(to_publish)
        # pub.publish(to_publish)
        for i in range(0,len(response.json()['items'])):

            to_print+=response.json()['items'][i]['message']['appId']+' '+response.json()['items'][i]['message']['data']
            if i != len(response.json()['items'])-1:
                to_print+=','
            # print(response.json()['items'][i]['message']['appId'])
        print(to_print)
        pub.publish(to_print)
except KeyboardInterrupt:
    print('interrupted!')





