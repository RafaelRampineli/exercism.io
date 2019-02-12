class SpaceAge(object):
	def __init__(self, seconds):
		self.seconds = seconds
		self.Earth_Seconds = 31557600		
		self.Earth_Days = 365.25
		self.Mercury_Days = 0.2408467
		self.Venus_Days = 0.61519726
		self.Mars_Days = 1.8808158
		self.Jupiter_Days = 11.862615
		self.Saturn_Days = 29.447498
		self.Uranus_Days = 84.016846
		self.Neptune_Days = 164.79132

	def on_mercury(self):
		return_var =(self.seconds/self.Earth_Seconds)/self.Mercury_Days
		return round(return_var,2)

	def on_venus(self):
		return_var =(self.seconds/self.Earth_Seconds)/self.Venus_Days
		return round(return_var,2)

	def on_earth(self):
		return_var =(self.seconds/self.Earth_Seconds)
		return round(return_var,2)

	def on_mars(self):
		return_var =(self.seconds/self.Earth_Seconds)/self.Mars_Days
		return round(return_var,2)

	def on_jupiter(self):
		return_var =(self.seconds/self.Earth_Seconds)/self.Jupiter_Days
		return round(return_var,2)

	def on_saturn(self):
		return_var =(self.seconds/self.Earth_Seconds)/self.Saturn_Days
		return round(return_var,2)

	def on_uranus(self):
		return_var =(self.seconds/self.Earth_Seconds)/self.Uranus_Days
		return round(return_var,2)

	def on_neptune(self):
		return_var =(self.seconds/self.Earth_Seconds)/self.Neptune_Days
		return round(return_var,2)

		
