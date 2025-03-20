def main():
    # Initialize an empty dictionary to store fruit data
    fruits = {}

    # Get the number of fruits to input (input statement). This will be the 
    # number of sets of data you need to collect.
    num_fruits = int(input("How many fruits would you like to enter? "))
    #fruitList = ['apple', 'orange', 'banana', 'cherry', 'blueberry', 'raspberry', 'strawberry', 'pineapple', 'grape', 'mango', 'kiwi', 'cantaloupe', 'lemon', 'melon', 'olive', 'pear', 'raisin', 'eggplant', 'pumpkin', 'peach', 'plum', 'almond', 'coconut', 'tangerine', 'papaya', 'santol', 'soursop', 'quince', 'pomegranate', 'honeydew', 'lime', 'lychee']
    
    # Collect data for the number of fruits above from the user. Should include name, color, 
    # weight in lbs, and price. Once each set of data points is collected
    # Think about what kind of control structure to create to complete this process
    for x in range(num_fruits):
        name = input("Enter the fruit's name: ").strip()
        color = input(f"Enter the color of {name}: ").strip()
        weight = float(input(f"Enter the average weight of {name} (in lbs): "))
        price = float(input(f"Enter the average price per pound of {name} ($): \n"))


        # Store the data
        fruits[name] = {
            'Color': color,
            'Average Weight': weight,
            'Price per Pound': price
        }

    # Output the fruit data
    print("\nFruit Data Overview\n")

    for fruit, details in fruits.items():
        print(f"Fruit: {fruit}")
        print(f"Color: {details['Color']}")
        print(f"Average Weight: {details['Average Weight']}")
        print(f"Price per Pound: ${details['Price per Pound']}")
        print("-" * 20)
        
        # After each set of input statements, store the data in the dictionary
        

    

    # Output each of the fruit's data as a vertical list. This happens one time
    # for each of the fruits in the dictionary. 
    

if __name__ == "__main__":
    main()

