from tkinter import*

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)
window.config(padx=40,pady=40)

def button_clicked():
    weight = int(weight_entry.get())
    height = int(height_entry.get())

    if weight == "" or height == "":
        label_3.config(text="Enter both and weight and height")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            string = write_result(bmi)
            label_3.config(text=string)
        except:
            label_3.config(text="Enter a valid number")

label = Label(text="Enter your weight (kg)")
label.pack()
weight_entry = Entry(width=15)
weight_entry.pack()

label_2 = Label(text="Enter your height (cm)")
label_2.pack()
height_entry = Entry(width=15)
height_entry.pack()

calculate = Button(text="Calculate",command=button_clicked)
calculate.config(padx=10,pady=5)
calculate.pack()

label_3 = Label()
label_3.pack()

def write_result(bmi):
    string = f"Your BMI is: {round(bmi,2)}. You are "
    if bmi <= 16:
        string += "severely thin!"
    elif 16 < bmi <= 17:
        string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        string += "mild thin"
    elif 18.5 < bmi <= 25:
        string += "normal"
    elif 25 < bmi <= 30:
        string += "overweight"
    elif 30 < bmi <= 35:
        string += "obese classs 1"
    elif 35 < bmi <= 40:
        string += "obese classs 2"
    else:
        string += "obese classs 3"
    return string


window.mainloop()