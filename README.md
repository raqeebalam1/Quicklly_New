Commands format for pytest:
pytest ./(path with python file name) --html= (Name of html file you want to create)

Catering:  pytest .\tests\Departments\Catering\testing_ShopWithCatering.py --html=Catering.html
Food:  pytest .\tests\Departments\Food\testing_ShopWithFood.py --html=food.html
Grocery:  pytest .\tests\Departments\Grocery\testing_ShopWithGrocery.py --html=grocery.html

P.S: Just change path for every python file.
