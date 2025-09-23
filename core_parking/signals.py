from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Parking


SPOTS_PL2 = [
    {"spot_number": "B202", "aisle": "mainAisleLeft"},
    {"spot_number": "B203", "aisle": "mainAisleLeft"},
    {"spot_number": "B229", "aisle": "mainAisleRight"},
    {"spot_number": "B230", "aisle": "mainAisleRight"},
    {"spot_number": "B231", "aisle": "mainAisleRight"},
    {"spot_number": "C216", "aisle": "mainAisleLeft"},
    {"spot_number": "C217", "aisle": "mainAisleLeft"},
    {"spot_number": "C218", "aisle": "mainAisleLeft"},
    {"spot_number": "C219", "aisle": "mainAisleLeft"},
    {"spot_number": "C220", "aisle": "mainAisleLeft"},
    {"spot_number": "C221", "aisle": "mainAisleLeft"},
    {"spot_number": "C222", "aisle": "mainAisleLeft"},
    {"spot_number": "C223", "aisle": "mainAisleLeft"},
    {"spot_number": "C237", "aisle": "mainAisleRight"},
    {"spot_number": "C238", "aisle": "mainAisleRight"},
    {"spot_number": "C239", "aisle": "mainAisleRight"},
    {"spot_number": "C240", "aisle": "mainAisleRight"},
    {"spot_number": "C242", "aisle": "mainAisleRight"},
    {"spot_number": "C243", "aisle": "mainAisleRight"},
    {"spot_number": "C247", "aisle": "mainAisleRight"},
    {"spot_number": "C248", "aisle": "mainAisleRight"},
    {"spot_number": "C249", "aisle": "mainAisleRight"},
    {"spot_number": "B209", "aisle": "leftAisleRight"},
    {"spot_number": "B210", "aisle": "leftAisleRight"},
    {"spot_number": "B211", "aisle": "leftAisleRight"},
    {"spot_number": "B215", "aisle": "leftAisleRight"},
    {"spot_number": "B216", "aisle": "leftAisleRight"},
    {"spot_number": "B217", "aisle": "leftAisleRight"},
    {"spot_number": "B218", "aisle": "leftAisleRight"},
    {"spot_number": "B219", "aisle": "leftAisleRight"},
    {"spot_number": "B221", "aisle": "leftAisleLeft"},
    {"spot_number": "B222", "aisle": "leftAisleLeft"},
    {"spot_number": "B223", "aisle": "leftAisleLeft"},
    {"spot_number": "B224", "aisle": "leftAisleLeft"},
    {"spot_number": "B225", "aisle": "leftAisleLeft"},
    {"spot_number": "B226", "aisle": "leftAisleLeft"},
    {"spot_number": "B227", "aisle": "leftAisleLeft"},
    {"spot_number": "B228", "aisle": "leftAisleLeft"},
    {"spot_number": "C201", "aisle": "leftAisleLeft"},
    {"spot_number": "C202", "aisle": "leftAisleLeft"},
    {"spot_number": "C203", "aisle": "leftAisleLeft"},
    {"spot_number": "C204", "aisle": "leftAisleLeft"},
    {"spot_number": "C208", "aisle": "leftAisleRight"},
    {"spot_number": "C209", "aisle": "leftAisleRight"},
    {"spot_number": "C210", "aisle": "leftAisleRight"},
    {"spot_number": "C211", "aisle": "leftAisleRight"},
    {"spot_number": "C212", "aisle": "leftAisleRight"},
    {"spot_number": "C213", "aisle": "leftAisleRight"},
    {"spot_number": "C214", "aisle": "leftAisleRight"},
    {"spot_number": "C215", "aisle": "leftAisleRight"},
    {"spot_number": "C257", "aisle": "rightAisleLeft"},
    {"spot_number": "C258", "aisle": "rightAisleLeft"},
    {"spot_number": "A257", "aisle": "tunnel"},
    {"spot_number": "A258", "aisle": "tunnel"},
]

SPOTS_PL3 = [
    {"spot_number": "A311", "aisle": "mainAisleLeft"},
    {"spot_number": "A313", "aisle": "mainAisleLeft"},
    {"spot_number": "A314", "aisle": "mainAisleLeft"},
    {"spot_number": "A315", "aisle": "mainAisleLeft"},
    {"spot_number": "A316", "aisle": "mainAisleLeft"},
    {"spot_number": "A317", "aisle": "mainAisleLeft"},
    {"spot_number": "A318", "aisle": "mainAisleLeft"},
    {"spot_number": "A319", "aisle": "topAisleTop"},
    {"spot_number": "A320", "aisle": "topAisleTop"},
    {"spot_number": "A359", "aisle": "topAisleTop"},
    {"spot_number": "A321", "aisle": "topAisleTop"},
    {"spot_number": "A322", "aisle": "topAisleTop"},
    {"spot_number": "A323", "aisle": "topAisleTop"},
    {"spot_number": "A324", "aisle": "topAisleTop"},
    {"spot_number": "A325", "aisle": "topAisleTop"},
    {"spot_number": "A326", "aisle": "topAisleTop"},
    {"spot_number": "A327", "aisle": "topAisleTop"},
    {"spot_number": "A342", "aisle": "topAisleBottom"},
    {"spot_number": "A343", "aisle": "topAisleBottom"},
    {"spot_number": "A346", "aisle": "topAisleBottom"},
    {"spot_number": "A333", "aisle": "bottomAisleBottom"},
    {"spot_number": "A334", "aisle": "bottomAisleBottom"},
]


@receiver(post_migrate)
def populate_parking(sender, **kwargs):
    if sender.name != "core_parking":  # replace with your app name
        return
    
    print("Populating parking spots table...")

    for spot in SPOTS_PL2:
        Parking.objects.get_or_create(
            spot_number=spot["spot_number"],
            floor=-2,
            aisle=spot["aisle"],
            defaults={"status": Parking.Status.FREE},
        )

    for spot in SPOTS_PL3:
        Parking.objects.get_or_create(
            spot_number=spot["spot_number"],
            floor=-3,
            aisle=spot["aisle"],
            defaults={"status": Parking.Status.FREE},
        )
