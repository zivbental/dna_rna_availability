# YHR162W
Status: ok. Length: 674 nt. Measured usable bases: 566. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 566 | 0.3818 | 0.3752 |
| rnafold | ok | 566 | 0.3884 | 0.3812 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 528 | -0.1724 | -0.1680 |
| seed_p | 528 | -0.4186 | -0.4060 |
| seed_p_vs_seed_pars | 438 | -0.5193 | -0.5355 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
