# YBR035C
Status: ok. Length: 803 nt. Measured usable bases: 556. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 556 | 0.3495 | 0.3447 |
| rnafold | ok | 556 | 0.2833 | 0.2653 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 336 | -0.0801 | -0.0592 |
| seed_p | 336 | -0.0288 | -0.0821 |
| seed_p_vs_seed_pars | 289 | -0.1920 | -0.2772 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
