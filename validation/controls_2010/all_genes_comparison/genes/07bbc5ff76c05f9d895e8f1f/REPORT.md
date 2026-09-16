# YER110C
Status: ok. Length: 3459 nt. Measured usable bases: 2752. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2752 | 0.2607 | 0.2461 |
| rnafold | ok | 2752 | 0.2496 | 0.2329 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2258 | -0.0866 | -0.0188 |
| seed_p | 2258 | -0.1528 | -0.1218 |
| seed_p_vs_seed_pars | 1901 | -0.1788 | -0.1836 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
