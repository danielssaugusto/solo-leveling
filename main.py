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

        self.daily_training_log = {
            "flexões": 0,
            "abdominais": 0,
            "agachamentos": 0,
            "corrida": 0
        }

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

    # Sistema de treino
    def daily_quest(self, workout, sets):
        DAILY_REPS = 100  # Repetições
        DAILY_RUNNING = 10  # Em Km

        XP_PER_REP_TRAINING = 50
        XP_PER_RUN_TRAINING = 100

        # Treinos em Repetições
        workout_reps = ["flexões", "abdominais", "agachamentos"]
        # Treinos em Distância
        workout_meters = ["corrida", "caminhada"]

        if workout not in self.daily_training_log:
            print("Treino desconhecido.")
            return

        # Soma ao histórico
        self.daily_training_log[workout] += sets
        total = self.daily_training_log[workout]

        # Verifica tipo de treino e metas
        if workout in workout_reps:
            meta = DAILY_REPS
            xp_por_treino = XP_PER_REP_TRAINING
            unidade = "reps"
        elif workout in workout_meters:
            meta = DAILY_RUNNING
            xp_por_treino = XP_PER_RUN_TRAINING
            unidade = "km"
        else:
            print("Tipo de treino inválido.")
            return

        # Verifica quantas vezes completou a meta
        completou_vezes = total // meta

        if completou_vezes > 0:
            xp_total = completou_vezes * xp_por_treino
            print(f"\n✅ {workout.title()} completo {completou_vezes}x! Ganhou {xp_total} XP.")
            self.gain_xp(xp_total)
        else:
            print(f"{workout.title()}: {total}/{meta} {unidade}")
        
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
    hunter_name = input("Nome: ")
    player = Hunter(hunter_name)
    player.display_status()

    while True:
        print("\nO que você quer fazer?")
        print("1. Treino Diário")
        print("2. Ganhar XP (Completar Missão/Dungeon)")
        print("3. Ver Status")
        print("4. Sair")

        choice = input("Sua escolha: ")

        if choice == '1':
            print("\nEscolha o treino (progresso do dia):")
            print(f"[1] Flexões: {player.daily_training_log['flexões']}/100 reps")
            print(f"[2] Abdominais: {player.daily_training_log['abdominais']}/100 reps")
            print(f"[3] Agachamentos: {player.daily_training_log['agachamentos']}/100 reps")
            print(f"[4] Corrida: {player.daily_training_log['corrida']}/10 km")
            treino_opcao = input("Treino: ")

            treinos = {
                '1': 'flexões',
                '2': 'abdominais',
                '3': 'agachamentos',
                '4': 'corrida'
            }

            treino_escolhido = treinos.get(treino_opcao)
            if not treino_escolhido:
                print("Opção inválida.")
                continue

            try:
                sets = int(input(f"Quantos {'km' if treino_escolhido == 'quilometros' else 'repetições'} você fez? "))
                player.daily_quest(treino_escolhido, sets)
            except ValueError:
                print("Digite um número válido.")

        elif choice == '2':
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
        # Aplicar lógica da opção 2 (Missões e Dungeons)

        elif choice == '3':
            player.display_status()
        elif choice == '4':
            print("Saindo do simulador. Até a próxima caçada!")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    run_simulation()