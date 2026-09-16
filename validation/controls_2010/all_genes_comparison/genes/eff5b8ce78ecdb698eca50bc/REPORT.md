# YKR049C
Status: ok. Length: 452 nt. Measured usable bases: 282. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 282 | 0.4102 | 0.3684 |
| rnafold | ok | 282 | 0.4566 | 0.4313 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | -0.0382 | 0.0976 |
| seed_p | 126 | -0.2485 | -0.2349 |
| seed_p_vs_seed_pars | 65 | -0.3559 | -0.2892 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
