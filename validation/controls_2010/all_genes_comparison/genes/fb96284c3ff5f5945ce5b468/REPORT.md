# YIL116W
Status: ok. Length: 1274 nt. Measured usable bases: 782. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 782 | 0.2916 | 0.2783 |
| rnafold | ok | 782 | 0.2538 | 0.2457 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 354 | 0.0844 | -0.1145 |
| seed_p | 354 | 0.0102 | 0.0860 |
| seed_p_vs_seed_pars | 236 | -0.0790 | -0.0295 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
