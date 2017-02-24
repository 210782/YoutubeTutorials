from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from threading import Thread
import requests
from bs4 import BeautifulSoup
import time
import re

class SneakerBot:
	def __init__(self, master): # Initialize Window
		frame = Frame(master)
		frame.pack()

		# Username Entry
		self.usernameLabel = Label(frame, text="Username")
		self.usernameLabel.pack(side=TOP,padx=10,pady=2)
		self.username = Entry(frame, textvariable="username")
		self.username.pack(side=TOP,padx=10,pady=2)

		# Password Entry
		self.passwordLabel = Label(frame, text="Password")
		self.passwordLabel.pack(side=TOP,padx=10,pady=2)
		self.password = Entry(frame, textvariable="password", show="*")
		self.password.pack(side=TOP,padx=10,pady=2)

		# Item Entry
		self.itemURLLabel = Label(frame, text="Item URL")
		self.itemURLLabel.pack(side=TOP,padx=10,pady=2)
		self.itemURL = Entry(frame, textvariable="itemURL")
		self.itemURL.pack(side=TOP,padx=10,pady=2)

		# Size Entry
		self.sizeLabel = Label(frame, text="Item Size")
		self.sizeLabel.pack(side=TOP,padx=10,pady=2)
		self.size = Entry(frame, textvariable="size")
		self.size.pack(side=TOP,padx=10,pady=2)

		# Login/Checkout Button
		self.printButton = Button(frame, text = "Check me out", command = self.Login)
		self.printButton.pack(side=TOP,padx=10,pady=10)

	def Login(self): # Login Function
		# Start session
		browser = webdriver.Chrome()
		browser.get(self.itemURL.get())

		# Select size
		select = Select(browser.find_element_by_id("commodity-show-form-size"))
		select.select_by_visible_text(self.size.get())

		# Add to cart
		add = browser.find_element_by_id("commodity-show-addcart-submit")
		add.click()

		# Wait for 5sec to load login page & load page
		time.sleep(1)
		x = browser.get("http://www.nakedcph.com/login?popup=1")

		# Look for username field
		lod_id = browser.find_element_by_xpath("/html/body/div/form/ul/li[1]/input")
		lod_id.send_keys(self.username.get())

		# Look for password field
		p_id = browser.find_element_by_xpath("/html/body/div/form/ul/li[2]/input")
		p_id.send_keys(self.password.get())
		p_id.send_keys(Keys.ENTER)

		# Log in
		browser.get(self.itemURL.get())

		# Load cart
		time.sleep(1)
		x = browser.get("http://www.nakedcph.com/checkout/details")

		# Look for email repeat
		remail_id = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div/form/ul/li[2]/input")
		remail_id.send_keys(self.username.get())
		remail_id.send_keys(Keys.ENTER)
		var = input("")

		browser.quit()

root = Tk()
b = SneakerBot(root)
root.title("Sneaker Bot")
root.mainloop()
