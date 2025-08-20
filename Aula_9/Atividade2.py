produtos = (
    ("Arroz", 5.99, 10),
    ("Feijão", 7.49, 3),
    ("Leite", 4.89, 5),
    ("Óleo", 9.99, 2),
    ("Açúcar", 3.29, 5)
)
Total = 0
print("LISTA DE PRODUTOS")
for nome, preco, qt in produtos:
    print(f"{nome:.<20} {preco:.2f} X {qt} = R$ {preco * qt:.2f}")
    Total = Total + preco * qt

print (f'\t valor total da compra : R$ {Total} ')
print(f'\t DEsconto : - 10% ')
print(f'\t Valor Final: {(Total * 0.9):.2f} ')