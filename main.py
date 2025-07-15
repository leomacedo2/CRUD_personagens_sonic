from database import (
    criar_tabela,
    adicionar_personagem,
    listar_personagens,
    atualizar_personagem,
    deletar_personagem,
    buscar_por_id,
    buscar_por_campo,
    importar_sql,
    limpar_tabela,
    exportar_para_csv
)

# Exibição do menu para interação do Banco de dados
def menu():
    print("\n--- Banco de Dados do Universo Sonic 🌀 ---")
    print("1. Adicionar personagem")
    print("2. Listar todos")
    print("3. Atualizar personagem")
    print("4. Remover personagem")
    print("5. Buscar personagem por campo")
    print("6. Sair")
    print("7. Importar dados iniciais sugeridos")
    print("8. Exportar backup da tabela para CSV")

def iniciar():
    criar_tabela()

    while True:
        menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do personagem: ")
            tipo = input("Tipo (Speed, Power, Fly): ")
            time = input("Time (Sonic, Dark, Chaotix, etc): ")
            cor = input("Cor predominante: ")
            poderes = input("Poderes: ")

            adicionar_personagem(nome, tipo, time, cor, poderes)
            print(f"{nome} adicionado com sucesso!")

        elif escolha == "2":
            personagens = listar_personagens()

            if not personagens:
                print("⚠️  Nenhum personagem cadastrado ainda.")
            
            else:
                print("\n--- Lista de Personagens ---")
                for p in personagens:
                    print(f"Nome: {p[1]} | Tipo: {p[2]} | Time: {p[3]} | Cor: {p[4]} | Poderes: {p[5]}")

        elif escolha == "3":
            personagens = listar_personagens()

            if not personagens:
                print("⚠️  Nenhum personagem cadastrado ainda.")

            else:
                print("\n--- Personagens disponíveis para atualização ---")
                for p in personagens:
                    print(f"ID: {p[0]} | {p[1]}")
            
                try:
                    id = int(input("\nID do personagem a atualizar: "))
                    personagem = buscar_por_id(id)

                    if personagem:
                        print("\n📝 Dados atuais do personagem:")
                        print(f"Nome: {personagem[1]} | Tipo: {personagem[2]} | Time: {personagem[3]} | Cor: {personagem[4]} | Poderes: {personagem[5]}")
                        print()

                        nome = input("Novo nome: ")
                        tipo = input("Novo tipo: ")
                        time = input("Novo time: ")
                        cor = input("Nova cor: ")
                        poderes = input("Novos poderes: ")

                        atualizar_personagem(id, nome, tipo, time, cor, poderes)
                        print("✅ Personagem atualizado com sucesso!")
                    else:
                        print("❌ ID não encontrado. Nenhuma atualização realizada.")
                except ValueError:
                    print("⚠️  Entrada inválida. Por favor, digite um número.")
        
        elif escolha == "4":
            personagens = listar_personagens()

            if not personagens:
                print("⚠️  Nenhum personagem cadastrado ainda.")
            
            else:
                print("\n--- Personagens disponíveis para exclusão ---")
                for p in personagens:
                    print(f"ID: {p[0]} | {p[1]}")

                try:
                    id = int(input("\nID do personagem a remover: "))
                    personagem = buscar_por_id(id)

                    if personagem:
                        print(f"\nVocê está prestes a remover: {personagem[1]} (ID: {personagem[0]})")
                        confirmacao = input("Tem certeza que deseja apagar? (s/n): ").lower()

                        if confirmacao == "s":
                            deletar_personagem(id)
                            print("🗑️  Personagem removido com sucesso!")
                        else:
                            print("❌ Remoção cancelada.")
                    else:
                        print("❌ ID não encontrado. Nenhuma exclusão realizada.")
                except ValueError:
                    print("⚠️  Entrada inválida. Por favor, digite um número.")
        
        elif escolha == "5":
            campos = {
                "1": "nome",
                "2": "tipo",
                "3": "time",
                "4": "cor",
                "5": "poderes"
            }
            
            print("\n🔎 Buscar personagem por campo")
            print("Digite o número do campo que deseja buscar:")
            print("1 - nome | 2 - tipo | 3 - time | 4 - cor | 5 - poderes")

            escolha_campo = input("\nEscolha: ")

            campo = campos.get(escolha_campo)

            if not campo:
                print("❌  Opção inválida. Campo não existe.")
                continue

            valor = input(f"Digite o valor que deseja buscar em '{campo}': ")

            # Faz a busca no banco
            personagens = buscar_por_campo(campo, valor)

            if personagens:
                print(f"\n📋 Resultados para {campo} = '{valor}':")
                for p in personagens:
                    print(f"Nome: {p[1]} | Tipo: {p[2]} | Time: {p[3]} | Cor: {p[4]} | Poderes: {p[5]}")
            else:
                print("⚠️ Nenhum personagem encontrado com esse critério.")

        elif escolha == "6":
            print("Encerrando programa. Até mais!")
            break


        elif escolha == "7":
            print("\n🧩 Importar personagens sugeridos")
            print("1 - Adicionar ao banco atual")
            print("2 - Substituir todos os dados existentes")
            opcao = input("Escolha uma opção (1 ou 2): ")

            if opcao not in ["1", "2"]:
                print("❌ Opção inválida.")
                continue

            if opcao == "2":
                confirm = input("⚠️  Isso apagará todos os personagens cadastrados. Tem certeza? (s/n): ").lower()
                if confirm != "s":
                    print("❌ Operação cancelada.")
                    continue
                limpar_tabela()

            try:
                importar_sql("dados_iniciais.sql")
                print("✅ Dados sugeridos importados com sucesso!")
            except FileNotFoundError:
                print("❌ Arquivo 'dados_iniciais.sql' não encontrado.")
            except Exception as e:
                print(f"❌ Erro ao importar dados: {e}")
        
        elif escolha == "8":
            exportar_para_csv()

        else:
            print("❌ Opção inválida. Tente novamente.")

# Inicia o sistema
iniciar()

