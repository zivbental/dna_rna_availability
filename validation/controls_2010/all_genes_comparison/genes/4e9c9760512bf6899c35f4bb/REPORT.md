# YKL032C
Status: ok. Length: 2111 nt. Measured usable bases: 835. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 835 | 0.3051 | 0.2988 |
| rnafold | ok | 835 | 0.2313 | 0.2198 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | -0.0959 | 0.2163 |
| seed_p | 28 | -0.1069 | 0.3531 |
| seed_p_vs_seed_pars | 17 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
