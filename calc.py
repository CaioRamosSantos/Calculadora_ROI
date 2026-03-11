campanhas = [
    {"nome": "Influencer Local", "custo": 1200, "receita": 3500},
    {"nome": "Anúncio Instagram", "custo": 500, "receita": 2800},
    {"nome": "Panfletagem", "custo": 300, "receita": 150}
]

print(f"{'CAMPANHA':<20} | {'ROI':>10}")
print("-" * 35)

for campanha in campanhas:
    nome = campanha["nome"]
    custo = campanha["custo"]
    receita = campanha["receita"]
    
    roi = (receita - custo) / custo

    print(f"{nome:<20} | {roi:>10.2f}")
