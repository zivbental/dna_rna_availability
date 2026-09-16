# YBR133C
Status: ok. Length: 2549 nt. Measured usable bases: 1448. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1448 | 0.2346 | 0.2111 |
| rnafold | ok | 1448 | 0.2393 | 0.2332 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 446 | -0.0844 | 0.0462 |
| seed_p | 446 | -0.0763 | -0.0184 |
| seed_p_vs_seed_pars | 322 | -0.1467 | -0.0748 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
