import sys
from json import load as load_json

with open("data.json", "rt") as data:
    data = load_json(data)

data.sort(key=lambda mls: mls["code"])

tbody = ""
for mls in data:
    code, en, ru, es = mls["code"], mls["en"], mls.get("ru", None), mls.get("es", None)

    tbody += "<tr class='header'>"
    tbody += "<td class='code' onclick='expand(\"" + code + "\", this)'>" + code + "</td>"
    tbody += "<td class='name' onclick='expand(\"" + code + "\", this)'>"
    tbody += "<span>" + en["name"] + "</span>"
    if ru is not None:
        tbody += "<span class='unselected'>" + ru["name"] + "</span>"
    else:
        tbody += "<span></span>"
    if es is not None:
        tbody += "<span class='unselected'>" + es["name"] + "</span>"
    else:
        tbody += "<span></span>"
    tbody += "<td class='lang-button selected' onclick='change_lang(\"" + code + "\", 0, this)'>en</td>"
    if ru is not None:
        tbody += "<td class='lang-button' onclick='change_lang(\"" + code + "\", 1, this)'>ru</td>"
    else:
        tbody += "<td class='lang-button undefined'>ru</td>"
    if es is not None:
        tbody += "<td class='lang-button' onclick='change_lang(\"" + code + "\", 2, this)'>es</td>"
    else:
        tbody += "<td class='lang-button undefined'>es</td>"
    tbody += "</tr>"
    tbody += "<tr class='body collapsed'>"
    tbody += "<td colspan='5'>"
    tbody += "<div><p class='description'>" + en["description"] + "</p><br><p class='explanation'>" + en["explanation"] + "</p></div>"
    if ru is not None:
        tbody += "<div class='unselected'><p class='description'>" + ru["description"] + "</p><br><p class='explanation'>" + ru["explanation"] + "</p></div>"
    else:
        tbody += "<div></div>"
    if es is not None:
        tbody += "<div class='unselected'><p class='description'>" + es["description"] + "</p><br><p class='explanation'>" + es["explanation"] + "</p></div>"
    else:
        tbody += "<div></div>"
    tbody += "</td>"
    tbody += "</tr>"

with open(sys.argv[1], "wt") as out:
    out.write("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Переводы умений в Войнах Чатов</title><link rel='stylesheet' href='./table.css'><script src='./table.js'></script></head>""")
    out.write("""<body><table id='skills-table'><tbody>""" + tbody + """</tbody></table></body></html>""")
