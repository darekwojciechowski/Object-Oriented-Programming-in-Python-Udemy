from datetime import datetime
class Foto:

  exectuion_time = datetime.now().strftime('%H:%M:%S')
  fname = 'image_' + exectuion_time + '.png'

  def current_time():
    return datetime.now().strftime('%H_%M_%S')

Foto.__dict__

Foto.exectuion_time

Foto.current_time()