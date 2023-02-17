#Paul Lorenz III

def get_miles_and_kilometers():

    display_message()

    try:

      miles_driven = int(input("\nPlease enter the total number of miles driven: "))

      convert_miles_to_kilometers(miles_driven)

    except:

      print("\nIncorrect input. Please use numbers instead of using letters or symbols to input the number of total miles.")
      print()

      get_miles_and_kilometers()
      
def display_message():
    print("Welcome to the miles and kilometers conversion program.")
    print("Notice that 1 mile equals 1.609 miles.")

def convert_miles_to_kilometers(miles):
    kilometers = miles * 1.609
    print(f"\nThe total number of miles driven is {miles} miles.")
    print(f"\nThe total number of kilometers driven is {kilometers} kilometers.")
    
get_miles_and_kilometers()

