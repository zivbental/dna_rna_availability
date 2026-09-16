# YOR327C
Status: ok. Length: 519 nt. Measured usable bases: 276. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 276 | 0.3499 | 0.3778 |
| rnafold | ok | 276 | 0.1898 | 0.2257 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 141 | -0.4844 | -0.6925 |
| seed_p | 141 | -0.4942 | -0.4547 |
| seed_p_vs_seed_pars | 81 | -0.5300 | -0.4935 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
