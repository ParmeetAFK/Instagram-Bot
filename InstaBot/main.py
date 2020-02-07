from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from tkinter import *
from tkinter import messagebox
import time


class GUI_main:

	def __init__(self,master):

		self.head = Label(master ,
						  text="InstaBot",
						  font=('Algerian',25),
						  fg='#fff',
						  bg='black'
						  )

		self.head.grid(column=0,
					   row=0,
					   columnspan=2,
					   pady=8,
					   padx=8
					   )


		self.user = Label(master,
						  text="Username",
						  fg="#fff",
						  bg='black',
						  font=('Arial Bold',8)
						  )

		self.user.grid(column=0,
					   row=1,
					   pady=8,
					   padx=8)

		self.e1 = Entry(master)

		self.e1.grid(column=1,
					 row=1,
					 pady=8,
					 padx=8
					 )

		self.pas = Label(master,
						  text="Password",
						  fg="#fff",
						  bg='black',
						  font=('Arial Bold',8)
						  )

		self.pas.grid(column=0,
					  row=2,
					  pady=8,
					  padx=8)

		self.e2 = Entry(master,
						show="*"
						)

		self.e2.grid(column=1,
					 row=2,
					 pady=8,
					 padx=8
					  )

		self.hash = Label(master,
						  text='#_Hashtag',
						  font=('Arial Bold',8),
						  fg='#fff',
						  bg='black'
						  )

		self.hash.grid(column=0,
					   row=3,
					   pady=8,
					   padx=8)

		self.e3 = Entry(master)

		self.e3.grid(column=1,
					 row=3,
					 padx=8,
					 pady=8)


		self.num = Label(master,
						  text='Number of Posts',
						  font=('Arial Bold',8),
						  fg='#fff',
						  bg='black'
						  )

		self.num.grid(column=0,
					  row=4,
					  pady=8,
					  padx=8)

		self.e4 = Entry(master)

		self.e4.grid(column=1,
					 row=4,
					 pady=8,
					 padx=8
					 )

		self.butt = Button(master,
						   text="GO InstaBoy GO",
						   font=('Arial Bold',12),
						   bg="black",
						   fg="#fff",
						   command=self.mai)

		self.butt.grid(column=0,
					   row=5,
					   columnspan=2,
					   pady=8,
					   padx=10)

		self.mebut = Button(master,
                              text="ME",
                              bg='#fff',
                              fg='#000',
                              font=('Arial Bold',6),
                              relief='ridge',
                              bd=2,
                              command=self.mei
                              )

        
		self.mebut.grid(column=0,
                        row=6,
                        pady=10)


		self.mebut1 = Button(master,
                              text="ME44",
                              bg='#fff',
                              fg='#000',
                              font=('Arial Bold',6),
                              relief='ridge',
                              bd=2,
                              command=self.meab
                              )

		self.mebut1.grid(column=1,
						 row=6,
						 pady=10
						 )

	def mei(self):
		messagebox.showinfo( "Contact", "Please Contact the Developer \n\n Gmail - Parmeet757@gmail.com\n Watsapp - 8788042372\n GitHub - @ParmeetAFK\n")
		

	def meab(self):
		messagebox.showinfo("")

	def mai(self):

		messagebox.showinfo("Alert","Please Sit Back and Relax \n Bot might take some time to open Browser")

		self.username = self.e1.get()
		self.pas = self.e2.get()
		self.has = self.e3.get()
		self.no = int(self.e4.get())

		b.login(self.username,self.pas)
		b.search(self.has)
		for i in range(self.no):
			b.like_next()


class InstaBoy(GUI_main):

	def login(self, username, password):

		self.driver = webdriver.Firefox(executable_path = r"Z:\InstaBot\drivers\geckodriver.exe")

		self.driver.get("https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher")
		
		time.sleep(4)

		self.driver.find_element_by_name('username').send_keys(username)
		self.driver.find_element_by_name('password').send_keys(password)
		self.driver.find_element_by_name('password').send_keys(Keys.RETURN)

		time.sleep(4)

		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

		time.sleep(4)


	def search(self, item):

		self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(item)
		time.sleep(5)

		self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.RETURN)
		time.sleep(5)
		
		self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.RETURN)
		time.sleep(8)

		self.actions = ActionChains(self.driver) 
		self.actions.send_keys(Keys.TAB * 20)
		self.actions.send_keys(Keys.RETURN)
		self.actions.perform()
		time.sleep(5)


	def like_next(self):

		#self.wait = WebDriverWait(self.driver, 10)
		#self.men_menu = self.wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(@class,'FY9nT fr66n')]//button[contains(@class,'wpO6b')]")))
		time.sleep(5)
		self.driver.find_element_by_xpath("//button[contains(@class,'wpO6b')]").click()
		time.sleep(5)
		self.driver.find_element_by_xpath("//a[contains(@class,'HBoOv coreSpriteRightPaginationArrow')]").click()



	def open_fol(self):

		self.driver.find_element_by_xpath("//body/div[@id='react-root']/section[contains(@class,'_9eogI E3X2T')]/nav[contains(@class,'')]/div[contains(@class,'Cx7Bp')]/div[contains(@class,'_lz6s')]/div[contains(@class,'MWDvN')]/div[contains(@class,'ctQZg')]/div[contains(@class,'_47KiJ')]/div[3]/a[1]/*[1]").click()

		time.sleep(4)

		self.driver.find_element_by_xpath().click()



root = Tk()
root.title("Boy")
root.configure(background='#000')
b = InstaBoy(root)
root.mainloop()