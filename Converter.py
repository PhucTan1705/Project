import PySimpleGUI as sg

layout = [
    [sg.Input(key = '-INPUT-'),
     sg.Spin(['Km to Mile','Kg to Pound','Sec To Min'], key = '-UNIT-'),
     sg.Button('Convert', key = '-CONVERT')],
    [sg.Text('OutPut', key = '-OUTPUT-')]

]

window = sg.Window('Converter',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNIT-']:
                case 'Km to Mile':
                    output = round(float(input_value)*0.6214,2)
                    output_string = f'{input_value} km  are {output} miles'
                case 'Kg to Pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg  are {output} pound'
                case 'Sec To Min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} sec  are {output} mintues'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')
window.close()