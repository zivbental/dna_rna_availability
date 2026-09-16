# YLR146W-A
Status: ok. Length: 286 nt. Measured usable bases: 135. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 135 | 0.4565 | 0.4350 |
| rnafold | ok | 135 | 0.4032 | 0.3903 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | -0.1627 | -0.2628 |
| seed_p | 51 | -0.3519 | -0.3231 |
| seed_p_vs_seed_pars | 37 | -0.6696 | -0.5720 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
