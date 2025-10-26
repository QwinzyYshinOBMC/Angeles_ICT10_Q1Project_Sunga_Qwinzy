from pyscript import display

#String: Name of the restaurant
restaurant_name=""

#String: Owner of the restaurant
owner="Qwinzy Yshin S. Sunga"

#Int: Year of the restaurant established
year_since= 1978

#Float
tax_rate= 0.08

delivery= True
dine_in= True
take_out= True

#List: Name of products on the menu
product_names= [ "Chocolate Fudge Cake" ,
    "Vanilla Butter Cake" ,
    "Red Velvet Cake" ,
    "Ube Cake" ,
    "Carrot Cake" ,
    "Mocha Cake" ,
    "Mango Cream Cake" ,
    "Cookies and Cream Cake" ,
    "Lemon Chiffon Cake" ,
    "Black Forest Cake" ,
    "Salted Caramel Cupcake" ,
    "Strawberry Shortcake Cupcake" ,
    "Chocolate Peanut Butter Cupcake" ,
    "Matcha Green Tea Cupcake" ,
    "Cookies and Cream Cupcake" ,
    "Banoffee Cupcake" ,
    "Blueberry Cheesecake Cupcake" ,
    "Choco Mint Cupcake" ,
    "Coconut Pandan Cupcake" ,
    "S’mores Cupcake" ]

#Tuple: Business operating hours
business_hours=("10:00AM", "11:00PM")

#Dictionary: Menu items and their prices
menu={
    "Chocolate Fudge Cake" : 780,
    "Vanilla Butter Cake" : 950,
    "Red Velvet Cake" : 780,
    "Ube Cake" : 950,
    "Carrot Cake" : 780,
    "Mocha Cake" : 950,
    "Mango Cream Cake" : 780,
    "Cookies and Cream Cake" : 950,    
    "Lemon Chiffon Cake" : 780,
    "Black Forest Cake" : 950,
    "Salted Caramel Cupcake" : 780,
    "Strawberry Shortcake Cupcake" : 950,
    "Chocolate Peanut Butter Cupcake" : 780,
    "Matcha Green Tea Cupcake" : 950,
    "Cookies and Cream Cupcake" : 780,
    "Banoffee Cupcake" : 950,
    "Blueberry Cheesecake Cupcake" : 780,
    "Choco Mint Cupcake" : 950,
    "Coconut Pandan Cupcake" : 780,
    "S’mores Cupcake" : 950,
}

#Set: Common allergens present
common_allergens= {"gluten", "Dairy", "Nuts"}

display(restaurant_name, target="name1")
display(f"Owner: {owner}", target="owner")
display(f"Since: {year_since}", target="since")

display(f"", target="heading1")

display(product_names[0], target="prod1")
display(f"P{menu['Chocolate Fudge Cake']:.2f}", target="price1")

display(product_names[1], target="prod2")
display(f"P{menu['Vanilla Butter Cake']:.2f}", target="price2")

display(product_names[2], target="prod3")
display(f"P{menu['Red Velvet Cake']:.2f}", target="price3")

display(product_names[3], target="prod4")
display(f"P{menu['Ube Cake']:.2f}", target="price4")

display(product_names[4], target="prod5")
display(f"P{menu['Carrot Cake']:.2f}", target="price5")

display(product_names[5], target="prod6")
display(f"P{menu['Mocha Cake']:.2f}", target="price6")

display(product_names[6], target="prod7")
display(f"P{menu['Mango Cream Cake']:.2f}", target="price7")

display(product_names[7], target="prod8")
display(f"P{menu['Cookies and Cream Cake']:.2f}", target="price8")

display(product_names[8], target="prod9")
display(f"P{menu['Lemon Chiffon Cake']:.2f}", target="price9")

display(product_names[9], target="prod10")
display(f"P{menu['Black Forest Cake']:.2f}", target="price10")

display(product_names[10], target="prod11")
display(f"P{menu['Salted Caramel Cupcake']:.2f}", target="price11")

display(product_names[11], target="prod12")
display(f"P{menu['Strawberry Shortcake Cupcake']:.2f}", target="price12")

display(product_names[12], target="prod13")
display(f"P{menu['Chocolate Peanut Butter Cupcake']:.2f}", target="price13")

display(product_names[13], target="prod14")
display(f"P{menu['Matcha Green Tea Cupcake']:.2f}", target="price14")

display(product_names[14], target="prod15")
display(f"P{menu['Cookies and Cream Cupcake']:.2f}", target="price15")

display(product_names[15], target="prod16")
display(f"P{menu['Banoffee Cupcake']:.2f}", target="price16")

display(product_names[16], target="prod17")
display(f"P{menu['Blueberry Cheesecake Cupcake']:.2f}", target="price17")

display(product_names[17], target="prod18")
display(f"P{menu['Choco Mint Cupcake']:.2f}", target="price18")

display(product_names[18], target="prod19")
display(f"P{menu['Coconut Pandan Cupcake']:.2f}", target="price19")

display(product_names[19], target="prod20")
display(f"P{menu['S’mores Cupcake']:.2f}", target="price20")