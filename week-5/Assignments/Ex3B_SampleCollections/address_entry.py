# Description: Working with dictionaries
# Author: Jonathan Lopez

contact_info = {
    "name": "Jonathan Lopez",
    "address": "123 Main St, Anytown, NY",
    "city": "Anytown",
    "state": "NY",
    "zip_code": "12345",

}

print(f"""{contact_info["name"]}
      {contact_info["address"]}
       {contact_info["city"]}, {contact_info["state"]} {contact_info["zip_code"]}""")

del contact_info["name"]

full_name = {
"first name": "Jonathan",
"last name": "Lopez"
}

full_name.update({"honorific": "Mr."})

contact_info.update({"full_name": full_name})

print(f"""{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}""")
print(f"""{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip_code"]}""")