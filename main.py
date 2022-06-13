from tkinter import *

import googletrans
import textblob
from tkinter import ttk,messagebox

root=Tk()
root.title('MY TRANSLATOR')

def translate_it():
    #delete any previous translations
    translated_text.delete(1.0,END)
    try:

        #Get Languages from Dictionary Keys
        #Get the FROM Language Key
        for key,value in languages.items():
            if(value==original_combo.get()):
                from_language_key=key

            #Get the TO Language Key
        for key,value in languages.items():
            if(value==translated_combo.get()):
                to_language_key=key

        #turn original text to textblob
        words=textblob.TextBlob(original_text.get(1.0,END))

        words=words.translate(from_lang= from_language_key,to=to_language_key)

        #output translated text to screen
        translated_text.insert(1.0,words)



    except EXCEPTION as e:
        messagebox.showerror("Translator",e)

def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)

#grab language list from google trans
languages=googletrans.LANGUAGES
language_list=list(languages.values())
print(language_list)

#Textboxes
original_text=Text(root, height=10,width=40)
original_text.grid(row=0,column=0,padx=10,pady=10)

translate_button=Button(root,text="Translate!",font=("Helvetica",24), command=translate_it)
translate_button.grid(row=0,column=1,padx=10)

translated_text=Text(root, height=10,width=40)
translated_text.grid(row=0,column=2,padx=10,pady=10)

#Combo boxes
original_combo=ttk.Combobox(root,width=50,values=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)


translated_combo=ttk.Combobox(root,width=50,values=language_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)

#Clear button
clear_button=Button(root,text="Clear", command=clear)
clear_button.grid(row=2,column=1)

root.mainloop()