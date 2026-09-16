# YGL062W
Status: ok. Length: 4007 nt. Measured usable bases: 1727. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1727 | 0.2822 | 0.2844 |
| rnafold | ok | 1727 | 0.2278 | 0.2257 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 312 | -0.0283 | -0.1909 |
| seed_p | 312 | -0.1247 | -0.1342 |
| seed_p_vs_seed_pars | 214 | -0.3625 | -0.5300 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
