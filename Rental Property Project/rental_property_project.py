# NOTES:
# from IPython.display import clear_output as clear

# IF TIME ALLOWS:
# creating an input for million$ homes, like, 1.5M (def rentalIncome)
# allowing % down payments (def initial_investments)
# commas in numbers vs having to enter straight numbers
# rent out vs sell (def rental_income)
# reusing "other rentals" to add more to the dictionary



class RentalPropInfo():
    def __init__(self):
        self.home_val = 0
        self.rent = 0
        self.extra_income = {}
        self.total_income = 0
        self.expenses = {}
        self.sum_exp = 0
        self.investments = {}

    def initial_investments(self):
        clear()
        # can you do a memo method here for "sorry that is not a valid response, please try again"
        # print(self.investments)
        # if self.investments:
        #     do_over = print("You've already completed this section! Would you like to start this section over again? enter yes or no: ")
        #     if do_over.lower() == 'yes':
        #         return
        #     elif do_over.lower() == 'no':
        #         Rental_Nav.run_nav()
        #     else:
        #         print("That is not a valid response.")

        down_payment = int(input("How much did you put in your down payment? (in $$ or %) \n(ie: for 100,000 enter 100: "))
        self.investments['down payment'] = down_payment
        closing_cost = int(input("How much did you spend on closing? "))
        self.investments['closing cost'] = closing_cost
        earnest = int(input("How much did you spend on the earnest fee? "))
        self.investments['earnest fee'] = earnest
        reno_repair = int(input("How much are you spending on renovations and repairs? "))
        self.investments['reno and repairs'] = reno_repair
        print("\nHang in there! We're almost done! Just a few more items: \n")
        appraisal = int(input("How much did you spend on the appraisal? "))
        self.investments['appraisal'] = appraisal
        inspection = int(input("How much was your inspection fee? "))
        self.investments['inspection'] = inspection 
        values = self.investments.values()
        sum_investments = sum(values)
        print(f"\n\nYour total investments amount to: ${sum_investments} \n")


    def rental_income(self):
        clear()
        home_val = input("\nWhat is your home value? \n(ie: for $500,000 enter 500, for $1,200,000 enter 1200: ")
        self.home_val = (int(home_val) * 1000)
        print(f"Congrats on purchasing your ${self.home_val} home!")
        rent_price = int(input(f"\nHow much would you like to rent out your ${self.home_val} home for? (ie: for $2000/mo, enter 2000) "))
        self.rent = rent_price
        while True:
            clear()
            rental_plus = input("""\n
                What else would you like to rent out? 
                (all calculations account for MONTHLY charges: 
                please enter your MONTHLY rental price)

                [1] storage unit
                [2] furniture 
                [3] other
                [4] nothing else/done!
                [5] review my rental source of income

                """)


            if rental_plus == '1':
                storage_price = int(input("How much would you like to rent out the storage unit for? "))
                self.extra_income['storage unit'] = storage_price
            elif rental_plus == '2':
                furniture_price = int(input("How much would you like to rent out the furniture for? "))
                self.extra_income['furniture'] = furniture_price
            elif rental_plus == '3':
                other = input("What else would you like to rent out? ")
                other_price = int(input(f"How much would you like to charge for {other}? "))
                self.extra_income[other] = other_price
            elif rental_plus == '4':
                print("Sounds good! Let's move on. ")
                values = self.extra_income.values()
                self.total_income.append(sum(values))
                break
            elif rental_plus == '5':
                print(f"""
                    Source        |       Income
                    Rent          |       {self.rent}
                    storage unit  |       {self.extra_income['storage unit']}
                    furniture     |       {self.extra_income['furniture']}
                    other         |       {self.extra_income[other]}
                    """)

            else:
                print("That is not a valid response, please try again! ") 

    def rental_expenses(self):
        clear()
        print("Let's talk about the upkeep costs of running a rental: ")
        taxes = int(input("What are your monthly taxes? "))
        self.expenses['taxes'] = taxes
        insurance = int(input("How much is your home insurance? "))
        self.expenses['insurance'] = insurance
        utilities = int(input("How much is the total utility cost? "))
        self.expenses['utilities'] = utilities
        hoa = int(input("How much is the monthly HOA fee? "))
        self.expenses['HOA'] = hoa
        landscape = int(input("How much does it cost to maintain lawn/snow? "))
        self.expenses['landscape'] = landscape
        print("\nJust a few more left!\n")
        repairs = int(input("What is your budget for repairs? "))
        self.expenses['repairs'] = repairs
        cap_exp = int(input("How much are your capital expenditures? "))
        self.expenses['capital expenditures'] = cap_exp
        mortgage = int(input("WHat is your monthly mortgage? "))
        self.expenses['mortgage'] = mortgage 
        values = self.expenses.values()
        self.sum_exp.append(sum(values))
        print(f"\n\nYour expected monthly expenses come out to: {self.sum_exp}\n")


    def roi(self):
        clear()
        next_step = input("Have you completed steps 1, 2, and 3? ")
        if next_step == 'no':
            print("\nPlease come back after completing steps 1, 2, and 3!\n")
        if next_step == 'yes':
            clear()
            print("\nGreat! Let's get started!\n")
            self.rent = 3500
            self.total_income = 1000
            self.sum_exp = 2000

            print(f"""
            Let's review your information: 
            Income       |       {(self.rent + self.total_income)}
            Expenses     |       {self.sum_exp}
            Total Return |       {((self.rent + self.total_income) - self.sum_exp)}

            """)



class Rental_Nav: #instructions for what user would like to fill out. can move from category to category: rental income/investment/expenses.
    def homePage(self):
        (clear)
        print(
            """
            Complete sections 1, 2, and 3 before section 4:

            [1] Investments: Just bought the house! 
            [2] Rental income: Show me the money! 
            [3] Rental Expenses: Investments for the long run
            [4] Calculate my ROI!
            [5] Quit

            """)

    def run_nav(self): 
        print("""
            Welcome to Budget Helper: your easy investment calculator. Where would you like to start? 
            (We recommend starting with [1]
            or not. [AS] ) \n""")
        while True:
            Rental_Nav.homePage(self)
            my_property = RentalPropInfo()
        
            choice = input("Enter your option here: ")
            if choice == '1':
                my_property.initial_investments()
            if choice == '2':
                my_property.rental_income()
            if choice == '3': 
                my_property.rental_expenses()
            if choice == '4':
                my_property.roi()

my_rental = Rental_Nav()
my_rental.run_nav()