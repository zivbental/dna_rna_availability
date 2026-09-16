# YDR459C
Status: ok. Length: 1372 nt. Measured usable bases: 601. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 601 | 0.3074 | 0.2954 |
| rnafold | ok | 601 | 0.2162 | 0.2116 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | -0.0727 | -0.2609 |
| seed_p | 129 | -0.0961 | 0.0683 |
| seed_p_vs_seed_pars | 91 | -0.2977 | -0.0105 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
