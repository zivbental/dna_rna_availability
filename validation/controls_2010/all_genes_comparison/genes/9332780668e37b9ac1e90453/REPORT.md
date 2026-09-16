# YGL173C
Status: ok. Length: 5044 nt. Measured usable bases: 2782. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2782 | 0.3273 | 0.3199 |
| rnafold | ok | 2782 | 0.3117 | 0.3110 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 890 | -0.0267 | -0.1369 |
| seed_p | 890 | -0.1911 | -0.2222 |
| seed_p_vs_seed_pars | 681 | -0.2362 | -0.2795 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
