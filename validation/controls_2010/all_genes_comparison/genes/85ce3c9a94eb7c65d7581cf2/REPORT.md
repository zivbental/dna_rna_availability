# YPL183C
Status: ok. Length: 3174 nt. Measured usable bases: 1413. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1413 | 0.3162 | 0.3078 |
| rnafold | ok | 1413 | 0.2609 | 0.2613 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 230 | 0.1709 | 0.2838 |
| seed_p | 230 | 0.0419 | -0.0814 |
| seed_p_vs_seed_pars | 160 | 0.0069 | -0.1611 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
