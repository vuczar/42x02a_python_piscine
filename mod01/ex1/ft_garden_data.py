class Plant:
	name: str
	height: int
	age: int
	def show(plant):
		print(f"{plant.name}: {plant.height}cm, {plant.age} days")

def	main():
	plant1 = Plant()
	plant2 = Plant()
	plant3 = Plant()
	plant1.name = "Rose"
	plant1.height = 25
	plant1.age = 30


if __name__ == "__main__":
	main()
