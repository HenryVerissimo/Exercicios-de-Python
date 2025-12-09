
DISCOUNT_PERCENTAGE = {
    "P": 15,
    "E": 10,
    "C": 5
}

def program() -> None:
    while True:
        try:
            value = input("Digite o valor da compra: ")

            if value.count(",") >= 1:
                value = value.replace(",", ".")

            value = float(value)
            break

        except Exception:
            print("Valor da compra é inválido! Digite novamente...")

    category = input("Digite a ctegoria do cliente: ").upper()

    if category not in ["P", "E", "C"]:
        print("Categoria de cliente inválida. Nenhum desconto será aplicado.")

    else:
        value = calculate_price(value, category)

    print(f"O valor total a pagar será: R${value:.2f}")

def calculate_price(value: float, category: str) -> float:
    new_value = value - ((value * DISCOUNT_PERCENTAGE[category]) / 100)
    return new_value


if __name__ == "__main__":

    program()