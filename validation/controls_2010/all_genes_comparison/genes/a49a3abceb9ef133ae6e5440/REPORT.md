# YBR236C
Status: ok. Length: 1485 nt. Measured usable bases: 630. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 630 | 0.3068 | 0.2871 |
| rnafold | ok | 630 | 0.2866 | 0.2859 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.3386 | -0.3113 |
| seed_p | 82 | -0.5858 | -0.4879 |
| seed_p_vs_seed_pars | 48 | -0.5152 | -0.5198 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
