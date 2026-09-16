# YIL135C
Status: ok. Length: 1517 nt. Measured usable bases: 646. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 646 | 0.1877 | 0.1748 |
| rnafold | ok | 646 | 0.1364 | 0.1304 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 23 | -0.0257 | 0.0198 |
| seed_p | 23 | 0.3171 | 0.3063 |
| seed_p_vs_seed_pars | 4 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
