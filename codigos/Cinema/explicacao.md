# RESUMO DA PARTE DO Jardel 

**Projeto 15 - Gestão de Cinema e Ingressos** | Luiz Jardel + Ana Rebeca

Minha parte está pronta e testada (5 testes passando). Este arquivo explica o que
tem nela e **o que você precisa saber para encaixar o seu módulo** (vender, cancelar
e relatório). O código completo está no arquivo `modulo_sessoes_assentos.py`.

---

## 1. Resumo do que está pronto

| Função | O que faz |
|---|---|
| `cadastrar_sessao(id, filme, sala, horario, capacidade)` | Cria a sessão e gera os assentos livres |
| `buscar_sessao(id)` | Devolve o dicionário da sessão, ou `None` se não existir |
| `atualizar_sessao(id, campo, novo_valor)` | Muda `filme`, `horario` ou `sala` sem mexer nos ingressos |
| `listar_assentos(id)` | Mostra o mapa da sala (código = livre, `XX` = ocupado) |
| `sessao_lotada(id)` | `True` se a sessão existe e não tem assento livre |
| `assentos_ocupados(sessao)` | Lista dos assentos já vendidos |
| `assentos_livres(sessao)` | Lista dos assentos livres (calculada na hora) |
| `ler_inteiro(msg)` e `ler_texto(msg)` | Leitura com validação, repetem até a entrada ser válida |

Também já tem:
- **12 sessões** cadastradas, com alguns ingressos de exemplo.
- **Menu** com `while True` (por enquanto só com as opções do meu módulo).
- **Testes 1, 2, 3, 4 e a minha parte do 7.**

---

## 2. Como os dados estão guardados (isso é o mais importante pra você)

```python
PRECOS = {"inteira": 30.0, "meia": 15.0, "vip": 45.0}   # tabela de preços
sessoes = []                                            # lista com todas as sessões

# cada sessão é um dicionário:
{
    "id_sessao": 1,
    "filme": "Interestelar",
    "horario": "14:00",
    "sala": "Sala 1",
    "assentos": ["A1", "A2", "A3", ...],   # todos os assentos da sala
    "ingressos": [                          # só os que foram vendidos
        {"assento": "A1", "tipo": "inteira", "preco": 30.0},
    ],
}
```

Pontos de atenção:
- A chave é **`"id_sessao"`** (não `"id"`).
- Os ingressos ficam na lista **`"ingressos"`** de cada sessão, e cada ingresso é um dicionário com `assento`, `tipo` e `preco`.
- Os assentos livres **não são guardados**. `assentos_livres(sessao)` calcula `assentos` menos os assentos de `ingressos`. Então, quando você vender ou cancelar, **só mexa na lista `ingressos`** e o resto se acerta sozinho.
- O código dos assentos é letra + número, em maiúsculas (`"A1"`, `"B3"`). Use `.strip().upper()` no que o usuário digitar.
- O **preço é guardado dentro do ingresso**, copiado de `PRECOS[tipo]` na hora da venda.

---

## 3. O que você pode usar do meu módulo

Para o `vender_ingresso(sessao, assento, tipo)`:
- `assentos_livres(sessao)`: se a lista estiver vazia, é **sessão lotada**.
- `assentos_ocupados(sessao)`: se o assento já estiver nela, é **assento já vendido**.
- `sessao["assentos"]`: para ver se o assento existe naquela sala.
- `PRECOS`: para validar o tipo (`tipo in PRECOS`) e pegar o valor.

Para `relatorio_consolidado()`:
- Percorra a lista global `sessoes` e, dentro de cada uma, `sessao["ingressos"]`.
- Os 3 indicadores podem ser, por exemplo: arrecadação por sessão, contagem e percentual por tipo de ingresso, e ocupação percentual.

**Sugestão de padrão de retorno (o mesmo que eu usei):** as funções devolvem uma
tupla `(True/False, "mensagem")`, e o menu mostra só a mensagem.

```python
ok, msg = vender_ingresso(sessao, "A1", "meia")
print(msg)
```

**Sugestão de ordem das validações em `vender_ingresso`:**
1. Sessão lotada
2. Tipo inválido
3. Assento inexistente
4. Assento já vendido

Se passar por tudo, adicione o ingresso na lista `sessao["ingressos"]` e devolva `True`.

---

## 4. Duas coisas pra gente decidir antes de juntar

**a) Cancelamento: "marcar como cancelado" ou remover da lista?**
No nosso combinado, o `cancelar_ingresso` "marca como cancelado". Mas o meu
`assentos_ocupados` conta **todo ingresso que estiver na lista**. Então temos duas opções:

- **Opção A (mais simples):** cancelar = **remover** o ingresso da lista `ingressos`. Não precisa mexer no meu código.
- **Opção B:** cancelar = colocar `"status": "cancelado"` no ingresso. Aí eu preciso ajustar `assentos_ocupados` para ignorar os cancelados, e o seu relatório também.

Eu voto na **opção A**, que é mais fácil de explicar e tem menos chance de erro.

**b) `id_ingresso`**
Se o `cancelar_ingresso` recebe `id_ingresso`, o ingresso precisa **ter** esse campo. Hoje ele
só tem `assento`, `tipo` e `preco`. Se formos usar `id_ingresso`, a gente decide quem cria
o número e adicionamos a chave `"id_ingresso"` no ingresso. Se cancelarmos pelo **assento**
(`cancelar_ingresso(sessao, assento)`), não precisa de ID e fica mais simples.

---

## 5. Os testes (a divisão que a gente fez)

Eu já fiz os testes 1, 2, 3, 4 e a minha parte do 7. Os seus são o 5, 6, 8 e a sua parte do 7.

Use a função `testar` que já está no código:

```python
testar(numero, nome, entrada, esperado, observado)
```

| Teste | Quem | Ideia |
|---|---|---|
| 5 - Venda normal | Ana | Vender um assento livre e esperar `True` |
| 6 - Assento já vendido | Ana | Vender de novo o mesmo assento e esperar `False` (na sessão 1, o `A1` já está vendido) |
| 7 - Sessão lotada | Luiz + Ana | A sessão 12 já nasce lotada. Eu confirmo com `sessao_lotada(12)`, e você tenta vender nela e espera `False` |
| 8 - Cancelar e revender | Ana | Cancelar um ingresso e vender o mesmo assento de novo, esperando `True` |

Dica: use uma sessão separada de teste e **remova no final** (como eu fiz com a sessão 99),
para os dados reais não ficarem sujos.

---

## 6. Regras para juntar sem dar erro

- **Só uma cópia** de cada função. Não redefina `assentos_ocupados`, `assentos_livres`, `ler_inteiro` e `ler_texto`.
- Use a lista global `sessoes` e o dicionário `PRECOS` que já estão no topo. Não crie outra lista de sessões.
- Mantenha os nomes das suas funções como no combinado (`vender_ingresso`, `cancelar_ingresso`, `relatorio_consolidado`), porque eu vou chamar elas no menu.
- Todo `def` começa na **coluna 0** (sem indentação). Se uma função "sumir", quase sempre é indentação.
- Ordem das células no notebook: **minha parte primeiro, depois a sua**, depois as sessões iniciais, os testes e o menu.

---

## 7. Como o meu menu vai chamar o seu código

Quando você mandar o código, eu acrescento ao menu as opções de vender, cancelar e
relatórios, chamando as suas funções. Assim o menu chega às 6 opções mínimas do PDF
(mais o sair).

---

## 8. Como os dados circulam (para a explicação técnica)

1. O menu lê a opção e os dados digitados, já validados por `ler_inteiro` e `ler_texto`.
2. O menu chama uma função (minha ou sua), que lê ou altera a lista global `sessoes`.
3. A função devolve `(True/False, mensagem)`, e o menu mostra a mensagem.
4. Como tudo fica em memória na lista `sessoes`, a próxima opção do menu já enxerga a mudança.

---

## 9. O que falta pra gente terminar

- [ ] Você: `vender_ingresso`, `cancelar_ingresso`, `relatorio_consolidado` e os testes 5, 6, 8 e a sua parte do 7.
- [ ] Gente decide: cancelar por remoção (opção A) ou por status (B), e se terá `id_ingresso`.
- [ ] Eu: ligar as suas funções ao menu.
- [ ] Juntar tudo no notebook, na ordem combinada, e rodar no **Colab**.
- [ ] Identificação da dupla, conclusão e quadro de contribuição.
- [ ] Cada um estudar o código do outro, porque o professor pode perguntar sobre qualquer trecho.