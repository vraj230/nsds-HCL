from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def add_data():
    mydb = mysql.connector.connect(host="mysql.cnc.hclets.com", port=61606, user="root", passwd="Intern@123",
                                   database="nsds")

    mycursor = mydb.cursor()

    sqlform = "Insert into system_event_windows(event_id, event_name, type, date_time) values(%s, %s, %s, %s)"

    events = [ (1004, "OPEN", "What", '2020-02-09 08:19:00'),
               (1005, "LOAD", "ever", '2021-01-20 01:20:20'), ]

    mycursor.executemany(sqlform, events)

    mydb.commit()


@app.route('/system_events_windows')

def capture_events():
    #invoke the function to capture data
    try:
        add_data()
        return ('Window Event data captured sucessfully')
    except all:
        return 'Window event data capture failed'


app.run(port = 5000)

