# SCR1
Status: ok. Length: 522 nt. Measured usable bases: 410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 410 | 0.4573 | 0.4293 |
| rnafold | ok | 410 | 0.4514 | 0.4397 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 340 | -0.1726 | -0.2145 |
| seed_p | 340 | -0.2231 | -0.2723 |
| seed_p_vs_seed_pars | 314 | -0.4842 | -0.4721 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
