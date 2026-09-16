# YDR194C
Status: ok. Length: 2151 nt. Measured usable bases: 814. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 814 | 0.2822 | 0.2629 |
| rnafold | ok | 814 | 0.2714 | 0.2791 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.2035 | -0.2193 |
| seed_p | 82 | 0.0795 | -0.1118 |
| seed_p_vs_seed_pars | 61 | -0.0568 | -0.1521 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
