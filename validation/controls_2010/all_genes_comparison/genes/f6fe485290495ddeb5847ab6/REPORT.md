# YIL008W
Status: ok. Length: 480 nt. Measured usable bases: 228. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 228 | 0.2031 | 0.1728 |
| rnafold | ok | 228 | 0.2435 | 0.2191 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | -0.6249 | -0.7010 |
| seed_p | 28 | -0.5819 | -0.6732 |
| seed_p_vs_seed_pars | 13 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
