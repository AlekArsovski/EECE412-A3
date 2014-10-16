# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import socket
from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib

import thread
from random import randrange

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Group 19 - VPN", pos = wx.DefaultPosition, size = wx.Size( 1107,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.tcpSetup = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.tcpSetup, wx.ID_ANY, u"Client/Server Setup" ), wx.VERTICAL )
        
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_server = wx.RadioButton( self.tcpSetup, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        bSizer15.Add( self.m_server, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_client = wx.RadioButton( self.tcpSetup, wx.ID_ANY, u"Client", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_client, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        sbSizer1.Add( bSizer15, 1, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.tcpSetup, wx.ID_ANY, u"Local IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer10.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.m_local_ip = wx.StaticText( self.tcpSetup, wx.ID_ANY, u"IP Address", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_local_ip.Wrap( -1 )
        bSizer10.Add( self.m_local_ip, 1, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.tcpSetup, wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.m_ip = wx.TextCtrl( self.tcpSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_ip, 1, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.tcpSetup, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.m_port = wx.TextCtrl( self.tcpSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_port, 1, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.tcpSetup, wx.ID_ANY, u"Shared\nSecret", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer9.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.m_secret = wx.TextCtrl( self.tcpSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_secret, 1, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )




        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self.tcpSetup, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer16.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self.m_status = wx.StaticText( self.tcpSetup, wx.ID_ANY, u"Not Set", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_status.Wrap( -1 )
        bSizer16.Add( self.m_status, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer16, 0, wx.EXPAND, 5 )
        
        self.m_set = wx.Button( self.tcpSetup, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_set, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.tcpSetup.SetSizer( sbSizer1 )
        self.tcpSetup.Layout()
        sbSizer1.Fit( self.tcpSetup )
        bSizer1.Add( self.tcpSetup, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Send/Receive" ), wx.VERTICAL )
        
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Data to be Sent (719 character maximum)" ), wx.VERTICAL )
        
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_sendBox = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
        self.m_sendBox.SetMaxLength( 719 ) 
        bSizer12.Add( self.m_sendBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_send = wx.Button( self.m_panel2, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_send, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer5.Add( bSizer12, 1, wx.EXPAND, 5 )
        
        
        sbSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )
        
        
        sbSizer2.AddSpacer( ( 20, 50), 0, 0, 5 )
        
        sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Data Received" ), wx.VERTICAL )
        
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_received = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer13.Add( self.m_received, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer7.Add( bSizer13, 1, wx.EXPAND, 5 )
        
        
        sbSizer2.Add( sbSizer7, 1, wx.EXPAND, 5 )
        
        
        self.m_panel2.SetSizer( sbSizer2 )
        self.m_panel2.Layout()
        sbSizer2.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Log" ), wx.VERTICAL )
        
        self.m_log = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        sbSizer3.Add( self.m_log, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_continue = wx.Button( self.m_panel3, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer3.Add( self.m_continue, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_enable = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Enable Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer3.Add( self.m_enable, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.m_panel3.SetSizer( sbSizer3 )
        self.m_panel3.Layout()
        sbSizer3.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_timer = wx.Timer()
        self.m_timer.SetOwner( self, wx.ID_ANY )
        self.m_timer.Start( 250 )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.cleanUP )
        self.m_server.Bind( wx.EVT_RADIOBUTTON, self.setServer )
        self.m_client.Bind( wx.EVT_RADIOBUTTON, self.setClient )
        self.m_set.Bind( wx.EVT_BUTTON, self.setupVPN )
        self.m_send.Bind( wx.EVT_BUTTON, self.send )
        self.m_continue.Bind( wx.EVT_BUTTON, self.step )
        self.m_enable.Bind( wx.EVT_CHECKBOX, self.enableStep )
        self.Bind( wx.EVT_TIMER, self.checkVPN, id=wx.ID_ANY )

    
    def __del__( self ):
        pass
    
    


class VPN(MyFrame1):
    isClient = False
    
    sharedKey = ''
    plaintext = ''
    received = ''
    log = ''
    status = False
    BLOCK_SIZE=16
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    state = 0
    clientID = randrange(11111,99999)
    serverID = "server"
    challenge = ''

    BS = 16





    #constructor
    def __init__(self,parent):
        #initialize parent class
        MyFrame1.__init__(self,parent)
 
    # Virtual event handlers, overide them in your derived class

    def server(self):
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        while 1:
            self.data1 = self.conn.recv(1024)

            if self.data1:

                if self.state == 0:
                    self.clientID = self.data1[:5]
                    self.challenge = self.data1[5:]
                    self.conn.send("challenge_"+str(int(self.m_port.Value)+1)+self.encrypt(self.serverID+self.m_port.Value+"challenge_"+self.m_port.Value+str(19), self.sharedKey))
                    self.state = 1
                elif self.state == 1:
                    self.data1, flag = self.decrypt(self.data1,self.sharedKey)
                    if flag:self.m_status.Label = "Channel Compromised!!!!!!!!! ABORT ABORT!!!"
                    if str(self.clientID)+"challenge_"+str(int(self.m_port.Value)+1)+str(8) != self.data1:
                        self.m_status.Label = "Channel Compromised!!!!!!!!! ABORT ABORT!!!"
                    else:
                        self.m_status.Label = "Server-mode: Authenticated"
                        self.sharedKey = hashlib.sha256('2').digest()
                        self.state = 2
                elif self.state == 2:
                    self.data1, flag = self.decrypt(self.data1,self.sharedKey)
                    if flag:self.m_status.Label = "Channel Compromised!!!!!!!!! ABORT ABORT!!!"
                    self.m_received.Value += self.data1+"\n"
        
            # conn.close()
    def client(self):
        self.s.send(str(self.clientID)+"challenge_"+self.m_port.Value)
        while 1:
            self.data2 = self.s.recv(1024)

            if self.data2:
                if self.state == 0:
                    self.challenge = self.data2[:len('challenge_'+str(int(self.m_port.Value)+1))]
                    self.data2, flag = self.decrypt(self.data2[len('challenge_'+str(int(self.m_port.Value)+1)):],self.sharedKey)
                    if flag:self.m_status.Label = "1Channel Compromised!!!!!!!!! ABORT ABORT!!!"
                    if self.serverID+self.m_port.Value != self.data2[:len(self.serverID+self.m_port.Value)]:
                        self.m_status.Label = "2Channel Compromised!!!!!!!!! ABORT ABORT!!!"
                    else:
                        print "challenge_"+str(self.m_port.Value)
                        print self.data2 
                        if "challenge_"+str(self.m_port.Value) != self.data2[len(self.serverID+str(self.m_port.Value)):len("challenge_"+self.m_port.Value+self.serverID+self.m_port.Value)]:
                            self.m_status.Label = "3Channel Compromised!!!!!!!!! ABORT ABORT!!!"
                        else:
                            self.s.send(self.encrypt(str(self.clientID)+self.challenge+str(8),self.sharedKey))
                            self.m_status.Label = "Client-mode: Authenticated"
                            self.state = 1
                            self.sharedKey = hashlib.sha256('2').digest()
                elif self.state == 1:
                    self.data2, flag = self.decrypt(self.data2,self.sharedKey)
                    if flag:self.m_status.Label = "Channel Compromised!!!!!!!!! ABORT ABORT!!!"
                    self.m_received.Value += self.data2+"\n"




        
            # conn.close()

    def cleanUP( self, event ):
        self.m_timer.Stop()
        self.s.close()
        self.Destroy()
    
    def setServer( self, event ):
        self.isClient = False
    
    def setClient( self, event ):
        self.isClient = True
    
    def setupVPN( self, event ):
        
        if self.isClient:
            
            try:
                
                if self.sharedKey == None:
                    raise Exception()
                test = self.s.connect((self.m_ip.Value, int(self.m_port.Value)))

                
                self.socket = True
                self.m_status.Label = 'Client-mode'
                self.status = True
                self.sharedKey =  hashlib.sha256(self.m_secret.Value).digest()
                thread.start_new_thread( self.client,() )
                
            except:
                
                self.m_status.Label = 'Error!'
                self.status = False    

        else:
            try:
                if self.sharedKey == None:
                    raise Exception()
            
                self.s.bind((self.m_ip.Value, int(self.m_port.Value)))
                

                
                self.socket = True
                self.m_status.Label = 'Server-mode'
                self.status = True
                self.sharedKey =  hashlib.sha256(self.m_secret.Value).digest()
                thread.start_new_thread( self.server,() )
            except:
                self.m_status.Label = 'Error!'
                self.status = False  
                

            
            
    
    def send( self, event ):
        try:
            self.s.send(self.encrypt(self.m_sendBox.Value,self.sharedKey))
        except:
            self.conn.send(self.encrypt(self.m_sendBox.Value,self.sharedKey))
        self.m_sendBox = ''
    
    def step( self, event ):
        event.Skip()
    
    def enableStep( self, event ):
        event.Skip()

    def checkVPN( self, event ):
        event.Skip()

    def encrypt(self, plaintext, privateKey):
        plaintext = self.pad(plaintext)
        iv = Random.new().read(AES.block_size)
        ciphertext = AES.new(privateKey, AES.MODE_CBC, iv)
        return hashlib.sha1(plaintext).hexdigest()+base64.b64encode(iv + ciphertext.encrypt(plaintext))

    def decrypt(self, ciphertext, privateKey):
        mac = ciphertext[:40]
        ciphertext = base64.b64decode(ciphertext[40:])
        iv = ciphertext[:16]
        plaintext = AES.new(privateKey, AES.MODE_CBC, iv)
        plaintext = self.unpad(plaintext.decrypt(ciphertext[16:]))
        flag = (mac == hashlib.sha1(plaintext).hexdigest())
        return (plaintext,flag)

    pad = lambda self,s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS) 
    unpad = lambda self,s : s[0:-ord(s[-1])]

 
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = VPN(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
