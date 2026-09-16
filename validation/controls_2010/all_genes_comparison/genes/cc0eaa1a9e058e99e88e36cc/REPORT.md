# YNL031C
Status: ok. Length: 663 nt. Measured usable bases: 438. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 438 | 0.4589 | 0.4454 |
| rnafold | ok | 438 | 0.4681 | 0.4424 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 333 | -0.0456 | -0.0752 |
| seed_p | 333 | -0.4486 | -0.4103 |
| seed_p_vs_seed_pars | 247 | -0.7181 | -0.6363 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
