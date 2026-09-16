# YGL092W
Status: ok. Length: 4051 nt. Measured usable bases: 1748. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1748 | 0.3163 | 0.2933 |
| rnafold | ok | 1748 | 0.2438 | 0.2321 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 168 | -0.1354 | 0.0022 |
| seed_p | 168 | -0.2264 | -0.1176 |
| seed_p_vs_seed_pars | 112 | 0.0567 | 0.0595 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
