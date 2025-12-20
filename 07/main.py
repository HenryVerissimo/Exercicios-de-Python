from typing import Dict, List

class ComercialPerformmanceProcessor:
    def __init__(self) -> None:
        self._top_performer: dict = {}
        self._average_ticket: float = 0.0
        self._total_volume: float = 0.0
        self._sales_value_per_category: dict = {}
        self._bonus_amount_per_seller: dict = {}
        self._valid_sales: int = 0

    def process_data(self, sales_data: List[dict]) -> Dict[str, str | float | dict] | None:
        for sale in sales_data:
            if not self._validate_sale(sale):
                continue

            self._calculate_bonus(sale)
            self._add_sales_value_per_category(sale)
            self._total_volume += sale["valor"]

        self._set_top_performer()

        if self._valid_sales >= 1:
            self._average_ticket = self._total_volume / self._valid_sales

            return {
                "top_performer": self._top_performer["vendedor"],
                "average_ticket": self._average_ticket,
                "total_volume": self._total_volume,
                "sales_value_per_category": self._sales_value_per_category 
            }

    def _validate_sale(self, sale) -> bool:
        if sale["valor"] <= 0 or not isinstance(sale["valor"], float):
            return False
        
        self._valid_sales += 1
        return True

    def _calculate_bonus(self, sale: dict) -> None:
        if sale["valor"] < 2000:
            rate = 0.05
        
        elif sale["valor"] >= 2000 and sale["valor"] <= 5000:
            rate = 0.10
        
        else:
            rate = 0.15
            
        bonus = sale["valor"] * rate
        self._bonus_amount_per_seller[sale["vendedor"]] = self._bonus_amount_per_seller.get(sale["vendedor"], 0) + bonus

    def _add_sales_value_per_category(self, sale: dict) -> None:
        self._sales_value_per_category[sale["categoria"]] = self._sales_value_per_category.get(sale["categoria"], 0) + sale["valor"]

    def _set_top_performer(self) -> None:
        for seller, bonus in self._bonus_amount_per_seller.items():
            if not self._top_performer:
                self._top_performer = dict()
                self._top_performer["vendedor"] = seller
                self._top_performer["bonus"] = bonus
            
            elif self._top_performer["bonus"] < bonus:
                self._top_performer["vendedor"] = seller
                self._top_performer["bonus"] = bonus
        
if __name__ == "__main__":

    dataset = [
        {"vendedor": "Ana", "valor": 7200.00, "categoria": "Eletrônicos"},
        {"vendedor": "João", "valor": 1200.00, "categoria": "Vestuário"},
        {"vendedor": "Maria", "valor": 3500.00, "categoria": "Eletrônicos"},
        {"vendedor": "Pedro", "valor": 4100.00, "categoria": "Alimentos"},
        {"vendedor": "Clara", "valor": 950.00, "categoria": "Vestuário"},
        {"vendedor": "Beatriz", "valor": 5000.00, "categoria": "Eletrônicos"}
    ]

    analiser = ComercialPerformmanceProcessor()
    report = analiser.process_data(dataset)

    if report is not None:
        print(f"Funcionário com maior Bonus: {report["top_performer"]}")
        print(f"Valor do ticket médio: R${report["average_ticket"]:.2f}")
        print(f"Valor Bruto de vendas: R${report["total_volume"]:.2f}")
        print("\nTotal de vendas por categoria:")

        if isinstance(report["sales_value_per_category"], dict):
            for category, value in report["sales_value_per_category"].items():
                print(f"{category} - R${value:.2f}")