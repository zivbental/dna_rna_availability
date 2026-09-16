# YBR222C
Status: ok. Length: 1846 nt. Measured usable bases: 1332. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1332 | 0.3232 | 0.3099 |
| rnafold | ok | 1332 | 0.2763 | 0.2748 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 933 | -0.0895 | -0.2280 |
| seed_p | 933 | -0.1386 | -0.1390 |
| seed_p_vs_seed_pars | 767 | -0.3045 | -0.3076 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
