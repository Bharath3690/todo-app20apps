import FreeSimpleGUI as sg
label1 = sg.Text("Enter Feet: ")
input_box1 = sg.Input()
label2 = sg.Text("Enter inches: ")
input_box2 = sg.Input()
convert_button = sg.Button("convert")
win = sg.Window("Convertor",layout=[[label1,input_box1],[label2,input_box2],[convert_button]])
win.read()
win.close()