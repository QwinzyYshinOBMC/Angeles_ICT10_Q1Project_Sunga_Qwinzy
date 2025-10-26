from pyscript import document, display


def create_order(e):
    #Get input values
    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")
    item6 = document.getElementById("item6")
    item7 = document.getElementById("item7")
    item8 = document.getElementById("item8")
    item9 = document.getElementById("item9")
    item10 = document.getElementById("item10")
    item11 = document.getElementById("item11")
    item12 = document.getElementById("item12")
    item13 = document.getElementById("item13")
    item14 = document.getElementById("item14")
    item15 = document.getElementById("item15")
    item16 = document.getElementById("item16")
    item17 = document.getElementById("item17")
    item18 = document.getElementById("item18")
    item19 = document.getElementById("item19")
    item20 = document.getElementById("item20")


    #Calculate total price
    #Multiply the value of each item by 1 if checked, otherwise 0
    total = (
        float(item1.value) * item1.checked +
        float(item2.value) * item2.checked +
        float(item3.value) * item3.checked +
        float(item4.value) * item4.checked +
        float(item5.value) * item5.checked +
        float(item6.value) * item6.checked +
        float(item7.value) * item7.checked +
        float(item8.value) * item8.checked +
        float(item9.value) * item9.checked +
        float(item10.value) * item10.checked +
        float(item11.value) * item11.checked +
        float(item12.value) * item12.checked +
        float(item13.value) * item13.checked +
        float(item14.value) * item14.checked +
        float(item15.value) * item15.checked +
        float(item16.value) * item16.checked +
        float(item17.value) * item17.checked +
        float(item18.value) * item18.checked +
        float(item19.value) * item19.checked +
        float(item20.value) * item20.checked
    )


    #Get customer details
    customer_name = document.getElementById("customer").value
    customer_address = document.getElementById("address").value
    contact_number = document.getElementById("contact_number").value


    #Display order summary
    display(f"Order for: {customer_name}", target="order_output1")
    display(f"Address: {customer_address}", target="order_output2")
    display(f"Contact number: {contact_number}", target="order_output3")
    display(f"Total: ₱ {total:.2f}", target="show")