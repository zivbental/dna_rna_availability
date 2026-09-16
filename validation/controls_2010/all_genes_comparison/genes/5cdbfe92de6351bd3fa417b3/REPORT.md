# YBR023C
Status: ok. Length: 3668 nt. Measured usable bases: 2174. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2174 | 0.2744 | 0.2663 |
| rnafold | ok | 2174 | 0.2180 | 0.2225 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 820 | -0.2424 | -0.1221 |
| seed_p | 820 | -0.3003 | -0.2214 |
| seed_p_vs_seed_pars | 641 | -0.4217 | -0.3508 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
