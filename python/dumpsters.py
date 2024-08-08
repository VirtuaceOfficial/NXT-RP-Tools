print("Dumpsters Probability Calculator\n")

##################################################
######                                      ######
######     MAIN DUMPSTER TRACKER SCRIPT     ######
######                                      ######
##################################################

class ItemTracker:
    def __init__(self):
        self.total_Rubber = 0
        self.total_Scrap = 0
        self.total_Steel = 0
        self.num_inputs = 0

    def add_items(self, Rubber, Scrap, Steel):
        self.total_Rubber += Rubber
        self.total_Scrap += Scrap
        self.total_Steel += Steel
        self.num_inputs += 1

    def display_totals_and_averages(self):
        if self.num_inputs == 0:
            avg_Rubber = avg_Scrap = avg_Steel = 0
        else:
            avg_Rubber = self.total_Rubber / self.num_inputs
            avg_Scrap = self.total_Scrap / self.num_inputs
            avg_Steel = self.total_Steel / self.num_inputs

        print(f"\nTotal Rubber: {self.total_Rubber}")
        print(f"Total Scrap: {self.total_Scrap}")
        print(f"Total Steel: {self.total_Steel}\n")
        print(f"Number of Inputs: {self.num_inputs}\n")
        print(f"Average Rubber: {avg_Rubber:.2f}")
        print(f"Average Scrap: {avg_Scrap:.2f}")
        print(f"Average Steel: {avg_Steel:.2f}\n\n")

def main():
    tracker = ItemTracker()
    while True:
        try:
            Rubber = float(input("Enter the amount of Rubber: "))
            Scrap = int(input("Enter the number of Scrap: "))
            Steel = int(input("Enter the number of Steel: "))
            tracker.add_items(Rubber, Scrap, Steel)
            tracker.display_totals_and_averages()
        except ValueError:
            print("Invalid input, please enter numeric values.")

if __name__ == "__main__":
    main()
