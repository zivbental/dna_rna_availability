# YJL179W
Status: ok. Length: 508 nt. Measured usable bases: 214. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 214 | 0.2943 | 0.3064 |
| rnafold | ok | 214 | 0.2824 | 0.2872 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.5203 | -0.6958 |
| seed_p | 57 | -0.5738 | -0.4988 |
| seed_p_vs_seed_pars | 54 | -0.3961 | -0.2311 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
