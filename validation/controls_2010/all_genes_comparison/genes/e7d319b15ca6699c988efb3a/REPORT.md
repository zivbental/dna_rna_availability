# YDR328C
Status: ok. Length: 826 nt. Measured usable bases: 682. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 682 | 0.3737 | 0.3604 |
| rnafold | ok | 682 | 0.3346 | 0.3229 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 591 | -0.2486 | -0.2248 |
| seed_p | 591 | -0.4135 | -0.4093 |
| seed_p_vs_seed_pars | 509 | -0.4659 | -0.4808 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
