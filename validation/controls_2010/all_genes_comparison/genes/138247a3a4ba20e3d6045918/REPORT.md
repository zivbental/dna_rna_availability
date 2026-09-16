# YML108W
Status: ok. Length: 581 nt. Measured usable bases: 208. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 208 | 0.4656 | 0.4871 |
| rnafold | ok | 208 | 0.3536 | 0.3824 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | -0.4494 | -0.9136 |
| seed_p | 25 | -0.5793 | -0.4069 |
| seed_p_vs_seed_pars | 10 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
