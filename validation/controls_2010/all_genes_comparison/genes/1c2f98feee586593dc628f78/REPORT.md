# YHR007C
Status: ok. Length: 1971 nt. Measured usable bases: 1709. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1709 | 0.3043 | 0.2925 |
| rnafold | ok | 1709 | 0.1915 | 0.2040 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1665 | -0.1402 | -0.1131 |
| seed_p | 1665 | -0.1587 | -0.1382 |
| seed_p_vs_seed_pars | 1507 | -0.2437 | -0.1796 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
