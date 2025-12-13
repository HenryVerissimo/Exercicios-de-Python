from typing import List

class BankAccount:
    def __init__(self, client_name: str) -> None:
        self.client_name: str = client_name
        self._account_balance: float = 0
        self._deposits_sequence: int = 0
        self._max_deposits_sequence: int = 0

    def make_transaction(self, transactions: List[tuple[str, float]]) -> None:
        for transaction in transactions:
            if transaction[0].upper() in ["DEPOSIT", "DEPOSITO"]:
                self._deposit_money(transaction[1])
            
            elif transaction[0].upper() in ["WITHDRAW", "SAQUE"]:
                self._withdraw_money(transaction[1])

            else:
                print(f'ERRO! Tipo de transação "{transaction[0]}" não reconhecida!')

    def _withdraw_money(self, value: float) -> None:
        if self._verify_money_limit(value):
            self._account_balance -= value
            self._deposits_sequence = 0

            print(f"Foram sacados R${value:.2f} em sua conta")

        else:
            print(f"Saldo insuficiente! Não foi possível sacar R${value:.2f}")
    
    def _deposit_money(self, value: float) -> None:
        self._account_balance += value
        self._deposits_sequence += 1

        if self._deposits_sequence > self._max_deposits_sequence:
                self._max_deposits_sequence = self._deposits_sequence

        print(f"Foram depositados R${value:.2f} em sua conta.")

    def _verify_money_limit(self, value: float) -> bool:
        return value <= self._account_balance
    
    def account_report(self) -> dict:
         return {
              "account_balance": self._account_balance,
              "max_deposits_sequence": self._max_deposits_sequence
         }


if __name__ == "__main__":

    new_account = BankAccount(client_name="Henrique")
    new_account.make_transaction([("DEPOSIT", 200.00),("WITHDRAW", 200.00), ("DEPOSIT", 200.00), ("DEPOSIT", 2500.00), ("DEPOSIT", 100.00)])
    account_report = new_account.account_report()

    print(f"Dinheiro em conta: R${account_report["account_balance"]:.2f}")
    print(f"Maior número de depósitos consecutivos: {account_report["max_deposits_sequence"]}")