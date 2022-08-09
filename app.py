# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:33:25 2022

@author: omkar
"""

import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

#from src.pythonREPL import execute_python, install_package

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    isPythonCode = False
    resp = MessagingResponse()
    msg = resp.message()
    
    if incoming_msg.startswith('#!python3'):
        code = incoming_msg.lstrip('#!python3')
        output = execute_python(code)
        msg.body(output)
        isPythonCode = True
        
    elif incoming_msg.startswith('!pip install'):
        package = incoming_msg.split()[-1]
        output = install_package(package)
        msg.body(output)
        isPythonCode = True
        
    if isPythonCode:
        return str(resp)
# translator.translate("troubleshooting", dest="hi")   
    incoming_msg = incoming_msg.lower()
    
    if 'hi' in incoming_msg:
        #out=translator.translate("troubleshooting", dest='hi')
        output=(" This is a WhatsApp Messaging intervention for enhancing treatment adherence in Latent Tuberculosis Patients in Delhi \n\n Hello, Have you taken your medicine today \n type 1 for YES type 0 for NO? ")   
    else:
        output = ("Bye")
        
        if '1' in incoming_msg:
            output = ("Are you facing any difficulties due to medicine? \n type 1 for YES type 0 for NO? ")
        else:
            output = ("Please take your medicines on time")
            
            if '1' in incoming_msg:
                output = ("What difficulties are you facing? \n 1.Fever \n 2.unexplained anorexia \n 3.brown urine (colour of coffee or cola)")
            else:
                output = ("Have you contacted doctor? \n if yes type 1 and if no type 0")
                
                if '1' in incoming_msg:
                    output = ("Have you received a call from your clinic?")
                msg.body(output)
                return str(resp) 

if __name__ == "__main__":
	app.run(debug=True)
        
    
