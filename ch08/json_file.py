import json

menu = \
{
"breakfast": {
    "hours": "7-11",
    "items": {
        "breakfast burritos": "$6.00",
        "pancakes": "$4.00"
        }
    },
"lunch" : {
    "hours": "11-3",
    "items": {
        "hamburger": "$5.00"
        }
    },
"dinner": {
    "hours": "3-10",
    "items": {
        "spaghetti": "$8.00"
        }
    }
}

print(menu)

menu_json = json.dumps(menu)   # converts Python data to a JSON string
print(menu_json)

menu2 = json.loads(menu_json) # # converts a JSON string to Python data 
print(menu2)