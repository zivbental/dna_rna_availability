# YNL197C
Status: ok. Length: 3002 nt. Measured usable bases: 1422. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1422 | 0.2514 | 0.2398 |
| rnafold | ok | 1422 | 0.2275 | 0.2285 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 202 | 0.0273 | -0.0597 |
| seed_p | 202 | -0.2026 | -0.0696 |
| seed_p_vs_seed_pars | 162 | -0.2678 | -0.0817 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
