import pyfiglet
from colorama import Fore, Back, Style

credits = pyfiglet.figlet_format("Trade Value!", font="standard")
print(Fore.YELLOW + credits)


def price_of(fruit_name: str) -> int: return name_to_price[fruit_name]


name_to_price = {
    "blank": 0, "": 0, "0": 0, "nothing": 0, "no": 0,
    "rocket": 7500,
    "spin": 10000,
    "chop": 100000,
    "spring": 20000,
    "bomb": 40000,
    "smoke": 200000,
    "spike": 100000,
    "flame": 450000,
    "falcon": 200000, "bird: falcon": 200000,
    "ice": 800000,
    "sand": 750000,
    "dark": 1000000,
    "revive": 450000,
    "diamond": 550000, "daimond": 550000, "dimond": 550000,
    "light": 900000,
    "love": 1750000,
    "rubber": 400000,
    "barrier": 400000,
    "magma": 1100000,
    "quake": 1100000,
    "buddha": 2400000, "human: buddha": 2400000, "buddah": 2400000, "budha": 2400000,
    "string": 1800000, "spider": 1800000,
    "phoenix": 1700000, "bird: pheonix": 1700000, "pheonix": 1700000, "phenix": 1700000, "fenix": 1700000,
    "portal": 2200000,
    "rumble": 2300000,
    "paw": 1750000, "pain": 1750000,
    "sound": 1700000,
    "blizzard": 2600000, "blizard": 2600000,
    "gravity": 2300000,
    "dough": 4900000,
    "shadow": 3300000,
    "mamute": 2700000, "mamooth": 2700000,
    "trex": 25000000, "t-rex": 25000000,
    "venom": 4000000,
    "control": 2600000,
    "spirit": 3400000,
    "dragon": 4100000,
    "leopard": 7800000, "lepard": 7800000, "leo": 7800000,
    "kitsune": 8000000, "kit": 8000000
}

offerfruit1 = input("Primeira Fruta Que Voce ta Oferecendo: ").lower()
offerfruit2 = input("Segunda Fruta Que Voce ta Oferecendo:").lower()
offerfruit3 = input("Terceira Fruta Que Voce ta Oferecendo: ").lower()
offerfruit4 = input("Ultima Fruta Que Voce ta Oferecendo: ").lower()

print(offerfruit1, price_of(offerfruit1), "+", offerfruit2, price_of(offerfruit2), "+", offerfruit3,
      price_of(offerfruit3), "+", offerfruit4, price_of(offerfruit4), "=",
      price_of(offerfruit1) + price_of(offerfruit2) + price_of(offerfruit3) + price_of(offerfruit4))

offertotal = price_of(offerfruit1) + price_of(offerfruit2) + price_of(offerfruit3) + price_of(offerfruit4)

receivefruit1 = input("Primeira Fruta Que Voce Recebeu: ").lower()
receivefruit2 = input("Segunda Fruta Que Voce Recebeu: ").lower()
receivefruit3 = input("Terceira Fruta Que Voce Recebeu: ").lower()
receivefruit4 = input("Quarta Fruta Que Voce Recebeu: ").lower()

receivetotal = price_of(receivefruit1) + price_of(receivefruit2) + price_of(receivefruit3) + price_of(receivefruit4)

if offertotal < (40 / 100 * receivetotal):
    print("\033[1;31;40m Offer must be more than 40% of receiving value. \n")
else:
    print(receivefruit1, price_of(receivefruit1), "+", receivefruit2, price_of(receivefruit2), "+", receivefruit3,
          price_of(receivefruit3), "+", receivefruit4, price_of(receivefruit4), "=",
          price_of(receivefruit1) + price_of(receivefruit2) + price_of(receivefruit3) + price_of(receivefruit4))

if offertotal >= (40/100 * receivetotal) and receivetotal >= (110/100 * offertotal):
    print("\033[1;32;40m Trade Boa! :) \n")
elif offertotal >= (40/100 * receivetotal) and (90 / 100 * offertotal) < receivetotal < (110 / 100 * offertotal):
    print("\033[1;33;40mTrade Justa")
elif offertotal >= (40/100 * receivetotal) and receivetotal < (90/100 * offertotal):
    print("\033[1;31;40m Pessima Trade :( \n")
