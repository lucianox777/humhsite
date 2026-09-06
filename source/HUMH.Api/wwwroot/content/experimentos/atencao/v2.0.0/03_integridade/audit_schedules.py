#!/usr/bin/env python3
"""HUMH A1 — auditoria pré-código de fila e schedules, v2.0.0.

Apenas aritmética de demandas, oportunidades e deadlines. Não importa nem
calcula p, EH, eta, consenso ou outcomes científicos. O testemunho A1b é
auxiliar e não congela braços, margens, tamanho amostral ou autoriza um run.
"""
from collections import deque
from dataclasses import dataclass
from pathlib import Path
import argparse
import json

@dataclass
class Job:
    arrival: int
    remaining: int
    completion: int | None = None
    expired: bool = False

def simulate(W, schedules, K_C=2, L_A=1):
    assert W > 0 and K_C > 0 and L_A >= 0
    queues = [deque() for _ in schedules]
    jobs = [[] for _ in schedules]
    cycles = []
    # Há demandas apenas em [0,W-1]. A cauda resolve todos os deadlines.
    for n in range(W + L_A + 2):
        if n < W:
            for i in range(len(schedules)):
                j = Job(n, K_C)
                queues[i].append(j)
                jobs[i].append(j)
        grants, used, updates = [], [], []
        for i, schedule in enumerate(schedules):
            q = schedule(n)
            assert type(q) is int and q >= 0
            grants.append(q)
            for j in list(queues[i]):
                if n > j.arrival + L_A:
                    j.expired = True
                    queues[i].remove(j)
            work = completed = 0
            for _ in range(q):
                if not queues[i]:
                    break
                j = queues[i][0]
                j.remaining -= 1
                work += 1
                if j.remaining == 0:
                    assert j.completion is None
                    j.completion = n
                    assert n <= j.arrival + L_A
                    queues[i].popleft()
                    completed += 1
            used.append(work)
            updates.append(completed)
        cycles.append({"cycle": n, "granted": grants,
                       "used": used, "updates": updates})
    assert all(not q for q in queues), "unresolved demand at right edge"
    assert all(len(row) == W for row in jobs)
    assert all(j.expired != (j.completion is not None)
               for row in jobs for j in row)
    U = [sum(j.completion is not None for j in row) for row in jobs]
    return {"D": [W]*len(schedules), "U": U,
            "A": [u/W for u in U], "cycles": cycles, "jobs": jobs}

def uniform(n):
    return 2 if n % 2 else 0

def high(n):
    return 4 if n % 2 else 0

def low(n):
    return 0

def self_test():
    # Deadline inclusivo: o ciclo de deadline ainda é válido.
    assert simulate(1, [lambda n: 1], L_A=1)["U"] == [1]
    assert simulate(1, [lambda n: 2 if n == 0 else 0], L_A=0)["U"] == [1]
    assert simulate(1, [lambda n: 1], L_A=0)["U"] == [0]
    assert simulate(1, [lambda n: 1 if n == 0 else 0], L_A=1)["U"] == [0]
    # Trabalho maior que a capacidade não é uma tarefa impossível.
    assert simulate(1, [lambda n: 1], L_A=5, K_C=3)["U"] == [1]

    # Uma oportunidade/ciclo, K_C=2, L_A=1: bloqueio de fase do FIFO.
    starved = simulate(20, [lambda n: 1])
    assert starved["U"] == [1]

    witnesses = []
    for W in (2, 4, 6, 8, 20):
        for N in (2, 4, 10):
            u = simulate(W, [uniform]*N)
            h = simulate(W, [high]*(N//2) + [low]*(N//2))
            assert u["U"] == [W//2]*N
            assert h["U"] == [W]*(N//2) + [0]*(N//2)
            assert sum(u["A"])/N == sum(h["A"])/N == 0.5
            assert max(u["A"]) == min(u["A"])
            assert sum(abs(a-0.5) for a in h["A"])/N == 0.5
            for n in range(W):
                for key in ("granted", "used", "updates"):
                    assert sum(u["cycles"][n][key]) == sum(h["cycles"][n][key])
            assert all(sum(c["updates"]) == 0
                       for c in u["cycles"][W+1:]+h["cycles"][W+1:])
            witnesses.append({"W": W, "N": N, "uniform_U": W//2,
                              "high_U": W, "low_U": 0,
                              "Abar": 0.5, "uniform_D_A": 0.0,
                              "heterogeneous_D_A": 0.5,
                              "per_cycle_mass_match": True,
                              "per_cycle_executed_work_match": True,
                              "per_cycle_update_count_match": True})
    # A paridade não é uma conveniência: W ímpar quebra o matching exato.
    odd = simulate(3, [uniform]*2)
    assert odd["U"] == [2, 2]
    assert sum(odd["A"])/2 != 0.5
    return {"status": "PASS", "scientific_run_authorized": False,
            "scope": "INSTRUMENTATION_ONLY",
            "q1_constant_W20_U": 1,
            "witnesses": witnesses,
            "derivational_witness":
              "D_uniform=0; D_heterogeneous=|p_target-p0|"
              "*(1-prod_n(1-eta_n)^2)/2 > 0 for p0!=p_target"
              " and eta_n in (0,1]. This is a construction consequence,"
              " not independent scientific confirmation."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = self_test()
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n",
                               encoding="utf-8")
    print("PASS — instrumentação, FIFO, deadline, borda direita e matching.")
    print("A1b: testemunho auxiliar; confirmação científica NÃO autorizada.")
