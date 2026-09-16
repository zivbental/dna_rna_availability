# YGR264C
Status: ok. Length: 2487 nt. Measured usable bases: 1988. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1988 | 0.3060 | 0.2985 |
| rnafold | ok | 1988 | 0.2659 | 0.2580 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1622 | -0.1269 | -0.1567 |
| seed_p | 1622 | -0.1930 | -0.2207 |
| seed_p_vs_seed_pars | 1345 | -0.3402 | -0.2981 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
