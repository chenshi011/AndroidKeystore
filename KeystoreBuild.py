#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*- 
'''
@author:     cs
'''
from Tkinter import *  
import tkMessageBox
import os,json,subprocess
import cmd

class KeystoreBuild:  
    def __init__(self):  
        self.window = Tk()                
        self.window.title("Key Creation")  
        self.window.minsize(300, 280)  
        self.center_wind(self.window, 300, 280)
        
        frame1 = Frame(self.window)       
        frame1.pack()                
        
        abspath = os.path.split(os.path.realpath(__file__))[0] + "/"
        with open(abspath + "KeystoreBuild.json", 'r') as js:
            json_data = json.load(js)  
         
        self.aliasN = json_data["alias"]["name"]
        self.aliasV = StringVar(value = json_data["alias"]["value"])
        self.storePasswordN = json_data["store_password"]["name"]
        self.storePasswordV = StringVar(value = json_data["store_password"]["value"])
        self.keyPasswordN = json_data["key_password"]["name"]
        self.keyPasswordV = StringVar(value = json_data["key_password"]["value"])  
        self.validityN = json_data["validity"]["name"]
        self.validityV = StringVar(value = json_data["validity"]["value"])
        self.FistLastNameN = json_data["FistLastName"]["name"]
        self.FistLastNameV = StringVar(value = json_data["FistLastName"]["value"])
        self.unitN = json_data["unit"]["name"]
        self.unitV = StringVar(value = json_data["unit"]["value"])  
        self.organizationN = json_data["organization"]["name"]
        self.organizationV = StringVar(value = json_data["organization"]["value"])
        self.cityN = json_data["city"]["name"]
        self.cityV = StringVar(value = json_data["city"]["value"])    
        self.provinceN = json_data["province"]["name"]
        self.provinceV = StringVar(value = json_data["province"]["value"])
        self.countryCodeN = json_data["countryCode"]["name"]
        self.countryCodeV = StringVar(value = json_data["countryCode"]["value"])
        self.savePathN = json_data["savePath"]["name"]
        self.savePathV = StringVar(value = json_data["savePath"]["value"])
        self.layout_input(frame1, json_data, [[self.aliasN, self.aliasV], [self.storePasswordN, self.storePasswordV], [self.keyPasswordN, self.keyPasswordV],
                                              [self.validityN, self.validityV], [self.FistLastNameN, self.FistLastNameV], [self.unitN, self.unitV],
                                              [self.organizationN, self.organizationV], [self.cityN, self.cityV], [self.provinceN, self.provinceV],
                                              [self.countryCodeN, self.countryCodeV], [self.savePathN, self.savePathV]])
        frame2 = Frame(self.window)        
        frame2.pack()            
        btGeneral = Button(frame2, text="生成", command=self.processButtonGeneral)  
        btGeneral.grid(row=1, column=1)   
        
        btCancel = Button(frame2, text="取消", command=self.processButtonCancel)  
        btCancel.grid(row=1, column=2)   
        
        # 监测事件直到window被关闭  
        self.window.mainloop()
    def center_wind(self, window, w = 300, h= 200):
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)   
        y = (hs/2) - (h/2)
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
           
    def layout_input(self, frame, json_data, keys):
        fontSize = 33
        index = 1
        for key in keys:
            lbl = Label(frame, text=key[0], font=fontSize)  
            entry = Entry(frame, textvariable = key[1], font=fontSize)  
            lbl.grid(row=index, column=1, sticky='e')  
            entry.grid(row=index, column=2)  
            index = index + 1
            
    def processButtonGeneral(self):  
        try:
            filepath = self.savePathV.get()
            fileName = "%s\%s" % (filepath , self.aliasV.get())
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            if os.path.isfile(fileName):
                print "%s is exists" % fileName
                tkMessageBox.showwarning("警告", "当前秘钥已经存在！");
            else:
                cmd = 'keytool -genkey -alias %s -keyalg RSA -validity %s -keystore %s -dname "CN=%s,OU=%s,O=%s,L=%s,ST=%s,C=%s" -keypass %s -storepass %s' % (self.aliasV.get(),self.validityV.get(), fileName,self.FistLastNameV.get(),self.unitV.get(),self.organizationV.get(),self.cityV.get(),self.provinceV.get(),self.countryCodeV.get(),self.keyPasswordV,self.storePasswordV.get())
                print cmd
                subprocess.check_output(cmd, shell=False)
                tkMessageBox.showinfo("消息", "生成秘钥成功，请妥善保管");
        except:
            tkMessageBox.showerror("错误", "生成秘钥失败，请检查参数");
            
    def processButtonCancel(self):
        self.window.quit()

if __name__ == "__main__":      
    KeystoreBuild()    
