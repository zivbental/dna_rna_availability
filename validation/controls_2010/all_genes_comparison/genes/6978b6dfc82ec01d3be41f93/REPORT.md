# YIL034C
Status: ok. Length: 931 nt. Measured usable bases: 659. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 659 | 0.3307 | 0.3161 |
| rnafold | ok | 659 | 0.2991 | 0.2813 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 397 | -0.1557 | -0.0527 |
| seed_p | 397 | -0.1358 | -0.1568 |
| seed_p_vs_seed_pars | 289 | -0.3441 | -0.2926 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
