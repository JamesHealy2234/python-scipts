def ground_shipping_cost(weight):
    if weight<=2:
        return 1.5 * weight + 20
    elif weight <=6:
        return 3.0 * weight + 20
    elif weight <=10:
        return 4.0 * weight  + 20
    else: 
        return 4.75 * weight  +20
    
def drone_shipping_cost(weight):
    if weight <=2:
        return 4.5 * weight
    elif weight <=6:
        return 9.0 * weight
    elif weight <=10:
        return 12.0 * weight
    else:
        return 14.25 * weight

def cheapest_shipping_method(weight):
    ground = ground_shipping_cost(weight)
    drone = drone_shipping_cost(weight)
    premium = 125.00

    if ground<min (drone,premium):
        return "Ground shipping" , ground
    elif drone < min (ground,premium):
        return "drone Shipping", drone 
    else:
        return "ground shipping Premium", premium
    
try:
    weight = float(input("Enter the weight of your package in pounds: "))
    if weight <= 0:
        print("Weight must be a positive number.")
    else:
        method, cost = cheapest_shipping_method(weight)
        print(f"The cheapest shipping method is: {method}")
        print(f"The cost to ship your package is: ${cost:.2f}")
except ValueError:
    print("Please enter a valid number for weight.")