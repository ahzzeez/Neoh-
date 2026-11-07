import customtkinter 
import subprocess
def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.title("Neoh!")
app.geometry("500x500")

def toggle_action():
    '''Changes functionality and interface based on switch value'''
    if(switch.get() == 0):
        switch.configure(text = "USB")
    else: 
        switch.configure(text = "Bluetooth")
        def check_devices():
            ps_command = "powershell Get-PnpDevice -Class AudioEndpoint | Select-Object Name, Status"
            with open("demofile.txt", "a") as f:
                data = subprocess.check_output(ps_command, text = True)  
                f.write(str(data)) 
            with open("demofile.txt", "r") as f:
                print(f.readlines())
            print(data)
    check_devices();



switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="USB", 
                                 variable=switch_var, onvalue=1, offvalue=0, command = toggle_action)



button = customtkinter.CTkButton(app, text="my button", command=button_callback)
switch.pack()
button.pack(padx=20, pady=20)

app.mainloop()
