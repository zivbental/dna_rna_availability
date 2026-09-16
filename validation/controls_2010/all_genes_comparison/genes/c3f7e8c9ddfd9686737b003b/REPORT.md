# YDR298C
Status: ok. Length: 928 nt. Measured usable bases: 717. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 717 | 0.2904 | 0.2742 |
| rnafold | ok | 717 | 0.1797 | 0.2019 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 566 | -0.1711 | -0.1349 |
| seed_p | 566 | -0.1574 | -0.1705 |
| seed_p_vs_seed_pars | 430 | -0.3787 | -0.3484 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
