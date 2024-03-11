from tkinter import *

app_window = Tk()
app_window.title("BMI Calculator")
app_window.minsize(width=300, height=600)
app_window.config(padx=20, pady=20)

main_label = Label(text="BOY & AĞIRLIK",font=("Arial",25,"bold"))
main_label_2 = Label(text="BİLGİLERİNİZİ GİRİN", font=("Arial",15,"bold"))
main_label.grid(row=1, column=1, columnspan=3)
main_label_2.grid(row=2, column=1, columnspan=3)

bmi = 0
over = 0
cm_value = 1
kg_value = 1
var_cm = DoubleVar()
var_kg = DoubleVar()

result = "Lütfen bilgileri giriniz"

def cm_scale_selected():
    global cm_value
    cm_value = var_cm.get()
    return cm_value

def kg_scale_selected(): 
    global kg_value
    kg_value = var_kg.get()
    return kg_value

def bmi_calculator():
    global bmi
    m2 = (cm_value/100)**2
    bmi = kg_value/m2
    
    return bmi

    
def bmi_interpreter():
    global result
    global over
    cm_scale_selected()
    kg_scale_selected()
    bmi_calculator()

    over += (kg_value/((cm_value/100)**2))-25
    over_res = over * ((cm_value/100)**2)
    over = int(over_res)
    
    if bmi < 18.5:
        result = "İdeal kilonun altındasınız."
    elif 18.5 < bmi < 25:
        result = "İdeal kilodasınız."
    elif 25 < bmi <= 30:
        result = f"İdeal kilonun üstündesiniz, \n{over} kilo fazlanız var."
    elif 30 < bmi <= 40:
        result = f"İdeal kilonun çok üstündesiniz, \n{over} kilo fazlanız var."
    else:
        result = f"ideal kilonun çok üstündesiniz, \n{over} kilo fazlanız var."
        
    
    
    
    result_label.config(text=result)
    over = 0
    



cm_scale = Scale(length=400, width=50, from_=215, to=115, variable=var_cm)
cm_scale.grid(row=3, column=1)


cm_label = Label(text="(cm)",font=("Arial",10,"normal"))
cm_label.grid(row=4, column=1)


kg_scale = Scale(length=400, width=50, from_=200, to=20, variable=var_kg)
kg_scale.grid(row=3, column=2)

kg_label = Label(text="(kg)",font=("Arial",10,"normal"))
kg_label.grid(row=4, column=2)

calc_button = Button(text="Hesapla", width=15, height=6, command=bmi_interpreter)
calc_button.grid(row=3, column=3)

result_label = Label(text=result,font=("Arial",20,"italic"))
result_label.grid(row=5, column=1, columnspan=10)

app_window.mainloop()

