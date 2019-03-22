from tkinter import *
import threading
import IoTMaster
import json

class app(Frame):

    def __init__(self, master):
        super().__init__(master)


        self.upload_data = Entry(self)
        self.label_1 = Label(self, text="Enter the value to be uploaded:")
        self.label_1.grid(row = 0, column = 0)
        self.upload_data.grid(row = 0, column = 1)


        self.button1 = Button(self, text="Upload Data", command=self.thingspeak_post)
        self.button1.grid(row = 1, columnspan = 2)

        self.get_data = Entry(self)
        self.label_2 = Label(self, text="Enter the number of values to be retrieved:")
        self.label_2.grid(row=3, column=0)
        self.get_data.grid(row=3, column=1)

        self.button2 = Button(self, text = "Get Data" , command = self.thingspeak_get)
        self.button2.grid(row = 4,columnspan = 2)

        self.quitButton = Button(self, text = "Quit" , command =self.quit)
        self.quitButton.grid(row = 5)

        self.pack()

    def thingspeak_post(self):
        # threading.Timer(60, thingspeak_post).start()

        self.distance = self.upload_data.get()
        # data = urllib.urlopen("https://api.thingspeak.com/update?api_key=94H9E5AMTQ8GMKF6&field1="+str(distance))
        self.ob = IoTMaster.Thingspeak(write_api_key="94H9E5AMTQ8GMKF6", read_api_key="EGAK6OZP7JY0KLDZ",
                                  channel_id="699618")
        self.ob.post_cloud(value1=self.distance, value2=0)

    def thingspeak_get(self):
        self.obj = IoTMaster.Thingspeak(write_api_key="94H9E5AMTQ8GMKF6", read_api_key="EGAK6OZP7JY0KLDZ",
                                  channel_id="699618")
        self.val = self.obj.read_cloud(result= self.get_data.get())
        print(self.val)

root = Tk()
n = app(root)
root.mainloop()