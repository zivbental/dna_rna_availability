# YDR348C
Status: ok. Length: 1880 nt. Measured usable bases: 827. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 827 | 0.3142 | 0.2955 |
| rnafold | ok | 827 | 0.2331 | 0.2261 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | -0.0216 | -0.0889 |
| seed_p | 126 | -0.4347 | -0.2892 |
| seed_p_vs_seed_pars | 100 | -0.2540 | -0.1696 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
