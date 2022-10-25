from tkinter import W
import requests
import json
import dearpygui.dearpygui as dpg
import wordProcessing
import re
import unidecode
import bigram 

language_list = ["Spanish", "Portuguese", "English"]
word=""

def getTranslation(sender,data,user_data):
    lang1 = dpg.get_value(user_data[0])
    lang2 = dpg.get_value(user_data[1])
    word = dpg.get_value(user_data[2])
    if lang1==lang2:
        dpg.set_value(user_data[3], word)
    else:
        sentence = ""
        regexp = re.compile("[^a-zA-Z\d\s]")
        s = wordProcessing.Sentence(word, lang1)
        for w in s.parseText():
            with open("data.html",'w') as file:
                pass
            if lang1=="English" and lang2=="Spanish":
                url = "https://www.wordreference.com/es/translation.asp?tranword=" + w
            if lang1=="Spanish" and lang2=="English":
                url = "https://www.wordreference.com/es/en/translation.asp?spen=" + w
            if lang1=="Spanish" and lang2=="Portuguese":
                url = 'https://www.wordreference.com/espt/' + w
            if lang1=="Portuguese" and lang2=="Spanish":
                url = 'https://www.wordreference.com/ptes/' + w
            if lang1=="English" and lang2=="Portuguese":
                url = "https://www.wordreference.com/enpt/" + w
            if lang1=="Portuguese" and lang2=="English":
                url = "https://www.wordreference.com/pten/" + w
            response = requests.get(url)
            print("response code: " + str(response.status_code))
            with open('data.html','w', encoding="utf-8", errors="ignore") as f:
                f.write(str(response.text))
                f.close()
            newText = response.text[response.text.find("<td class=\'ToWrd\' >")+19:response.text.find("<td class=\'ToWrd\' >")+1000]
            w = newText[0:newText.find("<")]
            if regexp.search(w):
                print("matched at index: " + str(regexp.search(w).start()))
                newText = response.text[response.text.find("<td class=\'ToWrd\' >")+19:response.text.find("<td class=\'ToWrd\' >")+1000]
                newText = newText[newText.find("<td class=\'ToWrd\' >")+19:newText.find("<td class=\'ToWrd\' >")+500]
                w = newText[0:newText.find("<")]
                try:
                    unaccented_string = unidecode.unidecode(w)
                    w = w[:regexp.search(unaccented_string).start()+1]
                except AttributeError:
                    w = " " + w
                if w[len(w)-1] == "," or w[len(w)-1] == "/" or w[len(w)-1] == "\"":
                    w = w[:len(w)-1]
                if w[0] == " ":
                    w = w[1:]
            word1 = wordProcessing.Word(w,lang1)
            sentence += word1.word + " "
            sentence += " "
            sentence = bigram.mostLikelySentence(sentence)
        dpg.set_value(user_data[3], sentence)

dpg.create_context()

with dpg.window(tag="Primary Window"):
    lister1 = dpg.add_listbox(label="Languages", items = language_list, num_items=4)
    lister2 = dpg.add_listbox(label="Languages", items = language_list, num_items=4)
    inputtxt = dpg.add_input_text(label="Word", hint="Enter a word to translate...")
    text = dpg.add_text(word)
    translateButton = dpg.add_button(label="Translate", callback=getTranslation, user_data=[lister1, lister2, inputtxt,text])
    
with dpg.font_registry():
    with dpg.font("unifont.ttf", 16) as unifont:
        dpg.add_font_range(0x0250, 0x02ff)
        dpg.add_font_range(0x1D00, 0x1D7F)
        dpg.add_font_range(0x1D80, 0x1DBF)
        dpg.add_font_range(0x02B0, 0x02FF)
        dpg.add_font_range(0x0300, 0x036F)
    dpg.bind_font(unifont)

dpg.create_viewport(title='Machine Translation Suite', width=1000, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()

