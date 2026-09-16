# YOL088C
Status: ok. Length: 1033 nt. Measured usable bases: 641. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 641 | 0.3046 | 0.3023 |
| rnafold | ok | 641 | 0.3123 | 0.3023 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 287 | -0.2336 | -0.2376 |
| seed_p | 287 | -0.2076 | -0.1988 |
| seed_p_vs_seed_pars | 222 | -0.2083 | -0.2734 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
