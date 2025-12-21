from delivery_order_schema import DeliveryOrder
from delivery_order_process import DeliveryOrderProcess


if __name__ == "__main__":

    orders = [
        DeliveryOrder(1, 500, 500.50, "comum", 1),
        DeliveryOrder(2, 1500, 500.50, "perigosa", 2),
        DeliveryOrder(3, 2000, 500.50, "comum", 2),
        DeliveryOrder(4, 500, 500.50, "perigosa", 1),
        DeliveryOrder(5, 4000, 500.50, "vital", 3),
        DeliveryOrder(6, 300, 500.50, "vital", 1),
        DeliveryOrder(7, 500, 500.50, "comum", 3),
        DeliveryOrder(8, 500, 500.50, "vital", 2),
    ]

    test1 = DeliveryOrderProcess()
    result = test1.process_orders(orders)

    print("Ordens processadas com sucesso:")
    for order in result["orders"]:
        print(order)

    print("\nOrdens com falha no processamento:")
    for invalid_order in result["invalid_orders"]:
        print(invalid_order)

    print(f"\nValor total de crétidos: R${result["total_credits"]:.2f}")