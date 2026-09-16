# YBR085C-A
Status: ok. Length: 649 nt. Measured usable bases: 337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 337 | 0.2682 | 0.2628 |
| rnafold | ok | 337 | 0.2266 | 0.2251 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 74 | -0.2308 | -0.3885 |
| seed_p | 74 | -0.5167 | -0.5249 |
| seed_p_vs_seed_pars | 51 | -0.1373 | -0.0647 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
