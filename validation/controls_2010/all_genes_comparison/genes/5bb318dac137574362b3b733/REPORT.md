# YPL095C
Status: ok. Length: 1558 nt. Measured usable bases: 646. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 646 | 0.3396 | 0.3232 |
| rnafold | ok | 646 | 0.3311 | 0.3144 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 128 | 0.1710 | -0.2013 |
| seed_p | 128 | -0.2004 | -0.0234 |
| seed_p_vs_seed_pars | 79 | -0.4733 | -0.1036 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
