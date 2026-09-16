# YBR115C
Status: ok. Length: 4322 nt. Measured usable bases: 1991. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1991 | 0.3553 | 0.3288 |
| rnafold | ok | 1991 | 0.3240 | 0.2964 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 235 | -0.0284 | -0.3331 |
| seed_p | 235 | -0.1887 | -0.2720 |
| seed_p_vs_seed_pars | 151 | -0.0431 | -0.1078 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
