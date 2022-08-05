#!/usr/bin/env python3
#COVID-19 info taken from https://www.cdc.gov/coronavirus/2019-ncov/your-health/quarantine-isolation.html

import jetson.inference
import jetson.utils
import time

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPPS".format(net.GetNetworkFPS()))
	time.sleep(2)
	for detection in detections:
		if net.GetClassDesc(detection.ClassID) == "person":
			running = True
			while running == True:
				exposure_status = input("Have you recently been in close contact with someone who has COVID-19, felt any symptoms of COVID-19, or tested positive for COVID-19? ('Y' or 'N') ")
				if exposure_status.lower() == "y":
					vaccination_status = input("Are you up to date on your COVID-19 vaccinations or have you tested positive for COVID-19 in the past 90 days? ('Y' or 'N') ")
					if vaccination_status.lower() == "y":
						print("You do not need to quarantine unless you develop symptoms. It is recommended you get tested at least 5 days after exposure unless you had COVID-19 in the past 90 days.")
						running = False
					elif vaccination_status.lower() == "n":
						print("Quarantine for at least 5 days and get tested at least 5 days after exposure.")
						running = False
					else:
						print("Sorry, I did not understand.")
				elif exposure_status.lower() == "n":
					vaccination_status = input("Are you up to date on your COVID-19 vaccinations or have you tested positive for COVID-19 in the past 90 days? ('Y' or 'N') ")
					if vaccination_status.lower() == "y":
						print("You do not need to quarantine. Make sure to wear a well-fitting mask!")
						running = False
					elif vaccination_status.lower() == "n":
						print("You do not need to quarantine, but for your safety it is strongly advised you get fully vaccinated.")
						running = False
					else:
						print("Sorry, I did not understand.")
				else:
					print("Sorry, I did not understand.")
			time.sleep(3)
			print("Refer to the CDC's updated Quarantine and Isolation website for further information: https://www.cdc.gov/coronavirus/2019-ncov/your-health/quarantine-isolation.html")
