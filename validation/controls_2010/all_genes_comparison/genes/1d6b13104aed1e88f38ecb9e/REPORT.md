# YIL043C
Status: ok. Length: 951 nt. Measured usable bases: 864. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 864 | 0.3398 | 0.3162 |
| rnafold | ok | 864 | 0.2660 | 0.2256 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 849 | -0.1332 | -0.1535 |
| seed_p | 849 | -0.2653 | -0.2134 |
| seed_p_vs_seed_pars | 786 | -0.4190 | -0.3355 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
