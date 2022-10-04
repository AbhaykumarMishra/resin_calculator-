from tkinter import * 
from tkinter import messagebox ,filedialog
import os 
from datetime import date 
#generate fuunction 





def generate():
	

	try : 
		consumption = int(water_entry.get())
		Tds = int(tds_entry.get())
		recharge_day = int(recharge_entry.get())
		if Tds >= 150:
			# recharge_day = int(recharge_entry.get())
			message = f'''                                                           

		      	                                                          Date : { date.today()}
                                                                


			Design A Water softener for daily {consumption} Liter per day and 
			The total hardness {Tds} Ppm
			----------------------------------------------------------------------------
			Water Consuption per day     : {consumption}
			Recharge period in every     : {recharge_day} days 
			Water Tds                    : {Tds} Ppm 

		
			Design Flow : ( Convert water consuption in to gallons)
			----------------------------------------------------------------------------
			Daily Consuption             : {consumption}
			Design Flow-1                : {consumption} consuption x {recharge_day} recharge day 
			(Total consumption into ltr)   {consumption*recharge_day} L 
		
			Design Flow-2                : Design Flow-1 / 3.785ltr  (3.785ltr= 1 gallons)
			(Total consumption into G)   : {consumption*recharge_day/3.785} Gallons

		
			Convert the total hardness to grain per gallons 
			----------------------------------------------------------------------------
			Total hardness               : {Tds/17.14} GPG

			Hence in order to soft 1 gallons of water we need {Tds/17.14} grain of resin

		
			Total number of grain required 
			-----------------------------------------------------------------------------
			Safety Factor                : 1.2
			Softnear Capacity            : {(consumption*recharge_day/3.785)*(Tds/17.14)*1.2} grains

		
			Quantity of resign required for {consumption} per day 
			Each and one Cubic feet high capacity can remove resin 30000 grains 
			-----------------------------------------------------------------------------
			Cubic ft resign              : {((consumption*recharge_day/3.785)*(Tds/17.14)*1.2)/30000}
			Resign into Ltr or kg        : {(((consumption*recharge_day/3.785)*(Tds/17.14)*1.2)/30000)*28.3168}	



			Purelife filtration pvt.ltd 
			-------------------------------------------------------------------------------
			Shop No 007, Mathura Complex, 2, BP Rd, Venkateshwar Nagar, 
			Bhayandar East, Mumbai, Maharashtra 401105
			Tell: 9004030985, web: www.purelifefiltration.in 
		

			'''

			displaye_result.config(state='normal')
			displaye_result.delete('1.0',END)
			displaye_result.insert('1.0',message)
			displaye_result.config(state='disable')
		else:
			messagebox.showinfo(title='TDS of water : '+str(Tds),message='there is no requirment of water softener')


	except : 
		messagebox.showinfo(title='Showinfo',message='Kindly fill all area and only number ')


# clear function 
def all_clear():
	water_entry.delete(0,END)
	tds_entry.delete(0,END)
	recharge_entry.delete(0,END)
	displaye_result.config(state='normal')
	displaye_result.delete('1.0',END)
	displaye_result.config(state='disable')


# Report 
def save_file():
	try : 
		consumption = int(water_entry.get())
		Tds = int(tds_entry.get())
		recharge_day = int(recharge_entry.get())
		if Tds >= 150:
			message = f''' 

			                                                                Date : {date.today()}

			Design A Water softener for daily {consumption} Liter per day and 
			The total hardness {Tds} Ppm
			----------------------------------------------------------------------------
			Water Consuption per day     : {consumption}
			Recharge period in every     : {recharge_day} days 
			Water Tds                    : {Tds} Ppm 

		
			Design Flow : ( Convert water consuption in to gallons)
			----------------------------------------------------------------------------
			Daily Consuption             : {consumption}
			Design Flow-1                : {consumption} consuption x {recharge_day} recharge day 
			(Total consumption into ltr)   {consumption*recharge_day} L 
		
			Design Flow-2                : Design Flow-1 / 3.785ltr  (3.785ltr= 1 gallons)
			(Total consumption into G)   : {consumption*recharge_day/3.785} Gallons

		
			Convert the total hardness to grain per gallons 
			----------------------------------------------------------------------------
			Total hardness               : {Tds/17.14} GPG

			Hence in order to soft 1 gallons of water we need {Tds/17.14} grain of resin

		
			Total number of grain required 
			-----------------------------------------------------------------------------
			Safety Factor                : 1.2
			Softnear Capacity            : {(consumption*recharge_day/3.785)*(Tds/17.14)*1.2} grains

		
			Quantity of resign required for {consumption} per day 
			Each and one Cubic feet high capacity can remove resin 30000 grains 
			-----------------------------------------------------------------------------
			Cubic ft resign              : {((consumption*recharge_day/3.785)*(Tds/17.14)*1.2)/30000}
			Resign into Ltr or kg        : {(((consumption*recharge_day/3.785)*(Tds/17.14)*1.2)/30000)*28.3168}	



			Purelife filtration pvt.ltd 
			-------------------------------------------------------------------------------
			Shop No 007, Mathura Complex, 2, BP Rd, Venkateshwar Nagar, 
			Bhayandar East, Mumbai, Maharashtra 401105
			Tell: 9004030985, web: www.purelifefiltration.in 

			'''

			displaye_result.config(state='normal')
			displaye_result.delete('1.0',END)
			displaye_result.insert('1.0',message)
			displaye_result.config(state='disable')
			save_file = filedialog.asksaveasfile(defaultextension = '.txt',
				filetypes=[('All pdf file','*.txt')],
				title='Save File',
				)
			if save_file is None:
				return
			save_file.write(message)
			save_file.close()
		else:
			messagebox.showinfo(title='TDS of water : '+str(Tds),message='there is no requirment of water softener')


	except : 
		messagebox.showinfo(title='Showinfo',message='Kindly fill all area and only number ')



win =Tk()
win.configure(bg='#e9f5fd')
win.title('RESIN CALCULATOR ')

name_label = Label(win,text="RESIN CALCULATOR BY PURELIFE FILTRAION PVT LTD",font = ('Arial',20,'bold','underline'), fg='#005b94',bg='#e9f5fd')
name_label.pack(pady=5)

text_area_frame = Frame(win)
text_area_frame.pack(expand=True)

scrollbar = Scrollbar(text_area_frame)
scrollbar.pack(side='right',fill=Y)

displaye_result = Text(text_area_frame,width=120,height=30,bg='white',yscrollcommand=scrollbar.set)
displaye_result.pack(fill='both')
displaye_result.config(state='disable')
displaye_result.tag_configure("center", justify='center')
scrollbar.config(command=displaye_result.yview)


#label frame 
widget_display_frame = Frame(win,bg='#e9f5fd')
widget_display_frame.pack()

#all label 
water_label = Label(widget_display_frame,text='DAILY CONSUMTION',bd=5,bg='#005b94',fg='white',width=30,)
water_label.pack(side='left',padx=5,pady=4)

Recharge = Label(widget_display_frame,text='RECHARGE / DAY',padx=5,bd=5 ,bg='#005b94',fg='white',width=30)
Recharge.pack(side='left',padx=5,pady=4)

Tds_label = Label(widget_display_frame,text='TDS PPM',padx=5,bd=5,width=30,bg='#005b94',fg='white')
Tds_label.pack(side='left',padx=5,pady=4)

# entry frame 
entry_frame = Frame(win,bg='#e9f5fd')
entry_frame.pack()


water_entry = Entry(entry_frame,width=30)
water_entry.pack(side='left',padx=5,pady=5)

recharge_entry = Entry(entry_frame,width=30,)
recharge_entry.pack(side='left',padx=5,pady=5)

tds_entry = Entry(entry_frame,width=30)
tds_entry.pack(padx=10,pady=5)

#button frame 
button_frame = Frame(win,bg='#e9f5fd')
button_frame.pack()

report= Button(button_frame,text='Generate Report',font=('Arial',13,'bold'),command=generate,bg='#005b94',fg='white')
report.pack(side='left',pady=5,padx=10)

save_repaort = Button(button_frame,text='Save report',font=('Arial',13,'bold'),command=save_file,bg='#005b94',fg='white')
save_repaort.pack(side='left',pady=5,padx=10)

clear = Button(button_frame,text='Clear',font=('Arial',13,'bold'),command=all_clear,bg='#005b94',fg='white')
clear.pack(side='left',pady=5,padx=10)


Abhay = Label(win,text='Design by abhay ',bg='#e9f5fd')
Abhay.pack(side='right')
win.mainloop()
