# YOR151C
Status: ok. Length: 3971 nt. Measured usable bases: 2220. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2220 | 0.3229 | 0.3089 |
| rnafold | ok | 2220 | 0.2775 | 0.2554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 829 | -0.0890 | -0.0170 |
| seed_p | 829 | -0.0541 | -0.0293 |
| seed_p_vs_seed_pars | 562 | -0.0823 | -0.0844 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
