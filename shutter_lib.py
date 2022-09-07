from ophyd import Device, EpicsSignal, EpicsSignalRO
from ophyd import Component as Cpt

class ShutterDevice(Device):
  status = Cpt(EpicsSignalRO, '{Galil:2}SHUT_STATUS') #XF:19IDC-ES{Galil:2}SHUT_STATUS
  open_pos = Cpt(EpicsSignalRO, '{Gon:1-Sht}Pos:Opn-I') #XF:19IDC-ES{Gon:1-Sht}Pos:Opn-I
  close_pos = Cpt(EpicsSignalRO, '{Gon:1-Sht}Pos:Cls-I') #XF:19IDC-ES{Gon:1-Sht}Pos:Cls-I
  command = Cpt(EpicsSignal, '{Galil:2}SHUT_CMD') #XF:19IDC-ES{Galil:2}SHUT_CMD

  def shutter_status():
    return status.read()['value']

  def open_shutter():
    #VEnum[Open(1)] open_pos for NYX
    command.set(open_pos.read()['value']).wait()

  def close_shutter():
    #VEnum[Close(0)] close_pos for NYX
    command.set(close_pos.read()['value']).wait()
