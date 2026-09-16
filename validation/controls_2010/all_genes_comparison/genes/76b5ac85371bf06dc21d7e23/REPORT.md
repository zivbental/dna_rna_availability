# YPL032C
Status: ok. Length: 2772 nt. Measured usable bases: 1249. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1249 | 0.2262 | 0.2047 |
| rnafold | ok | 1249 | 0.1672 | 0.1570 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 177 | -0.2381 | -0.3983 |
| seed_p | 177 | -0.2724 | -0.1249 |
| seed_p_vs_seed_pars | 155 | -0.2237 | -0.0677 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
