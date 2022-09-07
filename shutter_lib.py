from ophyd import Device, EpicsSignal, EpicsSignalRO
from ophyd import Component as Cpt

class ShutterDevice(Device):
  status = Cpt(EpicsSignalRO, '{Galil:2}SHUT_STATUS') #XF:19IDC-ES{Galil:2}SHUT_STATUS
  open_pos = Cpt(EpicsSignalRO, '{Gon:1-Sht}Pos:Opn-I') #XF:19IDC-ES{Gon:1-Sht}Pos:Opn-I
  close_pos = Cpt(EpicsSignalRO, '{Gon:1-Sht}Pos:Cls-I') #XF:19IDC-ES{Gon:1-Sht}Pos:Cls-I
  command = Cpt(EpicsSignal, '{Galil:2}SHUT_CMD') #XF:19IDC-ES{Galil:2}SHUT_CMD

  def get_status(self):
    return self.status.read()['shutter_status']['value']

  def open(self):
    #VEnum[Open(1)] open_pos for NYX
    self.command.set(self.open_pos.read()['shutter_open_pos']['value']).wait()

  def close(self):
    #VEnum[Close(0)] close_pos for NYX
    self.command.set(self.close_pos.read()['shutter_close_pos']['value']).wait()

  def get_close_pos(self):
    return self.close_pos.read()['shutter_close_pos']['value']

  def get_open_pos(self):
    return self.open_pos.read()['shutter_open_pos']['value']

  def is_open(self):
    return (self.status.read()['shutter_status']['value']==self.open_pos.read()['shutter_open_pos']['value']) 

  def is_closed(self):
    return (self.status.read()['shutter_status']['value']==self.close_pos.read()['shutter_close_pos']['value']) 
