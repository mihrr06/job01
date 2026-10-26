def plat(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légumes" and saison == "été":
        print("artichaut, aubergine, navet")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    else:
        print("On ne connaît pas ce que tu manges.")

plat("fruits", "été")
plat("légumes", "hiver")