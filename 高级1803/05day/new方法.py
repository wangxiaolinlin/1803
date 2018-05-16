class MusicPlayer(object):
	def __new__(cls,*args,**kwargs):
		return super().__new__(cls)
	def __init__(self):
		print("初始化音乐播放器")
player = MusicPlayer()
print(player)
