# YMR235C
Status: ok. Length: 1386 nt. Measured usable bases: 1066. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1066 | 0.3706 | 0.3562 |
| rnafold | ok | 1066 | 0.3208 | 0.3036 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 801 | -0.1853 | -0.2495 |
| seed_p | 801 | -0.3762 | -0.3187 |
| seed_p_vs_seed_pars | 688 | -0.4517 | -0.3844 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
