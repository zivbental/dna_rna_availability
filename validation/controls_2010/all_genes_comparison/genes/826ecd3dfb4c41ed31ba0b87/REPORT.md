# YGR227W
Status: ok. Length: 1724 nt. Measured usable bases: 793. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 793 | 0.1965 | 0.2035 |
| rnafold | ok | 793 | 0.1931 | 0.1986 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 128 | -0.0802 | 0.0028 |
| seed_p | 128 | -0.0367 | -0.0651 |
| seed_p_vs_seed_pars | 84 | -0.4282 | -0.4294 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
