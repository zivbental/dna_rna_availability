# YDR451C
Status: ok. Length: 1305 nt. Measured usable bases: 546. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 546 | 0.3014 | 0.3003 |
| rnafold | ok | 546 | 0.3210 | 0.3252 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | 0.2845 | 0.5521 |
| seed_p | 44 | 0.8447 | 0.6580 |
| seed_p_vs_seed_pars | 35 | 0.8519 | 0.6874 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
