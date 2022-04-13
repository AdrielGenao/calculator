import tkinter as tk



class Calculator:  # Create Calculator as a class
    def __init__(self):  # Create init method
        self.nums = []  # List for numbers pressed
        self.prev_num = 0  # First number
        self.next_num = 0  # Second number
        self.option = 0  # Used for determing which operation to use
        self.final = 0  # Final answer

    def num(self, x):  # Lists the numbers on the label of the calculator
        if self.option != 0:  # If operation button has been pressed
            self.answer.config(text='')  # Clear the previous number on the label
        main = ''
        self.nums.append(x)  # Add number pressed to list of numbers pressed
        if len(self.nums) == 1:  # If only one number is in the list
            self.answer.config(text=self.nums[0])  # Print number
        if len(self.nums) > 1:  # If more numbers are in the list
            for i in self.nums:
                main += str(i)
            self.answer.config(text=main)  # Print string of numbers from list

    def plus(self):  # Addition
        self.option = 1  # Option becomes the addition operation
        main = ''
        for i in self.nums:
            main += str(i)
            self.prev_num = main  # First number becomes saved
        self.nums.clear()  # Clear the list of numbers to prepare for second list of numbers
        if self.option == 5:  # Not first time adding
            self.option = 1  # Option to adding operation

    def divide(self):  # Division
        self.option = 4  # Option becomes the division operation
        main = ''
        for i in self.nums:
            main += str(i)
            self.prev_num = main  # First number becomes saved
        self.nums.clear()  # Clear the list of numbers to prepare for second list of numbers
        if (self.option == 5):  # Not first time dividing
            self.option = 4  # Option to dividing operation

    def multiply(self):  # Mulitplication
        self.option = 3  # Option becomes the mulitplication operation
        main = ''
        for i in self.nums:
            main += str(i)
            self.prev_num = main  # First number becomes saved
        self.nums.clear()  # Clear the list of numbers to prepare for second list of numbers
        if (self.option == 5):  # Not first time multiplying
            self.option = 3  # Option to multplying operation

    def minus(self):  # Subtraction
        if (self.option == 0):  # First time subtracting
            self.option = 2  # Option becomes the subtraction operation
            main = ''
            for i in self.nums:
                main += str(i)
                self.prev_num = main  # First number becomes saved
            self.nums.clear()  # Clear the list of numbers to prepare for second list of numbers
        if (self.option == 5):  # Not first time subtracting
            self.option = 2  # Option to subtracting operation

    def equals(self):
        main = ''
        for i in self.nums:
            main += str(i)
            self.next_num = main  # Save the second number
        if (self.option == 1):  # Addition
            self.final = int(self.prev_num) + int(self.next_num)  # Add
            self.answer.config(text=self.final)  # Display answer
            self.prev_num = self.final  # Final answer becomes previous answer
            self.nums.clear()  # Clear list
            self.option = 5
        if (self.option == 2):  # Subtraction
            self.final = int(self.prev_num) - int(self.next_num)  # Subrtact
            self.answer.config(text=self.final)  # Display answer
            self.prev_num = self.final  # Final answer becomes previous answer
            self.nums.clear()  # Clear list
            self.option = 5
        if (self.option == 3):  # Multiplication
            self.final = int(self.prev_num) * int(self.next_num)  # Multiply
            self.answer.config(text=self.final)  # Display answer
            self.prev_num = self.final  # Final answer becomes previous answer
            self.nums.clear()  # Clear list
            self.option = 5
        if (self.option == 4):  # Division
            self.final = int(self.prev_num) / int(self.next_num)  # Divide
            self.answer.config(text=int(self.final))  # Display answer
            self.prev_num = int(self.final)  # Final answer becomes previous answer
            self.nums.clear()  # Clear list
            self.option = 5

    def delete(self):  # Delete last number pressed
        main = ' '
        if (len(self.nums) == 0):  # If no number was pressed
            self.answer.config(text='')  # Print nothing
        if (len(self.nums) == 1):  # If only one number was pressed
            self.answer.config(text='')  # Print nothing
            self.nums.remove(self.nums[0])  # Delete that number from the list
        if (len(self.nums) > 1):  # If more than one number in the list
            self.nums.remove(self.nums[len(self.nums) - 1])  # Delete the last number pressed
            for i in self.nums:
                main += str(i)  # Create number from list of nums
            self.answer.config(text=main)  # Print new number
        if (self.option == 5):  # If trying to delete from answer
            for x in str(self.prev_num):  # Make answer into list of nums
                self.nums.append(x)
            if (len(self.nums) == 1):  # If answer is 1 number long
                self.answer.config(text='')  # Print nothing
                self.prev_num = 0  # Answer is now 0
            if (len(self.nums) > 1):  # If answer is more than 1 number long
                self.nums.remove(self.nums[len(self.nums) - 1])  # Remove last number
                for i in self.nums:  # Make list into string of nums
                    main += str(i)
                self.answer.config(text=main)  # Print the answer with the last number deleted
                self.prev_num = main  # answer is now the new refined number

    def GUI(self):  # Set up for the GUI
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("239x211")
        self.answer = tk.Label(width=28, height=2)
        self.answer.place(x=20, y=0)
        self.button7 = tk.Button(text="7", width=7, height=2, command=lambda: self.num(7))
        self.button7.place(x=0, y=42.5)
        self.button8 = tk.Button(text="8", width=7, height=2, command=lambda: self.num(8))
        self.button8.place(x=60, y=42.5)
        self.button9 = tk.Button(text="9", width=7, height=2, command=lambda: self.num(9))
        self.button9.place(x=120, y=42.5)
        self.buttondiv = tk.Button(text="/", width=7, height=2, command=lambda: self.divide())
        self.buttondiv.place(x=180, y=42.5)
        self.button4 = tk.Button(text="4", width=7, height=2, command=lambda: self.num(4))
        self.button4.place(x=0, y=85)
        self.button5 = tk.Button(text="5", width=7, height=2, command=lambda: self.num(5))
        self.button5.place(x=60, y=85)
        self.button6 = tk.Button(text="6", width=7, height=2, command=lambda: self.num(6))
        self.button6.place(x=120, y=85)
        self.buttonmul = tk.Button(text="X", width=7, height=2, command=lambda: self.multiply())
        self.buttonmul.place(x=180, y=85)
        self.button1 = tk.Button(text="1", width=7, height=2, command=lambda: self.num(1))
        self.button1.place(x=0, y=127.5)
        self.button2 = tk.Button(text="2", width=7, height=2, command=lambda: self.num(2))
        self.button2.place(x=60, y=127.5)
        self.button3 = tk.Button(text="3", width=7, height=2, command=lambda: self.num(3))
        self.button3.place(x=120, y=127.5)
        self.buttonmin = tk.Button(text="-", width=7, height=2, command=lambda: self.minus())
        self.buttonmin.place(x=180, y=127.5)
        self.buttondel = tk.Button(text="DEL", width=7, height=2, command=lambda: self.delete())
        self.buttondel.place(x=0, y=170)
        self.button0 = tk.Button(text="0", width=7, height=2, command=lambda: self.num(0))
        self.button0.place(x=60, y=170)
        self.buttonequ = tk.Button(text="=", width=7, height=2, command=lambda: self.equals())
        self.buttonequ.place(x=120, y=170)
        self.buttonplus = tk.Button(text="+", width=7, height=2, command=lambda: self.plus())
        self.buttonplus.place(x=180, y=170)
        self.window.mainloop()



run = Calculator()
run.GUI()
