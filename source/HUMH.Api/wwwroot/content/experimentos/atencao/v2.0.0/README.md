# HUMH A0/A1 v2.0.0 — estado pré-publicação

A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` (`ANBC0=FAIL_DERIVATIONAL`). A1b mantém `D` como candidato sob auditoria estrutural; a ausência de identidade geral não autoriza confirmação independente. O testemunho R8 é derivacional e somente demonstra mecanismo.

Congelamentos correntes:

- `D_i(W)=W`;
- `B_i=1 observer_capacity_unit`;
- workload homogêneo e mínimo não trivial: `K_C=2`;
- deadline canônico preferencial suportado pela arquitetura: `L_A=1`;
- regime basal homogêneo e `SYNCHRONOUS_SNAPSHOT_BARRIER`;
- basal numérico por `eta_EH0` e `lambda_state`;
- A1b HIGH/LOW pré-atribuído e massa global de oportunidades igual por ciclo;
- `ABENCH0` não escolhe mais `K_C` ou `L_A`; nesses itens seu papel é validação cega.

`SCIENTIFIC_RUN_NOT_AUTHORIZED`.

O auditor auxiliar `03_integridade/audit_schedules.py` verifica FIFO, deadlines, borda direita e um testemunho de matching sem executar trajetórias científicas. Seus números não congelam os braços A1b.
