# https://edabit.com/challenge/pa65DgwG5HMbtf6iY

class football_player_info:

	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight


	def get_age(self):
		return f"{self.name} is age {self.age}"


	def get_height(self):
		return f"{self.name} is {self.height} cm"


	def get_weight(self):
		return f"{self.name} weighs {self.weight} kg"		


player_one = football_player_info('josh spratt', 26, 168, 60)
player_two = football_player_info('kevin spratt', 29, 168, 57)
player_three = football_player_info('gary spratt', 56, 168, 66)

print(player_one.get_age())
print(player_two.get_age())
print(player_three.get_age())
print(player_one.get_height())
print(player_two.get_height())
print(player_three.get_height())
print(player_one.get_weight())
print(player_two.get_weight())
print(player_three.get_weight())
