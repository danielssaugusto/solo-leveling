class Hunter:
    def __init__(self, name="Caçador Iniciante"):
        self.name = name
        self.level = 1
        self.current_xp = 0
        self.xp_to_next_level = 100  # XP necessário para o próximo nível
        self.status_points_available = 0

        # Status do caçador
        self.strength = 10
        self.agility = 10
        self.perception = 10
        self.vitality = 10
        self.intelligence = 10

        self.hp = self.vitality * 10 + 50 # HP inicial baseado na vitalidade
        self.mp = self.intelligence * 5 + 20 # MP inicial baseado na inteligência

    def display_status(self):
        print(f"\n--- Status de {self.name} ---")
        print(f"Nível: {self.level}")
        print(f"XP Atual: {self.current_xp}/{self.xp_to_next_level}")
        print(f"Pontos de Status Disponíveis: {self.status_points_available}")
        print(f"HP: {self.hp}")
        print(f"MP: {self.mp}")
        print(f"Força (STR): {self.strength}")
        print(f"Agilidade (AGI): {self.agility}")
        print(f"Percepção (PER): {self.perception}")
        print(f"Vitalidade (VIT): {self.vitality}")
        print(f"Inteligência (INT): {self.intelligence}")
        print("----------------------------")

    def gain_xp(self, amount):
        print(f"\nVocê ganhou {amount} de XP!")
        self.current_xp += amount

        # Loop para garantir que o caçador suba múltiplos níveis se ganhar muito XP
        while self.current_xp >= self.xp_to_next_level:
            self.level_up()

        self.display_status()

    def level_up(self):
        self.level += 1
        self.current_xp -= self.xp_to_next_level # Subtrai o XP necessário para o nível atual
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5) # Aumenta XP necessário para o próximo nível
        self.status_points_available += 5 # Ganha 5 pontos para distribuir

        # >>> ADIÇÃO: Aumento automático de atributos a cada nível <<<
        self.strength += 1
        self.agility += 1
        self.perception += 1
        self.vitality += 1
        self.intelligence += 1
        print("Seus atributos base aumentaram um pouco com o nível!")
        # >>> FIM DA ADIÇÃO <<<
        
        print(f"*** PARABÉNS! {self.name} subiu para o Nível {self.level}! ***")
        print(f"Você ganhou {self.status_points_available} pontos de status para distribuir.")
        self.distribute_status_points()

        # Recalcula HP e MP baseados nos novos status (incluindo o aumento automático)
        self.hp = self.vitality * 10 + 50
        self.mp = self.intelligence * 5 + 20

    def distribute_status_points(self):
        # Evita entrar no loop se não houver pontos para distribuir
        if self.status_points_available == 0:
            return

        while self.status_points_available > 0:
            self.display_status()
            print("\nEscolha qual status aumentar (digite o número):")
            print("1. Força (STR)")
            print("2. Agilidade (AGI)")
            print("3. Percepção (PER)")
            print("4. Vitalidade (VIT)")
            print("5. Inteligência (INT)")
            print(f"Pontos restantes: {self.status_points_available}")

            try:
                choice = int(input("Sua escolha: "))
                points_to_add_str = input(f"Quantos pontos você quer adicionar (Máx: {self.status_points_available})? ")
                
                # Validação para garantir que o input seja um número
                if not points_to_add_str.isdigit():
                    print("Quantidade inválida. Digite um número.")
                    continue
                    
                points_to_add = int(points_to_add_str)

                if points_to_add > self.status_points_available or points_to_add <= 0:
                    print("Quantidade inválida de pontos. Tente novamente.")
                    continue

                if choice == 1:
                    self.strength += points_to_add
                elif choice == 2:
                    self.agility += points_to_add
                elif choice == 3:
                    self.perception += points_to_add
                elif choice == 4:
                    self.vitality += points_to_add
                elif choice == 5:
                    self.intelligence += points_to_add
                else:
                    print("Escolha inválida. Tente novamente.")
                    continue
                
                self.status_points_available -= points_to_add
                print(f"Status atualizado! Pontos restantes: {self.status_points_available}")

            except ValueError:
                print("Entrada inválida. Digite um número.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

# --- Execução do Simulador ---
def run_simulation():
    hunter_name = input("Digite o nome do seu caçador: ")
    player = Hunter(hunter_name)
    player.display_status()

    while True:
        print("\nO que você quer fazer?")
        print("1. Ganhar XP (Completar Missão/Dungeon)")
        print("2. Ver Status")
        print("3. Sair")

        choice = input("Sua escolha: ")

        if choice == '1':
            try:
                xp_gained_str = input("Quanto XP você ganhou? ")
                if not xp_gained_str.isdigit():
                    print("XP deve ser um número válido.")
                    continue

                xp_gained = int(xp_gained_str)
                if xp_gained <= 0:
                    print("XP deve ser um valor positivo.")
                    continue
                player.gain_xp(xp_gained)
            except ValueError:
                print("Entrada inválida. Digite um número para o XP.")
        elif choice == '2':
            player.display_status()
        elif choice == '3':
            print("Saindo do simulador. Até a próxima caçada!")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    run_simulation()