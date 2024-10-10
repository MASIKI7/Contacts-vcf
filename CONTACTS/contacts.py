contacts = [
    {"name": "SAYANSI1", "phone": "+255763051774"},
    {"name": "SAYANSI2", "phone": "+255767908201"},
    {"name": "SAYANSI3", "phone": "+255719702789"},
     {"name": "SAYANSI4", "phone": "+255622339260"},
    {"name": "SAYANSI5", "phone": "+255766835046"},
    {"name": "SAYANSI6", "phone": "+255625865598"},
     {"name": "SAYANSI7", "phone": "+255744762275"},
    {"name": "SAYANSI8", "phone": "+255755025701"},
    {"name": "SAYANSI9", "phone": "+255759262863"},
     {"name": "SAYANSI10", "phone": "+255653926351"},
    {"name": "SAYANSI11", "phone": "+255765411212"},
    {"name": "SAYANSI12", "phone": "+255623348941"},
     {"name": "SAYANSI13", "phone": "+255764169414"},
    {"name": "SAYANSI14", "phone": "+255753073799"},
    {"name": "SAYANSI15", "phone": "+255768711144"},
     {"name": "SAYANSI16", "phone": "+255753640919"},
    {"name": "SAYANSI17", "phone": "+255754679267"},
    {"name": "SAYANSI18", "phone": "+255764946100"},
     {"name": "SAYANSI19", "phone": "+255752082512"},
    {"name": "SAYANSI20", "phone": "+255688273176"},
    {"name": "SAYANSI21", "phone": "+255629126010"},
     {"name": "SAYANSI22", "phone": "+255754391924"},
    {"name": "SAYANSI23", "phone": "+255715797075"},
    {"name": "SAYANSI24", "phone": "+255627122382"},
     {"name": "SAYANSI25", "phone": "+255755807324"},
    {"name": "SAYANSI26", "phone": "+255762990911"},
    {"name": "SAYANSI27", "phone": "+255692620228"},
     {"name": "SAYANSI28", "phone": "+255692678333"},
    {"name": "SAYANSI29", "phone": "+4917630117408"},
    {"name": "SAYANSI30", "phone": "+255755032309"}
    
]

with open("contacts.vcf", "w") as f:
    for contact in contacts:
        f.write("BEGIN:VCARD\n")
        f.write("VERSION:3.0\n")
        f.write(f"FN:{contact['name']}\n")
        f.write(f"TEL;TYPE=CELL:{contact['phone']}\n")
        f.write("END:VCARD\n\n")
