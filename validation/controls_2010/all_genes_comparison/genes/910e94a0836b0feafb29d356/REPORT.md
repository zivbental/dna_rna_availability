# YKR085C
Status: ok. Length: 631 nt. Measured usable bases: 393. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 393 | 0.4086 | 0.4293 |
| rnafold | ok | 393 | 0.4006 | 0.4144 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 206 | -0.0784 | -0.2734 |
| seed_p | 206 | -0.2289 | -0.2806 |
| seed_p_vs_seed_pars | 156 | -0.0748 | -0.2979 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
