def arlaimejo(sarasas, kas):
    if sarasas[0] == kas and sarasas[1] == kas and sarasas[2] == kas:
        print("LAIMĖJO:", kas)
        return True
    if sarasas[3] == kas and sarasas[4] == kas and sarasas[5] == kas:
        print("LAIMĖJO:", kas)
        return True
    if sarasas[6] == kas and sarasas[7] == kas and sarasas[8] == kas:
        print("LAIMĖJO:", kas)
        return True
    if sarasas[0] == kas and sarasas[3] == kas and sarasas[6] == kas:
        print("LAIMĖJO:", kas)
        return True
    if sarasas[1] == kas and sarasas[4] == kas and sarasas[7] == kas:
        print("LAIMĖJO:", kas)
        return True
    if sarasas[2] == kas and sarasas[5] == kas and sarasas[8] == kas:
        print("LAIMĖJO:", kas)
        return True
    if sarasas[6] == kas and sarasas[4] == kas and sarasas[2] == kas:
        print("LAIMĖJO:", kas)
        return True
    if sarasas[0] == kas and sarasas[4] == kas and sarasas[8] == kas:
        print("LAIMĖJO:", kas)
        return True
    else:
        return False