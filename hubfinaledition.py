import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
class MainHub:
    def __init__(self):
        self.pwlist = []
        self.window = tk.Tk()
        self.window.title("The Decoding Hub")
        self.Choice()
    def Choice(self):
        self.fibcreate = ttk.Button(self.window, text="1. Fibonacci generator", command=self.CreateFibonacci)
        self.fibcreate.grid(row=1,column=1)
        self.calccreate = ttk.Button(self.window, text="2. Calculator", command=self.CreateCalculator)
        self.calccreate.grid(row=1, column=3)
        self.pwgencreate = ttk.Button(self.window, text="3. Password Generator", command=self.CreatePWGEN)
        self.pwgencreate.grid(row=2, column=1)
        self.dectobincreate = ttk.Button(self.window, text="4. Decimal to binary converter", command=self.CreateDec)
        self.dectobincreate.grid(row=2, column=3)
        self.bintodeccreate = ttk.Button(self.window, text="5. Binary to decimal converter", command=self.CreateBin)
        self.bintodeccreate.grid(row=3, column=1)
        self.txttobincreate = ttk.Button(self.window, text="6. Text to binary converter", command=self.CreateTxttoBin)
        self.txttobincreate.grid(row=3, column=3)
        self.bintotxtcreate = ttk.Button(self.window, text="7. Binary to text converter", command=self.CreateBintoTxt)
        self.bintotxtcreate.grid(row=4, column=1)
        self.txttob64create = ttk.Button(self.window, text="8. Text to Base64 converter", command=self.CreateTxtToB64)
        self.txttob64create.grid(row=4, column=3)
        self.pwarchivecreate = ttk.Button(self.window, text="9. Password archive", command=self.PasswordArchive)
        self.pwarchivecreate.grid(row=5, column=2)
        self.quit = ttk.Button(self.window, text="10. Quit",command=self.window.destroy)
        self.quit.grid(row=6, column=2)
        self.window.mainloop()
    def CreateFibonacci(self):
        fibgen = Fibonacci()
        fibgen.Main()
    def CreateCalculator(self):
        calc = Calculator()
        calc.Main()
    def CreatePWGEN(self):
        pwgen = Generator()
        pwgen.Main()
    def CreateDec(self):
        decttobin = DecimalToBinary()
        decttobin.Main()
    def CreateBin(self):
        bintodec = BinaryToDecimal()
        bintodec.Main()
    def CreateTxttoBin(self):
        txttobin = TextToBinary()
        txttobin.Main()
    def CreateBintoTxt(self):
        bintotxt = BinaryToText()
        bintotxt.Main()
    def CreateTxtToB64(self):
        txttob64 = TextToBase64()
        txttob64.Main()
    def PasswordArchive(self):
        print("wait")
class Fibonacci:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fibonacci Generator")
        self.count = 0
        self.counter = 0
    def Main(self):
        self.mainlabel = tk.Label(self.window, text="How many fibonacci sequence members do you want printed out?")
        self.mainlabel.grid(row=1, column=1)
        self.entryplace = tk.Entry(self.window)
        self.entryplace.grid(row=2, column=1)
        self.inputbutton= tk.Button(self.window, text="Input", command=self.Calculate)
        self.inputbutton.grid(row=3, column=1)
        self.quit = tk.Button(self.window, text="Quit", command=self.window.destroy)
        self.quit.grid(row=4, column=1)
    def Calculate(self):
        try:
            self.count = int(self.entryplace.get())
        except ValueError:
            messagebox.showerror("Error!", "Please input a valid integer into the generator!")
        self.counter = 0
        for self.i in self.FibonacciGenerator():
            print(self.i)
            self.counter += 1
            if self.counter == 1000:
                self.finalstring = "The value of the final fibonacci sequence member is: " + str(self.i)
                messagebox.showinfo("Final value", self.finalstring)
                messagebox.showwarning("Warning!", "You reached the limit!")
                break
            if self.counter >= self.count:
                self.finalstring = "The value of the final fibonacci sequence member is: " + str(self.i)
                messagebox.showinfo("Final value", self.finalstring)
                break
    def FibonacciGenerator(self):
        (self.a, self.b) = (1, 1)
        for i in range(1000):
            yield self.a
            (self.a, self.b) = (self.b, self.a + self.b)
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.result = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.decision = ""
    def Main(self):
        while self.running:
            self.c = self.Calc(self.a, self.b, action=self.decision)
            print("The number is:", self.c)
            print("Do you want to use the calculator again? Y/N")
            self.choice = input("Input: ")
            if self.choice != "Y" and self.choice != "Yes" and self.choice != "yes" and self.choice != "y":
                self.running = False
    def Calc(self,first,second,**options):
        if options.get("action") == "sum":
            result = first + second
        if options.get("action") == "multiply":
            result = first * second
        if options.get("action") == "subtract":
            result = first - second
        if options.get("action") == "divide":
            result = first / second
        if options.get("action") == "power":
            result = first**second
        return result
class Generator:
    def __init__(self):
        self.window = tk.Tk()
        self.UppercaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.LowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.Numbers = ["0","1","2","3","4","5","6","7","8","9"]
        self.Symbols = ["!","@","#","$","%","^","&","*","?",":",";"]
        self.rng = 0
        self.security = ""
        self.pw = ""
        self.choice = ""
        self.choicetwo = ""
        self.save = ""
    def Main(self):
        self.pw = ""
        self.MainLabel = tk.Label(self.window, text="How secure do you want your password to be?")
        self.MainLabel.grid(row=1,column=2)
        self.Easy = tk.Button(self.window, text="Baby can crack this", command=self.weak)
        self.Easy.grid(row=2,column=1)
        self.Medium = tk.Button(self.window, text="Medium spicy", command=self.medium)
        self.Medium.grid(row=2, column=2)
        self.Tough = tk.Button(self.window, text="Pentagon", command=self.tough)
        self.Tough.grid(row=2, column=3)
        self.quit = tk.Button(self.window, text="Quit",command=self.window.destroy)
        self.quit.grid(row=3, column=2)
    def weak(self):
        self.rng = random.randint(1, 4)
        if self.rng == 1:
            self.pw = self.UppercaseLetters[random.randint(0, 25)]
        if self.rng == 2:
            self.pw = self.LowercaseLetters[random.randint(0, 25)]
        if self.rng == 3:
            self.pw = self.Numbers[random.randint(0, 9)]
        if self.rng == 4:
            self.pw = self.Symbols[random.randint(0, 10)]
        self.finalstring = "Your password is: "+self.pw
        messagebox.showinfo("Result",self.finalstring)
    def medium(self):
        self.pw = self.UppercaseLetters[random.randint(0, 25)] + self.LowercaseLetters[random.randint(0, 25)] + \
                  self.Numbers[random.randint(0, 9)] + self.Numbers[random.randint(0, 9)]
        self.finalstring = "Your password is: " + self.pw
        messagebox.showinfo("Result", self.finalstring)
    def tough(self):
        for i in range(26):
            self.rng = random.randint(1, 4)
            if self.rng == 1:
                self.pw = self.pw + self.UppercaseLetters[random.randint(0, 25)]
            if self.rng == 2:
                self.pw = self.pw + self.LowercaseLetters[random.randint(0, 25)]
            if self.rng == 3:
                self.pw = self.pw + self.Numbers[random.randint(0, 9)]
            if self.rng == 4:
                self.pw = self.pw + self.Symbols[random.randint(0, 10)]
        self.finalstring = "Your password is: " + self.pw
        messagebox.showinfo("Result", self.finalstring)

class DecimalToBinary:
    def __init__(self):
        self.dec = 0
        self.bin = 0
        self.running = True
    def Main(self):
        while self.running:
            self.dec = int(input("Input the number you want to convert: "))
            self.bin = self.DecToBin(self.dec)
            print(self.bin)
            print("Do you want to use the converter again? Y/N")
            self.choice = input("Input: ")
            if self.choice != "Y":
                self.running = False
    def DecToBin(self,x):
        total = ""
        while x >= 1:
            y = x % 2
            x = x//2
            print(x,y)
            total = total + str(y)
        truetotal = total[::-1]
        return truetotal
class BinaryToDecimal:
    def __init__(self):
        self.bin = ""
        self.dec = 0
        self.choice = ""
        self.running = True
    def Main(self):
        self.bin = input("Input the number you want to convert: ")
        self.dec = self.BinToDec(self.bin)
        print(self.dec)
        print("Do you want to use the converter again? Y/N")
        self.choice = input("Input: ")
        if self.choice != "Y" and self.choice != "Yes" and self.choice != "yes" and self.choice != "y":
            self.running = False
    def BinToDec(self,x):
        total = 0
        for i in range(len(x)-1):
            total += int(x[i])*(2**(len(x)-1-i))
        if x[len(x)-1] == "1":
            total += 1
        return total
class TextToBinary:
    def __init__(self):
        self.str = ""
        self.encoded = ""
        self.choice = ""
        self.running = True
    def Main(self):
        while self.running:
            self.str = input("Input the string you want to convert to binary: ")
            self.encoded = self.TextToEncode(self.str)
            print(self.encoded)
            print("Do you want to use the converter again? Y/N")
            self.choice = input("Input: ")
            if self.choice != "Y" and self.choice != "Yes" and self.choice != "yes" and self.choice != "y":
                self.running = False
    def TextToEncode(self,x):
        totalbin = ""
        for i in x:
            number = ord(i)
            totalbin += self.DecToBin(number)
            totalbin += " "
        return totalbin
    def DecToBin(self,x):
        total = ""

        while x >= 1:
            y = x % 2
            x = x//2
            total = total + str(y)
        truetotal = total[::-1]
        return truetotal
class BinaryToText:
    def __init__(self):
        self.str = ""
        self.encoded = ""
        self.choice = ""
        self.running = True
    def Main(self):
        self.str = input("Input the binary you want to decode: ")
        self.encoded = self.TextToDecode(self.str)
        print(self.encoded)
        print("Do you want to use the converter again? Y/N")
        self.choice = input("Input: ")
        if self.choice != "Y" and self.choice != "Yes" and self.choice != "yes" and self.choice != "y":
            self.running = False

    def TextToDecode(self, x):
        totaltext = ""
        stop = 0
        for i in range(len(x)-1):
            if x[i] == " ":
                temp = self.BinToDec(x[stop:i])
                totaltext += chr(temp)
                stop = i+1
        laststring = self.BinToDec(x[len(x)-8:])
        totaltext += chr(laststring)
        return totaltext
    def BinToDec(self, x):
        total = 0
        for i in range(len(x) - 1):
            total += int(x[i]) * (2 ** (len(x) - 1 - i))
        if x[len(x) - 1] == "1":
            total += 1
        return total
class TextToBase64:
    def __init__(self):
        self.str = ""
        self.encoded = ""
        self.choice = ""
        self.Table = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X",
                      "Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
                      "w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
        self.running = True
        self.Main()
    def Main(self):
        self.str = input("Input the text you want to encode into base64: ")
        self.encoded = self.ConvertToBase64(self.str)
        print(self.encoded)
        print("Do you want to use the converter again? Y/N")
        self.choice = input("Input: ")
        if self.choice != "Y" and self.choice != "Yes" and self.choice != "yes" and self.choice != "y":
            self.running = False
    def ConvertToBase64(self,x):
        tempbin = self.TextToEncode(x)
        counter2 = 0
        final = ""
        finalstring = ""
        if len(x)%6 != 0:
            tempuno = len(x)//3
            print(tempuno)
            newlength = (tempuno+1)*3
            print(newlength)
            while len(tempbin) < newlength:
                tempbin += "0"
        if len(x)%3 == 2:
            finalstring = "="
        if len(x)%3 == 1:
            finalstring = "=="
        while counter2 < len(tempbin):
            tempdec = self.BinToDec(tempbin[counter2:counter2+6])
            character = self.Table[tempdec]
            if counter2+6 >= len(tempbin):
                if finalstring == "==":
                    character = self.Table[tempdec*16]
                if finalstring == "=":
                    character = self.Table[tempdec*4]
            final+=character
            counter2 += 6
        final+=finalstring
        return final
    def TextToEncode(self,x):
        totalbin = ""
        for i in x:
            number = ord(i)
            totalbin += self.DecToBin(number)
        return totalbin
    def DecToBin(self,x):
        total = ""
        while x >= 1:
            y = x % 2
            x = x//2
            total = total + str(y)
        truetotal = total[::-1]
        while len(truetotal)/8 != 1:
            truetotal = "0"+truetotal
        return truetotal
    def BinToDec(self, x):
        total = 0
        for i in range(len(x) - 1):
            total += int(x[i]) * (2 ** (len(x) - 1 - i))
        if x[len(x) - 1] == "1":
            total += 1
        return total
mainhub = MainHub()