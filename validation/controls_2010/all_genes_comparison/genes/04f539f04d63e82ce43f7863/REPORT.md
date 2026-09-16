# YDR326C
Status: ok. Length: 4648 nt. Measured usable bases: 1944. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1944 | 0.3188 | 0.2997 |
| rnafold | ok | 1944 | 0.2930 | 0.2806 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.3014 | -0.1965 |
| seed_p | 137 | -0.0439 | -0.0647 |
| seed_p_vs_seed_pars | 80 | -0.2462 | -0.1061 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
