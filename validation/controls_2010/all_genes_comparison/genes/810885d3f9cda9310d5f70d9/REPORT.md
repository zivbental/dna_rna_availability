# YML064C
Status: ok. Length: 972 nt. Measured usable bases: 436. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 436 | 0.2643 | 0.2602 |
| rnafold | ok | 436 | 0.2277 | 0.2330 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 33 | -0.6710 | -0.2770 |
| seed_p | 33 | -0.6686 | -0.4659 |
| seed_p_vs_seed_pars | 26 | -0.7803 | -0.6719 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
