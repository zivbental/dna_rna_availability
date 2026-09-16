# YFL017W-A
Status: ok. Length: 337 nt. Measured usable bases: 92. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 92 | 0.0047 | 0.0332 |
| rnafold | ok | 92 | 0.1518 | 0.1399 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | 0.1917 | 0.5009 |
| seed_p | 26 | 0.6229 | 0.6634 |
| seed_p_vs_seed_pars | 24 | 0.8802 | 1.0000 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
