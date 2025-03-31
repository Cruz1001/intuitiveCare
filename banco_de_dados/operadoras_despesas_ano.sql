SELECT contascontabeis.REG_ANS, planossaude.Nome_Fantasia, SUM(contascontabeis.VL_SALDO_FINAL) AS Total_Despesas
FROM ContasContabeis
JOIN PlanosSaude ON contascontabeis.REG_ANS = planossaude.Registro_ANS
WHERE contascontabeis.DESCRICAO ILIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%'
AND contascontabeis.DATA BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY contascontabeis.REG_ANS, planossaude.Nome_Fantasia
ORDER BY Total_Despesas DESC
LIMIT 10;