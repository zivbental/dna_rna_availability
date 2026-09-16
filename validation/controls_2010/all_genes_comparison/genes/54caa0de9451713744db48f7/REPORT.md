# YLR121C
Status: ok. Length: 1829 nt. Measured usable bases: 693. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 693 | 0.3065 | 0.3003 |
| rnafold | ok | 693 | 0.2352 | 0.2301 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | 0.0547 | -0.0431 |
| seed_p | 68 | -0.0667 | -0.0445 |
| seed_p_vs_seed_pars | 38 | -0.5385 | -0.4969 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
