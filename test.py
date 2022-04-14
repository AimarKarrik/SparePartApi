

dicts = [
    {
        "name": "käigukang",
        "laoseis": "10"
    },
    {
        "name": "uks",
        "laoseis": "7"
    },
    {
        "name": "mootor",
        "laoseis": "1"
    },
    {
        "name": "luup",
        "laoseis": "5"
    },
    {
        "name": "luumaja",
        "laoseis": "5"
    },
    {
        "name": "luisk",
        "laoseis": "5"
    }
]

field = ""
search = "lu"

searched_parts = []
if field != "":
    for i in dicts:
        if search in i[field]:
            searched_parts.append(i)

print(searched_parts)