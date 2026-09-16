# YJL076W
Status: ok. Length: 3659 nt. Measured usable bases: 1762. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1762 | 0.3896 | 0.3800 |
| rnafold | ok | 1762 | 0.3553 | 0.3384 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 284 | -0.0972 | -0.1564 |
| seed_p | 284 | -0.5434 | -0.2866 |
| seed_p_vs_seed_pars | 242 | -0.6224 | -0.3843 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
