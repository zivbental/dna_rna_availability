# YLR170C
Status: ok. Length: 708 nt. Measured usable bases: 260. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 260 | 0.5220 | 0.5126 |
| rnafold | ok | 260 | 0.3930 | 0.3848 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 3 | undefined | undefined |
| seed_p | 3 | undefined | undefined |
| seed_p_vs_seed_pars | 2 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
