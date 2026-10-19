class Plant():
    def __init__(self, name:str, height:float, age:int):
        self.name = name
        self.height = height
        self.age = age

def main() -> None:
    plant1 = Plant("Rose", 25.0, 30)
    

if __name__ == "__main__":
    main()

"""

Exercise3

ft_plant_factory

Directory: ex3/
Files to Submit: ft_plant_factory.py
Authorized: print(), range(), round()

The garden center needs to create many plants quickly using your Plant class with different starting values. You need to streamline the plant creation process: instantiate and
initialize the class for a new plant at the same time.

Requirements:
• Plants need to be created directly with their initial information (name, starting
height, starting age)
• Each plant should be ready to use immediately after construction (e.g., if you want
to make it grow())
• Create at least 5 different plants with varying characteristics
• Display all created plants in an organized format
Improve your Plant class from the previous exercises. Note that you may have already
streamlined your plant creation process in Exercise 1 if you were already familiar with
object-oriented programming.
13
Code Cultivation Object-Oriented Garden Systems

Example:
$> python3 ft_plant_factory.py
=== Plant Factory Output ===
Created: Rose: 25.0cm, 30 days old
Created: Oak: 200.0cm, 365 days old
Created: Cactus: 5.0cm, 90 days old
Created: Sunflower: 80.0cm, 45 days old
Created: Fern: 15.0cm, 120 days old


You should be able to use the show() method unchanged to display the
output above.
"""