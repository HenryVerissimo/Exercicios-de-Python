from typing import List, Dict

from delivery_order_schema import DeliveryOrder
from config import (
    ACCEPTED_TYPES,
    CREDITS_VALUE_STANDARD,
    MAX_WEIGHT
)


class DeliveryOrderProcess:
    def __init__(self) -> None:
        self._total_credits: float = 0.0
        self._order_queue: List[DeliveryOrder] = []
        self._invalid_orders: List[Dict[str, DeliveryOrder | str]] = []
        self._processed_orders: List[Dict[str, DeliveryOrder | str | float]] = []

    def process_orders(self, order_list: List[DeliveryOrder]) -> dict:
        self._organize_order_queue(order_list)

        for order in self._order_queue:
            credits_value: float = self._calculate_credits_value(order)

            processed_order: dict = {
                "order": order,
                "status": "Success",
                "value": credits_value
            }

            self._processed_orders.append(processed_order)

        return {
            "orders": self._processed_orders,
            "invalid_orders": self._invalid_orders,
            "total_credits": self._total_credits
        }
    
    def _validate_orders(self, new_order: DeliveryOrder, index: int, order_list: List[DeliveryOrder]) -> bool:
        if new_order.weight > MAX_WEIGHT:
            status: str = "Erro: Excesso de peso"

        elif new_order.distance <= 0:
            status: str = "Erro: Destino inválido"

        else:
            return True
        
        invalid_order = {
                "order": new_order,
                "status": status
        }
        
        self._invalid_orders.append(invalid_order)
        return False
                
    def _organize_order_queue(self, order_list: List[DeliveryOrder]) -> None:
        for index, new_order in enumerate(order_list):
            validated = self._validate_orders(new_order, index, order_list)
            if not validated:
                continue

            if not self._order_queue:
                self._order_queue.append(new_order)
                continue
            
            for index, order in enumerate(self._order_queue):
                if ACCEPTED_TYPES.index(new_order.type_of_load) < ACCEPTED_TYPES.index(order.type_of_load):
                    self._order_queue.insert(index, new_order)
                    break

                if ACCEPTED_TYPES.index(new_order.type_of_load) == ACCEPTED_TYPES.index(order.type_of_load):
                    if new_order.urgency > order.urgency:
                        self._order_queue.insert(index, new_order)
                        break
                    
                    if (new_order.urgency == order.urgency) and new_order.distance < order.distance:
                        self._order_queue.insert(index, new_order)
                        break

                if len(self._order_queue) == (index + 1):
                    self._order_queue.append(new_order)
                    break
            
    def _calculate_credits_value(self, order: DeliveryOrder) -> float:
        value = CREDITS_VALUE_STANDARD
        value += int(order.distance) * 10

        if order.weight > 500:
            value += (value * 15) / 100

        if order.type_of_load == ACCEPTED_TYPES[1]:
            value += 50

        if order.type_of_load == ACCEPTED_TYPES[2]:
            value += 100

        if order.distance < 5 and order.type_of_load == ACCEPTED_TYPES[0]:
            value -= (value * 5) / 100
        
        self._total_credits += value
        return value
