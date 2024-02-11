from datetime import datetime

datetime.now().strftime('%H:%M:%S')

class Foto:

  exectuion_time = datetime.now().strftime('%H:%M:%S')
  fname = 'image_' + exectuion_time + '.png'

Foto.__dict__

class Foto:

  exectuion_time = datetime.now().strftime('%H:%M:%S')
  fname = 'image_' + exectuion_time + '.png'

  def current_time():
    return datetime.now().strftime('%H_%M_%S')

print(Foto.__dict__)

print(Foto.exectuion_time)

print(Foto.fname)

foto = Foto()
print(foto.exectuion_time)

print(Foto.__mro__)

print(Foto.mro())

print(help(Foto.mro))