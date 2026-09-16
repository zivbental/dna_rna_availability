# YPL256C
Status: ok. Length: 2009 nt. Measured usable bases: 1181. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1181 | 0.2778 | 0.2587 |
| rnafold | ok | 1181 | 0.2485 | 0.2278 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 502 | -0.1562 | -0.1091 |
| seed_p | 502 | -0.1595 | -0.1586 |
| seed_p_vs_seed_pars | 389 | -0.2340 | -0.2232 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
